import streamlit as st

st.set_page_config(page_title="For Riani Senjawati ❤️", page_icon="💙", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0f7fa;
    }
    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        color: #212121;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul dengan warna hitam pekat langsung agar tidak tembus pandang
st.markdown("<h1 style='text-align: center; color: #1a237e; font-weight: 900;'>For Riani Senjawati 💙</h1>", unsafe_allow_html=True)

if 'buka' not in st.session_state:
    st.session_state.buka = False

if not st.session_state.buka:
    st.markdown("<p style='text-align: center; color: #01579b; font-weight: 700; font-size: 1.2rem;'>Aku punya sesuatu spesial buat kamu...</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💌 Buka ", use_container_width=True):
            st.session_state.buka = True
            st.rerun()
else:
    st.markdown(
        """
        <div class='letter-box'>
            <p>Bagaikan sebuah sistem database yang terstruktur rapi, hatiku ini sudah mengunci satu data paling istimewa dan memposisikan kamu sebagai satu-satunya primary key yang mutlak.</p>
            <p>Karena sifatnya yang unik dan tidak tergantikan, sama sekali tidak ada ruang bagi data asing atau entitas lain untuk masuk atau menyusup ke dalam hidupku, sebab seluruh batasan dan aturan aksesnya sudah terikat permanen hanya untuk kamu seorang.</p>
            <p>Ditambah lagi, koneksi perasaan yang aku punya ke kamu itu ibarat jaringan privat yang terhubung secara langsung tanpa jeda, tanpa hambatan jarak, dan selalu aktif menerima sinyal rindu dari kamu setiap detik tanpa pernah mengalami gangguan.</p>
            <p style='text-align: right; font-style: italic; color: #01579b; margin-top: 25px; font-weight: bold;'>
                Dengan sepenuh hati,<br>Rado Ananda Pratama 💙
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("⬅️ Kembali ke Menu Awal"):
        st.session_state.buka = False
        st.rerun()