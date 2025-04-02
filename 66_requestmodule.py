import requests
#to get code of the site 
response=requests.get("https://www.google.com")
print(response.text)

#post requests to send data to a site
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Hanan",
    "body":"yes",
    "userID":15
}
headers={"Content-type":"application/json; charset=UTF-8"}
response=requests.post(url,headers=headers,json=data)
print(response.text)

#for scrapping and i want to parse and get all the h2 headings- beautiful soup is used
url="https://www.codewithharry.com/blogpost/%60how-to-integrate-mongodb-into-your-nextjs-apps%60/"
r=requests.get(url)
print(r.text)
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)