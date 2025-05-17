import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import customtkinter as ctk
import os
import time
import json
import sys
import webbrowser
from tkinter import PhotoImage
from datetime import datetime

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

veriler = []

try:
    os.makedirs("MYLAUNCHER/data", exist_ok=True)
    open("MYLAUNCHER/data/application.json", "x", encoding="utf-8")
except:
    pass
        
def add_application_command(event=None):
    def select_app_path():
        path = filedialog.askopenfilename(title="Uygulama Seç")

        if path:
            applications.insert(tk.END, f"{app_name.get().strip().upper()} | {path}")

            veriler.append({
                "name":f"{app_name.get().strip().upper()}",
                "path":f"{path.strip()}"
            })

            with open("MYLAUNCHER/data/application.json","w", encoding="utf-8") as f:
                json.dump(veriler, f, ensure_ascii=False, indent=4)

            settings_app.destroy()
        
    settings_app = ctk.CTkToplevel()
    settings_app.title("MY LAUNCHER | EKLE")
    settings_app.geometry("350x200")
    settings_app.resizable(False,False)
    settings_app.focus()

    window_width = 350
    window_height = 200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    settings_app.geometry(f"{window_width}x{window_height}+{x}+{y}")

    settings_app.attributes("-topmost", True)

    title_selection = ctk.CTkLabel(settings_app, text="UYGULAMA EKLE", font=("century gothic",22,"bold"))
    title_selection.pack()

    app_name = ctk.CTkEntry(settings_app, placeholder_text="Uygulama adı...")
    app_name.pack(pady=25)

    app_path = ctk.CTkButton(settings_app, text="Uygulama Seç",font=("century gothic",18,"bold") ,command=select_app_path)
    app_path.pack(pady=10)

    settings_app.mainloop()

def run(event=None):
    selection = applications.curselection()

    if selection:        
        progress = ctk.CTkProgressBar(root, width=670)
        progress.set(0)
        progress.pack()
        progress.place(x=231, y=690)

        for i in range(101):
            progress.set(i / 100)
            root.update()
            time.sleep(0.002)

        progress.destroy()

        time.sleep(0.1)

        app = applications.get(selection)
        parca_sys = str(app).split("|")
        system_path = str(parca_sys[1]).strip()

        os.startfile(system_path)
    
    else:
        messagebox.showerror("MY LAUNCHER","Uygulama başlatmak için önce liste menüsünden eklediğiniz bir uygulama seçiniz.")

