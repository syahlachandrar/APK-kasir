#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

class LaundryApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple Application Laundry Cashier")
        self.root.geometry('400x310')
        self.root['bg'] = "#DEB887"

        self.nama_pelanggan = tk.StringVar()
        self.berat_pakaian = tk.StringVar()
        self.jenis_laundry = tk.StringVar()
        self.total_harga = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label judul
        heading = tk.Label(self.root, text="--- Laundry Rwesix ---", font=('verdana', 20, 'bold', 'italic'), bg="#DEB887")
        heading.place(x=60, y=5)

        # Label dan Entry untuk nama pelanggan
        lbl_nama_pelanggan = tk.Label(self.root, text="Nama Pelanggan", bg="#DEB887")
        lbl_nama_pelanggan.place(x=10, y=60)
        entry_nama_pelanggan = tk.Entry(self.root, textvariable=self.nama_pelanggan)
        entry_nama_pelanggan.place(x=180, y=60)

        # Label dan OptionMenu untuk jenis laundry
        lbl_jenis_laundry = tk.Label(self.root, text="Jenis Laundry", bg="#DEB887")
        lbl_jenis_laundry.place(x=10, y=90)
        options = ['Cuci', 'Setrika', 'Cuci + Setrika', 'Selimut', 'Boneka', 'Lainnya per pcs']
        option_menu = tk.OptionMenu(self.root, self.jenis_laundry, *options)
        option_menu.place(x=180, y=90)

        # Label dan Entry untuk berat pakaian
        lbl_berat_pakaian = tk.Label(self.root, text="Berat(kg)/(pcs)", bg="#DEB887")
        lbl_berat_pakaian.place(x=10, y=135)
        entry_berat_pakaian = tk.Entry(self.root, textvariable=self.berat_pakaian)
        entry_berat_pakaian.place(x=180, y=135)

        # Tombol Hitung
        btn_hitung = tk.Button(self.root, text="Hitung", command=self.hitung_total_harga)
        btn_hitung.place(x=180, y=170)

        # Label untuk total harga
        lbl_total_harga = tk.Label(self.root, text="Total Harga", bg="#DEB887")
        lbl_total_harga.place(x=10, y=210)
        lbl_total_harga_value = tk.Label(self.root, textvariable=self.total_harga, bg="#DEB887")
        lbl_total_harga_value.place(x=180, y=210)

        # Label ucapan terima kasih
        lbl_terima_kasih = tk.Label(self.root, text="Budayakan Malas Mencuci. Cuci Aja Di Sini!", bg="#DEB887", font=('verdana', 12, 'italic'), fg="#801622")
        lbl_terima_kasih.place(relx=0.5, rely=0.95, anchor='s')

    def hitung_total_harga(self):
        try:
            berat = float(self.berat_pakaian.get())
            jenis = self.jenis_laundry.get()

            if jenis == 'Cuci':
                harga_per_kg = 5000  # Harga per kilogram cuci
            elif jenis == 'Setrika':
                harga_per_kg = 3000  # Harga per kilogram setrika
            elif jenis == 'Cuci + Setrika':
                harga_per_kg = 7000  # Harga per kilogram cuci dan setrika
            elif jenis == 'Selimut':
                harga_per_kg = 8000  # Harga per kilogram selimut
            elif jenis == 'Boneka':
                harga_per_kg = 7000  # Harga per kilogram boneka
            elif jenis == 'Lainnya per pcs':
                harga_per_kg = 10000  # Harga per pcs

            total = berat * harga_per_kg
            self.total_harga.set(f"Rp {total:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan berat pakaian yang valid")

if _name_ == "_main_":
    root = tk.Tk()
    app = LaundryApp(root)
    root.mainloop()

