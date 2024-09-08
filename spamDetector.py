import pickle
import streamlit as st

model=pickle.load(open('spam.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))

def main():
    st.title("Email Spam Classification")
    st.subheader("Built Using Streamlit & Python")
    msg=st.text_input("Enter a Text: ")
    if st.button("Predict"):
       data=[msg]
       vect=vectorizer.transform(data).toarray()
       prediction=model.predict(vect)
       result=prediction[0]
       if result == 1:
           st.error("This is a Spam Mail")
       else:
           st.success("This is a ham Mail")

main()