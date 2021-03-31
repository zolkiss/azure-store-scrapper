import urllib
import unicodedata
from lxml import html
from .path_util import get_url_segment_from

from .classes import category
from .classes import book

def process_category(base_url: str, category_data: category) -> [category, list[book]]:
    with urllib.request.urlopen(f"{base_url}/catalogue/category/books/{category_data.technical_name}_{category_data.category_num}/index.html") as response:
        html_content = response.read().decode('utf-8')
        parsed_html = html.fromstring(html_content)

        book_data =  list(map(lambda book_tag: extract_basic_book_data(category_data, book_tag), parsed_html.xpath("//article/h3/a")))

        for book in book_data:
            extract_extended_book_data(base_url, book)

        return [category_data, book_data]

        
def extract_basic_book_data(parent_category: category, html_part: html.HtmlElement) -> book:
    href_value = html_part.attrib["href"]
    book_url_parts = get_url_segment_from(href_value, 3).split("_")

    return book(
        technical_name = book_url_parts[0],
        title = html_part.text.strip(),
        book_num = book_url_parts[1],
        category_num = parent_category.category_num
    )

def extract_extended_book_data(base_url: str, book: book):
    with urllib.request.urlopen(f"{base_url}/catalogue/{book.technical_name}_{book.book_num}/index.html") as response:
        html_content = response.read()
        parsed_html = html.fromstring(html_content)
        article = parsed_html.xpath("//article")[0]

        product_table = article.xpath("table//tr/td")
        description = article.xpath("p")

        update_description(description, book)
        update_product_table(product_table, book)
        return book

def update_description(description: html.HtmlElement, book: book):
    if (len(description)):
        book.description = unicodedata.normalize('NFKD', description[0].text)
        if("\xad" in book.description):
            book.description = book.description.replace(u'\xad', u'')
        if("\ufeff" in book.description):
            book.description = book.description.replace(u'\ufeff', u'')

def update_product_table(product_table: html.HtmlElement, book: book):
        book.upc = product_table[0].text.strip()
        book.net_price = float(product_table[2].text.strip()[1:])
        book.currency = product_table[2].text.strip()[:1]
        book.gross_price = float(product_table[3].text.strip()[1:])
        book.tax = float(product_table[4].text.strip()[1:])
        book.availability = product_table[5].text.strip()
        book.number_of_reviews = int(product_table[6].text.strip())

