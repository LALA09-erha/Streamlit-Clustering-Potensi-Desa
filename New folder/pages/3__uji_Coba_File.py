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
    dark_mode=True
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

st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Pengujian dengan Data Baru Dengan File Excel</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>Download Tamplate dan Upload data baru di bawah ini</p>", unsafe_allow_html=True)

# buatkan tombol download di tengah halaman dengan link external menggunakn st.markdown
# buatkan di tengah halaman
st.markdown("""
            <br>
<div style="text-align: center; align-items: center;">
<button style='font-size: 20px; font-weight: bold; text-align:center; 
padding: 10px; border-radius: 10px; color: white; text-transform: capitalize;'>
<a href='https://drive.google.com/uc?export=download&id=1STCQ6EP2slYkLGcxgfwmo2azm9QBy74E' target='_blank'>Download Tamplate</a>
</button>
</div>
            """, unsafe_allow_html=True)

# buatkan file upload di tengah halaman  xlsx , xls, csv
input_file = st.file_uploader("Upload File Excel", type=["csv", "xlsx", "xls"])
if input_file is not None:
    data_input = pd.read_csv(input_file)
else: 
    st.warning("Silahkan upload file excel terlebih dahulu, disarankan pakai tamplate excel diatas.")

# buatkan tombol submit di tengah halaman
st.markdown("""
<style>
[data-testid="stButton"] {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 10px;
    color: yellow;
    text-transform: capitalize;
}
</style>
""", unsafe_allow_html=True)

# buat tombol submit
submit = st.button('Submit')
# logika jika tombol submit di klik
if submit:
    with st.spinner('Sedang memproses data...'):
        # menyimpan data input ke dalam variabel
        data_input_shape = data_input.shape

        # proses pre - processing
        data_preproses = pk.pre_processing(data_input)
        # normalisasi untuk ubah data menjadi angka
        data_normalisasi = pk.transform(data_preproses)
        # drop kolom
        data_normalisasi = data_normalisasi.drop(['Desa/Kelurahan', 'Kecamatan'], axis=1)
        # proses convert data menjadi int
        data_normalisasi = pk.convert_to_int(data_normalisasi)
        # copy data normalisasi
        data_skala = data_normalisasi.copy()

         # perhitungan skala
        data_skala = ps.skala_kriteria(data_skala)
        # proses normalisasi minmax 
        data_normalisasi = pk.normalisasi(data_normalisasi) 
        # proses clustering
        data_cluster = pk.clustering(data_normalisasi)

        # transform to dataframe
        data_cluster = pd.DataFrame(data_cluster)

        # transform to label 
        data_label_transform = data_cluster[0].iloc[-data_input_shape[0]:].map({0: 'Potensi Kurang', 1: 'Potensi Sedang', 2: 'Potensi Tinggi'})

    
        # iloc ke jumlah data_input_shape[0] masuk ke dataframe baru
        data_final = data_skala.iloc[-data_input_shape[0]:]

        # tambahkan kolom label
        data_final['Label'] = data_label_transform.values

        # tampilkan data
        st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Hasil Pengujian</h1>", unsafe_allow_html=True)
        
        # ambil kolom Desa/Kelurahan dan Kecamatan dari data_input
        data_show_with_desa = data_input[['Desa/Kelurahan', 'Kecamatan']]

        # gabungkan data_show_with_desa dengan data_label_transform
        data_show_with_desa['Label'] = data_label_transform.values

        # pisah label dengan label Potensi Tinggi
        data_show_with_desa_potensi_tinggi = data_show_with_desa[data_show_with_desa['Label'] == 'Potensi Tinggi']

        # pisah label dengan label Potensi Kurang
        data_show_with_desa_potensi_kurang = data_show_with_desa[data_show_with_desa['Label'] == 'Potensi Kurang']

        # pisah label dengan label Potensi Sedang
        data_show_with_desa_potensi_sedang = data_show_with_desa[data_show_with_desa['Label'] == 'Potensi Sedang']


        # tampilkan data_show_with_desa
        
        with st.columns(3)[1]:
            st.write('Desa yang Potensi Tinggi')
            # tampilkan data_show_with_desa_potensi_tinggi
            st.dataframe(data_show_with_desa_potensi_tinggi)

            st.write('Desa yang Potensi Sedang')
            # tampilkan data_show_with_desa_potensi_kurang
            st.dataframe(data_show_with_desa_potensi_sedang)

            st.write('Desa yang Potensi Kurang')
            # tampilkan data_show_with_desa_potensi_sedang
            st.dataframe(data_show_with_desa_potensi_kurang)




