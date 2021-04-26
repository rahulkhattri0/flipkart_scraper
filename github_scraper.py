import streamlit as st
import requests
from bs4 import BeautifulSoup
def get_url(brand):
        domain='https://github.com/'
        keyword=brand
        url=domain+keyword.replace(' ','%20')
        return url
def fetchdata(url):
    try:
        data=requests.get(url)
        return data
    except Exception as e:
        print("some error")
        print(e)
def parseData(text):
    try:
        soup=BeautifulSoup(text,features='html.parser')
        return soup
    except Exception as e:
        print('error while parsing')
        print(e)
def users(usernames):
        soup=None 
        try:
            data=fetchdata(get_url(usernames))
            if data.status_code==200:
                soup=parseData(data.text)
                    
            elif data.status_code==404:
                st.warning('invalid username')
        except Exception as e:
            print(e)
    
        user_details=soup.find_all('div',attrs={'class':"h-card mt-md-n5"})
        for u in user_details:
            st.image(u.find('img').attrs.get('src'),caption="profile photo")
            st.header("FULL NAME")
            st.write(u.find('span',attrs={'class':'p-name vcard-fullname d-block overflow-hidden'}).text)
            st.header('user status')
            st.image(soup.find('g-emoji').attrs.get('fallback-src'))
            st.write(soup.find('div',attrs={'class':'user-status-message-wrapper f6 color-text-primary ws-normal lh-condensed'}).find('div').text)
st.title("GITHUB SCRAPER")
us=st.text_input("enter username")
users(us)
