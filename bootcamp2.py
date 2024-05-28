# Kode ini mengimpor modul tkinter, yang digunakan untuk membuat antarmuka grafis di Python, 
# serta modul messagebox dari tkinter untuk menampilkan kotak pesan.

import tkinter as tk
from tkinter import messagebox

# Fungsi ini akan mengambil input dari pengguna untuk username dan password, kemudian memeriksa apakah sesuai 
# dengan nilai yang diharapkan (username = '16' dan password = '539231184'). Jika tidak sesuai, 
# pesan error akan ditampilkan. Jika sesuai, form login akan disembunyikan dan fungsi show_cashier akan dipanggil.
 
def submit_form():
    username = entry_name.get()
    password = entry_password.get()
    
    if username != '16' or password != '539231184':
        messagebox.showerror("Error", "Invalid username or password")
    else:
        form_frame.pack_forget()
        show_cashier()

# Fungsi ini membuat antarmuka kasir. Terdapat beberapa label dan input untuk pengguna memasukkan nama pembeli, 
# nama barang, jumlah produk, harga produk, dan uang pembeli. Saat tombol Total ditekan, fungsi show_result akan 
#dihitung dan menampilkan faktur belanja dengan detail yang dimasukkan.

def show_cashier():
    cashier_frame = tk.Frame(root)
    cashier_frame.pack()

    tk.Label(cashier_frame, text='Nama Pembeli:').pack()
    nama_pembeli = tk.Entry(cashier_frame)
    nama_pembeli.pack()

    tk.Label(cashier_frame, text='Nama Barang:').pack()
    nama_barang = tk.Entry(cashier_frame)
    nama_barang.pack()

    tk.Label(cashier_frame, text='Jumlah Produk: (Angka)').pack()
    jumlah_produk = tk.Entry(cashier_frame)
    jumlah_produk.pack()

    tk.Label(cashier_frame, text='Harga Produk: (Angka)').pack()
    harga_produk = tk.Entry(cashier_frame)
    harga_produk.pack()

    tk.Label(cashier_frame, text='Uang Pembeli: (Angka)').pack()
    uang_pembeli = tk.Entry(cashier_frame)
    uang_pembeli.pack()

    def show_result():
        message = f'''
        Nama Pembeli = {nama_pembeli.get()}
        ===================================
        Nama Barang = {nama_barang.get()}
        Jumlah Barang = {jumlah_produk.get()}
        Harga Rp. {harga_produk.get()}
        ===================================
        Total = Rp. {int(harga_produk.get()) * int(jumlah_produk.get())}
        Tunai = Rp. {uang_pembeli.get()}
        -----------------------------------
        Kembali = Rp. {int(uang_pembeli.get()) - int(harga_produk.get()) * int(jumlah_produk.get())}

        Terima Kasih Telah Berbelanja!!
        '''
        messagebox.showinfo('Invoice', message)
    
    tk.Button(cashier_frame, text='Total', command=show_result).pack()

# Bagian ini adalah bagian utama dari program yang dijalankan. Membuat jendela utama (root) dan frame untuk form 
# login (form_frame). Form login terdiri dari label dan input untuk username dan password serta tombol login 
# yang memanggil fungsi submit_form. root.mainloop() digunakan untuk menjalankan aplikasi Tkinter.

root = tk.Tk()

form_frame = tk.Frame(root)
form_frame.pack()

label_name = tk.Label(form_frame, text="Username")
label_name.pack()
entry_name = tk.Entry(form_frame)
entry_name.pack()

label_password = tk.Label(form_frame, text="Password")
label_password.pack()
entry_password = tk.Entry(form_frame, show="*")
entry_password.pack()

submit_button = tk.Button(form_frame, text="Login", command=submit_form)
submit_button.pack()

root.mainloop()

# Secara keseluruhan, program ini membuat aplikasi login sederhana dengan Tkinter,
# dan jika login berhasil, menampilkan antarmuka kasir untuk input dan perhitungan transaksi.
