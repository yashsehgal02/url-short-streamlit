import streamlit as st 
import requests

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
    if check(Id_textbox) == "True":
        st.error("choose another Id")
    else:
        requests.get(post_db)
        shortned_url = f"https://url-shortner-yash.herokuapp.com/{Id_textbox}"
        st.success("Your URL has been shortened")
        st.write(f"Your shortened URL is: {shortned_url}")



