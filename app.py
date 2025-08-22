#venv olustur
#python3 -m venv env
#source env/bin/activate

#requirements.txt olustur
#streamliti ekle
#terminalde pip install -r requirements.txt



#Üretken Yapay Zeka ile Uygulama Geliştirme Eğitimi
#Modül 1: Streamlit ile Hizlı Prototipleme
#Streamlit101

#1 Streamlit kütüphanesini ekleme

import streamlit as st

#2 Streamlit uygulamasını başlatma

#st.write("Hello World")

#3 Streamlit ile sayfa bilgilerini düzenleme

#bu metod streamlit uygulamasının başında olmalı
st.set_page_config(page_title="Steamlit 101", page_icon=":robot_face:")

#4 Streamlit ile metin gösterme

st.write("En yaygan metin gösterme yöntemi")

st.markdown("_Biçimlendirilmiş Metin_")

st.header("Bu bir header örneği")

st.subheader("Bu ise bir subheader örneği")

st.code('for i in range(10): my_function()')

st.latex(r'''e^{i\pi} +1=0 ''')


#5 Streamlit ile multimedya gösterme

# st.image(image="1-image_sample.png")

# st.video(data="2-video_sample.mp4")

# st.audio(data="3-audio_sample. mp3")


#6 Streamlit ile kullanıcı etkileşimi (button, radio, checkbox, slider, number input, file uploader)

st.write("Lütfen Bilgilerinizi Girin")

st.text_input(label="Lütfen e-posta adresinizi giriniz:")

st.text_input(label="Lütfen şifrenizi giriniz:", type="password")

st.checkbox(label="Şifremi Unuttum")

st.divider()

st.number_input(label="Lütfen yasinizi giriniz:", min_value=18, max_value=40, value=22)

st.slider(label="Lutfen yasinizi giriniz:", min_value=18, max_value=40, value=22)

st.divider()

st.radio(label="Statünüz Nedir?", options=["Öğrenci", "Mezun"])

st.button(label="Giriş Yap")

st.divider()

st.file_uploader(label="Dosya Yüklemek İçin Tiklayiniz")

st.divider()
st.divider()
st.divider()

#7 Streamlit ile ara yüz yerleşimi (col, tab, sidebar)

import json

st.sidebar.markdown("<h4>Uygulamamiza Hos geldin!</h4>", unsafe_allow_html=True)
#st.sidebar.image("1-image_sample.png")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3><b> Kullanici Bilgileri </b> </h3>", unsafe_allow_html=True)
    st.text_input(label="E-Posta Adresinizi Giriniz:")
    st.text_input(label="$ifrenizi Giriniz", type="password")
    st.checkbox(label="$ifremi Unuttum")
    st.divider()
    st.button(label="Giris Yap")

with col2:
    st.markdown("<h3><b> Kullanma Tercihleri </b> </h3>", unsafe_allow_html=True)
    st.divider()
    st.radio(label="Hesap Türü", options=["Öğrenci", "Mezun"])
    st.slider(label="Zaman Aşım Süresi (saniye)", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Güncel Özgeçmişinizi Yükleyiniz")

st.divider()
st.divider()
st.divider()

tab1, tab2 = st.tabs(["Kullanici Bilgileri", "Kullanma Tercihleri"])

with tab1:
    eposta = st.text_input(label="E-Posta Adresiniz:")
    sifre = st.text_input(label="Şifreniz", type="password")
    st.checkbox(label="Unuttum")
    st.divider()
    kaydet_btn = st.button(label="Kaydet")

with tab2:
    hesap_turu =st.radio(label="Hesap", options=["Öğrenci", "Mezun"])
    st.slider(label="Zaman Aşıma Süresi", min_value=3, max_value=30, value=5)
    st.file_uploader(label="Güncel Özgeçmişinizi Yükleyin")


if kaydet_btn:
    data = []
    data.append({"eposta": eposta})
    data.append({"sifre": sifre})

    if hesap_turu == "Öğrenci":
        gecerlilik_suresi = 365
    elif hesap_turu == "Mezun":
        gecerlilik_suresi = 30

    data.append({"geçerlilik süresi": gecerlilik_suresi})

    with open("kullanici.txt", "w") as file:
        file.write(json.dumps(data))    


    st.balloons()
    st.success("Bilgileriniz Kaydedildi!")
    st.write(f"belirlenen gecerlilik süresi: {gecerlilik_suresi} gün")


#8 Streamlit bileşenleriyle program akışı
#9 Streamlit ile session state