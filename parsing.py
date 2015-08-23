from bs4 import BeautifulSoup
import urllib.request

FileToStore = open("ParsingDataDemo", "w")

URL = "http://ntusweety.herokuapp.com/search?m=0&m=1&m=2&m=3&m=4&m=5&m=6&m=7&m=8&m=9&m=10&m=A&m=B&m=C&m=D&t=0&t=1&t=2&t=3&t=4&t=5&t=6&t=7&t=8&t=9&t=10&t=A&t=B&t=C&t=D&w=0&w=1&w=2&w=3&w=4&w=5&w=6&w=7&w=8&w=9&w=10&w=A&w=B&w=C&w=D&h=0&h=1&h=2&h=3&h=4&h=5&h=6&h=7&h=8&h=9&h=10&h=A&h=B&h=C&h=D&f=0&f=1&f=2&f=3&f=4&f=5&f=6&f=7&f=8&f=9&f=10&f=A&f=B&f=C&f=D&s=0&s=1&s=2&s=3&s=4&s=5&s=6&s=7&s=8&s=9&s=10&s=A&s=B&s=C&s=D&sem=104-1&faculty=&depart=&name=&teacher=&page="

PageCount = 0
PageMax = 603
# PageMax = 2
while PageCount < PageMax:
    #print (PageCount)

    Content = urllib.request.urlopen(URL + str(PageCount)).read()
    Soup = BeautifulSoup(Content, "html.parser")
    TableStats = Soup.find('table', {"id" : "searchresult"})

    for Row in TableStats.findAll('tr')[1:]:
        Col = Row.findAll('td')
        ColCouter = 0
        for Item in Col:
            if ColCouter == 15:
                break
            FileToStore.write(Item.text + "#");
            ColCouter += 1
        FileToStore.write('\n');

    PageCount += 1

FileToStore.close()
