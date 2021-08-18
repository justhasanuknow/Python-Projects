import requests as rq
from bs4 import BeautifulSoup


url = "__TEST HTML GOES GERE__"

response = rq.get(url)

htmlContent = response.content

soup = BeautifulSoup(htmlContent, "html.parser")

for i in soup.find_all("a"):
    print(i)
    print("____________________________________________________________________________________\n")