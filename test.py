import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
#from google.cloud import firestore
#from google.oauth2 import service_account
import json
from fastapi import FastAPI, Request

#key_dict = json.loads(st.secrets["textkey"])
#cred = service_account.Credentials.from_service_account_info(key_dict)


# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

app = FastAPI()
app.state.db_state = False


@app.on_event("startup")
def load_model():
    """this function will run once when the application starts up"""
    print("Connecting to firebase...")
    if app.state.db_state == False:
        cred = credentials.Certificate("firestore-key.json")
        firebase_admin.initialize_app(cred)
        app.state.db_state = True
    print("Connected to the database successfully!")
    

def app():
# Usernm = []
    st.title('Welcome to :orange[LinkScribe] :globe_with_meridians:')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''



    def f(): 
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
	        

            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


        
    
        
    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if  not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        

        
        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password,uid=username)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()

                doc_ref = db.collection("users").document(username)
                doc_ref.set({'r':'r'},merge=True)
        else:
            # st.button('Login', on_click=f)          
            st.button('Login', on_click=f)
            
            
    if st.session_state.signout:
                st.text('Name '+st.session_state.username)
                st.text('Email id: '+st.session_state.useremail)
                st.button('Sign out', on_click=t) 
            
                
    

                            
    def ap():
        st.write('Posts')

    