def delete_app_command(event=None):
    selected_app = applications.curselection()

    if selected_app:
        ask = messagebox.askyesno("MY LAUNCHER",f"Uygulamayı başlatıcıdan silmek istediğinizden emin misiniz?")
        if ask == True:
            selected_del = str(applications.get(selected_app)).strip().split("|")

            select = selected_del[0].strip()

            with open("MYLAUNCHER/data/application.json", "r", encoding="utf-8") as f:
                data = json.load(f) 

            data = [item for item in data if item["name"] != select]
            
            with open("MYLAUNCHER/data/application.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            applications.delete(selected_app)
            
            start_app.configure(state="disabled")
            delte_app.configure(state="disabled")
    else:
        messagebox.showerror("MY LAUNCHER","Silmek istediğiniz uygulamayı seçiniz.")

def settings_function():

    def go_github():
        settings_win.attributes("-topmost", False)
        ask_leave_launcher = messagebox.askyesno("MY LAUNCHER","Başlatıcıdan ayrılıyorsunuz, gitmek istediğinizden emin misiniz?")

        if ask_leave_launcher == True:
            webbrowser.open("https://github.com/TheKeops/My-Launcher")
    
    def about_function():
        settings_win.attributes("-topmost", False)
        ask_leave_launcher = messagebox.askyesno("MY LAUNCHER","Başlatıcıdan ayrılıyorsunuz, gitmek istediğinizden emin misiniz?")

        if ask_leave_launcher == True:
            webbrowser.open("https://github.com/TheKeops/My-Launcher/blob/main/README.md")

    def sifirla_function():
        settings_win.attributes("-topmost", False)
        ask_sifirla = messagebox.askyesno("MY LAUNCHER", "Uygulamayı sıfırlamak istiyor musunuz? Eğer sıfırlarsanız tüm veriler silinir.")

        if ask_sifirla == True:
            with open("MYLAUNCHER/data/application.json","w",encoding="utf-8") as f:
                f.write("")

            root.destroy()

    def reset_function():
        os.execv(sys.executable, ['python'] + sys.argv)

    settings_win = ctk.CTkToplevel()
    settings_win.title("MY LAUNCHER | AYARLAR")
    settings_win.resizable(False,False)
    settings_win.attributes("-topmost", True)
    settings_win.iconbitmap("MYLAUNCHER/image/my-launcher-logo.ico")

    window_width = 550
    window_height = 450

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    settings_win.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    title_st = ctk.CTkLabel(settings_win, text="AYARLAR", font=("century gothic",27,"bold"))
    title_st.pack()

    reset = ctk.CTkButton(settings_win, text="RESET", corner_radius=35,font=("century gothic",22,"bold"), command=reset_function)
    reset.pack()
    reset.place(x=30, y=60)

    reset_context = ctk.CTkLabel(settings_win, text="Uygulamayı yeniden başlatır.", font=("century gothic",15,"bold"))
    reset_context.pack()
    reset_context.place(x=200, y=60)

    sifirla = ctk.CTkButton(settings_win,text="SIFIRLA", corner_radius=35,font=("century gothic",22,"bold"), command=sifirla_function)
    sifirla.pack()
    sifirla.place(x=30, y=120)

    sifirla_context = ctk.CTkLabel(settings_win, text="Uygulamayı sıfırlar. (Verileri silinir)", font=("century gothic",15,"bold"))
    sifirla_context.pack()
    sifirla_context.place(x=200, y=120)

    github = ctk.CTkButton(settings_win, text="Github",corner_radius=35,hover_color="#707070",fg_color="gray", font=("century gothic",23,"bold"), command=go_github)
    github.pack()
    github.place(x=100,y=290)

    about = ctk.CTkButton(settings_win, text="Hakkımda",corner_radius=35,hover_color="#e62e00",fg_color="red", font=("century gothic",23,"bold"), command=about_function)
    about.pack()
    about.place(x=300,y=290)

    settings_win.iconbitmap("MYLAUNCHER/image/my-launcher-logo.ico")
    settings_win.mainloop()

def select_control(event):
    select_control = applications.curselection()
    
    if select_control:
        start_app.configure(state="normal")
        delte_app.configure(state="normal")
    else:
        start_app.configure(state="disabled")
        delte_app.configure(state="disabled")

root = ctk.CTk()
root.title("MY LAUNCHER")
root.resizable(False,False)
try:
    icon = PhotoImage(file="MYLAUNCHER/image/my-launcher-logo.png")
    root.iconphoto(False, icon)
except:
    pass

window_width = 900
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

pencere_menu_sol = ctk.CTkFrame(root, width=230, height=700, fg_color="#333333")
pencere_menu_sol.pack(side="left")

title = ctk.CTkLabel(root, text="MY LAUNCHER",bg_color="#333333" ,font=("century gothic",27,"bold"))
title.pack()
title.place(x=15, y=30)

version = ctk.CTkLabel(root, text="v1.1-alpha",bg_color="#333333" ,font=("century gothic",17,"bold"))
version.pack()
version.place(x=13, y=60)

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
         "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

tarih = datetime.now()
gun = tarih.day
ay = aylar[tarih.month - 1]

date = ctk.CTkLabel(root, text=f"{gun} {ay}",bg_color="#333333" ,font=("century gothic",19,"bold"))
date.pack()
date.place(x=13,y=100)

applications = tk.Listbox(root, width=50, height=30, font=("century gothic",18,"bold"), bg="#333333", fg="white")
applications.pack(pady=50)
applications.bind("<<ListboxSelect>>", select_control)

try:
    with open("MYLAUNCHER/data/application.json","r",encoding="utf-8") as f:
        data = json.load(f)
except:
    with open("MYLAUNCHER/data/application.json","w", encoding="utf-8") as f:
        f.write("[]")

with open("MYLAUNCHER/data/application.json","r",encoding="utf-8") as f:
    data = json.load(f)

add_application = ctk.CTkButton(root, text="➕ Ekle", corner_radius=35,hover_color="#f0c000",bg_color="#333333" ,fg_color="orange", font=("century gothic",23,"bold"), command=add_application_command)
add_application.pack()
add_application.place(x=10, y=300)

delte_app = ctk.CTkButton(root, text="🗑  Sil", corner_radius=35,hover_color="#e62e00",bg_color="#333333" ,fg_color="red", font=("century gothic",23,"bold"), command=delete_app_command)
delte_app.pack()
delte_app.place(x=10, y=250)
delte_app.configure(state="disabled")

start_app = ctk.CTkButton(root, text="🚀 Başlat",bg_color="#333333", corner_radius=35,font=("century gothic",25,"bold"), command=run)
start_app.pack()
start_app.configure(state="normal")
start_app.place(x=10, y=200)
start_app.configure(state="disabled")

settings = ctk.CTkButton(root, text="⚙ Ayarlar",corner_radius=35,hover_color="#707070",bg_color="#333333" ,fg_color="gray", font=("century gothic",23,"bold"), command=settings_function)
settings.pack()
settings.place(x=20, y=650)

if ctk.get_appearance_mode() == "Light":
    date.configure(text_color="white")
    title.configure(text_color="white")
    version.configure(text_color="white")
    applications.configure(bg="white", fg="black")

for i in data:
    applications.insert(tk.END, f'{i["name"]} | {i["path"]}')
    root.update()
    time.sleep(0.06)

root.bind("<Return>", run)
root.bind("<e>", add_application_command)
root.bind("<space>", add_application_command)
root.bind("<Delete>", delete_app_command)

root.mainloop()
