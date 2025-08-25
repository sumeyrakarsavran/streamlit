import streamlit as st

#session state, streamlitin bizim icin olusturdugu ve surekli guncelledigi bir konteynerdir
#yani bir takim verileri tasimamiza muhafaza etmemize yardimci olur

import pandas as pd

st.header("Session State Mekanizması: Pratik Kullanım")

if "satir_sayisi" not in st.session_state:
    st.session_state.satir_sayisi = 10

dataframe = pd.read_csv("data.csv", sep=",")

st.table(dataframe.head(st.session_state.satir_sayisi))

def artir():   #callback fonksiyonu
    st.session_state.satir_sayisi += 1

def dusur():
    st.session_state.satir_sayisi -= 1

artir_btn = st.button(label="Artir")
dusur_btn = st.button(label="Düşür")

st.divider()
st.header(st.session_state.satir_sayisi)






'''
st.session_state.mesaj = "Merhaba"
st.session_state.yil= 2023
st.session_state['kullanici'] = "admin"
st.session_state["Kullan1ici Adi"] = "Miuu1"
gunler = ["Pazartesi", "Sali", "Çarşamba", "Perşembe", "Cuma"]
st.session_state.liste = gunler

st.write(st.session_state)

st.session_state.yil += 10

st.write(st.session_state)

st.session_state.eposta = st.text_input(label="Epostanizi Giriniz")
st.text_input(label="Şifrenizi Giriniz", type="password", key="sifre")

goruntule_btn = st.button(label="Görüntüle")

if goruntule_btn:
    st.info(st.session_state.eposta)
    st.info(st.session_state.sifre)


'''


