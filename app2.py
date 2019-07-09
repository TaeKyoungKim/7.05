import requests 
from bs4 import BeautifulSoup

def get_info():
    resp = requests.request("get", "https://naver.com")
    # print(resp)
    # print(resp.encoding)
    # print(resp.headers)
    # print(resp.url)
    soup = BeautifulSoup(resp.content , 'html.parser')
    # print(soup.prettify())
    print(soup.span)


if __name__== "__main__":
    get_info()