import joblib
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
 
def pre_processing(data_input):
    # read csv file x_train
    x_train = pd.read_csv('data/X_train.csv')
    # masukkan  dataframe to dataframe
    x_train = pd.concat([x_train, data_input], axis=0)

    # drop kolom
    x_train = x_train.drop(['No'], axis=1)
    # standarisasi
    
    return x_train


def normalisasi(data_input):
    
    # 1. Ubah kolom "Jenis prasarana trasportasi" menjadi numerik (1 jika "Darat", 0 untuk lainnya)
    data_input['Jenis prasarana trasportasi'] = data_input['Jenis prasarana trasportasi'].replace({
        'Darat': 1, 'Air' : '2', 'Darat dan Air' : 3,'Lainnya': 4
        })

    # 2. Ubah kolom "Jenis permukaan jalan darat"
    data_input['Jenis permukaan  jalan darat'] = data_input['Jenis permukaan  jalan darat'].replace({
        'Aspal/Beton': 1,
        'Diperkeras (kerikil. batu. dll)': 2,
        'Kerikil. Batu. dll	': 3,
        'lainnya': 4
    })

    # 3. Ubah kolom "Media Online" menjadi numerik (1 untuk "Ada", 0 untuk "Tidak Ada")
    data_input['Media Online'] = data_input['Media Online'].replace({'Ada': 1, 'Tidak Ada': 0})

    # 4. Ubah kolom "Desa/Kelurahan" menjadi numerik
    data_input['Desa/Kelurahan'] = data_input['Desa/Kelurahan'].astype('category').cat.codes

    # 5. Ubah kolom "Kecamatan" menjadi numerik
    data_input['Kecamatan'] = data_input['Kecamatan'].astype('category').cat.codes


    # 7. Pastikan kolom angka lainnya sesuai tipe data yang diinginkan
    data_input['Jarak ke ibu kota kecamatan'] = data_input['Jarak ke ibu kota kecamatan'].astype(int)
    data_input['Jarak ke ibu kota kabupaten'] = data_input['Jarak ke ibu kota kabupaten'].astype(int)

    return data_input

def som(data_input):
    # Data setelah normalisasi (misalnya, data_input_normalized adalah hasil normalisasi)
    data_normalized = data_input.iloc[:, 2:].values  # Mengambil kolom fitur saja (tanpa No, Desa/Kelurahan, Kecamatan)

    # 1. Tentukan dimensi grid SOM
    grid_rows, grid_cols = 3, 3  # Dimensi SOM (3x3 grid)

    # 2. Tentukan jumlah fitur (dimensi input)
    num_features = data_normalized.shape[1]

    # 3. Inisialisasi bobot random (nilai antara 0 dan 1)
    weights = np.random.rand(grid_rows, grid_cols, num_features)

    # 4. Perhitungan jarak Euclidean untuk setiap data ke setiap bobot
    distances = np.zeros((data_normalized.shape[0], grid_rows, grid_cols))

    for i, data_point in enumerate(data_normalized):
        for row in range(grid_rows):
            for col in range(grid_cols):
                # Hitung jarak Euclidean
                distances[i, row, col] = np.sqrt(np.sum((data_point - weights[row, col]) ** 2))
    # 5. Temukan jarak terkecil dan indeksnya
    closest_units = []

    for i, distance_matrix in enumerate(distances):
        min_distance = np.min(distance_matrix)  # Nilai jarak terkecil
        min_index = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)  # Indeks dari jarak terkecil
        closest_units.append((i, min_distance, min_index))

    # Output bobot awal, jarak, dan unit terdekat
    return closest_units

def clustering(data_input):
    # Data setelah normalisasi (data_normalized adalah hasil normalisasi)
    data = data_input

    # Rentang jumlah cluster (K)
    k_values = range(2, 11)  # Mulai dari 2 hingga 10

    # List untuk menyimpan hasil akurasi
    accuracy_results = []

    for k in k_values:
        # 1. Klustering dengan K-Means
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans_labels = kmeans.fit_predict(data)

        # 2. Split data menjadi training dan testing
        X_train, X_test, y_train, y_test = train_test_split(
            data, kmeans_labels, test_size=0.3, random_state=42
        )

        # 3. Training model Naive Bayes
        nb_model = GaussianNB()
        nb_model.fit(X_train, y_train)

        # 4. Prediksi pada data testing
        y_pred = nb_model.predict(X_test)

        # 5. Hitung akurasi
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_results.append((k, accuracy))

        # 6. Confusion Matrix dan Classification Report
        conf_matrix = confusion_matrix(y_test, y_pred)
        class_report = classification_report(y_test, y_pred)

        # print(f"K={k}: Akurasi = {accuracy:.4f}")
        # print("Confusion Matrix:")
        # print(conf_matrix)
        # print("Classification Report:")
        # print(class_report)

    return kmeans_labels

    # Output hasil akurasi
    # def print_accuracies():
    #     print("\nHasil Akurasi untuk Setiap K:")
    #     for k, acc in accuracy_results:
    #         print(f"Jumlah Cluster (K): {k}, Akurasi: {acc:.4f}")

    # print_accuracies()

    # # Validasi silang menggunakan cross-validation untuk K terbaik
    # best_k = max(accuracy_results, key=lambda x: x[1])[0]
    # print(f"\nMelakukan cross-validation untuk K terbaik (K={best_k}):")

    # kmeans = KMeans(n_clusters=best_k, random_state=42)
    # kmeans_labels = kmeans.fit_predict(data)
    # scores = cross_val_score(GaussianNB(), data, kmeans_labels, cv=5)

    # print("Cross-Validation Scores:", [f"{score:.4f}" for score in scores])
    # print("Mean Accuracy:", f"{np.mean(scores):.4f}")

def convert_to_int(data_input):
    # Contoh: Membaca df
    # df = pd.read_csv("path_to_dataset.csv")

    # Daftar kolom dengan tipe data object
    object_columns = data_input.select_dtypes(include=['object']).columns

    # Ubah kolom 'object' menjadi 'int' (jika memungkinkan)
    for column in object_columns:
        try:
            data_input[column] = pd.to_numeric(data_input[column], errors='coerce').fillna(0).astype(int)
            print(f"Kolom '{column}' berhasil diubah ke integer.")
        except Exception as e:
            print(f"Gagal mengubah kolom '{column}' ke integer: {e}")

    return data_input
