import requests
from bs4 import BeautifulSoup
import pandas as pd

url1='https://www.voanews.com/a/israel-conducts-airstrikes-on-rafah/7483633.html'
page1=requests.get(url1)
soup=BeautifulSoup(page1.content,'html.parser')

title1=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate1=soup.find(class_="published").text.replace("\n","  ")

links1=soup.find(class_="links__item").text.replace("\n","  ")

article1=soup.find(class_="wsw").text.replace("\n","  ")

data1=[[url1,title1,publishdate1,links1,article1]]



url2='https://www.voanews.com/a/israeli-airstrikes-pound-southern-gaza-city-of-rafah/7482142.html'
page2=requests.get(url2)
soup=BeautifulSoup(page2.content,'html.parser')

title2=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate2=soup.find(class_="published").text.replace("\n","  ")

links2=soup.find(class_="links__item").text.replace("\n","  ")

article2=soup.find(class_="wsw").text.replace("\n","  ")

data2=[[url2,title2,publishdate2,links2,article2]]



url3='https://www.voanews.com/a/israel-airstrikes-hit-gaza-bordertown-of-rafah/7480774.html'
page3=requests.get(url3)
soup=BeautifulSoup(page3.content,'html.parser')

title3=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate3=soup.find(class_="published").text.replace("\n","  ")

links3=soup.find(class_="links__item").text.replace("\n","  ")

article3=soup.find(class_="wsw").text.replace("\n","  ")

data3=[[url3,title3,publishdate3,links3,article3]]



url4='https://www.voanews.com/a/blinken-israeli-officials-discuss-efforts-to-free-hostages-held-in-gaza-/7479145.html'
page4=requests.get(url4)
soup=BeautifulSoup(page4.content,'html.parser')

title4=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate4=soup.find(class_="published").text.replace("\n","  ")

links4=soup.find(class_="links__item").text.replace("\n","  ")

article4=soup.find(class_="wsw").text.replace("\n","  ")

data4=[[url4,title4,publishdate4,links4,article4]]



url5='https://www.voanews.com/a/blinken-discussing-israel-hamas-cease-fire-proposal-with-israeli-officials/7477413.html'
page5=requests.get(url5)
soup=BeautifulSoup(page5.content,'html.parser')

title5=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate5=soup.find(class_="published").text.replace("\n","  ")

links5=soup.find(class_="links__item").text.replace("\n","  ")

article5=soup.find(class_="wsw").text.replace("\n","  ")

data5=[[url5,title5,publishdate5,links5,article5]]



url6='https://www.voanews.com/a/media-weigh-ethics-over-access-for-military-embeds-to-gaza/7476768.html'
page6=requests.get(url6)
soup=BeautifulSoup(page6.content,'html.parser')

title6=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate6=soup.find(class_="published").text.replace("\n","  ")

links6=soup.find(class_="links__item").text.replace("\n","  ")

article6=soup.find(class_="wsw").text.replace("\n","  ")

data6=[[url6,title6,publishdate6,links6,article6]]






df=pd.DataFrame([
    [url1,title1,publishdate1,links1,article1],
    [url2,title2,publishdate2,links2,article2],
    [url3,title3,publishdate3,links3,article3],
    [url4,title4,publishdate4,links4,article4],
    [url5,title5,publishdate5,links5,article5],
    [url6,title6,publishdate6,links6,article6]]
    ,columns=['URL','Title','PublishDate','Links','Article'])


df.to_csv("final report.csv",index=False)

print('ok')