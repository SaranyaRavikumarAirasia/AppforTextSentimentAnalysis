import streamlit as st
import sidebarpage
import textblobalgthm
import texttoemot
page=sidebarpage.show()
if(page=="TextBlob Analysis"):
  textblobalgthm.displayPage()
elif(page=="Text2Emotion Analysis"):
  texttoemot.displayPage()
