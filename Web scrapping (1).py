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

url7='https://www.voanews.com/a/funeral-held-for-al-jazeera-journalist-killed-in-israel-strike-/7401061.html'
page7=requests.get(url7)
soup=BeautifulSoup(page7.content,'html.parser')

title7=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate7=soup.find(class_="published").text.replace("\n","  ")

links7=soup.find(class_="links__item").text.replace("\n","  ")

article7=soup.find(class_="wsw").text.replace("\n","  ")

data7=[[url7,title7,publishdate7,links7,article7]]

url8='https://www.voanews.com/a/israeli-military-admits-mistakenly-killing-3-israeli-hostages-in-gaza-/7400543.html'
page8=requests.get(url8)
soup=BeautifulSoup(page8.content,'html.parser')

title8=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate8=soup.find(class_="published").text.replace("\n","  ")

links8=soup.find(class_="links__item").text.replace("\n","  ")

article8=soup.find(class_="wsw").text.replace("\n","  ")

data8=[[url8,title8,publishdate8,links8,article8]]

url9='https://www.voanews.com/a/palestinian-americans-sue-biden-administration-over-relatives-stuck-in-gaza-/7400521.html'
page9=requests.get(url9)
soup=BeautifulSoup(page9.content,'html.parser')

title9=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate9=soup.find(class_="published").text.replace("\n","  ")

links9=soup.find(class_="links__item").text.replace("\n","  ")

article9=soup.find(class_="wsw").text.replace("\n","  ")

data9=[[url9,title9,publishdate9,links9,article9]]

url10='https://www.voanews.com/a/israeli-army-opens-probe-into-killing-of-2-palestinians-at-close-range-/7400256.html'
page10=requests.get(url10)
soup=BeautifulSoup(page10.content,'html.parser')

title10=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate10=soup.find(class_="published").text.replace("\n","  ")

links10=soup.find(class_="links__item").text.replace("\n","  ")

article10=soup.find(class_="wsw").text.replace("\n","  ")

data10=[[url10,title10,publishdate10,links10,article10]]

url11='https://www.voanews.com/a/washington-urges-israel-to-scale-down-its-gaza-offensive-/7400127.html'
page11=requests.get(url11)
soup=BeautifulSoup(page11.content,'html.parser')

title11=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate11=soup.find(class_="published").text.replace("\n","  ")

links11=soup.find(class_="links__item").text.replace("\n","  ")

article11=soup.find(class_="wsw").text.replace("\n","  ")

data11=[[url11,title11,publishdate11,links11,article11]]

url12='https://www.voanews.com/a/leaders-of-turkey-egypt-work-to-stop-israel-s-looming-offensive-in-gaza-s-rafah/7487453.html'
page12=requests.get(url12)
soup=BeautifulSoup(page12.content,'html.parser')

title12=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate12=soup.find(class_="published").text.replace("\n","  ")

links12=soup.find(class_="links__item").text.replace("\n","  ")

article12=soup.find(class_="wsw").text.replace("\n","  ")

data12=[[url12,title12,publishdate12,links12,article12]]

url13='https://www.voanews.com/a/unrwa-chief-agency-essential-to-respond-to-humanitarian-crisis-in-gaza/7486115.html'
page13=requests.get(url13)
soup=BeautifulSoup(page13.content,'html.parser')

title13=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate13=soup.find(class_="published").text.replace("\n","  ")

links13=soup.find(class_="links__item").text.replace("\n","  ")

article13=soup.find(class_="wsw").text.replace("\n","  ")

data13=[[url13,title13,publishdate13,links13,article13]]

url14='https://www.voanews.com/a/israel-hamas-battle-in-gaza-as-warring-sides-consider-new-temporary-cease-fire-/7466317.html'
page14=requests.get(url14)
soup=BeautifulSoup(page14.content,'html.parser')

title14=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate14=soup.find(class_="published").text.replace("\n","  ")

links14=soup.find(class_="links__item").text.replace("\n","  ")

article14=soup.find(class_="wsw").text.replace("\n","  ")

data14=[[url14,title14,publishdate14,links14,article14]]

