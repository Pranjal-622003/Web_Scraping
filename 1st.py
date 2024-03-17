from bs4 import BeautifulSoup
import requests
import pandas as pd
df=pd.read_excel('input.xlsx')
url=df.URL
id=37
for link in url:
    data=requests.get(link)
    htmlContent=data.content
    soup=BeautifulSoup(htmlContent,'html.parser')
    title=soup.title.text
    title=title.split('|')[0]
    # print(title)
    f=open('web/'+str(id)+".txt","w")
    id+=1
    f.write(title)
    f.write('\n')
    try:
        para=soup.find_all('div',class_="tdb-block-inner td-fix-index")[14]
    except:
        try:
            para=soup.find('div',class_="td-post-content tagdiv-type")
        except:
            print('Page not found')
    try:      
        f.write(para.text+'\n')
    except:
        print('file not created')
    f.close()