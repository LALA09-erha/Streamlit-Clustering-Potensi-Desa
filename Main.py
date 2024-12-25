# inisialisasi library
import streamlit as st
import pandas as pd

# judul website
st.set_page_config(
    page_title="Pemetaan potensi desa wisata di Madura",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title('Website Pemetaan potensi desa wisata di Madura dengan pendekatan metode algoritma self organizing map (SOM) dan optimasi cluster elbow')

# ambil [data-testid="stSidebarNavLink"] yang pertama dari sidebar
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
# change name of menu like name of this file in sidebar just in this page

# tampilkan gambar dari link

st.markdown("<img src='https://images.tokopedia.net/blog-tokopedia-com/uploads/2019/08/wisata-madura-1-Native-Indonesia.jpg' style='max-width: 100%; display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)

st.text("")
#penjelasan   

st.markdown('<div style="text-align: justify;"> <b>Pemetaan Potensi Desa Wisata di Madura dengan Pendekatan Metode Algoritma Self Organizing Map (SOM) dan Optimasi Cluster Elbow</b> bertujuan untuk mengidentifikasi dan mengelompokkan desa-desa di Madura berdasarkan potensi wisatanya. Algoritma Self Organizing Map (SOM) digunakan untuk memetakan data berdimensi tinggi, seperti karakteristik ekonomi, budaya, geografis, dan infrastruktur desa, ke dalam peta berdimensi lebih rendah yang mudah divisualisasikan. Teknik ini memungkinkan pengelompokan desa secara otomatis berdasarkan pola yang ditemukan dalam data tanpa memerlukan label sebelumnya. Optimasi Cluster Elbow kemudian diterapkan untuk menentukan jumlah kelompok (cluster) optimal, memastikan hasil pemetaan yang akurat dan relevan dengan kondisi nyata di lapangan.</div>', unsafe_allow_html=True)

st.text("")

# penjelasan  
st.markdown('<div style="text-align: justify;">Melalui pendekatan ini, penelitian berusaha memberikan rekomendasi strategis untuk pengembangan desa wisata di Madura sesuai dengan karakteristik masing-masing kelompok. Hasil pemetaan ini diharapkan menjadi acuan bagi pemerintah daerah, pelaku usaha, dan masyarakat lokal dalam menyusun strategi promosi, pengelolaan sumber daya, dan pengembangan infrastruktur yang sesuai. Dengan demikian, penelitian ini tidak hanya berkontribusi pada peningkatan daya saing pariwisata lokal tetapi juga mendorong pembangunan berkelanjutan berbasis potensi daerah.</div>', unsafe_allow_html=True)
