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
#6 Streamlit ile kullanıcı etkileşimi (button, radio, checkbox, slider, number input, file uploader)
#7 Streamlit ile ara yüz yerleşimi (col, tab, sidebar)
#8 Streamlit bileşenleriyle program akışı
#9 Streamlit ile session state