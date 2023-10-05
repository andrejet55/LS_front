import streamlit as st

from streamlit_option_menu import option_menu


import home, test, about, andrea



st.set_page_config(
        page_title="LinkScribe",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
             
        test.app()          
            
             
          
             
    run()            
         
