from bs4 import BeautifulSoup
from requests import get


def main(name):
    url = "http://mnds.qcwyhr.com/peoplelist.aspx"
    soup = BeautifulSoup(get(url).text, "html.parser")
    lists = soup.select("span.ape a")
    for tag in lists:
        if name in tag:
            rank = lists.index(tag) + 1
            print(f"目前位次为：第 {rank} 名")
            break
    
    
if __name__ == "__main__":
    main("李蒙双")
    