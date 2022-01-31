import streamlit as st 
import requests
import re

# regex code taken from geeks for geeks
def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False

def check(name):
    data = requests.get("https://docs.google.com/spreadsheets/d/1QAUlWAbMRemISJJe0Ujjk0vdtz5oq67ZOG-GWcRlcII/gviz/tq?tqx=out:csv&tq=SELECT *")
    data_format = data.text.split("\n")
    data_final = [i.split(",") for i in data_format]
    ids = []
    for i in data_final:
        ids.append(i[0].replace('"',''))
    if name in ids:
        return "True"
    else:
        return "False"

st.title("Yash's URL Shortner")
url_textbox = st.text_input("Enter URL to be shortened",placeholder="url")
Id_textbox = st.text_input("Enter Id you want",placeholder="Id")
post_db = f"https://script.google.com/macros/s/AKfycbyO28VlEsqwwMWILb687tUg0-mmoAmGAQpd1Kat18vVoICpMy-KrXoitHYxLjpcdRLktQ/exec?url={url_textbox}&Unique_id={Id_textbox}"
if st.button("Shorten"):
    if url_textbox == "":
        st.error("Enter the URL to be shortened")
    if Id_textbox == "":
        st.error("Enter the Id")
    if "https://" not in url_textbox:
        url_textbox = f"https://{url_textbox}"
    else:
        if check(Id_textbox) == "True":
            st.error("choose another Id")
        else:
            requests.get(post_db)
            shortned_url = f"https://shortopop.herokuapp.com/{Id_textbox}"
            st.success("Your URL has been shortened")
            st.write(f"Your shortened URL is: {shortned_url}")






