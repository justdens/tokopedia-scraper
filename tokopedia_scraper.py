
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_tokopedia(keyword, max_results=20):
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }

    base_url = "https://www.tokopedia.com/search?st=product&q="
    query = keyword.replace(" ", "%20")
    url = base_url + query

    products = []
    page = 1

    while len(products) < max_results:
        paginated_url = f"{url}&page={page}"
        response = requests.get(paginated_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.select('div.css-974ipl')
        if not items:
            print("Tidak menemukan produk di halaman ini.")
            break

        for item in items:
            if len(products) >= max_results:
                break
            try:
                name = item.select_one('div.css-1b6t4dn').text
                price = item.select_one('div.css-o5uqvq').text
                location = item.select_one('span.css-1kdc32b').text if item.select_one('span.css-1kdc32b') else "N/A"
                rating = item.select_one('span.css-t70v7i').text if item.select_one('span.css-t70v7i') else "N/A"
                products.append({
                    'Product Name': name,
                    'Price': price,
                    'Location': location,
                    'Rating': rating
                })
            except Exception:
                continue

        page += 1
        time.sleep(1)

    df = pd.DataFrame(products)
    output_filename = f"{keyword.replace(' ', '_')}_tokopedia.xlsx"
    df.to_excel(output_filename, index=False)
    print(f"Hasil disimpan di: {output_filename}")
    return output_filename

if __name__ == "__main__":
    keyword = input("Masukkan kata kunci produk: ")
    scrape_tokopedia(keyword)
