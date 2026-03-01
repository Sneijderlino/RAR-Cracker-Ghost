<!-- ==================== BANNER ==================== -->

<h1 align="center">🔓 RAR‑Cracker‑Ghost</h1>
<h3 align="center">Aplikasi Python untuk Peretasan kata sandi file RAR</h3>

<p align="center">
  <img src="/img/sampel.png" alt="Sample Preview" width="80%" style="border-radius:12px; box-shadow:0 0 25px #00fff7;">
</p>

<p align="center">
  <em>Dirancang untuk tujuan pentesing dan bahan pelajaran, bukan untuk kejahatan.</em>
</p>

---

**Repository:** <https://github.com/Sneijderlino/RAR-Cracker-Ghost>

> **Penting!** Sebelum menjalankan program ini, pastikan kamu memiliki hak atas file RAR yang diuji. Aplikasi ini hanya untuk tujuan **pengujian keamanan** dan **pemulihan password**. Menggunakan teknik ini pada file orang lain tanpa izin adalah ilegal.

> Jika kamu tidak yakin apakah kamu punya izin, hentikan dan tanyakan pemiliknya.

---

## 🧰 Fitur Utama

Bagian ini memberitahu apa yang bisa dilakukan program dan alat apa yang digunakan.

- **GUI ** menggunakan pustaka Tkinter sehingga terlihat seperti aplikasi biasa di Windows/Linux.
- Dapat menggunakan daftar kata (wordlist) bawaan `rockyou.txt` atau daftar kustom buatan sendiri.
- Menggabungkan `rar2john` untuk mengekstrak hash password dari file RAR, lalu `john` (John the Ripper) untuk mencoba menebak password.
- Menampilkan **progress bar** agar pengguna tahu operasinya masih berjalan.
- Jika GUI tidak tersedia (misalnya di Termux/Android), instruksi cara menjalankan versi **baris perintah (CLI)** juga disediakan.

> `rockyou.txt` adalah file teks berisi jutaan kata sandi umum yang sering digunakan para peneliti keamanan untuk latihan.

---

## 📷 Preview
<p align="center">
  <img src="/img/sampel-berhasil.png" alt="Sample Preview" width="80%" style="border-radius:12px; box-shadow:0 0 25px #00fff7;">
</p>
> Gambar diatas menunjukkan tampilan GUI ketika memilih file dan wordlist, kemudian mengeksekusi proses.

---

## ⚙️ Persiapan & Instalasi

Sebelum menjalankan program, kamu perlu menyiapkan beberapa hal. Jangan khawatir, kami akan jelaskan langkah demi langkah!

### 🔍 Apa yang perlu kamu miliki

1. **Komputer/laptop** dengan sistem operasi Windows, Linux (Debian/Kali) atau Android (melalui Termux).
2. **Koneksi internet** untuk mengunduh software dan repositori GitHub.
3. **Hak istimewa administrator/root** pada sistem untuk instalasi beberapa paket.
4. **Python 3 versi 3.8 atau lebih baru**.
5. **John the Ripper** (alat cracking) beserta utilitas `rar2john`.
6. **Git** (untuk mengunduh kode dari GitHub) — nilai tambah jika belum punya.

> 📁 File utama proyek bernama `cracker-rar.py`. Kamu bisa membukanya dengan editor teks (Notepad, VS Code) atau menjalankannya langsung dari terminal.

### 📦 Windows

1. **Download dan instal Python**
   - Buka <https://www.python.org/downloads/windows/> dan klik tombol "Download Python 3.x".
   - Jalankan installer dan centang opsi **"Add Python 3.x to PATH"** sebelum mengklik "Install Now".
   - Setelah selesai, buka Command Prompt (tekan Windows + R, ketik `cmd`, tekan Enter) dan jalankan:
     ```cmd
     python --version
     ```
     Jika muncul versi Python, berarti berhasil.

2. **Perbarui manajer paket pip** dengan perintah:

   ```cmd
   python -m pip install --upgrade pip
   ```

