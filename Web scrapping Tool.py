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

url21='https://www.voanews.com/a/ukraine-says-russian-attacks-target-kyiv/7488474.html'
page21=requests.get(url21)
soup=BeautifulSoup(page21.content,'html.parser')

title21=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate21=soup.find(class_="published").text.replace("\n","  ")

links21=soup.find(class_="links__item").text.replace("\n","  ")

article21=soup.find(class_="wsw").text.replace("\n","  ")

data21=[[url21,title21,publishdate21,links21,article21]]

url22='https://www.voanews.com/a/momentum-builds-in-efforts-to-seize-russian-assets-for-ukraine-/7488319.html'
page22=requests.get(url22)
soup=BeautifulSoup(page22.content,'html.parser')

title22=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate22=soup.find(class_="published").text.replace("\n","  ")

links22=soup.find(class_="links__item").text.replace("\n","  ")

article22=soup.find(class_="wsw").text.replace("\n","  ")

data22=[[url22,title22,publishdate22,links22,article22]]

url23='https://www.voanews.com/a/some-republican-lawmakers-not-concerned-with-trump-s-nato-comments-/7485162.html'
page23=requests.get(url23)
soup=BeautifulSoup(page22.content,'html.parser')

title23=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate23=soup.find(class_="published").text.replace("\n","  ")

links23=soup.find(class_="links__item").text.replace("\n","  ")

article23=soup.find(class_="wsw").text.replace("\n","  ")

data23=[[url23,title23,publishdate23,links23,article23]]

url24='https://www.voanews.com/a/trump-s-dominance-in-iowa-sets-tone-for-republican-primary-/7442836.html'
page24=requests.get(url24)
soup=BeautifulSoup(page24.content,'html.parser')

title24=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate24=soup.find(class_="published").text.replace("\n","  ")

links24=soup.find(class_="links__item").text.replace("\n","  ")

article24=soup.find(class_="wsw").text.replace("\n","  ")

data24=[[url24,title24,publishdate24,links24,article24]]

url25='https://www.voanews.com/a/us-senate-set-for-final-foreign-aid-bill-vote/7485440.html'
page25=requests.get(url25)
soup=BeautifulSoup(page25.content,'html.parser')

title25=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate25=soup.find(class_="published").text.replace("\n","  ")

links25=soup.find(class_="links__item").text.replace("\n","  ")

article25=soup.find(class_="wsw").text.replace("\n","  ")

data25=[[url25,title25,publishdate25,links25,article25]]

url26='https://www.voanews.com/a/health-officials-report-israeli-attack-on-khan-younis-hospital/7488543.html'
page26=requests.get(url26)
soup=BeautifulSoup(page26.content,'html.parser')

title26=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate26=soup.find(class_="published").text.replace("\n","  ")

links26=soup.find(class_="links__item").text.replace("\n","  ")

article26=soup.find(class_="wsw").text.replace("\n","  ")

data26=[[url26,title26,publishdate26,links26,article26]]

url26='https://www.voanews.com/a/netanyahu-vows-rafah-attack-pulls-out-of-cease-fire-talks-/7488350.html'
page26=requests.get(url26)
soup=BeautifulSoup(page26.content,'html.parser')

title26=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate26=soup.find(class_="published").text.replace("\n","  ")

links26=soup.find(class_="links__item").text.replace("\n","  ")

article26=soup.find(class_="wsw").text.replace("\n","  ")

data26=[[url26,title26,publishdate26,links26,article26]]

url27='https://www.voanews.com/a/china-s-vpn-usage-nearly-doubles-amid-internet-censorship/7488465.html'
page27=requests.get(url27)
soup=BeautifulSoup(page27.content,'html.parser')

title27=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate27=soup.find(class_="published").text.replace("\n","  ")

links27=soup.find(class_="links__item").text.replace("\n","  ")

article27=soup.find(class_="wsw").text.replace("\n","  ")

data27=[[url27,title27,publishdate27,links27,article27]]

url28='https://www.voanews.com/a/china-russia-double-down-on-ties-despite-complications-in-trade-relations/7488511.html'
page28=requests.get(url28)
soup=BeautifulSoup(page28.content,'html.parser')

title28=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate28=soup.find(class_="published").text.replace("\n","  ")

links28=soup.find(class_="links__item").text.replace("\n","  ")

article28=soup.find(class_="wsw").text.replace("\n","  ")

data28=[[url28,title28,publishdate28,links28,article28]]

