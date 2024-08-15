import streamlit as st
from cipher import caesar_cipher

st.title("CrypStique: Cryptic & Mystique")
st.text("Masukkan Teks dan Geser Cipher untuk Mengenkripsi atau Mendekripsi.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Enkripsi")
    text_to_encrypt = st.text_area("Masukkan Teks untuk Enkripsi:", "")
    shift_encrypt = st.slider("Besaran Shift untuk Enkripsi:", -25, 25, 3)
    
    if st.button("Enkripsi", key='encrypt'):
        encrypted_text = caesar_cipher(text_to_encrypt, shift_encrypt)
        st.text("Enkripsi Teks:")
        st.code(encrypted_text)

with col2:
    st.subheader("Dekripsi")
    text_to_decrypt = st.text_area("Masukkan Teks untuk Dekripsi:", "")
    shift_decrypt = st.slider("Besaran Shift untuk Dekripsi:", -25, 25, 3)
    
    if st.button("Dekripsi", key='decrypt'):
        decrypted_text = caesar_cipher(text_to_decrypt, -shift_decrypt)
        st.text("Dekripsi Teks:")
        st.code(decrypted_text)