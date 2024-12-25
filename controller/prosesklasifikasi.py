# import joblib
# import pandas as pd
# import re
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


# # Fungsi untuk memisahkan tanda baca yang terhubung dengan kata
# def separate_punctuation(text):
#     # Define pattern to separate punctuation
#     pattern = r'(?<=[A-Za-z])([.,!?])|([.,!?])(?=[A-Za-z])'
#     separated_text = re.sub(pattern, r' \1\2 ', text)
#     return separated_text

# # Fungsi untuk membersihkan teks
# def clean_text(df, text_field, new_text_field_name):
#     # Lowercasing
#     df[new_text_field_name] = df[text_field].apply(lambda x: ' '.join(x)).str.lower()
#     # Menghapus tanda baca, mention, link, dan karakter khusus lainnya
#     df[new_text_field_name] = df[new_text_field_name].apply(lambda elem: re.sub(r"(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))
#     # Menghapus angka
#     df[new_text_field_name] = df[new_text_field_name].apply(lambda elem: re.sub(r"\d+", "", elem))
#     # Pisahkan tanda baca yang terhubung dengan kata
#     df[new_text_field_name] = df[new_text_field_name].apply(lambda elem: separate_punctuation(elem))
#     # Tokenisasi kembali setelah pemisahan tanda baca
#     df[new_text_field_name] = df[new_text_field_name].apply(lambda x: x.split())
#     return df

# # Fungsi untuk normalisasi
# def normalisasi(teks, kamus):
#     kalimat_final = []
#     for kata in teks:
#         kata_benar = kamus[kamus['Tidak Baku'] == kata]['Baku'].values
#         if len(kata_benar) > 0:
#             kalimat_final.append(kata_benar[0])
#         else:
#             kalimat_final.append(kata)
#     return kalimat_final

# # Daftar kata-kata stop words tambahan
# more_stopwords = {
# 'dar', 'hai', 'txffzhybv', 'bg', 'bot', 'yg', 'deh', 'ypdhl', 'tidak', 'nic', 'bos', 'hmmm', 'ky', 'yaa', 'mo', 'fb', 'laah', 'br', 'blg', 'da', 'x', 'jt', 'dan',
# 'y', 'b', 't', 'yang', 'sj', 'faq', 'jsajan', 'aja', 'mis', 'mf', 'hmm', 'jii', 'issi', 'the', 'kok', 'ng', 'di', 'nih', 'lah', 'adm', 'nig', 'min', 'y', 'kak', 'k', 'va',
# 'dong', 'ai', 'nya', 'e', 'tuh', 'nih', 'di' , 'min','ke', 'dgn', 'nya', 'jadi', 'ada', 'nya', 'ah', 'aamiin', 'hehehe', 'hhhh', 'hey', 'hmmm', 'hmm', 'ram', 'the', 'tfr', 'wkwk'
# }

# # Membuat daftar kata-kata stop words
# stop_words_factory = StopWordRemoverFactory()
# stop_words = stop_words_factory.get_stop_words()
# stop_words = stop_words.extend(more_stopwords)

# # Menginisialisasi StopWordRemover dengan daftar stop words yang diperbarui
# stopword_remover = stop_words_factory.create_stop_word_remover()

# # Fungsi untuk menghapus stop words dari teks
# def remove_stopwords(text):
#     if isinstance(text, list):
#         text = ' '.join(text)
#     return stopword_remover.remove(text)

# # Inisialisasi Stemmer dari Sastrawi
# factory = StemmerFactory()
# stemmer = factory.create_stemmer()

# # Fungsi lemmatization menggunakan Sastrawi
# def lemmatize_indonesian(token):
#     return stemmer.stem(token.text)