url29='https://www.voanews.com/a/us-officials-push-back-after-lawmaker-sounds-alarm-on-security-threat/7488429.html'
page29=requests.get(url29)
soup=BeautifulSoup(page29.content,'html.parser')

title29=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate29=soup.find(class_="published").text.replace("\n","  ")

links29=soup.find(class_="links__item").text.replace("\n","  ")

article29=soup.find(class_="wsw").text.replace("\n","  ")

data29=[[url29,title29,publishdate29,links29,article29]]

url30='https://www.voanews.com/a/us-senate-set-for-final-foreign-aid-bill-vote/7485440.html'
page30=requests.get(url30)
soup=BeautifulSoup(page30.content,'html.parser')

title30=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate30=soup.find(class_="published").text.replace("\n","  ")

links30=soup.find(class_="links__item").text.replace("\n","  ")

article30=soup.find(class_="wsw").text.replace("\n","  ")

data30=[[url30,title30,publishdate30,links30,article30]]

url31='https://www.voanews.com/a/shots-fired-near-super-bowl-champs-parade-several-injured-official-says/7487815.html'
page31=requests.get(url31)
soup=BeautifulSoup(page31.content,'html.parser')

title31=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate31=soup.find(class_="published").text.replace("\n","  ")

links31=soup.find(class_="links__item").text.replace("\n","  ")

article31=soup.find(class_="wsw").text.replace("\n","  ")

data31=[[url31,title31,publishdate31,links31,article31]]

url32='https://www.voanews.com/a/private-us-moon-lander-launched-half-century-after-last-apollo-lunar-mission-/7488476.html'
page32=requests.get(url32)
soup=BeautifulSoup(page32.content,'html.parser')

title32=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate32=soup.find(class_="published").text.replace("\n","  ")

links32=soup.find(class_="links__item").text.replace("\n","  ")

article32=soup.find(class_="wsw").text.replace("\n","  ")

data32=[[url32,title32,publishdate32,links32,article32]]

url33='https://www.voanews.com/a/enough-space-for-everyone-us-china-target-africa-/7388756.html'
page33=requests.get(url33)
soup=BeautifulSoup(page33.content,'html.parser')

title33=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate33=soup.find(class_="published").text.replace("\n","  ")

links33=soup.find(class_="links__item").text.replace("\n","  ")

article33=soup.find(class_="wsw").text.replace("\n","  ")

data33=[[url33,title33,publishdate33,links33,article33]]

url34='https://www.voanews.com/a/botswana-opposition-slams-electoral-body-for-benchmarking-in-zimbabwe-/7487587.html'
page34=requests.get(url34)
soup=BeautifulSoup(page34.content,'html.parser')

title34=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate34=soup.find(class_="published").text.replace("\n","  ")

links34=soup.find(class_="links__item").text.replace("\n","  ")

article34=soup.find(class_="wsw").text.replace("\n","  ")

data34=[[url34,title34,publishdate34,links34,article34]]

url35='https://www.voanews.com/a/botswana-opposition-slams-electoral-body-for-benchmarking-in-zimbabwe-/7487587.html'
page35=requests.get(url35)
soup=BeautifulSoup(page35.content,'html.parser')

title35=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate35=soup.find(class_="published").text.replace("\n","  ")

links35=soup.find(class_="links__item").text.replace("\n","  ")

article35=soup.find(class_="wsw").text.replace("\n","  ")

data35=[[url35,title35,publishdate35,links35,article35]]

url36='https://www.voanews.com/a/us-north-korea-trying-to-advance-nuclear-program-with-satellite-launch/7372425.html'
page36=requests.get(url36)
soup=BeautifulSoup(page36.content,'html.parser')

title36=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate36=soup.find(class_="published").text.replace("\n","  ")

links36=soup.find(class_="links__item").text.replace("\n","  ")

article36=soup.find(class_="wsw").text.replace("\n","  ")

data36=[[url36,title36,publishdate36,links36,article36]]

url37='https://www.voanews.com/a/here-for-the-long-haul-protesting-indian-farmers-set-up-camp-/7488606.html'
page37=requests.get(url37)
soup=BeautifulSoup(page37.content,'html.parser')

title37=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate37=soup.find(class_="published").text.replace("\n","  ")

links37=soup.find(class_="links__item").text.replace("\n","  ")

article37=soup.find(class_="wsw").text.replace("\n","  ")

data37=[[url37,title37,publishdate37,links37,article37]]

url38='https://www.voanews.com/a/us-japan-accelerate-war-drills-to-deter-china-/7481724.html'
page38=requests.get(url38)
soup=BeautifulSoup(page38.content,'html.parser')

