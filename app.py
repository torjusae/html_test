from PIL import Image
import requests
import streamlit as st
import streamlit.components.v1 as components

with st.container():
    HtmlFile = open("geithusfoss_export_html.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code)