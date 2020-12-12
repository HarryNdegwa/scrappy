import mechanicalsoup

browser = mechanicalsoup.Browser()

url = "http://127.0.0.1:8000/"

submit_url = "http://127.0.0.1:8000/contact/"

page = browser.get(url) # a request object

# print(dir(page))

# print(page.status_code)

# print(type(page.soup)) # mechanicalsoup uses beautifulsoup to parse html from requested pages

# interacting with the contact form in pixenweb

page_html = page.soup

contact_form = page_html.select("form")[0]

contact_form.select("input")[0]["value"] = "Harrison Ndegwa"
contact_form.select("input")[1]["value"] = "harryndegwa4@gmail.com"
contact_form.select("input")[2]["value"] = "I need a your services"
contact_form.select("textarea")[0]["value"] = "I need a web scrapper"

submission = browser.submit(contact_form,submit_url)
