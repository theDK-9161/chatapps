import streamlit as st
from pymongo.mongo_client import MongoClient
import pymongo
import requests
import threading
import time
import bson
import datetime
import pytz
uri = "mongodb+srv://gembot:footfootfoot444@cluster0.ort1r.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
dbclient = MongoClient(uri)
# Send a ping to confirm a successful connection

db = dbclient["gemmy"]
collection = db["footcoin"]
promocodes = db['promocodes']
globalmsgs = db["global-msgs"]
messages1 = db["chatMESSAGES"]

color = ''

st.title("Clush - Special Force Group")
st.header("Chat App")
def send_message():
    messages1.insert_one({'name': "TestSubject", 'message': f"{st.session_state.user_name}: {st.session_state.user_input}", 'time': datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc), 'color': st.session_state.message_color})
prompt = st.chat_input("Type a message...", on_submit=send_message, key='user_input')


st.color_picker('Pick the color you want your message to be.', '#FFFFFF', key='message_color')
st.text_input('Enter your username here!', key='user_name')
@st.fragment(run_every="5s")
def reload_messages():
    messages = []
    print("/")
    print("?")
    for msg in messages1.find():
        messages.append({'name': msg['color'], 'color': msg['color'], 'message': msg['message'], 'time': msg['time']})
    for message in messages:
        python_datetime = message["time"].astimezone(pytz.timezone("US/Pacific"))
        formatted_date = python_datetime.strftime('%Y-%m-%d %I:%M:%S %p')
        messageUser = st.chat_message(message['name'])
        messageUser.write(f'<p style="text-color: #b4b4b4; font-size: 14px;">{formatted_date}</p><span style="color:{message["color"]}">{message["message"]}</span>', unsafe_allow_html=True)


reload_messages()
