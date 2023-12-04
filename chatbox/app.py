import streamlit as st

from chatbox.bot import generate_response

st.set_page_config(page_title="Chatbox", page_icon="📦", layout="wide")


st.title("Chatbox 📦")


def main():
    with st.form("my_form"):
        text = st.text_area("Enter text:", "Recommend me a bomb vegan recipe")
        if st.form_submit_button("Submit"):
            st.info(generate_response(text))


if __name__ == "__main__":
    main()