title38=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate38=soup.find(class_="published").text.replace("\n","  ")

links38=soup.find(class_="links__item").text.replace("\n","  ")

article38=soup.find(class_="wsw").text.replace("\n","  ")

data38=[[url38,title38,publishdate38,links38,article38]]

url39='https://www.voanews.com/a/north-korea-says-it-tested-long-range-cruise-missiles-to-sharpen-attack-capabilities/7464493.html'
page39=requests.get(url39)
soup=BeautifulSoup(page39.content,'html.parser')

title39=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate39=soup.find(class_="published").text.replace("\n","  ")

links39=soup.find(class_="links__item").text.replace("\n","  ")

article39=soup.find(class_="wsw").text.replace("\n","  ")

data39=[[url39,title39,publishdate39,links39,article39]]

url40='https://www.voanews.com/a/analysts-north-korea-seeks-to-dominate-south-korea-through-nuclear-coercion-/7464411.html'
page40=requests.get(url40)
soup=BeautifulSoup(page40.content,'html.parser')

title40=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate40=soup.find(class_="published").text.replace("\n","  ")

links40=soup.find(class_="links__item").text.replace("\n","  ")

article40=soup.find(class_="wsw").text.replace("\n","  ")

data40=[[url40,title40,publishdate40,links40,article40]]

url41='https://www.voanews.com/a/north-korea-says-it-tested-new-strategic-cruise-missile-/7456418.html'
page41=requests.get(url41)
soup=BeautifulSoup(page41.content,'html.parser')

title41=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate41=soup.find(class_="published").text.replace("\n","  ")

links41=soup.find(class_="links__item").text.replace("\n","  ")

article41=soup.find(class_="wsw").text.replace("\n","  ")

data41=[[url41,title41,publishdate41,links41,article41]]

url42='https://www.voanews.com/a/indian-pm-modi-opens-hindu-temple-in-uae-ahead-of-elections/7487172.html'
page42=requests.get(url42)
soup=BeautifulSoup(page42.content,'html.parser')

title42=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate42=soup.find(class_="published").text.replace("\n","  ")

links42=soup.find(class_="links__item").text.replace("\n","  ")

article42=soup.find(class_="wsw").text.replace("\n","  ")

data42=[[url42,title42,publishdate42,links42,article42]]

url43='https://www.voanews.com/a/us-urges-north-korea-to-halt-provocations-return-to-diplomacy/7455894.html'
page43=requests.get(url43)
soup=BeautifulSoup(page43.content,'html.parser')

title43=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate43=soup.find(class_="published").text.replace("\n","  ")

links43=soup.find(class_="links__item").text.replace("\n","  ")

article43=soup.find(class_="wsw").text.replace("\n","  ")

data43=[[url43,title43,publishdate43,links43,article43]]

url44='https://www.voanews.com/a/analysts-us-south-korea-should-be-ready-for-russia-north-korea-alliance/7456346.html'
page44=requests.get(url44)
soup=BeautifulSoup(page44.content,'html.parser')

title44=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate44=soup.find(class_="published").text.replace("\n","  ")

links44=soup.find(class_="links__item").text.replace("\n","  ")

article44=soup.find(class_="wsw").text.replace("\n","  ")

data44=[[url44,title44,publishdate44,links44,article44]]

url45='https://www.voanews.com/a/south-korea-says-north-korea-fired-several-cruise-missiles-into-the-sea/7454744.html'
page45=requests.get(url45)
soup=BeautifulSoup(page45.content,'html.parser')

title45=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate45=soup.find(class_="published").text.replace("\n","  ")

links45=soup.find(class_="links__item").text.replace("\n","  ")

article45=soup.find(class_="wsw").text.replace("\n","  ")

data45=[[url45,title45,publishdate45,links45,article45]]

url46='https://www.voanews.com/a/north-korea-foreign-minister-ready-to-greet-putin-/7448774.html'
page46=requests.get(url46)
soup=BeautifulSoup(page46.content,'html.parser')

title46=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate46=soup.find(class_="published").text.replace("\n","  ")

links46=soup.find(class_="links__item").text.replace("\n","  ")

article46=soup.find(class_="wsw").text.replace("\n","  ")

data46=[[url46,title46,publishdate46,links46,article46]]

url47='https://www.voanews.com/a/former-nato-chief-warns-against-axis-of-autocracies-/7447098.html'
page47=requests.get(url47)
soup=BeautifulSoup(page47.content,'html.parser')

