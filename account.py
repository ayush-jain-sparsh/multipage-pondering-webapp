import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('pondering-tutorial-54749-9aeaba71c87b.json')
#firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome To:red[ Account Section]')

    if 'username' not in st.session_state :
        st.session_state.username = ""
    if 'useremail' not in st.session_state :
        st.session_state.useremail = ""

    if 'signedout' not in st.session_state :
        st.session_state.signedout = False
    if 'signout' not in st.session_state :
        st.session_state.signout = False
    
    def check():
        try:
            user = auth.get_user_by_email(email)
            st.success(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True
        except :
            st.warning('Login Failed')

    def signOut():
        st.session_state.signedout = False
        st.session_state.signout = False
        st.session_state.useremail = ""
        st.session_state.username = ""
    
    if not st.session_state["signedout"] :
        choice = st.selectbox('Login/SignUp',['Login','Sign Up'])

        email = st.text_input('Email ID :')
        password = st.text_input('Password :',type='password')
        if choice == 'Login' :
            st.button('Login' , on_click=check) # Call check function(User Made) to verify things
        else :
            username = st.text_input('Select Unique User Name :')
            if st.button('Create My Account') :
                user = auth.create_user(email = email , password = password , uid = username)
                st.success('Account Created Successfully')
                st.markdown('Please Login Using email id and password')
                st.balloons()
    if st.session_state.signout :
        st.text('User Name : '+ st.session_state.username)
        st.text('Email Id : '+ st.session_state.useremail)
        st.button('Sign Out' , on_click= signOut)