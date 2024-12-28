# # Fungsi klasifikasi untuk kriteria tambahan
# def klasifikasi_luas_area(value):
#     if value > 5:
#         return 3  # Sangat luas
#     elif 4 <= value <= 5:
#         return 2  # Luas
#     elif 2 <= value < 4:
#         return 1  # Cukup sempit
#     else:
#         return 0  # Sempit

# def klasifikasi_jarak(value):
#     if value > 5:
#         return 3  # Sangat dekat
#     elif 4 <= value <= 5:
#         return 2  # Dekat
#     elif 2 <= value < 4:
#         return 1  # Cukup jauh
#     else:
#         return 0  # Jauh

# def klasifikasi_akomodasi(value):
#     if value > 5:
#         return 3  # Sangat murah
#     elif 4 <= value <= 5:
#         return 2  # Murah
#     elif 2 <= value < 4:
#         return 1  # Cukup mahal
#     else:
#         return 0  # Mahal

# def klasifikasi_tempat_makan(value):
#     if value > 5:
#         return 3  # 5 bintang
#     elif 4 <= value <= 5:
#         return 2  # 4 bintang
#     elif 2 <= value < 4:
#         return 1  # 3 bintang
#     else:
#         return 0  # 1 bintang

# def klasifikasi_prasarana(value):
#     if value > 5:
#         return 3  # Sangat memadai
#     elif 4 <= value <= 5:
#         return 2  # Memadai
#     elif 2 <= value < 4:
#         return 1  # Cukup terbatas
#     else:
#         return 0  # Terbatas

# # def klasifikasi_permukaan_jalan(value):
# #     if value == 1:
# #         return 3  # Sangat bagus
# #     elif value == 2:
# #         return 2  # Bagus
# #     elif value == 3:
# #         return 1  # Cukup rusak
# #     elif value == 4:
# #         return 0  # Rusak
# def klasifikasi_permukaan_jalan(value):
#     if value == 1:
#         return 3  # Sangat bagus
#     elif value == 2:
#         return 2  # Cukup bagus
#     elif value == 3:
#         return 1  # Cukup rusak
#     elif value == 4:
#         return 0  # Rusak
#     else:
#         return None  # Jika ada nilai yang tidak valid



# def klasifikasi_jumlah_tower_telepon(value):
#     if value > 5:
#         return 3  # Sangat banyak
#     elif 4 <= value <= 5:
#         return 2  # Banyak
#     elif 2 <= value < 4:
#         return 1  # Cukup sedikit
#     else:
#         return 0  # Sedikit

# def klasifikasi_media_online(value):
#     if value > 5:
#         return 3  # Sangat banyak
#     elif 4 <= value <= 5:
#         return 2  # Banyak
#     elif 2 <= value < 4:
#         return 1  # Cukup sedikit
#     else:
#         return 0  # Sedikit

# def klasifikasi_pantai(value):
#     if value > 5:
#         return 3  # Sangat banyak
#     elif 4 <= value <= 5:
#         return 2  # Banyak
#     elif 2 <= value < 4:
#         return 1  # Cukup sedikit
#     else:
#         return 0  # Sedikit

# def klasifikasi_fasilitas(value):
#     if value > 5:
#         return 3  # Sangat baik
#     elif 4 <= value <= 5:
#         return 2  # Baik
#     elif 2 <= value < 4:
#         return 1  # Cukup baik
#     else:
#         return 0  # Kurang

# def klasifikasi_harga_tiket(value):
#     if value < 5000:
#         return 3  # Sangat murah
#     elif 5000 <= value <= 10000:
#         return 2  # Murah
#     elif 10001 <= value <= 15000:
#         return 1  # Cukup mahal
#     else:
#         return 0  # Sangat mahal


# def klasifikasi_rating(value):
#     if value > 5:
#         return 3  # 5 bintang
#     elif 4 <= value <= 5:
#         return 2  # 4 bintang
#     elif 2 <= value < 4:
#         return 1  # 3 bintang
#     else:
#         return 0  # 1 bintang

# def klasifikasi_wisman(value):
#     if value > 5:
#         return 3  # > 5 orang
#     elif 4 <= value <= 5:
#         return 2  # 4 - 5 orang
#     elif 2 <= value < 4:
#         return 1  # 2 - 3 orang
#     else:
#         return 0  # 0 - 1 orang

# def klasifikasi_wisnus(value):
#     if value > 5:
#         return 3  # > 5 orang
#     elif 4 <= value <= 5:
#         return 2  # 4 - 5 orang
#     elif 2 <= value < 4:
#         return 1  # 2 - 3 orang
#     else:
#         return 0  # 0 - 1 orang

def klasifikasi_luas_area(value):
    if value > 5:
        return "Sangat luas"
    elif 4 <= value <= 5:
        return "Luas"
    elif 2 <= value < 4:
        return "Cukup sempit"
    else:
        return "Sempit"

def klasifikasi_jarak(value):
    if value > 5:
        return "Sangat dekat"
    elif 4 <= value <= 5:
        return "Dekat"
    elif 2 <= value < 4:
        return "Cukup jauh"
    else:
        return "Jauh"

