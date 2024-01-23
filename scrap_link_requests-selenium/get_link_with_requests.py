from requests_html import HTMLSession

url = "https://www.beerwulf.com/en-gb/c/all-beers?segment=Beers&catalogCode=Beer_1"
session = HTMLSession()

#access the url
r = session.get(url)

#scrolldown to 25 point and sleep before rendering
r.html.render(sleep=3,scrolldown = 25)

#provide the complete URL in the Xpath location
link = r.html.xpath('//*[@id="product-items-container"]', first = True).absolute_links

print(link)
print(type(link))
print(len(link))