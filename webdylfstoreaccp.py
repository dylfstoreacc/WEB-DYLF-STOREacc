import streamlit as st
import base64
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="DYLF STORE OFFICIAL", page_icon="🤖", layout="centered")

# ==============================================================================
# ⚙️ PANEL KONTROL (UBAH SEMUANYA DI SINI)
# ==============================================================================

# 1. FILE ANIMASI UTAMA & BACKGROUND 
FILE_MASKOT_UTAMA = "dfstoreacc.png"
FILE_BACKGROUND = "difibotv2.mp4"

# 2. WATERMARK KIRI ATAS (Bisa PNG, GIF, atau MP4)
FILE_WATERMARK = "dfstoreacc.png"

# 3. ICON DI DALAM TOMBOL
ICON_ADMIN = "v2df2.png" 
ICON_GRUP = "v2df2.png"
ICON_SALURAN = "v2df2.png"
ICON_TIKTOK = "v2df2.png"
ICON_IG = "v2df2.png"

# 4. TEKS PROFIL & BIO
NAMA_TOKO = "DYLF STOREacc"
BIO_TOKO = "Welcome to web DYLF STOREacc Pusat Layanan Jual & Beli Akun Digital Terpercaya khususnya akun game yg sedang kamu cari. Silahkan Join Komunitas dibawah ini untuk mendapatkan informasi lengkapnya dan jangan lupa untuk follow akun admin dibawah ini. Terimakasih🌱"

# 5. LINK SOSMED & KONTAK
LINK_WA_ADMIN = "https://wa.me/6285266953530"
LINK_GRUP_WA = "https://chat.whatsapp.com/IyHj3XJikuX90k6HSiMpDP"
LINK_SALURAN_WA = "https://whatsapp.com/channel/0029VbCmpXQ8vd1RqxIn6h0z"
LINK_TIKTOK = "https://www.tiktok.com/@dylfrvr?_r=1&_t=ZS-95E7GPLE9qB"
LINK_INSTAGRAM = "https://instagram.com/dylfrvr"

# ==============================================================================
# (JANGAN UBAH KODE DI BAWAH INI KECUALI ANDA PAHAM CSS/HTML)
# ==============================================================================

