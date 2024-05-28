# Mengimpor pustaka tkinter untuk membuat antarmuka pengguna 
# grafis (GUI) dan messagebox untuk menampilkan kotak pesan.

import tkinter as tk
from tkinter import messagebox

# Menetapkan username dan password yang akan digunakan untuk login.

nama = "16"
kunci = "539231184"

# Fungsi ini mengambil username dan password dari entri, lalu memeriksa kecocokannya dengan nama dan kunci.
# Jika cocok, elemen-elemen login dihapus dan aplikasi kasir dibuka. Jika tidak cocok, pesan "Login Gagal" dicetak.

def buttonLogin():
    username = ussernameEntry.get()
    password = passwordEntry.get()
    if username == nama and password == kunci:
        print("Login Berhasil")
        ussernameLabel.pack_forget()
        ussernameEntry.pack_forget()
        passwordLabel.pack_forget()
        passwordEntry.pack_forget()
        submit.pack_forget()
        menu.destroy()
        kasir()
    else:
        print("Login Gagal")

# Fungsi ini mengambil data pembeli, nama barang, jumlah barang, harga barang, dan uang yang diterima. 
# Kemudian menghitung total harga, kembalian, dan menampilkan informasi tersebut dalam kotak pesan.

def calculate_change():

    buyer = buyer_entry.get()
    item = item_entry.get()
    quantity = int(quantity_entry.get())
    price = int(price_entry.get())
    received = int(received_entry.get())

    total = quantity * price
    change = received - total
    info = f"""
    Nama Pembeli = {buyer}
    ============================
    Nama Barang = {item}
    Jumlah Barang = {quantity}
    Harga Rp. {price}
    ============================
    Total = Rp. {total}
    Tunai = Rp. {change}
    --------------------------
    Kembali = Rp. {change}

    Terima Kasih Telah Berbelanja!!
    """
    messagebox.showinfo("Invoice", info)

# Fungsi ini membuat jendela baru untuk aplikasi kasir, dengan beberapa entri untuk memasukkan data pembeli, 
# barang, jumlah, harga, dan uang yang diterima. Terdapat juga tombol untuk menghitung total dan kembalian.

def kasir():
    window = tk.Tk()
    window.geometry("250x400")

    buyer_label = tk.Label(window, text="Nama Pembeli:")
    buyer_label.pack()

    global buyer_entry
    buyer_entry = tk.Entry(window)
    buyer_entry.pack()

    item_label = tk.Label(window, text="Nama Barang:")
    item_label.pack()

    global item_entry
    item_entry = tk.Entry(window)
    item_entry.pack()

    quantity_label = tk.Label(window, text="Jumlah Produk: (Angka)")
    quantity_label.pack()

    global quantity_entry
    quantity_entry = tk.Entry(window)
    quantity_entry.pack()

    price_label = tk.Label(window, text="Harga Produk: (Angka)")
    price_label.pack()

    global price_entry
    price_entry = tk.Entry(window)
    price_entry.pack()

    received_label = tk.Label(window, text="Uang Pembeli: (Angka)")
    received_label.pack()

    global received_entry
    received_entry = tk.Entry(window)
    received_entry.pack()

    calculate_button = tk.Button(window, text="Total", command=calculate_change)
    calculate_button.pack()

    window.mainloop()

# Bagian ini membuat jendela login dengan dua entri untuk 
# username dan password serta tombol login yang memanggil fungsi buttonLogin.

menu = tk.Tk()
menu.geometry("250x300")
ussernameLabel = tk.Label(menu, text="Username")
ussernameLabel.pack()

ussernameEntry = tk.Entry(menu)
ussernameEntry.pack()

passwordLabel = tk.Label(menu, text="Password")
passwordLabel.pack()

passwordEntry = tk.Entry(menu, show="*")
passwordEntry.pack()

submit = tk.Button(menu, text="Login", command=buttonLogin)
submit.pack()

menu.mainloop()
