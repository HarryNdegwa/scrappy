import mechanicalsoup

browser = mechanicalsoup.Browser()

url = "http://127.0.0.1:8000/"

page = browser.get(url) # a request object

# print(dir(page))

# print(page.status_code)

# print(type(page.soup)) # mechanicalsoup uses beautifulsoup to parse html from requested pages

# interacting with the contact form in pixenweb

page_html = page.soup

contact_form = page_html.select("form")[0]
