# import streamlit as st # type: ignore
# import controller.prosesklasifikasi as pk
# import controller.prosesSkala as ps
# import pandas as pd # type: ignore

# # judul halaman
# st.set_page_config(
#     page_title="Uji Coba",
#     page_icon="🌏",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# st.markdown("""
# <style>
            
# [data-testid="stSidebarNavLink"] {
#     font-size: 20px;
#     font-weight: bold;
#     text-align: center;
#     padding: 10px;
#     border-radius: 10px;
#     color: black;
#     text-transform: capitalize;
# }
# </style>
# """, unsafe_allow_html=True)

# st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Hasil Cluster</h1>", unsafe_allow_html=True)

# # ambil data dari controller
# potensi_kurang = pd.read_csv('data/potensi_kurang.csv')
# potensi_sedang = pd.read_csv('data/potensi_sedang.csv')
# potensi_tinggi = pd.read_csv('data/potensi_tinggi.csv')



# data1, data2, data3 = st.columns(3)

# with data1:
#     st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Potensi Kurang</h2>", unsafe_allow_html=True)
#     st.dataframe(potensi_kurang, use_container_width=True)

# with data2:
#     st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Potensi Sedang</h2>", unsafe_allow_html=True)
#     st.dataframe(potensi_sedang, use_container_width=True)

# with data3:
#     st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Potensi Tinggi</h2>", unsafe_allow_html=True)
#     st.dataframe(potensi_tinggi, use_container_width=True)

import streamlit as st # type: ignore
import controller.prosesklasifikasi as pk
import controller.prosesSkala as ps
import pandas as pd # type: ignore

# judul halaman
st.set_page_config(
    page_title="Uji Coba",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
            
[data-testid="stSidebarNavLink"] {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 10px;
    color: black;
    text-transform: capitalize;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;'>Hasil Cluster</h1>", unsafe_allow_html=True)

# ambil data dari controller dan CSV
potensi_kurang = pd.read_csv('data/potensi_kurang.csv')
potensi_sedang = pd.read_csv('data/potensi_sedang.csv')
potensi_tinggi = pd.read_csv('data/potensi_tinggi.csv')

# Menambahkan analisis potensi dari file CSV lain
analisis_potensi_kurang = pd.read_csv('data/analisis_potensi_kurang.csv')
analisis_potensi_tinggi = pd.read_csv('data/analisis_potensi_tinggi.csv')
analisis_potensi_sedang = pd.read_csv('data/analisis_potensi_sedang.csv')

# Tampilkan data dalam kolom Streamlit
data1, data2, data3 = st.columns(3)

with data1:
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black; margin:0 ; padding:0;'>Potensi Kurang</h2>", unsafe_allow_html=True)
    st.dataframe(potensi_kurang, use_container_width=True)

with data2:
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black; margin:0 ; padding:0;'>Potensi Sedang</h2>", unsafe_allow_html=True)
    st.dataframe(potensi_sedang, use_container_width=True)

with data3:
    st.markdown("<h2 style='text-align: center; color: white; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black; margin:0 ; padding:0;'>Potensi Tinggi</h2>", unsafe_allow_html=True)
    st.dataframe(potensi_tinggi, use_container_width=True)

# Tampilkan analisis potensi kuran dan tinggi
st.markdown("<h2 style='text-align: center; color: white; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black; margin:0 ; padding:0;'>Analisis Potensi Kurang</h2>", unsafe_allow_html=True)
st.dataframe(analisis_potensi_kurang, use_container_width=True)

st.markdown("<h2 style='text-align: center; color: white; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black; margin:0 ; padding:0;'>Analisis Potensi Tinggi</h2>", unsafe_allow_html=True)
st.dataframe(analisis_potensi_tinggi, use_container_width=True)

st.markdown("<h2 style='text-align: center; color: white; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black; margin:0 ; padding:0;'>Analisis Potensi sedang</h2>", unsafe_allow_html=True)
st.dataframe(analisis_potensi_sedang, use_container_width=True)