url15='https://www.voanews.com/a/china-circumspect-after-international-court-ruling-on-israel/7465514.html'
page15=requests.get(url15)
soup=BeautifulSoup(page15.content,'html.parser')

title15=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate15=soup.find(class_="published").text.replace("\n","  ")

links15=soup.find(class_="links__item").text.replace("\n","  ")

article15=soup.find(class_="wsw").text.replace("\n","  ")

data15=[[url15,title15,publishdate15,links15,article15]]

url16='https://www.voanews.com/a/israel-defends-itself-at-the-un-s-top-court-against-gaza-genocide-allegations-/7438408.html'
page16=requests.get(url16)
soup=BeautifulSoup(page16.content,'html.parser')

title16=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate16=soup.find(class_="published").text.replace("\n","  ")

links16=soup.find(class_="links__item").text.replace("\n","  ")

article16=soup.find(class_="wsw").text.replace("\n","  ")

data16=[[url16,title16,publishdate16,links16,article16]]

url17='https://www.voanews.com/a/un-calls-for-cease-fire-in-gaza-grow-louder-as-conditions-deteriorate-/7437640.html'
page17=requests.get(url17)
soup=BeautifulSoup(page17.content,'html.parser')

title17=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate17=soup.find(class_="published").text.replace("\n","  ")

links17=soup.find(class_="links__item").text.replace("\n","  ")

article17=soup.find(class_="wsw").text.replace("\n","  ")

data17=[[url17,title17,publishdate17,links17,article17]]

url18='https://www.voanews.com/a/who-life-saving-aid-not-reaching-millions-of-people-caught-in-health-emergencies/7435701.html'
page18=requests.get(url18)
soup=BeautifulSoup(page18.content,'html.parser')

title18=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate18=soup.find(class_="published").text.replace("\n","  ")

links18=soup.find(class_="links__item").text.replace("\n","  ")

article18=soup.find(class_="wsw").text.replace("\n","  ")

data18=[[url18,title18,publishdate18,links18,article18]]

url19='https://www.voanews.com/a/health-catastrophe-unfolding-in-gaza-as-humanitarian-space-shrinks-/7432854.html'
page19=requests.get(url19)
soup=BeautifulSoup(page19.content,'html.parser')

title19=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate19=soup.find(class_="published").text.replace("\n","  ")

links19=soup.find(class_="links__item").text.replace("\n","  ")

article19=soup.find(class_="wsw").text.replace("\n","  ")

data19=[[url19,title19,publishdate19,links19,article19]]

url20='https://www.voanews.com/a/indian-pm-modi-opens-hindu-temple-in-uae-ahead-of-elections/7487172.html'
page20=requests.get(url20)
soup=BeautifulSoup(page20.content,'html.parser')

title20=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate20=soup.find(class_="published").text.replace("\n","  ")

links20=soup.find(class_="links__item").text.replace("\n","  ")

article20=soup.find(class_="wsw").text.replace("\n","  ")

data20=[[url20,title20,publishdate20,links20,article20]]







df=pd.DataFrame([
    [url1,title1,publishdate1,links1,article1],
    [url2,title2,publishdate2,links2,article2],
    [url3,title3,publishdate3,links3,article3],
    [url4,title4,publishdate4,links4,article4],
    [url5,title5,publishdate5,links5,article5],
    [url6,title6,publishdate6,links6,article6],
    [url1,title7,publishdate7,links7,article7],
    [url8,title8,publishdate8,links8,article8],
    [url9,title9,publishdate9,links9,article9],
    [url10,title10,publishdate10,links10,article10],
    [url11,title11,publishdate11,links11,article11],
    [url12,title12,publishdate12,links12,article12],
    [url13,title13,publishdate13,links13,article13],
    [url14,title14,publishdate14,links14,article14],
    [url15,title15,publishdate15,links15,article15],
    [url16,title16,publishdate16,links16,article16],
    [url17,title17,publishdate17,links17,article17],
    [url18,title18,publishdate18,links18,article18],
    [url19,title19,publishdate19,links19,article19],
    [url20,title20,publishdate20,links20,article20]]
    ,columns=['URL','Title','PublishDate','Links','Article'])


df.to_csv("final report.csv",index=True)

print('ok')