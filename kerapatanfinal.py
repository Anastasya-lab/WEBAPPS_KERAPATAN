# library yang digunakan

import streamlit as st
import requests
import pandas as pd
import time

from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Membuat Option menu pada tampilan

with st.sidebar :
    selected = option_menu (
       menu_title='Main Menu',
       options=['Halaman Utama','Kerapatan Curah','Kerapatan Absolut dan Kerapatan Relatif', 'Tabel Kerapatan Air' ] )
    
# Halaman Utama Homescreen

if selected == 'Halaman Utama':
    st.markdown("<h1 style='text-align: center; color: red;'>APLIKASI PERHITUNGAN KERAPATAN</h1>", unsafe_allow_html=True)
    st.markdown('----')
    st.markdown("<h5 style='text-align: center; color: black;'> Aplikasi yang dapat membantu anda untuk menghitung kerapatan curah, kerapatan absolut, dan kerapatan relatif. </h5>", unsafe_allow_html=True)
    

    #Menampilkan animasi pada homescreen
    
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_1 = 'https://assets6.lottiefiles.com/packages/lf20_hgjskqs0.json'
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key = 'hello')
    
    st.markdown("<h5 style='text-align: center; color: red;'>APA SIH BEDANYA KERAPATAN CURAH, KERAPATAN ABSOLUT, DAN KERAPATAN RELATIF</h5>", unsafe_allow_html=True)
    
    #Menampilkan informasi seputar perbedaan kerapatan curah, absolut, relatif
    
        
    col1, col2, col3, = st.columns([1,2,1])
    col1.markdown(' # Kerapatan Curah')
    col1.markdown (':green[Kerapatan Curah] adalah bobot bahan padat berbentuk butiran dibagi volume curah yaitu volume bahan dalam bentuk tercurah seperti beras pada takaran.   Rumus kerapatan curah : ')
    
    col2.markdown("<h1 style='text-align: center; color:green;'>Kerapatan Absolut </h1>", unsafe_allow_html=True)
    col2.markdown(':green[Kerapatan Absolut] adalah bobot bahan dibagi volume nyata bahan. Untuk benda yang bersifat curah, volume nyata adalah volume curah dikurangi volume udara di antara butiran-butiran bahan. Volume celah-celah butiran ini bisa diketahui dengan cara menambahkan cairan (yang akan mengisi celah-celah butiran) yang tidak bereaksi (diserap, diresapatau membentuk ikatan) dengan bahan.')
    
    col3.markdown(' # Kerapatan Relatif ')
    col3.markdown(':green[Kerapatan Relatif] perbandingan kerapatan bahan dengan kerapatan air pada temperatur dan tekanan yang sama.')
    

# Halaman Perhitungan Kerapatan Curah

if selected == 'Kerapatan Curah':
    st.markdown("<h3 style='text-align: center; color:red ;'> PERHITUNGAN KERAPATAN CURAH </h3>", unsafe_allow_html=True)
    st.markdown('----')
    st.markdown('''Rumus mencari kerapatan curah : ''')
    st.latex(r''' Bobot Sampel/ Volume Curah
    ''')
    
    # Input

    Bobot_gelas_kosong = st.number_input(
        "Masukkan Bobot Gelas kosong (g)",
        step=1e-6,
        format="%.4f")                                
    
    Bobot_gelas_sampel = st.number_input(
        "Masukkan Bobot gelas yang Berisi sampel (g)",
        step=1e-6,
        format="%.4f")
    
    Volume_curah = st.number_input("Masukkan Volume curah(mL)")
    
    #Tombol Hasil Perhitungan
    
    tombol = st.button('Lihat hasil perhitungan')
    with st.spinner('Memproses hasil...'):
        time.sleep(2)
        if tombol:
            st.write(f':blue[Nilai Kerapatan Curah dalam satuan (g/mL) adalah : ]', round (((Bobot_gelas_sampel)- (Bobot_gelas_kosong)) / (Volume_curah), 4))
  
    
# Halaman Perhitungan Kerapatan Absolut

