

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
def plotBar(labels, values):
    fig = go.Figure(
        go.Bar(
        labels = labels,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig)

       
def textEmot(userText):
    emotion = dict(te.get_emotion(userText))
    return emotion

def getSentiments(userText):
    emotion1=textEmot(userText)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Happy 😊", emotion1['Happy'], None)
    col2.metric("Sad 😔", emotion1['Sad'], None)
    col3.metric("Angry 😠", emotion1['Angry'], None)
    col4.metric("Fear 😨", emotion1['Fear'], None)
    col5.metric("Surprise 😲", emotion1['Surprise'], None)
    print(emotion1)
    plotBar(list(emotion1.keys()), list(emotion1.values()))  
     
       
def displayPage():
    st.subheader("User Input Text Analysis")
    st.text("Analyzing text data given by the user and find sentiments within it.")
    st.text("")
    userText = st.text_input('User Input', placeholder='Input text HERE')
    st.text("")
    if st.button('Predict'):
        if(userText!=""):
            st.text("")
            st.components.v1.html("""<h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>""", height=100)
            getSentiments(userText)

          

