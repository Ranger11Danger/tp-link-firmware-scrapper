from bs4 import BeautifulSoup
import requests


data = requests.get("https://www.tp-link.com/us/support/download/").text


soup = BeautifulSoup(data, "html.parser")

router_list = soup.find("div", {"data-class" : "wi-fi-routers"}).find_all("a")

for router in router_list:
    data = requests.get(f"https://www.tp-link.com{router['href']}").text
    soup = BeautifulSoup(data, 'html.parser').find_all('a', {'class' : 'download-resource-btn'})
    try:
        for link in soup:
            if 'firmware' in link['href']:
                print(link['href'])
    except:
        pass