if selected == 'Kerapatan Absolut dan Kerapatan Relatif':
    st.markdown("<h3 style='text-align: center; color:red ;'> PERHITUNGAN KERAPATAN ABSOLUT </h3>", unsafe_allow_html=True)
    st.markdown('----')
    st.markdown('Rumus mencari kerapatan Absolut :')
    st.latex(r''' Bobot sampel / Volume Nyata
    ''')
    st.markdown('''Rumus mencari kerapatan Relatif  : ''')
    st.latex(r'''  Kerapatan Absolut / Kerapatan Air 
    ''')
   
    
    # Input
    Volume_air_awal = st.number_input("Masukkan Volume Awal Air (mL)")
    
    Bobot_gelas_air = st.number_input(
        "Masukkan Bobot Gelas yang Berisi Air (g)",
        step=1e-6,
        format="%.4f")
    
    Volume_air_akhir = st.number_input("Masukkan Volume Akhir Air(mL)")
    
    Bobot_gelas_air_sampel = st.number_input(
        "Masukkan Bobot gelas yang Berisi Air dan Sampel (g)",
        step=1e-6,
        format="%.4f")
    
    Suhu_Ruang = st.selectbox(
    'Masukkan suhu ruang saat praktikum',   (20,21,22,23,24,25,26,27,27.5,28,29,30,31,32,33,34,35,36,37,38,39,40))
    if Suhu_Ruang == 20 :
        st.write(f':blue[Kerapatan air pada suhu 20 derajat celcius adalah 0,9982] g/mL')
    elif Suhu_Ruang ==21 :
        st.write(f':blue[Kerapatan air pada suhu 21 derajat celcius adalah 0,9980] g/mL')
    elif Suhu_Ruang ==22 :
        st.write(f':blue[Kerapatan air pada suhu 22 derajat celcius adalah 0,9978] g/mL')
    elif Suhu_Ruang ==23 :
        st.write(f':blue[Kerapatan air pada suhu 23 derajat celcius adalah 0,9976] g/mL')
    elif Suhu_Ruang ==24 :
        st.write(f':blue[Kerapatan air pada suhu 24 derajat celcius adalah 0,9973] g/mL')
    elif Suhu_Ruang ==25 :
        st.write(f':blue[Kerapatan air pada suhu 25 derajat celcius adalah 0,9971] g/mL')  
    elif Suhu_Ruang ==26 :
        st.write(f':blue[Kerapatan air pada suhu 26 derajat celcius adalah 0,9968] g/mL')
    elif Suhu_Ruang ==27 :
        st.write(f':blue[Kerapatan air pada suhu 27 derajat celcius adalah 0,9965] g/mL')   
    elif Suhu_Ruang ==28 :
        st.write(f':blue[Kerapatan air pada suhu 28 derajat celcius adalah 0,9963] g/mL')
    elif Suhu_Ruang ==29 :
        st.write(f':blue[Kerapatan air pada suhu 29 derajat celcius adalah 0,9960] g/mL') 
    elif Suhu_Ruang ==30 :
        st.write(f':blue[Kerapatan air pada suhu 30 derajat celcius adalah 0,9957] g/mL')
    elif Suhu_Ruang ==31 :
        st.write(f':blue[Kerapatan air pada suhu 31 derajat celcius adalah 0,9954] g/mL')
    elif Suhu_Ruang ==32 :
        st.write(f':blue[Kerapatan air pada suhu 32 derajat celcius adalah 0,9951] g/mL')
    elif Suhu_Ruang ==33 :
        st.write(f':blue[Kerapatan air pada suhu 33 derajat celcius adalah 0,9947] g/mL')
    elif Suhu_Ruang ==34 :
        st.write(f':blue[Kerapatan air pada suhu 34 derajat celcius adalah 0,9944] g/mL')
    elif Suhu_Ruang ==35 :
        st.write(f':blue[Kerapatan air pada suhu 35 derajat celcius adalah 0,9941] g/mL')  
    elif Suhu_Ruang ==36 :
        st.write(f':blue[Kerapatan air pada suhu 36 derajat celcius adalah 0,9937] g/mL')
    elif Suhu_Ruang ==37 :
        st.write(f':blue[Kerapatan air pada suhu 37 derajat celcius adalah 0,9934] g/mL')   
    elif Suhu_Ruang ==38 :
        st.write(f':blue[Kerapatan air pada suhu 38 derajat celcius adalah 0,9930] g/mL')
    elif Suhu_Ruang ==39 :
        st.write(f':blue[Kerapatan air pada suhu 39 derajat celcius adalah 0,9926] g/mL') 
    elif Suhu_Ruang ==40 :
        st.write(f':blue[Kerapatan air pada suhu 40 derajat celcius adalah 0,9922] g/mL') 
        
        
    Kerapatan_Air = st.number_input(
        "Masukkan kerapatan air pada suhu ruang",
        step=1e-6,
        format="%.4f")
        
    #Tombol Hasil Perhitungan
    
    tombol = st.button('Lihat hasil perhitungan kerapatan Absolut dan Relatif')
    with st.spinner('Memproses hasil...'):
        time.sleep(2)
        if tombol :
            st.write(f':blue[Nilai Kerapatan Absolut dalam satuan (g/mL) adalah : ]', round (((Bobot_gelas_air_sampel) - (Bobot_gelas_air))/((Volume_air_akhir)- (Volume_air_awal)), 4))
             
            st.write(f':blue[Nilai Kerapatan Relatif dalam satuan (g/mL) adalah : ]', round ( ((Bobot_gelas_air_sampel) - (Bobot_gelas_air))/((Volume_air_akhir)- (Volume_air_awal)) / (Kerapatan_Air), 4))
            
                
            
# Tabel Kerapatan air

if selected == 'Tabel Kerapatan Air':
    st.markdown("<h2 style='text-align: center; color: red;'> Tabel Kerapatan air</h2>", unsafe_allow_html=True)
    st.markdown('----')
    def load_data():
        return pd.DataFrame(
              {
                  "Temperatur ": [20,21,22,23,24,25,26,27,27.5,28,29,30,31,32,33,34,35,36,37,38,39,40],
                  "Kerapatan air ":[0.9982,0.9980,0.9978,0.9976,0.9973,0.9971,0.9968,0.9965,0.9964,0.9963,0.9960,0.9957,0.9954,0.9951,0.9947,0.9944,0.9941,0.9937,0.9934,0.9930,0.9926,0.9922],
        }
    )
    st.checkbox("Tampilkan tabel dengan format lebar", value=False, key="use_container_width")
    df = load_data()
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
    st.markdown("<h6 style='text-align: center; color:red ;'> Sumber : https://satujam.com/massa-jenis-air/ </h6>", unsafe_allow_html=True)