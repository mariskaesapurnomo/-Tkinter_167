# Mengimport library tkinter dengan alias tk
import tkinter as tk
# Mengimport modul messagebox dari tkinter untuk menampilkan dialog
from tkinter import messagebox

#Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasilprediksi():
   # Mencoba validasi input
   try:
       # Loop untuk mengecek setiap entry
       for entry in entries:
           nilai = int(entry.get())
           # Memastikan nilai antara 0-100
           if not (0<= nilai <= 100):
               raise ValueError("Nilai harus antara 0 dan 100.")
       # Jika valid, tampilkan hasil prediksi        
       hasil_label.config(text ="Prediksi Prodi: Teknologi Informasi")
   # Menangkap error jika input tidak valid
   except ValueError as ve:
       messagebox.showerror("input error", "pastikan semua input adalah angka antara 0 sampai 100 ")

# Membuat window utama
root = tk.Tk()
# Mengatur judul window
root.title("Aplikasi Prediksi Prodi Pilihan")
# Mengatur ukuran window
root.geometry("500x600")
# Mengatur warna background window
root.configure(bg="sky blue")

#label judul
# Membuat label judul dengan font Arial 16
judul_label = tk.Label(root, text ="Aplikasi Prediksi Prodi Pilihan", font =("times new roman", 16))
# Menempatkan label judul dengan padding y 20
judul_label.pack(pady = 20)

#frame untuk input nilai mata pelajaran
# Membuat frame untuk mengelompokkan input fields
frame_input = tk.Frame(root, bg="sky blue")
# Menempatkan frame dengan padding y 10
frame_input.pack(pady =10)

# List untuk menyimpan entry fields
entries = []

# Loop untuk membuat 10 input fields
for i in range(10):
   # Membuat label untuk setiap mata pelajaran
   label = tk.Label(frame_input, text =f"Nilai Mata Pelajaran {i+1}:", font=("times new roman", 12))
   # Mengatur posisi label menggunakan grid
   label.grid(row =i, column=0, padx=10, pady=5, sticky="e")
   # Membuat entry field
   entry = tk.Entry(frame_input, width=10, font=("times new roman", 12))
   # Mengatur posisi entry menggunakan grid
   entry.grid(row=i, column=1, padx=10, pady=5)
   # Menambahkan entry ke dalam list entries
   entries.append(entry)

# Membuat tombol prediksi
prediksi_button = tk.Button(root, text = "Hasil Prediksi", command= hasilprediksi, font=("times new roman", 12))
# Menempatkan tombol dengan padding y 30
prediksi_button.pack(pady=30)

# Membuat label untuk menampilkan hasil
hasil_label =tk.Label(root, text="", font =("times new roman", 14, "italic", "bold"), fg="cyan", bg="sky blue")
# Menempatkan label hasil dengan padding y 20
hasil_label.pack(pady= 20)

# Memulai main loop aplikasi
root.mainloop()