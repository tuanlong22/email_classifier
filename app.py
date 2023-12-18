import pickle
import streamlit as st
import sys
from streamlit_option_menu import option_menu
import json 

sys.path.insert(1,"C:\Users\admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\streamlit_option_menu")
model = pickle.load(open("spam.pkl","rb"))
cv = pickle.load(open("vectorizer.pkl","rb"))

st.set_page_config(
    page_title="Spam Email Detector App",
    page_icon="📫",
)
def main():
    st.title("Hệ thống nhận diện Spam Email :envelope_with_arrow:")
    st.sidebar.success("Select a page above.")
    st.subheader("Thực hiện bởi nhóm 6 :two_hearts:")
    msg = st.text_input("Enter a Text:")
    if st.button("Dự đoán"):
        data = [msg]
        vect = cv.transform(data).toarray()
        prediction = model.predict(vect)
        result = prediction[0]
        if result == 1:
            st.error("Đây là Spam Mail :outbox_tray:")
        else:
            st.success("Đây không phải là spam mail :incoming_envelope:")

main()
