import streamlit as st
from PIL import Image
import io
import base64
import math

# ===== Fungsi Konversi Base64 ke Gambar =====
def load_image_from_base64(base64_str):
    image_data = base64.b64decode(base64_str)
    return Image.open(io.BytesIO(image_data))

# ===== Gambar Bangun dalam Base64 =====
# Contoh: Gambar kotak 200x200 sebagai placeholder
persegi_base64 = '''
iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBIWXMAAAsTAAALEwEAmpwYAAAExElEQVR4nO3cMW7jOBAEwQeJu+H9b4uWkn5zNpgqGhH8lWubnUJfYAwAAAAAAAAAA4Gfg9+qBBfJ7Oef4F/P28uXVXt9/X/vnL3c/ffvN/Z6+2z5eNzH99ztfLV3nH2xrkQdvB8X/zfUOmVrgxzv10xfMxhd2uXnhGrl1xtcU3kQz+XPa+8kctnv+e6wdZr0bnqz/Z3slfVVp/XN8Z/npydp0jH3Etc67J5p3WzX+5n7NcYdY3V7uvR6VX4S1y77YbzvGXiV9JZ/bnbfG0Xr2av0y/U/3S1W57eMe5n2e7YpfU+Z9C2zF1jvM3nq6uF8AAAAASUVORK5CYII=
'''

lingkaran_base64 = persegi_base64  # ganti dengan base64 lingkaran
kubus_base64 = persegi_base64      # ganti dengan base64 kubus
bola_base64 = persegi_base64       # ganti dengan base64 bola

# ===== Data Bangun =====
bangun_data = {
    "Persegi": {
        "tipe": "datar",
        "gambar": persegi_base64,
        "input": ["Sisi"],
        "fungsi": lambda x: {
            "Ciri-ciri": "4 sisi sama panjang, 4 sudut siku-siku.",
            "Keliling": 4 * x[0],
            "Luas": x[0] ** 2
        }
    },
    "Lingkaran": {
        "tipe": "datar",
        "gambar": lingkaran_base64,
        "input": ["Jari-jari"],
        "fungsi": lambda x: {
            "Ciri-ciri": "Bentuk bundar sempurna, tidak memiliki sisi atau sudut.",
            "Keliling": round(2 * math.pi * x[0], 2),
            "Luas": round(math.pi * x[0] ** 2, 2)
        }
    },
    "Kubus": {
        "tipe": "ruang",
        "gambar": kubus_base64,
        "input": ["Sisi"],
        "fungsi": lambda x: {
            "Ciri-ciri": "6 sisi berbentuk persegi, 12 rusuk, 8 titik sudut.",
            "Volume": x[0] ** 3
        }
    },
    "Bola": {
        "tipe": "ruang",
        "gambar": bola_base64,
        "input": ["Jari-jari"],
        "fungsi": lambda x: {
            "Ciri-ciri": "Bentuk bulat sempurna, tidak memiliki rusuk dan sisi datar.",
            "Volume": round((4/3) * math.pi * x[0] ** 3, 2)
        }
    }
}

# ===== UI Streamlit =====
st.title("🧮 Kalkulator Geometri Interaktif (Dengan Gambar Tanam)")

bangun = st.selectbox("Pilih Bangun Geometri:", list(bangun_data.keys()))
data = bangun_data[bangun]

st.subheader(f"{bangun} ({data['tipe'].capitalize()})")

# Tampilkan Gambar dari Base64
try:
    img = load_image_from_base64(data["gambar"])
    st.image(img, width=250)
except Exception as e:
    st.warning(f"Gagal memuat gambar: {e}")

# Input Dinamis
nilai = []
for label in data["input"]:
    val = st.number_input(f"{label}:", min_value=0.0, step=1.0)
    nilai.append(val)

# Tombol Hitung
if st.button("Hitung"):
    try:
        hasil = data["fungsi"](nilai)
        st.success("Hasil Perhitungan:")
        for k, v in hasil.items():
            st.write(f"**{k}**: {v}")
    except:
        st.error("Terjadi kesalahan saat perhitungan.")