title47=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate47=soup.find(class_="published").text.replace("\n","  ")

links47=soup.find(class_="links__item").text.replace("\n","  ")

article47=soup.find(class_="wsw").text.replace("\n","  ")

data47=[[url47,title47,publishdate47,links47,article47]]

url48='https://www.voanews.com/a/north-korea-s-hostility-could-snag-china-s-bid-for-better-us-ties-analysts-say/7447992.html'
page48=requests.get(url48)
soup=BeautifulSoup(page48.content,'html.parser')

title48=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate48=soup.find(class_="published").text.replace("\n","  ")

links48=soup.find(class_="links__item").text.replace("\n","  ")

article48=soup.find(class_="wsw").text.replace("\n","  ")

data48=[[url48,title48,publishdate48,links48,article48]]

url49='https://www.voanews.com/a/china-urges-end-of-harassment-of-vessels-in-red-sea/7447626.html'
page49=requests.get(url49)
soup=BeautifulSoup(page49.content,'html.parser')

title49=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate49=soup.find(class_="published").text.replace("\n","  ")

links49=soup.find(class_="links__item").text.replace("\n","  ")

article49=soup.find(class_="wsw").text.replace("\n","  ")

data49=[[url49,title49,publishdate49,links49,article49]]

url50='https://www.voanews.com/a/us-re-designates-yemen-s-houthis-as-a-major-terror-group/7443801.html'
page50=requests.get(url50)
soup=BeautifulSoup(page50.content,'html.parser')

title50=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate50=soup.find(class_="published").text.replace("\n","  ")

links50=soup.find(class_="links__item").text.replace("\n","  ")

article50=soup.find(class_="wsw").text.replace("\n","  ")

data50=[[url50,title50,publishdate50,links50,article50]]

url51='https://www.voanews.com/a/houthis-attack-maltese-flagged-vessel-in-the-gulf-of-aden-/7442506.html'
page51=requests.get(url51)
soup=BeautifulSoup(page51.content,'html.parser')

title51=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate51=soup.find(class_="published").text.replace("\n","  ")

links51=soup.find(class_="links__item").text.replace("\n","  ")

article51=soup.find(class_="wsw").text.replace("\n","  ")

data51=[[url51,title51,publishdate51,links51,article51]]

url52='https://www.voanews.com/a/us-owned-vessel-hit-by-missile-in-gulf-of-aden-/7440794.html'
page52=requests.get(url52)
soup=BeautifulSoup(page52.content,'html.parser')

title52=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate52=soup.find(class_="published").text.replace("\n","  ")

links52=soup.find(class_="links__item").text.replace("\n","  ")

article52=soup.find(class_="wsw").text.replace("\n","  ")

data52=[[url52,title52,publishdate52,links52,article52]]

url53='https://www.voanews.com/a/us-launches-follow-up-strike-on-houthi-radar-site-/7438870.html'
page53=requests.get(url53)
soup=BeautifulSoup(page53.content,'html.parser')

title53=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate53=soup.find(class_="published").text.replace("\n","  ")

links53=soup.find(class_="links__item").text.replace("\n","  ")

article53=soup.find(class_="wsw").text.replace("\n","  ")

data53=[[url53,title53,publishdate53,links53,article53]]

url54='https://www.voanews.com/a/us-launches-follow-up-strike-on-houthi-radar-site-/7438462.html'
page54=requests.get(url54)
soup=BeautifulSoup(page54.content,'html.parser')

title54=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate54=soup.find(class_="published").text.replace("\n","  ")

links54=soup.find(class_="links__item").text.replace("\n","  ")

article54=soup.find(class_="wsw").text.replace("\n","  ")

data54=[[url54,title54,publishdate54,links54,article54]]

url55='https://www.voanews.com/a/israel-defends-itself-at-the-un-s-top-court-against-gaza-genocide-allegations-/7438408.html'
page55=requests.get(url55)
soup=BeautifulSoup(page55.content,'html.parser')

title55=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate55=soup.find(class_="published").text.replace("\n","  ")

links55=soup.find(class_="links__item").text.replace("\n","  ")

article55=soup.find(class_="wsw").text.replace("\n","  ")

data55=[[url55,title55,publishdate55,links55,article55]]

url56='https://www.voanews.com/a/us-reveals-second-wave-of-strikes-on-houthis-braces-for-reprisals-/7438072.html'
page56=requests.get(url56)
soup=BeautifulSoup(page56.content,'html.parser')

title56=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate56=soup.find(class_="published").text.replace("\n","  ")

