import streamlit as st
# import controller.prosesklasifikasi as pk
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
    page_icon="💮",
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

st.title('Uji Data Dengan Data Baru')

st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>MENU</p>", unsafe_allow_html=True)

# menu string input
data_input = st.text_input(placeholder='Masukkan data yang ingin diuji' , label='Data Input')
submit = st.button('Submit')

# if submit:
#     with st.spinner('Sedang memproses data...'):
#         # load csv hasilstopword
#         data = pd.read_csv('data/hasilstopword.csv' , nrows=402)
#         data = data[['content']]
        
#         # masukkan data baru ke dalam data
#         data.loc[len(data)] = data_input
        
#         data = data.tail(1)
        
#         data['text_token'] = data['content'].apply(lambda x: x.split())
#         data = pk.clean_text(data, 'text_token' , 'text_clean')
        
#         # ambil data kamus 
#         data_kamus  = pd.read_csv('data/kamus_normalization.csv')
        
#         data['content_norm'] = data['text_clean'].apply(lambda x: pk.normalisasi(x, data_kamus))
        
#         data['text_stopword'] = data['content_norm'].apply(pk.remove_stopwords)

#         # spacy.cli.download("en_core_web_sm")
#         nlp = spacy.load("en_core_web_sm")
#         # Tambahkan ekstensi untuk Token spaCy
#         Token.set_extension('lemma_indonesian', getter=pk.lemmatize_indonesian, force=True)
        
#         # Inisialisasi spaCy dengan model bahasa Indonesia
#         nlp = spacy.blank('id')
        
#         # Tambahkan pipeline tokenizer spaCy
#         def custom_tokenizer(nlp):
#             return spacy.tokenizer.Tokenizer(nlp.vocab)

#         nlp.tokenizer = custom_tokenizer(nlp)
        
#         data['hasil_lemma'] = data['text_stopword'].apply(lambda x: ' '.join([token._.lemma_indonesian for token in nlp(x)]))
        
        
#         data_test = pd.read_csv('data/labellingfix.csv')['text_prepro']
        
#         # masukkan variabel data  ke dalam data_test
#         data_test.loc[len(data_test)] = data['hasil_lemma'].values[0]
        
#         # convert data_test to dataframe
#         data_test = pd.DataFrame(data_test)
        
#         data_test['text_prepro'] = data_test['text_prepro'].fillna('')
        
#         # Membuat objek CountVectorizer dan TfidfVectorizer
#         count_vectorizer = CountVectorizer()
#         tfidf_vectorizer = TfidfVectorizer()

#         # Transformasi teks dengan CountVectorizer
#         TF_vector = count_vectorizer.fit_transform(data_test["text_prepro"])
#         normalized_tf_vector = normalize(TF_vector, norm='l1', axis=1)

#         # Transformasi teks dengan TfidfVectorizer
#         tfs = tfidf_vectorizer.fit_transform(data_test["text_prepro"])
#         IDF_vector = tfidf_vectorizer.idf_
        
#         # # save tfs with joblib
#         # joblib.dump(tfs, 'data/tfs.pkl')
        
#         # joblib.dump(tfidf_vectorizer, 'data/tfidf_vectorizer.pkl')
        
#         # joblib.dump(TF_vector, 'data/TF_vector.pkl')

#         # Mengalikan matriks TF yang sudah dinormalisasi dengan IDF
#         tfidf_mat = normalized_tf_vector.multiply(IDF_vector).toarray()

#         # Mengubah hasil menjadi DataFrame
#         df_tfidf = pd.DataFrame(tfidf_mat, columns=tfidf_vectorizer.get_feature_names_out())
        
#         # ambil data terakhir
#         df_tfidf = df_tfidf.tail(1)
        
#         # ambil data tfidf csv
#         data_tfidf = pd.read_csv('data/tfidffix.csv')
        
#         data_tfidf = pd.concat([data_tfidf, df_tfidf], ignore_index=True).tail(1)
        
        
        
            
#         # load model SVM 
#         model1 = joblib.load('models/modelsvm.pkl')
#         y_pred1 = model1.predict(data_tfidf)
        
        
#         model3 = joblib.load('models/modelsvm+smote.pkl')
#         y_pred3 = model3.predict(data_tfidf)
        
#         data_tfidf = data_tfidf.iloc[:,:1842]
#         model2 = joblib.load('models/modelsvm+chisquare.pkl')
#         y_pred2 = model2.predict(data_tfidf)
        
#         model4 = joblib.load('models/modelsvm+chisquare+smote.pkl')
#         y_pred4 = model4.predict(data_tfidf)
        
#         # hasil prediksi dari data_input pakai h3 di tengah
#         st.write('Hasil Prediksi dari kalimat :' , data_input)
        
        
#         ps1,ps3 = st.columns(2)
#         with ps1:
#             st.markdown('**Model SVM**')
#             st.write(y_pred1)
#         with ps3:
#             st.markdown('**Model SVM + SMOTE**')
#             st.write(y_pred3)
        
#         ps2,ps4 = st.columns(2)
#         with ps2:
#             st.markdown('**Model SVM + Chi Square**')
#             st.write(y_pred2)
#         with ps4:
#             st.markdown('**Model SVM + SMOTE + Chi Square**')
#             st.write(y_pred4)    
# else:
#     st.warning('Silahkan masukkan data yang ingin diuji dan klik submit')