import pickle
import streamlit as st
import json 

model = pickle.load(open("spam.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(
    page_title="Spam Email Detector App",
    page_icon="📫",
)

def detect_spam(emails):
    spam_titles = []
    ham_titles = []
    for email in emails:
        vect = cv.transform([email["body_text"]]).toarray()
        prediction = model.predict(vect)
        if prediction[0] == 1:
            spam_titles.append(email["subject"])
        else:
            ham_titles.append(email["subject"])
    return spam_titles, ham_titles

def main():
    st.title("Hệ thống nhận diện Spam Email :envelope_with_arrow:")
    st.sidebar.success("Chào mừng đến với hệ thống nhận diện spam!")

    st.subheader("Nhận diện thư rác từ JSON File")
    uploaded_file = st.file_uploader("Upload a JSON file", type=["json"])

    if uploaded_file is not None:
        try:
            emails = json.load(uploaded_file)
            spam_titles, ham_titles = detect_spam(emails)

            st.success(f"Detected {len(spam_titles)} spam emails and {len(ham_titles)} ham emails.")
            
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Spam Email Titles")
                for i, spam_title in enumerate(spam_titles, 1):
                    st.write(f"{i}. {spam_title}")

            with col2:
                st.subheader("Ham Email Titles")
                for i, ham_title in enumerate(ham_titles, 1):
                    st.write(f"{i}. {ham_title}")

        except json.JSONDecodeError:
            st.error("Invalid JSON file. Please upload a valid JSON file.")

main()
