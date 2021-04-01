import urllib

from lxml import html

from . import category_crawler
from .classes import Category
from .path_util import get_url_segment_from


def process_url(url: str):
    with urllib.request.urlopen(url) as response:
        html_content = response.read()
        parsed_html = html.fromstring(html_content)

        category_html = parsed_html.xpath("//div[@class='side_categories']/ul/li/ul/li/a")
        categories = extract_category_data(category_html)

        return list(map(lambda category: category_crawler.process_category(url, category), categories))


def extract_category_data(list_of_categories):
    return list(map(lambda tag: extract_category_a_tag(tag), list_of_categories))


def extract_category_a_tag(category_a_tag: html.HtmlElement) -> Category:
    href_value = category_a_tag.attrib["href"]
    category_parts = get_url_segment_from(href_value, 3).split("_")

    return Category(
        category_num=category_parts[1],
        technical_name=category_parts[0],
        readable_name=category_a_tag.text.strip()
    )
