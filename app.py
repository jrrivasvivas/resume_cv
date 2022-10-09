import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# frind more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="JoseRoberto Portfolio", page_icon=":rocket:", layout="wide")


lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")


# ---- Header Section ------
with st.container():
    st.subheader("Hi, I am Jose Roberto :wave:")
    st.title("A Data Analayst from Venezuela" )

    st.write("I am passionate about finding ways to use Python and VBA to be more efficience.")

#--- What i do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Provided quantitative analyses using multiples data sets to understand business questions and problems.

            - Designed a data model to classify the maintenance of radio bases stations according to historical consumption.

            - Designed data processes and deployment solutions to provide AI and ML insights to the Network Operation Center. 

            - Coached data team through short and long-term projects on how to improve their storytelling and streamline visualizations.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")