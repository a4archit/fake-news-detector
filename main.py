import streamlit as st



# ***************** Streamlit working: starts ************** #

# ------------------ Sidebar -------------------------- #

st.sidebar.title("About the developer")
st.sidebar.divider()
st.sidebar.write("I am creating this web application with \
**Streamlit** and build a **Deep LSTM Model** that able \
to detect fake news with an accuracy of **91.29**%. \
Point to Remember that, In this model there is no any proper NLP Pipeline is used. ")
st.sidebar.write("You can check my social media accounts: ")
st.sidebar.write("[Website](https://a4archit.github.io/my-portfolio)")
st.sidebar.write("[Kaggle](https://www.kaggle.com/architty108)")
st.sidebar.write("[Github](https://www.github.com/a4archit)")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/archit-tyagi-191323296)")



st.header("Fake News Detector")

st.divider()


# showing information to the user
info = """\
Real News:
> Pahalgam terror attack: Mallikarjun Kharge claims PM Modi cancelled Kashmir visit after receiving intelligence report.


\n\n
Fake News:
> *Update in future*
"""

st.write(info)




#       Taking a news from user

news = st.text_input(
    label = "Enter a news headline here: ",
    key = "news_input",
    max_chars = 250, # 📖
    icon = "📝"
)
