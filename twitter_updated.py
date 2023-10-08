import streamlit as st
#import streamlit_authenticator as stauth
#from streamlit_option_menu import option_menu
# import yaml
# import sqlite3 
# import os
# import glob
# import pandas as pd
# import random
# from serpapi import GoogleSearch
# from streamlit_text_rating.st_text_rater import st_text_rater
# from streamlit_extras.stoggle import stoggle
# from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.colored_header import colored_header
from datetime import date
#import streamlit.components.v1 as components
# import numpy as np
import tempfile
from pathlib import Path
import tweepy as tw
# from streamlit_elements import elements, mui, html
from st_aggrid import AgGrid
#import pyperclip
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# import plotly_express as px
#from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
today = date.today()
#import base64
#from streamlit_quill import st_quill
#from google_trans_new import google_translator
#from googletrans import Translator
# from google_trans_new import google_translator
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
# translator = google_translator()
from googletrans import Translator
translator=Translator()
trans=Translator()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
#translator = google_translator()
st.set_page_config(layout='wide')
#from pandas import json_normalize

hide_menu="""
<style>

footer{
visibility:visible;
}
footer:after{
content: 'Copyright @ MHA 2023';
display:block;
position:relative;
color:tomato;
padding:5px;
top:3px;
}
</style>
"""


API_key = 'KdYjNSxDgvGvH8uIGczNrLM1k'
API_secret_key = '3RjTLc9lH3e8Rrjc0qguyZtlS5ICZtbLGS9vrEe5cXlLCld8Cs'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAG%2FvLAEAAAAAb49MZ3oaTCGg3eNJNEtE6ttnr4g%3DAxyiPxaMKSQo0pJnUNbVuzKwORd55rlvmobwB5BhaidjWk8tEs'
access_token = '1345774941392707585-euj6EyBkRNsexAlnkVQYroNVF5EUZl'
access_token_secret = 'VQrZuvRbw3daEV7pyMCloCaQ1QeXqFXnMVQkOQ6Uab9bP'
st.markdown(hide_menu,unsafe_allow_html=True)
        
auth = tw.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
client = tw.Client(
    consumer_key=API_key,
    consumer_secret=API_secret_key,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token
)



   #st.info('Logged In successfully')
#menu =['Post tweet','Post media with tweet','Fetch recent tweets','Search users']
menu =['Post tweet','Post media with tweet']
choice = st.sidebar.selectbox("Select the function",menu)
def create_thread(message_text, media_ids=None):
    tweets = [message_text[i:i + 280] for i in range(0, len(message_text), 280)]
    if media_ids:
        response = client.update_status(status=tweets[0], media_ids=media_ids)
    else:
        response = client.create_tweet(text=tweets[0])
    for tweet in tweets[1:]:
        response = client.create_tweet(text=tweet, in_reply_to_tweet_id = tweet.data['id'])
    return response

if choice == 'Post tweet':
       st.subheader('Posting tweet')
       with st.form(key='formtwit'):

           tweet=st.text_input('enter the tweet')
           n = 270
           
            
            
           sel1 = st.selectbox('Select the language',['English','Hindi','Bengali','Marathi','Gujarati','Kannada','Tamil','Urdu','Malayalam','Telugu'])
           if sel1 == 'English':
                    lang = 'en'
           if sel1 == 'Hindi':
                    lang = 'hi'
           if sel1 == 'Bengali':
                    lang = 'bn'
           if sel1 == 'Marathi':
                    lang = 'mr'
           if sel1 == 'Gujarati':
                    lang = 'gu'
           if sel1 == 'Kannada':
                    lang = 'kn'
           if sel1 == 'Telugu':
                    lang = 'te'
           if sel1 == 'Tamil':
                    lang = 'ta'
           if sel1 == 'Urdu':
                    lang = 'ur'
           if sel1 == 'Malayalam':
                    lang = 'ml'
        #    if sel1 == 'English':
        #        tweet1 = translator.translate(tweet,dest='en')
        #    if sel1 == 'Hindi':
        #        tweet1 = translator.translate(tweet,dest='hi')
        #    if sel1 == 'Bengali':
        #        tweet1 = translator.translate(tweet,dest='bn')
        #    if sel1 == 'Marathi':
        #        tweet1 = translator.translate(tweet,dest='mr')
        #    if sel1 == 'Gujarati':
        #        tweet1 = translator.translate(tweet,dest='gu')
        #    if sel1 == 'Kannada':
        #        tweet1 = translator.translate(tweet,dest='ka')
        #    if sel1 == 'Tamil':
        #        tweet1 = translator.translate(tweet,dest='ta')
        #    if sel1 == 'Telugu':
        #        tweet1 = translator.translate(tweet,dest='te')
        #    if sel1 == 'Malayalam':
        #        tweet1 = translator.translate(tweet,dest='ml')
        #    if sel1 == 'Urdu':
        #        tweet1 = translator.translate(tweet,dest='ur')
           
           submitted1 = st.form_submit_button('Post tweet')
           if submitted1:
            tweet1 = translator.translate(tweet,dest=lang)
            final = tweet1.text
            #create_thread(final)
            total = len(final)
            if total >= n:
                total_parts=int(round(total/n))
                words = iter(final.split())
                lines, current = [], next(words)
                for word in words:
                    if(len(current) + 1 + len(word) > n):
                        lines.append(current)
                        current = word
                    else:
                        current += " " + word

                lines.append(current)

                for a in range(total_parts+1):    
                                       
                        part=lines[a]
                   
                        if a==0:
                            st.write("ok")
                    
                            result = client.create_tweet(text=part)
                            print(result)
                            
                        else:
                            
                            p = client.create_tweet(text=part,in_reply_to_tweet_id = result.data['id'])

                st.success('Tweeted') 
                          
            else:
                result = client.create_tweet(text= final)
                #print("nowwww................................",result.data['id'])
               #api.update_status(tweet1)
            st.success('Tweeted')
