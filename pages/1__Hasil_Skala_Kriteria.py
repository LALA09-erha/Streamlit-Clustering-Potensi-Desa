# inisiasi library
import streamlit as st # type: ignore
import pandas as pd # type: ignore

# judul
st.set_page_config(
    page_title="Hasil Skala Kriteria",
    page_icon="🌏",
    layout="wide",
)
# setting sidebar
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

st.title('Hasil Skala Kriteria')
st.write('')

# buatkan kolom 2 untuk menampilkan 2 tabel sekaligus samping 
data1, data2 , data3= st.columns(3)

# tabel_luas_area
luas_area = pd.read_csv('data/tabel_luas_area.csv')
luas_area = luas_area.drop(['No'], axis=1)
data1.markdown('**Luas Area**')
data1.write('3 : Sangat Luas , 2 : Luas , 1 : Cukup Sempit , 0 : Sempit' )
data1.write(luas_area)

# tabel_jarak_kecamatan
cluster = pd.read_csv('data/tabel_jarak_kecamatan.csv')
cluster = cluster.drop(['No'], axis=1)
data2.markdown('**Jarak Kecamatan**')
data2.write('3 : Sangat Dekat , 2 : Dekat , 1 : Cukup Jauh , 0 : Jauh')
data2.write(cluster)

# tabel_jarak_kab
tabel_jarak_kab = pd.read_csv('data/tabel_jarak_kab.csv')
tabel_jarak_kab = tabel_jarak_kab.drop(['No'], axis=1)
data3.markdown('**Jarak Kabupaten**')
data3.write('3 : Sangat Dekat , 2 : Dekat , 1 : Cukup Jauh , 0 : Jauh')
data3.write(tabel_jarak_kab)

data4 , data5, data6 = st.columns(3)
# tabel_akomodasi
tabel_akomodasi = pd.read_csv('data/tabel_akomodasi.csv')
tabel_akomodasi = tabel_akomodasi.drop(['No'], axis=1)
data4.markdown('**Akomodasi**')
data4.write('3 : Sangat Murah , 2 : Murah , 1 : Cukup Mahal , 0 : Mahal')
data4.write(tabel_akomodasi)


# tabel_tempat_makan
tabel_tempat_makan = pd.read_csv('data/tabel_tempat_makan.csv')
tabel_tempat_makan = tabel_tempat_makan.drop(['No'], axis=1)
data5.markdown('**Tempat Makan**')
data5.write('3 : 5 bintang , 2 : 4 bintang , 1 : 3 bintang , 0 : 1 bintang')
data5.write(tabel_tempat_makan)

# tabel_prasarana
tabel_prasarana = pd.read_csv('data/tabel_prasarana.csv')
tabel_prasarana = tabel_prasarana.drop(['No'], axis=1)
data6.markdown('**Prasarana**')
data6.write('3 : Sangat Memadai , 2 : Memadai , 1 : Cukup Tebatas , 0 : Tebatas')
data6.write(tabel_prasarana)


data7, data8, data9 = st.columns(3)
# tabel_kondisi_jalan_per_kecamatan
tabel_kondisi_jalan_per_kecamatan = pd.read_csv('data/tabel_kondisi_jalan_per_kecamatan.csv')
tabel_kondisi_jalan_per_kecamatan = tabel_kondisi_jalan_per_kecamatan.drop(['No'], axis=1)
data7.markdown('**Kondisi Jalan Per Kecamatan**')
data7.write('3 : Sangat Bagus , 2 : Bagus , 1 : Cukup Rusak , 0 : Rusak')
data7.write(tabel_kondisi_jalan_per_kecamatan)

# tabel_tower_telepon
tabel_tower_telepon = pd.read_csv('data/tabel_tower_telepon.csv')
tabel_tower_telepon = tabel_tower_telepon.drop(['No'], axis=1)
data8.markdown('**Tower Telepon**')
data8.write('3 : Sangat Banyak , 2 : Banyak , 1 : Cukup Sedikit , 0 : Sedikit')
data8.write(tabel_tower_telepon)

# tabel_media_online
tabel_media_online = pd.read_csv('data/tabel_media_online.csv')
tabel_media_online = tabel_media_online.drop(['No'], axis=1)
data9.markdown('**Media Online**')
data9.write('3 : Sangat Banyak , 2 : Banyak , 1 : Cukup Sedikit , 0 : Sedikit')
data9.write(tabel_media_online)

data10, data11, data12 = st.columns(3)
# tabel_pantai
tabel_pantai = pd.read_csv('data/tabel_pantai.csv')
tabel_pantai = tabel_pantai.drop(['No'], axis=1)
data10.markdown('**Pantai**')
data10.write('3 : Sangat Bagus , 2 : Bagus , 1 : Cukup Rusak , 0 : Rusak')
data10.write(tabel_pantai)

# tabel_fasilitas
tabel_fasilitas = pd.read_csv('data/tabel_fasilitas.csv')
tabel_fasilitas = tabel_fasilitas.drop(['No'], axis=1)
data11.markdown('**Fasilitas**')
data11.write('3 : Sangat Memadai , 2 : Memadai , 1 : Cukup Tebatas , 0 : Tebatas')
data11.write(tabel_fasilitas)

# tabel_harga_tiket
tabel_harga_tiket = pd.read_csv('data/tabel_harga_tiket.csv')
tabel_harga_tiket = tabel_harga_tiket.drop(['No'], axis=1)
data12.markdown('**Harga Tiket**')
data12.write('3 : Sangat Murah , 2 : Murah , 1 : Cukup Mahal , 0 : Mahal')
data12.write(tabel_harga_tiket)

# tabel_rating
data13 , data14, data15 = st.columns(3)
tabel_rating = pd.read_csv('data/tabel_rating.csv')
tabel_rating = tabel_rating.drop(['No'], axis=1)
data13.markdown('**Rating**')
data13.write('3 : 5 bintang , 2 : 4 bintang , 1 : 3 bintang , 0 : 1 bintang')
data13.write(tabel_rating)

# tabel_wisatawan_mancanegara
tabel_wisatawan_mancanegara = pd.read_csv('data/tabel_wisatawan_mancanegara.csv')
tabel_wisatawan_mancanegara = tabel_wisatawan_mancanegara.drop(['No'], axis=1)
data14.markdown('**Wisatawan Mancanegara**')
data14.write('3 : > 5 orang , 2 : 4 - 5 Orang , 1 : 2 - 3 Orang , 0 : 0 - 1 Orang')
data14.write(tabel_wisatawan_mancanegara)

# tabel_wisatawan_nusantara
tabel_wisatawan_nusantara = pd.read_csv('data/tabel_wisatawan_nusantara.csv')
tabel_wisatawan_nusantara = tabel_wisatawan_nusantara.drop(['No'], axis=1)
data15.markdown('**Wisatawan Nusantara**')
data15.write('3 : > 5 orang , 2 : 4 - 5 Orang , 1 : 2 - 3 Orang , 0 : 0 - 1 Orang')
data15.write(tabel_wisatawan_nusantara)