# 📧 TempMail CLI
Script sederhana untuk mengambil alamat email sementara langsung dari terminal (Termux/Linux). Dibuat dengan Python + Requests.

![Screenshot](https://github.com/user-attachments/assets/b94d233f-622b-451c-bc71-4d6799ecc711)

---

## 🔥 Fitur
- ✅ Generate email sementara
- ✅ Dapatkan inbox secara real-time
- ✅ Ganti alamat email baru
- ✅ Tampilan CLI dengan warna menarik
- ✅ Cocok untuk verifikasi email tanpa akun pribadi

---

## 📦 Cara Instalasi (Termux)
```bash
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/AinxBOT/TempMail
cd TempMail
termux-setup-storage
pip install -r requirements.txt
python mail.py
