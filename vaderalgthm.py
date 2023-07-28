import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def displayPage():
  st.subheader("Text Analysis using VADER")
  st.text("Enter the input text to analyze")
  userText = st.text_input('User Input', placeholder='Input text HERE')
  st.text("")
  if st.button('Predict'):
    if(userText!=""):
      st.components.v1.html("""<h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>""", height=100)
      getSentiments(userText)

def getSentiments(userText):
  compoundscore1,vadermaxscore1,status1=getVaderscore(userText)
  if(status1=="Positive"):
    image1 = Image.open('images/positive.PNG')
  elif(status1 == "Negative"):
    image1 = Image.open('images/negative.PNG')
  else:
    image1 = Image.open('images/neutral.PNG')
  col1, col2, col3= st.columns(3)
  col1.metric("Compound Score",compoundscore1, None)
  col2.metric("VaderMaximum(Positive/Negative) Score",vadermaxscore1 , None)
  col3.metric("Result",status1, None)
  st.image(image1, caption=status1)


def getVaderscore(userText):
  vd = SentimentIntensityAnalyzer().polarity_scores(userText)
  compoundscore = vd['compound']
  positivescore=vd['pos']
  negativescore=vd['neg']
  neutralscore=vd['neu']
  if compoundscore >= 0.05 :
    return compoundscore, positivescore,"Positive"
  elif compoundscore <= - 0.05 :
    return compoundscore, negativescore,"Negative"
  else:
    return compoundscore, neutralscore,"Neutral"
