import streamlit as st
import subprocess

# judul/title dan icon
st.set_page_config(page_title="Nerjemahake",
    initial_sidebar_state="expanded")
# Header
st.title("Nerjemahake")

# Membuat fungsi to translate the text
def translate(source_text):
    # menyimpan source_text ke file
    with open("data/source.txt", "w") as f:
        f.write(source_text)

    # menjalankan kode untuk menerjemahkan
    @st.cache_data
    command = "onmt_translate -model data/model_step_2000.pt -src data/source.txt -output data/pred.txt"
    subprocess.run(command)

    # membaca file pred.txt
    with open("data/pred.txt", "r") as f:
        pred_text = f.read()
    return pred_text

# Sidebar
st.sidebar.markdown("# Nerjemahake: Aplikasi Penerjemaionhan Bahasa Jawa Ngoko - Krama")
st.sidebar.markdown("Aplikasi ini adalah demo penerjemahan dengan metode Neural Machine Translation menggunakan OpenNMT.")
st.sidebar.markdown("Masukkan teks yang ingin diterjemahkan pada kotak teks dan klik 'Terjemahkan'.")
# st.sidebar.markdown("---")
# st.sidebar.markdown("# Help")
# st.sidebar.markdown("Jika ada pertanyaan, silahkan kontak saya di purwaningsihleni85@gmail.com.")

# form untuk tampilan fungsi
with st.form("my_form"):
    source_text = st.text_area("Masukkan kalimat dalam bahasa jawa ngoko", placeholder="Contoh: Nggawa jeruk kuwi!", height=40, max_chars=200)
    if st.form_submit_button("Terjemahkan"):
        # buat nampilin icon muter
        with st.spinner("Sedang proses"):
            # untuk fungsi memanggil hasil terjemahan dari source_text
            pred_text = translate(source_text)
        # Show translated text in alert box
        st.info(pred_text)

# menyembunyikan menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
