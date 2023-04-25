import requests
from bs4 import BeautifulSoup

base_url = 'https://www.thewhiskyexchange.com/'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36.'
    }

products_links = []
for page in range(1, 2):
    print(f'----- PAGINA {page} -----')
    r = requests.get(f'{base_url}c/477/french-whisky?pg={page}')
    soup = BeautifulSoup(r.content, 'lxml')

    products = soup.find_all('li', class_='product-grid__item')

    for product in products:
        for link in product.find_all('a', href=True):
            products_links.append(base_url + link['href'])

products_infos = []
for product_link in products_links:
    print(f'{products_links.index(product_link)} de {len(products_links)}')
    product_info = {}
    r_product = requests.get(product_link, headers=headers)
    soup_product = BeautifulSoup(r_product.content, 'lxml')
    product_info['name'] = soup_product.find('h1', class_='product-main__name').text.strip()
    product_info['price'] = soup_product.find('p', class_='product-action__price').text.strip()

    products_infos.append(product_info)

print(products_infos)