if choice == 'Post media with tweet':
       st.subheader('Posting media with tweet')
       with st.form(key='formtwit'):

           tweet=st.text_input('enter the caption')
           n=270
           media_file = st.file_uploader("Upload Media")
           if media_file is not None:
            #    if media_file.type == 'mp3':
            #        b = media_file.read()
            #        fp = Path(b.name)
            #        fp.write_bytes(b.getvalue())
            #audio_bytes = media_file.read()
       # Make temp file path from uploaded file
               with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                
                fp = Path(tmp_file.name)
             

                fp.write_bytes(media_file.getvalue())
                   #st.write(show_pdf(tmp_file.name))

           sel1 = st.selectbox('Select the language',['English','Hindi','Bengali','Marathi','Gujarati','Kannada','Tamil','Urdu','Malayalam','Telugu'])
           if sel1 == 'English':
                    lang = 'en'
           if sel1 == 'Hindi':
                    lang = 'hi'
           if sel1 == 'Bengali':
                    lang = 'bn'
           if sel1 == 'Marathi':
                    lang = 'mr'
           if sel1 == 'Gujarati':
                    lang = 'gu'
           if sel1 == 'Kannada':
                    lang = 'kn'
           if sel1 == 'Telugu':
                    lang = 'te'
           if sel1 == 'Tamil':
                    lang = 'ta'
           if sel1 == 'Urdu':
                    lang = 'ur'
           if sel1 == 'Malayalam':
                    lang = 'ml'
           submitted = st.form_submit_button('Post tweet')
           if submitted:
               
               uplo = api.media_upload(fp)
               tweet2 = translator.translate(tweet,dest=lang)

               client.create_tweet(text=tweet2.text, media_ids=[uplo.media_id_string])
               #api.update_with_media(fp,tweet1)
               st.success('Tweeted')


# if choice == 'Fetch recent tweets':
#        st.subheader('Fetching recent tweets..')
#        with st.form(key='formtwit'):

#            search_words = st.text_input('Enter the hastag')
#            #number_of_tweets = st.number_input('Enter the number of latest tweets(Maximum 50 tweets)', 0,50,10)
#            submitted = st.form_submit_button('Submit')
#            if submitted:
#                #client = tw.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAG%2FvLAEAAAAAb49MZ3oaTCGg3eNJNEtE6ttnr4g%3DAxyiPxaMKSQo0pJnUNbVuzKwORd55rlvmobwB5BhaidjWk8tEs')
#                #tweets = client.search_all_tweets(query=search_words)
#                for tweet in tw.Paginator(client.search_all_tweets, search_words,
#                                 max_results=100,user_auth=True).flatten(limit=250):
#                     print(tweet.id)
 
#             #    tweets =tw.Paginator(client.search_recent_tweets, search_words)
#             #    print(tweets)
#             #    ids = []
#             #    createdat = []
#             #    userscreenname = []
#             #    texttweet = []
#             #    loc = []
#             #    for tweet in tweets:
#             #        ids.append(tweet.id_str)
#             #        #createdat.append(tweet.created_at)
#             #        userscreenname.append(tweet.user.screen_name)
#             #        texttweet.append(tweet.text)

                   
#             #        #st.write("TWEET ID:",tweet.id_str,"CREATED AT:",tweet.created_at,"\tUSER:",tweet.user.screen_name,"\tTWEET TEXT:",tweet.text,"\nGEO LOCATION:",tweet.user.location)
#             #        #st.write("\n")
#             #    dis_tweets = pd.DataFrame(list(zip(ids,userscreenname,texttweet)),
#             #    columns =['ID', 'Screen Name','Tweet'])
#             #    st.table(dis_tweets)

