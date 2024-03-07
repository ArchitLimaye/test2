import streamlit as st
import time
login={"FS23AI001":"FS23AI001","FS23AI002":"FS23AI002","FS23AI003":"FS23AI003","FS23AI004":"FS23AI004"}
st.header("Login Form",divider="rainbow")
st.write("Valid only from fs1 to fs4")
email=st.text_input("Please enter your fs number: ")
password=st.text_input("Please enter password: ")
btn=st.button("Login")
if btn:
    with st.spinner('Wait for it...'):
        time.sleep(3)
    if email in login and login[email] == password:
        st.success("Login Successful")
        if email=="FS23AI001":
            st.title('Welcome Archit! :sunglasses:')
        elif email=="FS23AI002":
            st.title('Welcome Divya! :sunglasses:')
        elif email=="FS23AI003":
            st.title('Welcome Rashid! :sunglasses:')
        elif email=="FS23AI004":
            st.title('Welcome Nikhil! :sunglasses:')
        st.balloons()
    else:
        st.error("Login Failed!! Please try again!!!")
