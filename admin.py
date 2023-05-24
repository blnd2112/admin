import streamlit as st
from deta import Deta
from PIL import Image
import os
#from dotenv import load_dotenv
import secrets
import time

deta = Deta("d0ch7irs_xPBuMonK6BH8MS61RsHvQH9dkWDWD3XB")
# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("bb")
dbm = deta.Base("bbb")


primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

image4 = Image.open('4sss.png')
st.image(image4, width=400)












st.subheader("Welcome")
st.markdown("This is admin page so just you can use it...")
en = st.text_input("Enter your password")
l = st.button("log in ")

if en == "blnd":



    n = st.text_input("Name")
    nd = st.button("Add")
    if nd == True:
        ph = " "
        iit = db.put({"Name": n})
        st.write(f"{n} added")



else:
    st.write("incorrect password")



