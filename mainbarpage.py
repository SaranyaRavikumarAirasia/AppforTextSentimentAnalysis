import streamlit as st
import sidebarpage
import textblobalgthm
page=sidebarpage.show()
if(page=="TextBlob Analysis"):
  textblobalgthm.displayPage()