#        with st.form(key = 'newform'):
#                    st.subheader("Retweet Tweets")
#                    twid = st.text_input("Enter the tweet id to retweet")
#                    retw = st.form_submit_button('Retweet')
#                    if retw:
#                        api.retweet(twid)
#                        st.success('Retweeted!')
            
# if choice == 'Search users':
#        st.subheader('Searching Users..')
#        with st.form(key='formtwit'):
#             search_words = st.text_input('Enter the query')
#             #number_of_tweets = st.number_input('Enter the number of users(Max 50)', 0,50,10)
#             submitted = st.form_submit_button('Submit')
#             nm = []
#             scrnm = []
#             urls = []
#             if submitted:
#                 users = api.search_users(search_words)
#                 for user in users:
#                     nm.append(user.name)
#                     scrnm.append(user.screen_name)
#                     urls.append(user.url)
#                     #st.write(user.name,'-------',user.screen_name)
#                     #st.write(user.url)
#                     #st.write('\n')
#                 srch_usrs = pd.DataFrame(list(zip(nm,scrnm,urls)),
#                 columns =['Name', 'Screen Name','Associated Links(if any)'])
#                 st.table(srch_usrs)

                

#        with st.form(key = 'newfollowrm'):
#                    st.subheader("Follow User")
#                    twid = st.text_input("Enter user's screen name")
#                    retw = st.form_submit_button('Follow')
#                    if retw:
#                        api.create_friendship(screen_name=twid)
#                        st.success('Followed!')
    



# st.write("heloo")
# API_key = 'FZSz8FgQcHOrPWsXaRo37jivM'
# API_key_secret = 'X2JyBPj9xZz8LLWD5hkwKwx2tzrHGs5K9YRyhG7aCtgFjACrf5J'
# Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAAMG8kQEAAAAAam1a6Us4owKLETyQdib9m1ITtMI%3DyGIhJJrUcMBy44VvfWXysF3ULXDXclGsCRgH85Fmd1HAXKrsB6'
# access_token = '1601969777815453696-2JTqC6Y14JJafGy1aGzgvv5vzR0SWr'
# access_token_secret = 'JO6Y4HR1SUcfVPsTAfcNWmynD9yJOsS1jW3IYbzFhha0c'
# auth = tw.OAuthHandler(API_key, API_key_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tw.API(auth, wait_on_rate_limit=True)
# # API_key = 'Tjot57ysSbJRDliwI615EIIEQ'
# # API_secret_key = '60hksBXcDaBhJadiynQLB9oFIzYzaDzEILKtkmkkSzwAIDIwrL'
# # bearer_token = 'AAAAAAAAAAAAAAAAAAAAAG%2FvLAEAAAAAb49MZ3oaTCGg3eNJNEtE6ttnr4g%3DAxyiPxaMKSQo0pJnUNbVuzKwORd55rlvmobwB5BhaidjWk8tEs'
# # access_token = '1345774941392707585-euj6EyBkRNsexAlnkVQYroNVF5EUZl'
# # access_token_secret = 'VQrZuvRbw3daEV7pyMCloCaQ1QeXqFXnMVQkOQ6Uab9bP'
  
        
# # auth = tw.OAuthHandler(API_key, API_secret_key)
# # auth.set_access_token(access_token, access_token_secret)
# # api = tw.API(auth, wait_on_rate_limit=True)
# #cl = tw.Client(consumer_key = API_key,consumer_secret=API_key_secret,access_token=access_token,access_token_secret=access_token_secret)
# #res = cl.create_tweet(text='Hello')
# # cli_id = 'VV9yLWh4OFBkR2V5T1FLcm0yTjM6MTpjaQ'
# # cli_sec_id = 'HF4kEUqyJ0VEMNuuDBaScSYgZdqgEFsbl3x_w4b6gRrKgc9RHY'
# # auth = tw.OAuth1UserHandler(
# #     cli_id, cli_sec_id, access_token, access_token_secret
# # )

# #api = tw.API(auth)

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)
# with st.form(key='frst'):
#     tweet=st.text_input('enter the tweet')
#     k = st.form_submit_button("Okay")
# if k:
#     api.update_status(tweet)


