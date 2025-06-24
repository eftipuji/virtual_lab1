import streamlit as st
import math
import time
import random
import pandas as pd
import plotly.express as px

# Fungsi untuk menghitung jarak Euclidean 3D
def hitung_jarak_3d(x1, y1, z1, x2, y2, z2):
    """Menghitung jarak Euclidean antara dua titik di ruang 3D."""
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    jarak_kuadrat = dx**2 + dy**2 + dz**2
    return math.sqrt(jarak_kuadrat)

# --- Konfigurasi Halaman Streamlit ---
st.set_page_config(
    page_title="Petualangan Jarak Objek Antariksa 🌌",
    page_icon="🌠",
    layout="wide", # Menggunakan layout lebar untuk visualisasi yang lebih baik
    initial_sidebar_state="expanded"
)

# --- Judul dan Deskripsi Aplikasi ---
st.title("✨ Petualangan Mengukur Jarak di Alam Semesta ✨")
st.markdown("""
Selamat datang di kalkulator jarak 3D antar objek antariksa!
Aplikasi ini membantu Anda menghitung **jarak Euclidean** antara dua titik di ruang tiga dimensi.
Masukkan koordinat **X, Y, Z** untuk dua objek (misalnya, planet, wahana antariksa, atau bintang)
di **sidebar kiri**, lalu saksikan keajaiban perhitungannya!
""")

st.sidebar.header("Koordinat Objek Antariksa 🛰️")
st.sidebar.markdown("---")

# --- Input Koordinat Objek 1 ---
st.sidebar.subheader("Objek Pertama (Titik A)")
nama_objek1 = st.sidebar.text_input("Nama Objek 1", "Bumi", help="Contoh: Bumi, Satelit X").strip()
# Default values diambil dari contoh jarak Matahari-Bumi (juta km)
x1 = st.sidebar.number_input(f"Koordinat X {nama_objek1} (km)", value=149_600_000.0, format="%.2f", key="x1_input")
y1 = st.sidebar.number_input(f"Koordinat Y {nama_objek1} (km)", value=0.0, format="%.2f", key="y1_input")
z1 = st.sidebar.number_input(f"Koordinat Z {nama_objek1} (km)", value=0.0, format="%.2f", key="z1_input")

st.sidebar.markdown("---")

# --- Input Koordinat Objek 2 ---
st.sidebar.subheader("Objek Kedua (Titik B)")
nama_objek2 = st.sidebar.text_input("Nama Objek 2", "Mars", help="Contoh: Mars, Wahana Voyager").strip()
# Default values diambil dari contoh jarak Matahari-Mars (juta km) dan sedikit diubah untuk z
x2 = st.sidebar.number_input(f"Koordinat X {nama_objek2} (km)", value=227_900_000.0, format="%.2f", key="x2_input")
y2 = st.sidebar.number_input(f"Koordinat Y {nama_objek2} (km)", value=50_000_000.0, format="%.2f", key="y2_input")
z2 = st.sidebar.number_input(f"Koordinat Z {nama_objek2} (km)", value=10_000_000.0, format="%.2f", key="z2_input")

st.markdown("---") # Garis pemisah konten utama dari sidebar

# --- Tombol Hitung dan Animasi ---
st.header("🔬 Hasil Perhitungan Jarak")

