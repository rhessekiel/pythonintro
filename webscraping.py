from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.lwhs.org/page")
print(r)
titles = r.html.find(".result-title")
for title in titles:
  url = title.attrs.get("href")
  name = title.text
  
  # open the URL we found
  r = session.get(url)
  # we found the part of the page we want in the article page has an id "postingbody"
  # so we get the part of the page with the id (ids are prefaced by #)
  content = r.html.find("#postingbody", first=True)
  
  if (content.text) # only if we found something
    print (content.text)
  
    # without the first=True attribute we'd get a list, and content.text would throw an error
  content = r.html.find("#postingbody")