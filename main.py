import streamlit as st

from scripts import FakeNewsDetector

model = FakeNewsDetector()


# page general configurations
st.set_page_config("Fake News Detector", page_icon="🕵️‍♀️")


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
Demo of Real News:
> Israel’s military says it has fully disabled Yemen’s main airport with airstrikes.


\n\n
Demo of Fake News:
> In the Amazon forest an ant eat an elephant in mid night
"""

st.write(info)

st.divider()

col1, col2 = st.columns([2,1])


with col1:
    # Taking a news from user
    news = st.text_input(
        label = "Enter a news headline here: ",
        key = "news_input",
        max_chars = 250, # 📖
        icon = "📝"
    )

with col2:
    st.button(
        label = "Detect Now",
        key = 'detect_now_button_key',
        type = 'secondary',
        use_container_width = True,
        help = ""
    )


if st.session_state.detect_now_button_key:
    try:
        if news:
            # cleaning text
            news = news.lower().strip()

            label, confidense = model.predict(news)

            if label == 'real':
                msg = ":green[😃 Given news is real]"
            elif label == 'fake':
                msg = ":red[⚠️ Given news is fake]"
            else:
                msg = "😞 I am confused to detect it..."

            st.write(f"{round(confidense*100)}%")
            st.subheader(msg)

    except:
        pass
