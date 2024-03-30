import streamlit as st
import plotly.express as px
import glob
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('stopwords')
nltk.download('vader_lexicon')

english_stopwords = stopwords.words("english")

filepaths = glob.glob('Diary/*.txt')

analyzer = SentimentIntensityAnalyzer()

Dates = []
Pos = []
Neg = []
for filepath in filepaths:
    with open(f"{filepath}","r") as file:
        filestring = file.readline()
        scores = analyzer.polarity_scores(filestring)

        positive_score = scores['pos']
        negative_score = scores['neg']
        
        #Get the date from the filename
        y = filepath.split(".")
        y = y[0].split("\\")
        Dates.append(y[1])
        Pos.append(positive_score)
        Neg.append(negative_score)

figure1 = px.line(x=Dates, y=[float(y) for y in Pos])
figure2 = px.line(x=Dates, y=[float(y) for y in Neg])

# Adding x and y labels to figure1
figure1.update_layout(
    xaxis_title="Date",
    yaxis_title="Positive Scores"
)

# Adding x and y labels to figure2
figure2.update_layout(
    xaxis_title="Date",
    yaxis_title="Negative Scores"
)

#Frontend
st.title("Diary Tone")
st.subheader("Positivity")
st.plotly_chart(figure1,x ="Test")
st.subheader("Negativity")
st.plotly_chart(figure2)