def load_local_file(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()
            ext = file_path.split('.')[-1].lower()
            if ext == "mp4":
                mime = "video/mp4"
            elif ext == "gif":
                mime = "image/gif"
            else:
                mime = f"image/{ext}"
            return f"data:{mime};base64,{encoded}"
    return None

# Eksekusi Maskot Utama
file_maskot_data = load_local_file(FILE_MASKOT_UTAMA)
if file_maskot_data and FILE_MASKOT_UTAMA.lower().endswith(".mp4"):
    html_maskot = f'<video src="{file_maskot_data}" class="profile-img" autoplay loop muted playsinline></video>'
elif file_maskot_data:
    html_maskot = f'<img src="{file_maskot_data}" class="profile-img" alt="Mascot">'
else:
    html_maskot = '<img src="https://dummyimage.com/200x200/0b0c10/bc13fe.png&text=ISI+VIDEO" class="profile-img" alt="Mascot">'

# Eksekusi Watermark Kiri Atas
watermark_data = load_local_file(FILE_WATERMARK)
if watermark_data and FILE_WATERMARK.lower().endswith(".mp4"):
    html_watermark = f'<video src="{watermark_data}" class="watermark-img" autoplay loop muted playsinline></video>'
elif watermark_data:
    html_watermark = f'<img src="{watermark_data}" class="watermark-img" alt="Watermark">'
else:
    html_watermark = ""

# Latar Belakang
bg_data = load_local_file(FILE_BACKGROUND)
html_bg = ""
css_bg = "background-color: #050508;"

if bg_data:
    if FILE_BACKGROUND.lower().endswith(".mp4"):
        html_bg = f'<video src="{bg_data}" autoplay loop muted playsinline class="background-video"></video>'
    else:
        css_bg = f"background-image: url('{bg_data}'); background-size: cover; background-position: center; background-attachment: fixed;"

# Fungsi render icon di dalam tombol
def get_icon_html(file_path):
    base64_img = load_local_file(file_path)
    if base64_img:
        return f'<img src="{base64_img}" class="btn-icon" alt="icon">'
    return ""

html_icon_admin = get_icon_html(ICON_ADMIN)
html_icon_grup = get_icon_html(ICON_GRUP)
html_icon_saluran = get_icon_html(ICON_SALURAN)
html_icon_tiktok = get_icon_html(ICON_TIKTOK)
html_icon_ig = get_icon_html(ICON_IG)

# --- CSS CUSTOM ---
st.markdown(f"""
    <style>
    /* Reset */
    a, a:hover, a:visited, a:active, h1, h2, h3, p, div, span {{
        text-decoration: none !important;
        border-bottom: none !important;
        outline: none !important;
    }}

    .stApp {{ {css_bg} color: #ffffff; }}
    
    .stApp::before {{
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(5, 5, 8, 0.70); z-index: 0;
    }}
    
    .block-container {{ padding-top: 2rem; padding-bottom: 2rem; max-width: 600px; z-index: 1; position: relative; }}

    .background-video {{
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; object-fit: cover;
    }}

    /* --- WATERMARK KIRI ATAS --- */
    .watermark-container {{
        position: absolute; top: 20px; left: 20px; width: 65px; z-index: 1000;
        filter: drop-shadow(0px 2px 5px rgba(0, 255, 255, 0.3));
    }}
    .watermark-img {{ width: 100%; height: auto; object-fit: contain; }}

    @media (max-width: 768px) {{
        .watermark-container {{ top: 15px; left: 15px; width: 50px; }}
    }}

    /* --- ANIMASI FLOATING & NEON PULSE NAVY --- */
    @keyframes floating {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-12px); }}
        100% {{ transform: translateY(0px); }}
    }}
    
    @keyframes neonPulseNavy {{
        0% {{ box-shadow: 0 0 10px #bc13fe, 0 0 20px #bc13fe; border-color: #bc13fe; }}
        50% {{ box-shadow: 0 0 20px #0a2463, 0 0 40px #0a2463; border-color: #0a2463; }}
        100% {{ box-shadow: 0 0 10px #bc13fe, 0 0 20px #bc13fe; border-color: #bc13fe; }}
    }}
    
    /* --- MASKOT UTAMA (TIDAK BULAT, TIDAK ADA GARIS NEON) --- */
    .profile-img-container {{
        display: flex; justify-content: center; margin-bottom: 15px; animation: floating 4s ease-in-out infinite;
    }}
    
    .profile-img {{
        width: 170px; /* Ukuran pas agar terlihat jelas */
        height: auto; 
        max-height: 170px;
        border-radius: 0; /* Menghilangkan bentuk bulat */
        object-fit: contain; /* Tidak terpotong */
        border: none; /* Menghilangkan garis luar */
        background-color: transparent !important; 
        /* Animasi glow dipindahkan dari sini */
    }}

    /* --- TEKS DENGAN STROKE (GARIS LUAR HITAM) AGAR ANTI-PUDAR --- */
    .profile-title {{
        text-align: center; color: #00ffff; font-family: 'Courier New', Courier, monospace;
        font-size: 26px; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000, 0px 0px 15px rgba(0, 255, 255, 0.9);
    }}
    
    .profile-bio {{
        text-align: center; color: #ffffff; font-size: 14px; font-weight: 600; line-height: 1.6;
        margin-bottom: 30px; background: rgba(188, 19, 254, 0.15); padding: 15px;
        border-radius: 15px; border: 1px solid rgba(188, 19, 254, 0.3); backdrop-filter: blur(5px);
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000, 0px 3px 6px rgba(0,0,0,0.9);
    }}

    /* --- TOMBOL LINK (SEKARANG MEMILIKI ANIMASI NEON PULSE!) --- */
    .link-btn {{
        display: flex; 
        align-items: center;
        justify-content: center;
        position: relative; 
        width: 100%;
        background: transparent !important; 
        color: #00ffff !important;
        padding: 16px;
        margin-bottom: 15px;
        border-radius: 30px;
        border: 2px solid #bc13fe; 
        font-family: 'Arial', sans-serif;
        font-weight: 800;
        font-size: 15px;
        transition: all 0.3s ease;
        animation: neonPulseNavy 3s infinite; /* EFEK NEON HIDUP SEKARANG DI SINI */
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000, 0px 2px 5px rgba(0,0,0,0.8);
    }}
    
    .link-btn:hover, .link-btn:active {{
        animation: none !important; /* Animasi berhenti saat disentuh */
        background-color: #bc13fe !important;
        color: #ffffff !important;
        border: 2px solid #0a2463 !important;
        box-shadow: 0px 0px 25px rgba(10, 36, 99, 0.9) !important;
        transform: scale(1.02); 
    }}

    .btn-icon {{
        position: absolute;
        left: 20px; 
        width: 35px;
        height: 35px;
        object-fit: contain; 
        filter: drop-shadow(0px 0px 3px rgba(0,0,0,0.8)); /* Sedikit bayangan pada icon agar tidak menyatu dengan background terang */
    }}
    </style>
""", unsafe_allow_html=True)

# --- RENDER HTML KONTEN ---
st.markdown(f"""
    {html_bg} 
    
    <div class="watermark-container">
        {html_watermark}
    </div>

    <div class="profile-img-container">
        {html_maskot}
    </div>
    
    <div class="profile-title">{NAMA_TOKO}</div>
    <div class="profile-bio">{BIO_TOKO}</div>
    
    <a href="{LINK_WA_ADMIN}" target="_blank" class="link-btn">
        {html_icon_admin} ADMIN REAL (Dileppp IsStarrr)
    </a>
    <a href="{LINK_GRUP_WA}" target="_blank" class="link-btn">
        {html_icon_grup} GB 1: DYLF STOREacc (GRUB JUAL&BELI)
    </a>
    <a href="{LINK_SALURAN_WA}" target="_blank" class="link-btn">
        {html_icon_saluran} CH: DYLF STOREacc (INFO STOK&TESTI)
    </a>
    <a href="{LINK_TIKTOK}" target="_blank" class="link-btn">
        {html_icon_tiktok} Official Tiktok: Dileppp
    </a>
    <a href="{LINK_INSTAGRAM}" target="_blank" class="link-btn">
        {html_icon_ig} Official Instagram: Dileppp
    </a>

    <div style="text-align: center; color: #ff4b4b; font-size: 13px; margin-top: 30px; padding: 12px; border-top: 1px dashed #ff4b4b; border-bottom: 1px dashed #ff4b4b; background: rgba(255, 0, 0, 0.05); border-radius: 8px; text-shadow: -0.5px -0.5px 0 #000, 0.5px -0.5px 0 #000, -0.5px 0.5px 0 #000, 0.5px 0.5px 0 #000;">
        ⚠️ WASPADA AKUN CLONE! Selalu cek nomor Admin & Link di atas sebelum transaksi.<br>
        <strong>Be smart buyer guys, jangan lupa baca deskripsi!</strong>
    </div>
    
    <div style="text-align: center; color: gray; font-size: 10px; margin-top: 20px;">
        © 2026 {NAMA_TOKO} | Protected by Difibot V2
    </div>
""", unsafe_allow_html=True)