links56=soup.find(class_="links__item").text.replace("\n","  ")

article56=soup.find(class_="wsw").text.replace("\n","  ")

data56=[[url56,title56,publishdate56,links56,article56]]

url57='https://www.voanews.com/a/who-are-the-houthis-and-why-did-the-us-and-uk-launch-strikes-on-them-/7437022.html'
page57=requests.get(url57)
soup=BeautifulSoup(page57.content,'html.parser')

title57=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate57=soup.find(class_="published").text.replace("\n","  ")

links57=soup.find(class_="links__item").text.replace("\n","  ")

article57=soup.find(class_="wsw").text.replace("\n","  ")

data57=[[url57,title57,publishdate57,links57,article57]]

url58='https://www.voanews.com/a/us-uk-strike-back-at-several-houthi-sites-in-yemen-/7436954.html'
page58=requests.get(url58)
soup=BeautifulSoup(page58.content,'html.parser')

title58=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate58=soup.find(class_="published").text.replace("\n","  ")

links58=soup.find(class_="links__item").text.replace("\n","  ")

article58=soup.find(class_="wsw").text.replace("\n","  ")

data58=[[url58,title58,publishdate58,links58,article58]]

url59='https://www.voanews.com/a/blinken-sissi-to-discuss-israel-hamas-war/7435338.html'
page59=requests.get(url59)
soup=BeautifulSoup(page59.content,'html.parser')

title59=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate59=soup.find(class_="published").text.replace("\n","  ")

links59=soup.find(class_="links__item").text.replace("\n","  ")

article59=soup.find(class_="wsw").text.replace("\n","  ")

data59=[[url59,title59,publishdate59,links59,article59]]

url60='https://www.voanews.com/a/biden-not-signaling-for-gaza-cease-fire-white-house-says/7433667.html'
page60=requests.get(url60)
soup=BeautifulSoup(page60.content,'html.parser')

title60=soup.find(class_="title pg-title").text.replace("\n","  ")

publishdate60=soup.find(class_="published").text.replace("\n","  ")

links60=soup.find(class_="links__item").text.replace("\n","  ")

article60=soup.find(class_="wsw").text.replace("\n","  ")

data60=[[url60,title60,publishdate60,links60,article60]]






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
    [url20,title20,publishdate20,links20,article20],
    [url21,title21,publishdate21,links21,article21],
    [url22,title22,publishdate22,links22,article22],
    [url23,title23,publishdate23,links23,article23],
    [url24,title24,publishdate24,links24,article24],
    [url25,title25,publishdate25,links25,article25],
    [url26,title26,publishdate26,links26,article26],
    [url27,title27,publishdate27,links27,article27],
    [url28,title28,publishdate28,links28,article28],
    [url29,title29,publishdate29,links29,article29],
    [url30,title30,publishdate30,links30,article30],
    [url31,title31,publishdate31,links31,article31],
    [url32,title32,publishdate32,links32,article32],
    [url33,title33,publishdate33,links33,article33],
    [url34,title34,publishdate34,links34,article34],
    [url35,title35,publishdate35,links35,article35],
    [url36,title36,publishdate36,links36,article36],
    [url37,title37,publishdate37,links37,article37],
    [url38,title38,publishdate38,links38,article38],
    [url39,title39,publishdate39,links39,article39],
    [url40,title40,publishdate40,links40,article40],
    [url41,title41,publishdate41,links41,article41],
    [url42,title42,publishdate42,links42,article42],
    [url43,title43,publishdate43,links43,article43],
    [url44,title44,publishdate44,links44,article44],
    [url45,title45,publishdate45,links45,article45],
    [url46,title46,publishdate46,links46,article46],
    [url47,title47,publishdate47,links47,article47],
    [url48,title48,publishdate48,links48,article48],
    [url49,title49,publishdate49,links49,article49],
    [url50,title50,publishdate50,links50,article50],
    [url51,title51,publishdate51,links51,article51],
    [url52,title52,publishdate52,links52,article52],
    [url53,title53,publishdate53,links53,article53],
    [url54,title54,publishdate54,links54,article54],
    [url55,title55,publishdate55,links55,article55],
    [url56,title56,publishdate56,links56,article56],
    [url57,title57,publishdate57,links57,article57],
    [url58,title58,publishdate58,links58,article58],
    [url59,title59,publishdate59,links59,article59],
    [url60,title60,publishdate60,links60,article60]
    ]
    ,columns=['URL','Title','PublishDate','Links','Article'])


df.to_csv("final report.csv",index=False)

print('ok')