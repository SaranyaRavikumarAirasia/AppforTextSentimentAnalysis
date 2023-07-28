import streamlit as st
import sidebarpage
import textblobalgthm
import texttoemotion
import vaderalgthm
page=sidebarpage.show()
if page=="Text2Emotion Analysis":
  texttoemotion.displayPage()
elif page=="TextBlob Analysis":
  textblobalgthm.displayPage()
elif page=="VADER Sentiment Analysis":
  vaderalgthm.displayPage()
