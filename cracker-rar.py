import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import threading
import time

class CrackerRAR:
    def __init__(self, root):
        self.root = root
        self.root.title("RAR- CRACKER - PRO")
        self.root.geometry("500x600")
        self.root.configure(bg="#000000") 

        self.header = tk.Label(root, text="CRACKER-RAR PRO", font=("Courier", 25, "bold"), 
                              fg="#ff0000", bg="#000000", pady=20)
        self.header.pack()

        self.btn_rar = tk.Button(root, text="1. PILIH FILE RAR TARGET", command=self.select_rar, 
                                 bg="#330000", fg="#ffffff", font=("Courier", 12), width=30)
        self.btn_rar.pack(pady=10)
        self.lbl_rar = tk.Label(root, text="No File Selected", fg="#aaaaaa", bg="#000000", font=("Courier", 8))
        self.lbl_rar.pack()

        # --- OPSI 1: ROCKYOU ---
        self.btn_rock = tk.Button(root, text="2. PAKAI ROCKYOU (BAWAAN)", command=self.use_rockyou, 
                                  bg="#660000", fg="#ffffff", font=("Courier", 12), width=30)
        self.btn_rock.pack(pady=10)

        # --- OPSI 2: CUSTOM WORDLIST ---
        self.btn_custom = tk.Button(root, text="3. PAKAI WORDLIST CUSTOM", command=self.select_wordlist, 
                                    bg="#990000", fg="#ffffff", font=("Courier", 12), width=30)
        self.btn_custom.pack(pady=10)
        self.lbl_wl = tk.Label(root, text="Using: None", fg="#aaaaaa", bg="#000000", font=("Courier", 8))
        self.lbl_wl.pack()

        # --- PROGRESS BAR (REAL) ---
        self.lbl_status = tk.Label(root, text="SYSTEM READY", fg="#ff0000", bg="#000000", font=("Courier", 10))
        self.lbl_status.pack(pady=20)
        
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Red.Horizontal.TProgressbar", background='#ff0000', troughcolor='#000000')
        self.progress = ttk.Progressbar(root, length=400, mode='determinate', style="Red.Horizontal.TProgressbar")
        self.progress.pack(pady=5)

        # --- TOMBOL HAJAR ---
        self.btn_start = tk.Button(root, text="[ EXECUTE PENETRATION ]", command=self.start_cracking, 
                                   bg="#ff0000", fg="#000000", font=("Courier", 14, "bold"), width=25)
        self.btn_start.pack(pady=30)

        self.target_rar = ""
        self.wordlist = ""

    def select_rar(self):
        self.target_rar = filedialog.askopenfilename(filetypes=[("RAR Files", "*.rar")])
        self.lbl_rar.config(text=os.path.basename(self.target_rar))

    def use_rockyou(self):
        self.wordlist = "/usr/share/wordlists/rockyou.txt"
        if not os.path.exists(self.wordlist):
             # Ekstrak otomatis jika masih .gz
             subprocess.run(["sudo", "gunzip", "/usr/share/wordlists/rockyou.txt.gz"])
        self.lbl_wl.config(text="Mode: Rockyou.txt")

    def select_wordlist(self):
        self.wordlist = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.lbl_wl.config(text=f"Mode: {os.path.basename(self.wordlist)}")

    def start_cracking(self):
        if not self.target_rar or not self.wordlist:
            messagebox.showerror("Error", "Pilih File RAR dan Wordlist dulu!")
            return
        
        # Jalankan di Thread agar GUI tidak freeze
        threading.Thread(target=self.crack_engine, daemon=True).start()

    def crack_engine(self):
        self.lbl_status.config(text="EXTRACTING HASH...")
        subprocess.run(f"rar2john {self.target_rar} > crack.hash", shell=True)
        
        self.lbl_status.config(text="CRACKING IN PROGRESS...")
        # Jalankan John
        process = subprocess.Popen(["john", "--format=rar5", f"--wordlist={self.wordlist}", "crack.hash"], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Simulasi Progress Bar
        for i in range(1, 101):
            time.sleep(0.05) 
            self.progress['value'] = i
            self.root.update_idletasks()

        process.wait()
        
        # Ambil Hasil
        result = subprocess.check_output(["john", "--show", "crack.hash"]).decode()
        if ":" in result:
            password = result.split(":")[1].split("\n")[0]
            self.lbl_status.config(text="SUCCESS!")
            messagebox.showinfo("PHANTOM FOUND", f"PASSWORD: {password}")
        else:
            self.lbl_status.config(text="FAILED!")
            messagebox.showerror("Failed", "Sandi tidak ada di wordlist!")
        
        os.remove("crack.hash")

if __name__ == "__main__":
    root = tk.Tk()
    app = CrackerRAR(root)
    root.mainloop()