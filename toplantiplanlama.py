import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
from PIL import Image, ImageTk

class ToplantiUygulamasi:
    def __init__(self, master):
        self.master = master
        self.master.title("Toplanti Uygulamasi")

        # Arkaplan rengi
        self.master.configure(bg='#ADD8E6')  # Açık mavi renk

        # Toplanti olusturma kismi
        self.label_toplanti_kodu = tk.Label(master, text="Toplanti Kodu:", bg='#ADD8E6')  # Açık mavi renk
        self.label_isim = tk.Label(master, text="Isim:", bg='#ADD8E6')  # Açık mavi renk
        self.label_tarih = tk.Label(master, text="Toplanti Tarihi:", bg='#ADD8E6')  # Açık mavi renk
        self.label_aciklama = tk.Label(master, text="Aciklama:", bg='#ADD8E6')  # Açık mavi renk

        self.entry_toplanti_kodu = tk.Entry(master)
        self.entry_isim = tk.Entry(master)
        self.entry_tarih = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_aciklama = tk.Entry(master)

        self.button_toplanti_olustur = tk.Button(master, text="Toplantiyi Olustur", command=self.toplantiyi_olustur, bg='green', fg='white')  # Yeşil renk

        # Toplantiya katilma kismi
        self.label_katilma_kodu = tk.Label(master, text="Toplanti Kodu:", bg='#ADD8E6')  # Açık mavi renk
        self.label_katilma_isim = tk.Label(master, text="Isim:", bg='#ADD8E6')  # Açık mavi renk
        self.label_katilma_tarih = tk.Label(master, text="Uygun Tarih:", bg='#ADD8E6')  # Açık mavi renk

        self.entry_katilma_kodu = tk.Entry(master)
        self.entry_katilma_isim = tk.Entry(master)
        self.entry_katilma_tarih = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)

        self.button_toplantiya_katil = tk.Button(master, text="Toplantiya Katil", command=self.toplantiya_katil, bg='green', fg='white')  # Yeşil renk

        # Grid kismi
        self.grid_label = tk.Label(master, text="Grid:", bg='#ADD8E6')  # Açık mavi renk
        self.grid_tree = ttk.Treeview(master, columns=("Toplanti Kodu", "Isim", "Tarih", "Aciklama"), show="headings")

        # Grid layout
        self.label_toplanti_kodu.grid(row=0, column=0, padx=10, pady=10)
        self.label_isim.grid(row=1, column=0, padx=10, pady=10)
        self.label_tarih.grid(row=2, column=0, padx=10, pady=10)
        self.label_aciklama.grid(row=3, column=0, padx=10, pady=10)

        self.entry_toplanti_kodu.grid(row=0, column=1, padx=10, pady=10)
        self.entry_isim.grid(row=1, column=1, padx=10, pady=10)
        self.entry_tarih.grid(row=2, column=1, padx=10, pady=10)
        self.entry_aciklama.grid(row=3, column=1, padx=10, pady=10)

        self.button_toplanti_olustur.grid(row=4, column=0, columnspan=2, pady=10)

        self.label_katilma_kodu.grid(row=0, column=2, padx=10, pady=10)
        self.label_katilma_isim.grid(row=1, column=2, padx=10, pady=10)
        self.label_katilma_tarih.grid(row=2, column=2, padx=10, pady=10)

        self.entry_katilma_kodu.grid(row=0, column=3, padx=10, pady=10)
        self.entry_katilma_isim.grid(row=1, column=3, padx=10, pady=10)
        self.entry_katilma_tarih.grid(row=2, column=3, padx=10, pady=10)

        self.button_toplantiya_katil.grid(row=4, column=2, columnspan=2, pady=10)

        self.grid_label.grid(row=5, column=0, padx=10, pady=10, columnspan=4)
        self.grid_tree.grid(row=6, column=0, columnspan=4)

        # Set column headings
        self.grid_tree.heading("Toplanti Kodu", text="Toplanti Kodu")
        self.grid_tree.heading("Isim", text="Isim")
        self.grid_tree.heading("Tarih", text="Tarih")
        self.grid_tree.heading("Aciklama", text="Aciklama")

        # Bind double-click event to show full details
        self.grid_tree.bind("<Double-1>", self.show_full_details)

        # JSON dosyası için dosya adı
        self.json_filename = "toplanti_verileri.json"

        # Başlangıçta varolan verileri yükle
        self.load_data()

        # Resimleri yükle
        self.toplanti1_image = ImageTk.PhotoImage(Image.open("toplanti1.jpg"))
        self.toplanti2_image = ImageTk.PhotoImage(Image.open("toplanti2.jpg"))

        # Resimleri göster
        self.toplanti1_label = tk.Label(master, image=self.toplanti1_image, bg='#ADD8E6')  # Açık mavi renk
        self.toplanti1_label.grid(row=0, column=4, rowspan=5, padx=10, pady=10)

        self.toplanti2_label = tk.Label(master, image=self.toplanti2_image, bg='#ADD8E6')  # Açık mavi renk
        self.toplanti2_label.grid(row=5, column=4, rowspan=5, padx=10, pady=10)

    def toplantiyi_olustur(self):
        toplanti_kodu = self.entry_toplanti_kodu.get()
        isim = self.entry_isim.get()
        tarih = self.entry_tarih.get_date()
        aciklama = self.entry_aciklama.get()

        if toplanti_kodu and isim and tarih and aciklama:
            messagebox.showinfo("Toplanti Oluşturuldu", f"Toplanti Kodu: {toplanti_kodu}\nIsim: {isim}\nTarih: {tarih}\nAciklama: {aciklama}")
            self.insert_grid_row((toplanti_kodu, 'Oluşturan: '+isim, tarih, aciklama))
            # Verileri JSON dosyasına kaydet
            self.save_data()
        else:
            messagebox.showerror("Hata", "Lütfen tüm bilgileri doldurun!")

    def toplantiya_katil(self):
        toplanti_kodu = self.entry_katilma_kodu.get()
        isim = self.entry_katilma_isim.get()
        uygun_tarih = self.entry_katilma_tarih.get_date()

        found = False
        for item in self.grid_tree.get_children():
            values = self.grid_tree.item(item, "values")
            if values[0] == toplanti_kodu:
                found = True
                break

        if found:
            messagebox.showinfo("Toplantiya Katilma", f"Toplanti Kodu: {toplanti_kodu}, Isim: {isim}, Uygun Tarih: {uygun_tarih}")
            self.insert_grid_row((toplanti_kodu, f"Katilan: {isim}", f"Uygun Tarih: {uygun_tarih}", ""))
            # Verileri JSON dosyasına kaydet
            self.save_data()
        else:
            messagebox.showerror("Hata", "Boyle bir toplanti bulunmamaktadir!")

    def show_full_details(self, event):
        selected_item = self.grid_tree.selection()
        values = self.grid_tree.item(selected_item, "values")
        if values:
            toplanti_kodu, isim, tarih, aciklama = values
            messagebox.showinfo("Toplanti Detaylari", f"Toplanti Kodu: {toplanti_kodu}\nIsim: {isim}\nTarih: {tarih}\nAciklama: {aciklama}")

    def insert_grid_row(self, values):
        # Uzun aciklama kontrolu
        aciklama = values[3]
        if len(aciklama) > 50:
            aciklama = aciklama[:50] + "..."
        values = (values[0], values[1], values[2], aciklama)
        self.grid_tree.insert("", "end", values=values)

    def load_data(self):
        try:
            with open(self.json_filename, "r") as file:
                data = json.load(file)
                for values in data:
                    self.insert_grid_row(values)
        except FileNotFoundError:
            pass  # İlk çalıştırma, dosya henüz oluşturulmamış olabilir

    def save_data(self):
        # Grid'deki tüm verileri al
        all_data = []
        for item in self.grid_tree.get_children():
            values = self.grid_tree.item(item, "values")
            all_data.append(values)

        # Verileri JSON dosyasına kaydet
        with open(self.json_filename, "w") as file:
            json.dump(all_data, file)

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = ToplantiUygulamasi(root)
    root.mainloop()