# Menggunakan st.form untuk mengelompokkan input dan tombol submit
with st.form("jarak_form"):
    st.write("Tekan tombol di bawah untuk memulai perhitungan!")
    submit_button = st.form_submit_button("Hitung Jarak Antar Objek 🚀")

    if submit_button:
        # Menampilkan pesan proses
        status_placeholder = st.empty()
        status_placeholder.info("Menganalisis posisi objek di alam semesta...")
        
        # Animasi progress bar
        progress_bar = st.progress(0)
        for percent_complete in range(101):
            time.sleep(0.01) # Jeda kecil untuk animasi
            progress_bar.progress(percent_complete)
            if percent_complete < 30:
                status_placeholder.info("Membandingkan lokasi objek...")
            elif percent_complete < 70:
                status_placeholder.info("Menerapkan rumus jarak Euclidean 3D...")
            elif percent_complete < 99:
                status_placeholder.info("Mengamankan hasil akhir...")
            
        progress_bar.empty() # Menghilangkan progress bar setelah selesai
        status_placeholder.empty() # Menghilangkan pesan status setelah selesai

        jarak_final = hitung_jarak_3d(x1, y1, z1, x2, y2, z2)

        # Memilih warna secara acak untuk hasil
        colors = ["#4CAF50", "#2196F3", "##FFC107", "#9C27B0", "#E91E63"] # Palet warna Material Design
        selected_color = random.choice(colors)

        # Menampilkan hasil dengan HTML/CSS sederhana untuk efek visual
        # Dihindari animasi CSS kompleks untuk kompatibilitas lebih baik
        st.markdown(f"""
        <div style="background-color:{selected_color}; padding: 25px; border-radius: 12px; text-align: center; margin-top: 20px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
            <h3 style="color: white; margin-bottom: 15px; font-size: 28px;">🎉 Jarak Terukur! 🎉</h3>
            <p style="font-size: 22px; font-weight: normal; color: white;">
                Jarak antara <span style="font-style: italic; font-weight: bold;">{nama_objek1}</span> dan <span style="font-style: italic; font-weight: bold;">{nama_objek2}</span> adalah:
            </p>
            <p style="font-size: 48px; font-weight: bolder; color: white;">
                {jarak_final:,.2f} km
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.success("Perhitungan berhasil diselesaikan! Selamat menjelajah alam semesta!")

        # --- Visualisasi Sederhana dengan Plotly ---
        st.header("🗺️ Visualisasi Posisi Objek")
        st.write("Grafik di bawah menunjukkan posisi relatif kedua objek di ruang 3D.")

        data = {
            'Objek': [nama_objek1, nama_objek2],
            'X': [x1, x2],
            'Y': [y1, y2],
            'Z': [z1, z2]
        }
        df = pd.DataFrame(data)

        # Membuat plot scatter 3D
        fig = px.scatter_3d(df, x='X', y='Y', z='Z', color='Objek', text='Objek',
                            title='Posisi Objek di Ruang Angkasa',
                            labels={'X': 'X Koordinat (km)', 'Y': 'Y Koordinat (km)', 'Z': 'Z Koordinat (km)'},
                            height=650) # Ukuran plot yang lebih baik

        # Menambahkan garis yang menghubungkan kedua titik untuk menunjukkan jarak
        fig.add_scatter3d(x=[x1, x2], y=[y1, y2], z=[z1, z2],
                          mode='lines',
                          line=dict(color='gray', width=5, dash='dot'), # Garis putus-putus
                          name='Garis Jarak')

        # Mengatur tata letak agar sumbu terlihat lebih jelas dan proporsional
        fig.update_layout(scene_aspectmode='data')
        fig.update_traces(marker=dict(size=8, opacity=0.8), selector=dict(mode='markers')) # Ukuran marker

        st.plotly_chart(fig, use_container_width=True)

# Jika tombol belum ditekan atau halaman baru dimuat
if not submit_button:
    st.info("Masukkan koordinat objek di **sidebar kiri** dan klik tombol 'Hitung Jarak Antar Objek' di atas untuk memulai.")


st.markdown("---")
st.caption("Disclaimer: Koordinat yang digunakan dalam aplikasi ini bersifat **ilustratif** dan **fiktif**. Untuk data posisi objek astronomi yang akurat (efemeris), diperlukan model dan data yang jauh lebih kompleks dan presisi.")
st.caption("Dibuat dengan ❤️ dan Streamlit di Pekalongan, " + time.strftime("%A, %d %B %Y", time.localtime()))
