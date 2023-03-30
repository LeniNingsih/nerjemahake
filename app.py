import streamlit as st
import subprocess

# Title for the page and nice icon
st.set_page_config(page_title="Nerjemahake",
    initial_sidebar_state="expanded")
# Header
st.title("Nerjemahake")

# Define function to translate the text
def translate(source_text):
    # Save the source text to file
    with open("data/source.txt", "w") as f:
        f.write(source_text)
    
    # Run the translation command
    command = "onmt_translate -model data/model_step_2000.pt -src data/source.txt -output data/pred.txt -verbose"
    subprocess.run(command, shell=True)
    
    # Read the predicted text from file and return it
    with open("data/pred.txt", "r") as f:
        pred_text = f.read()
    
    return pred_text

# Create sidebar with app information and help section
st.sidebar.markdown("# Nerjemahake: Aplikasi Penerjemahan Bahasa Jawa Ngoko - Krama")
st.sidebar.markdown("Aplikasi ini adalah demo penerjemahan dengan metode Neural Machine Translation menggunakan OpenNMT.")
st.sidebar.markdown("Masukkan teks yang ingin diterjemahkan pada kotak teks dan klik 'Terjemahkan'.")
# st.sidebar.markdown("---")
# st.sidebar.markdown("# Help")
# st.sidebar.markdown("Jika ada pertanyaan, silahkan kontak saya di support@gmail.com.")

# Form to add your items
with st.form("my_form"):
    source_text = st.text_area("Masukkan kalimat dalam bahasa jawa ngoko", placeholder="Contoh: Nggawa jeruk kuwi!", height=40, max_chars=200)
    if st.form_submit_button("Terjemahkan"):
        # Show loading spinner while translating
        with st.spinner("Sedang proses"):
            # Call translate function and store the result in pred_text
            pred_text = translate(source_text)
        # Show translated text in alert box
        st.info(pred_text)

# Hide footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
