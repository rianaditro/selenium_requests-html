from bs4 import BeautifulSoup
from selenium import webdriver

urls = ["https://www.ikea.co.id/in/produk/dekorasi/tanaman-hias/chrysalidocarpus-lutescens-27-art-00001103",
       "https://www.ikea.co.id/in/produk/dekorasi/tanaman-hias/peperomia-obtu-sipolia-15-art-00001087"]



result = []

def run_url(url):
    output = dict()
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    print(soup)
    table_html = soup.find("div", id="modal-measurements")
    tables = table_html.find_all("table")
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            td = row.find_all("td")
            key = td[0].get_text().replace(": ","").replace("\n","").replace(":","")
            value = td[1].get_text()
            output[key] = value
        print(output)

    result.append(output)

    driver.quit()

for url in urls:
    run_url(url)

print(result)