3. **Pastikan Tkinter terpasang**
   - Biasanya sudah ikut terinstall.
   - Untuk memeriksa, jalankan Python lalu ketik:
     ```python
     import tkinter
     tkinter._test()
     ```
     Jika jendela kecil muncul, Tkinter siap pakai.

4. **Instal John the Ripper**
   - Kunjungi <https://www.openwall.com/john/> dan unduh versi Windows (archive ZIP).
   - Ekstrak dan salin file `john.exe` dan `rar2john.exe` ke folder yang sudah ada di PATH (misalnya `C:\Windows\System32` atau gunakan Chocolatey:
     ```cmd
     choco install john
     ```
   - Untuk memeriksa, buka cmd dan jalankan:
     ```cmd
     john --help
     ```

5. **Unduh kode dari GitHub**
   - Jika Git belum ada, download <https://git-scm.com/download/win> dan instal.
   - Kemudian di Command Prompt:
     ```cmd
     git clone https://github.com/Sneijderlino/RAR-Cracker-Ghost.git
     cd RAR-Cracker-Ghost
     ```
   - Kamu sekarang berada di folder proyek.

6. **Jalankan aplikasi**

   ```cmd
   python cracker-rar.py
   ```

   - Jendela GUI akan muncul.
   - Jika muncul pesan kesalahan, baca pesan tersebut; mungkin Python atau John belum berada di PATH.

> **Tips untuk pemula:** jika wordlist `rockyou.txt` tidak ada di sistem, kamu bisa mengunduhnya dari internet atau mencarinya di folder lain, lalu pilih melalui tombol "PAKAI WORDLIST CUSTOM" pada aplikasi.

### 🐧 Kali Linux / Debian‑based (contoh: Ubuntu, Kali)

Instruksi berikut ditujukan untuk pengguna baru Linux yang nyaman membuka terminal.

1. **Buka terminal** (biasanya Ctrl+Alt+T).
2. Jalankan perintah berikut satu per satu. Yang pertama memperbarui daftar paket, yang kedua menginstal program yang dibutuhkan.

   ```bash
   sudo apt update                  # perbarui informasi paket
   sudo apt install python3 python3-tk john unrar git
   ```

   - `python3` = interpreter Python versi 3
   - `python3-tk` = pustaka untuk GUI Tkinter
   - `john` = John the Ripper
   - `unrar` = membantu membuka arsip RAR (opsional)
   - `git` = alat untuk mengunduh repositori GitHub

3. **Siapkan wordlist rockyou** (umumnya terkompresi pada sistem Kali):

   ```bash
   sudo zcat /usr/share/wordlists/rockyou.txt.gz > /usr/share/wordlists/rockyou.txt
   ```

   - Perintah ini mengekstrak file `.gz` menjadi teks biasa.
   - Jika tidak ada file tersebut, kamu bisa mengunduh wordlist dari internet atau membuat sendiri.

4. **Clone repo dan jalankan aplikasi**

   ```bash
   git clone https://github.com/Sneijderlino/RAR-Cracker-Ghost.git
   cd RAR-Cracker-Ghost
   python3 cracker-rar.py
   ```

   - Perintah terakhir membuka aplikasi GUI. Pastikan kamu berada di lingkungan desktop (bukan murni terminal server).

> 🔎 **Catatan pemula:** apabila muncul error terkait `tkinter` atau `python3`, pastikan paket sudah terinstal. Jika `python3` tidak ditemukan, jalankan `which python3` untuk mengecek.

#### Menggunakan versi terminal

Jika kamu menggunakan komputer tanpa layar grafis (mis. SSH), cukup jalankan John sendiri:

```bash
rar2john target.rar > crack.hash       # ekstrak hash dari file RAR
john --wordlist=/usr/share/wordlists/rockyou.txt crack.hash
john --show crack.hash                # tampilkan password bila berhasil
```

- Ganti `target.rar` dengan nama file RAR yang ingin kamu uji.
- `crack.hash` adalah file sementara yang dibuat John.

> Tip: gunakan paket `screen` atau `tmux` jika proses memakan waktu lama, agar kamu bisa memutus sambungan SSH tanpa menghentikan cracking.

### 📱 Termux (Android) – Versi baris perintah saja

Termux adalah aplikasi terminal untuk Android.
Karena tidak ada dukungan GUI (Tkinter tidak berjalan di Android), kamu hanya bisa memakai mode CLI.

1. **Update paket dan instal prasyarat**

   ```bash
   pkg update && pkg upgrade
   pkg install python git clang make
   ```

   - `clang` dan `make` diperlukan untuk mengompilasi John the Ripper karena tidak selalu tersedia dalam repos.

2. **Unduh dan kompilasi John the Ripper**

   ```bash
   git clone https://github.com/openwall/john.git
   cd john/src
   ./configure && make -s clean && make -sj4
   cp ../run/john /data/data/com.termux/files/usr/bin/
   cp ../run/rar2john /data/data/com.termux/files/usr/bin/
   ```

   - Ini memerlukan beberapa menit. Jika kamu menemukan error, pastikan `pkg install g++` juga.

3. **Ambil kode aplikasi**
   ```bash
   cd $HOME
   git clone https://github.com/Sneijderlino/RAR-Cracker-Ghost.git
   cd RAR-Cracker-Ghost
   ```

> Jalankan `python3 cracker-rar.py` hanya untuk melihat pesan kesalahan GUI (tidak akan tampil). Fokuslah pada perintah John di bawah.

#### Contoh penggunaan CLI di Termux

```bash
# ekstrak hash dari file RAR
rar2john nama_file.rar > crack.hash

# jalankan John dengan wordlist
john --wordlist=rockyou.txt crack.hash

# lihat hasil jika password ditemukan
john --show crack.hash
```

- Gantilah `nama_file.rar` dengan path arsip yang ingin kamu uji.
- Simpan wordlist (`rockyou.txt` atau file buatan sendiri) pada direktori yang mudah diakses (misalnya $HOME).

> 💡 Jika John tidak mengenali perintah `rar2john`, cek kembali apakah file sudah dipindah ke `/data/data/com.termux/files/usr/bin/` dan jalankan `hash -r` untuk memperbarui cache shell.

---

## 🚀 Penggunaan

1. Buka aplikasi (`python cracker-rar.py`).
2. Klik **"PILIH FILE RAR TARGET"** dan pilih arsip.
3. Pilih wordlist:
   - `PAKAI ROCKYOU (BAWAAN)` (jika terpasang di sistem), atau
   - `PAKAI WORDLIST CUSTOM` untuk file `.txt` sendiri.
4. Tekan tombol **[ EXECUTE PENETRATION ]**.
5. Tunggu progress selesai; hasil password akan tampil di jendela popup.

Untuk penggunaan terminal, ikuti contoh CLI di atas.

---

## 📝 Kontribusi

Bug report, PR, atau saran fitur sangat disambut. Silakan buka issue di repositori GitHub.

Untuk panduan kontribusi yang lebih rinci, lihat [CONTRIBUTING.md](CONTRIBUTING.md). Harap juga baca [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) sebelum berpartisipasi.

---

## 📄 Lisensi

Distribusi ini menggunakan lisensi **MIT**. Salinan lengkap tersedia di file [LICENSE](LICENSE).

---

## 📂 Berkas Pendukung

Kami telah menyertakan beberapa berkas tambahan agar repositori terlihat lebih profesional:

- `.gitignore` – mengabaikan file sementara dan lingkungan virtual
- `requirements.txt` – daftar dependensi (hanya standar untuk saat ini)
- `CONTRIBUTING.md` – pedoman kontribusi
- `CODE_OF_CONDUCT.md` – etika berkolaborasi
- `CHANGELOG.md` – riwayat perubahan proyek

Silakan baca masing-masing jika Anda ingin berkontribusi atau memahami struktur proyek.

---

> Dibuat oleh **Sneijderlino** – 🎯 _ethical research · secure systems · continuous growth_.
# RAR-Cracker-Ghost
