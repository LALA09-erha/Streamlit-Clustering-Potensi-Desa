import streamlit as st
import controller.prosesklasifikasi as pk
import pandas as pd
# import spacy
# from spacy.tokens import Token
# import spacy.cli
# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# from sklearn.preprocessing import normalize
# import joblib

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

st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Pengujian dengan Data Baru</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Masukkan data baru di bawah ini</p>", unsafe_allow_html=True)

# menu dengan 4 kolom ke bawah
input1, input2 = st.columns(2)
input3 , input4 , input5 , input6, input7 = st.columns(5)
input8, input9, input10, input11, input12 = st.columns(5)
input13, input14, input15, input16, input17 = st.columns(5)

with input1:
    desa = st.text_input(placeholder='Masukkan nama desa / kelurahan' , label='Desa')
with input2:
    kecamatan = st.text_input(placeholder='Masukkan nama kecamatan' , label='Kecamatan')
with input3:
    luas_wilayah = st.number_input(placeholder='Masukkan luas wilayah' , label='Luas Wilayah (km2)' )
with input4:
    jenis_permukaan_jalan =  st.selectbox('Jenis Permukaan Jalan', ['lainnya','Aspal/Beton', 'Kerikil, Batu, dll' ,'Diperkeras (kerikil. batu. dll)', ] )
with input5:
    jenis_transport =  st.selectbox('Jenis Transport', ['Darat', 'Air'])  
with input6:
    jumlah_penginapan = st.number_input(placeholder='Jumlah Penginapan' , label='Jumlah Penginapan' , min_value=0)
with input7:
    jumlah_tempat_makan = st.number_input(placeholder='Jumlah Tempat Makan' , label='Jumlah Tempat Makan' , min_value=0)
with input8:
    jumlah_menara_telekomunikasi = st.number_input(placeholder='Jumlah Menara Telepon Seluler' , label='Jumlah Menara Telepon Seluler' , min_value=0)

with input9:
    jarak_ke_kecamatan = st.number_input(placeholder='Jarak ke Ibu Kota Kecamatan' , label='Jarak ke Ibu Kota Kecamatan (km)')

with input10:
    jarak_ke_kabupaten = st.number_input(placeholder='Jarak ke Ibu Kota Kabupaten' , label='Jarak ke Ibu Kota Kabupaten (km)')

with input11:
    jumlah_wisnus = st.number_input(placeholder='Jumlah Wisatawan Nusantara (orang)' , label='Jumlah Wisatawan Nusantara (orang)' , min_value=0)

with input12:
    jumlah_wisman = st.number_input(placeholder='Jumlah Wisatawan Mancanegara (orang)' , label='Jumlah Wisatawan Mancanegara (orang)' , min_value=0)
with input13:
    jumlah_fasilitas = st.number_input(placeholder='Jumlah Fasilitas Pendukung' , label='Jumlah Fasilitas Pendukung' , min_value=0)
with input14:
    harga_tiket = st.number_input(placeholder='Harga Tiket Wisata' , label='Harga Tiket Wisata (Rp)' , min_value=0 )
with input15:
    rating_wisata = st.number_input(placeholder='Rating Wisata' , label='Rating Wisata')
with input16:
    jumlah_pantai = st.number_input(placeholder='Jumlah Pantai/Danau' , label='Jumlah Pantai/Danau' , min_value=0)
with input17:
    media_online = st.selectbox('Media Online', ['Tidak Ada', 'Ada']) 


# buatkan tombol submit di tengah halaman
st.markdown("""
<style>
[data-testid="stButton"] {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 10px;
    color: white;
    text-transform: capitalize;
}
</style>
""", unsafe_allow_html=True)

submit = st.button('Submit')





if submit:
    with st.spinner('Sedang memproses data...'):
        
        if(desa == '' or kecamatan == ''):
            st.error('Nama desa atau kecamatan belum diisi. Silahkan isi terlebih dahulu.')
        elif rating_wisata > 5 or rating_wisata < 0 or luas_wilayah < 0 or jarak_ke_kabupaten < 0 or jarak_ke_kecamatan < 0:
            if(rating_wisata > 5):
                st.error('Rating wisata tidak boleh lebih besar dari 5')
            else:
                st.error('Nilai tidak boleh negatif')
            
        else:
            # Tampung data
            data_input = pd.DataFrame({
                'Desa/Kelurahan': [desa],
                'Kecamatan' : [kecamatan],
                'Luas total area' : [luas_wilayah],
                'Jenis permukaan  jalan darat' : [jenis_permukaan_jalan],
                'Jenis prasarana trasportasi' : [jenis_transport],
                'Akomodasi. hotel. homestay' : [jumlah_penginapan],
                'Restourant/Tempat makan' : [jumlah_tempat_makan],
                'Jumlah Menara Telepon Seluler' : [jumlah_menara_telekomunikasi],
                'Jarak ke ibu kota kecamatan' : [jarak_ke_kecamatan],
                'Jarak ke ibu kota kabupaten' : [jarak_ke_kabupaten],
                'Wisnus' : [jumlah_wisnus],
                'Wisman' : [jumlah_wisman],
                'Failitas' : [jumlah_fasilitas],
                'Harga Tiket' : [int(harga_tiket)],
                'Rating' : [rating_wisata],
                'Pantai/Danau' : [jumlah_pantai],
                'Media Online' : [media_online]
            })
            # st.write(data_input.dtypes)
            # proses pre - processing
            data_preproses = pk.pre_processing(data_input)

            # normalisasi untuk ubah data menjadi angka
            data_normalisasi = pk.normalisasi(data_preproses)
            data_normalisasi = data_normalisasi.drop(['Desa/Kelurahan', 'Kecamatan'], axis=1)

            # proses convert data menjadi int
            data_normalisasi = pk.convert_to_int(data_normalisasi)
            # proses SOM  
            # data_som = pk.som(data_normalisasi)

            # proses clustering
            data_cluster = pk.clustering(data_normalisasi)

            st.write(data_cluster)