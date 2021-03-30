import urllib
from lxml import html

def process_url(url):
    with urllib.request.urlopen(url) as response:
        html_content = response.read()
        parsed_html = html.fromstring(html_content)
        
        category_urls = parsed_html.xpath("//div[@class='side_categories']/ul/li/ul/li/a/@href")
        print(category_urls)