def klasifikasi_akomodasi(value):
    if value > 5:
        return "Mahal"
    elif 4 <= value <= 5:
        return "Cukup mahal"
    elif 2 <= value < 4:
        return "Murah"
    else:
        return "Sangat murah"

def klasifikasi_tempat_makan(value):
    if value > 5:
        return "5 bintang"
    elif 4 <= value <= 5:
        return "4 bintang"
    elif 2 <= value < 4:
        return "3 bintang"
    else:
        return "1 bintang"

def klasifikasi_prasarana(value):
    if value > 5:
        return "Sangat memadai"
    elif 4 <= value <= 5:
        return "Memadai"
    elif 2 <= value < 4:
        return "Cukup terbatas"
    else:
        return "Terbatas"

def klasifikasi_permukaan_jalan(value):
    if value == 1:
        return "Sangat bagus"
    elif value == 2:
        return "Cukup bagus"
    elif value == 3:
        return "Cukup rusak"
    elif value == 4:
        return "Rusak"
    else:
        return None  # Jika ada nilai yang tidak valid

def klasifikasi_jumlah_tower_telepon(value):
    if value > 5:
        return "Sangat banyak"
    elif 4 <= value <= 5:
        return "Banyak"
    elif 2 <= value < 4:
        return "Cukup sedikit"
    else:
        return "Sedikit"

def klasifikasi_media_online(value):
    if value > 5:
        return "Sangat banyak"
    elif 4 <= value <= 5:
        return "Banyak"
    elif 2 <= value < 4:
        return "Cukup sedikit"
    else:
        return "Sedikit"

def klasifikasi_pantai(value):
    if value > 5:
        return "Sangat banyak"
    elif 4 <= value <= 5:
        return "Banyak"
    elif 2 <= value < 4:
        return "Cukup sedikit"
    else:
        return "Sedikit"

def klasifikasi_fasilitas(value):
    if value > 5:
        return "Sangat baik"
    elif 4 <= value <= 5:
        return "Baik"
    elif 2 <= value < 4:
        return "Cukup baik"
    else:
        return "Kurang"

def klasifikasi_harga_tiket(value):
    if value < 5000:
        return "Sangat murah"
    elif 5000 <= value <= 10000:
        return "Murah"
    elif 10001 <= value <= 15000:
        return "Cukup mahal"
    else:
        return "Sangat mahal"

def klasifikasi_rating(value):
    if value > 5:
        return "5 bintang"
    elif 4 <= value <= 5:
        return "4 bintang"
    elif 2 <= value < 4:
        return "3 bintang"
    else:
        return "1 bintang"

def klasifikasi_wisman(value):
    if value > 5:
        return "> 5 orang"
    elif 4 <= value <= 5:
        return "4 - 5 orang"
    elif 2 <= value < 4:
        return "2 - 3 orang"
    else:
        return "0 - 1 orang"

def klasifikasi_wisnus(value):
    if value > 5:
        return "> 5 orang"
    elif 4 <= value <= 5:
        return "4 - 5 orang"
    elif 2 <= value < 4:
        return "2 - 3 orang"
    else:
        return "0 - 1 orang"


def skala_kriteria(data_input):
    data_input['Luas total area'] = data_input['Luas total area'].apply(klasifikasi_luas_area)
    data_input['Jarak ke ibu kota kecamatan'] = data_input['Jarak ke ibu kota kecamatan'].apply(klasifikasi_jarak)
    data_input['Jarak ke ibu kota kabupaten'] = data_input['Jarak ke ibu kota kabupaten'].apply(klasifikasi_jarak)
    data_input['Akomodasi. hotel. homestay'] = data_input['Akomodasi. hotel. homestay'].apply(klasifikasi_akomodasi)
    data_input['Restourant/Tempat makan'] = data_input['Restourant/Tempat makan'].apply(klasifikasi_tempat_makan)
    data_input['Jenis prasarana trasportasi'] = data_input['Jenis prasarana trasportasi'].apply(klasifikasi_prasarana)
    data_input['Jenis permukaan  jalan darat'] = data_input['Jenis permukaan  jalan darat'].apply(klasifikasi_permukaan_jalan)
    data_input['Jumlah Menara Telepon Seluler'] = data_input['Jumlah Menara Telepon Seluler'].apply(klasifikasi_jumlah_tower_telepon)
    data_input['Media Online'] = data_input['Media Online'].apply(klasifikasi_media_online)
    data_input['Pantai/Danau'] = data_input['Pantai/Danau'].apply(klasifikasi_pantai)
    data_input['Failitas'] = data_input['Failitas'].apply(klasifikasi_fasilitas)
    data_input['Harga Tiket'] = data_input['Harga Tiket'].apply(klasifikasi_harga_tiket)
    data_input['Rating'] = data_input['Rating'].apply(klasifikasi_rating)
    data_input['Wisman'] = data_input['Wisman'].apply(klasifikasi_wisman)
    data_input['Wisnus'] = data_input['Wisnus'].apply(klasifikasi_wisnus)

    return data_input