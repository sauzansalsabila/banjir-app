import streamlit as st
import pickle
from PIL import Image
#membaca model
databanjir = pickle.load(open("coba.csv", "rb"))

#judul web
st.title("UJIAN AKHIR SISTEM INFORMASI KELAUTAN")
st.write('Hello Word!')
