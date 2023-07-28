import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import text2emotion as te
import plotly.graph_object as go

def displayPage():
  st.subheader("Text analysis using Text2Emotion Algorithm")
  st.text("Enter the text to be analyzed")
  userText=st.text_input("User Input",placeholder="Input the text here")
  st.text("")
  if st.button("Predict"):
    if (userText!=""):
      
