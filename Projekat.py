from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import date, datetime, timedelta
import os
import random

# Prozor

root=Tk()
root.title("Super liga")
root.geometry("1000x800")
root.resizable(width=False,height=False)

root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)


# Rezultati utakmica

match_details = {
    "28.01.2025_Arsenal_Bayern": {
        "score": "2-1",
        "goals": [("Gabriel Jesus", "45'"), ("Saka", "67'"), ("Kane", "78'")],
        "assists": [("Odegaard", "45'"), ("Martinelli", "67'"), ("Muller", "78'")]
    },
    "28.01.2025_Barcelona_Chelsea": {
        "score": "3-2",
        "goals": [("Lewandowski", "12'"), ("Ferran Torres", "38'"), ("Felix", "59'"), ("Sterling", "65'"), ("Nkunku", "82'")],
        "assists": [("Pedri", "12'"), ("Gavi", "38'"), ("Cancelo", "59'"), ("James", "65'"), ("Gallagher", "82'")]
    },
    "28.01.2025_Inter_Liverpool": {
        "score": "0-3",
        "goals": [("Salah", "32'"), ("Salah", "43'"), ("Nunez", "88'")],
        "assists": [("Mac allister", "32'"), ("Nunez", "43'"), ("Gakpo", "88'")]
    },
    "28.01.2025_Leverkusen_Real Madrid": {
        "score": "1-4",
        "goals": [("Bellingham", "2'"), ("Rodrygo", "27'"), ("Boniface", "46'"), ("Bellingham", "62'"), ("Mbappe", "88'")],
        "assists": [("Valverde", "2'"), ("Mbappe", "27'"), ("Xhaka", "46'"), ("Vini Jr", "62'"), ("Bellingham", "88'")]
    },
    "28.01.2025_Man City_Atletico Madrid": {
        "score": "2-0",
        "goals": [("Haaland", "32'"), ("Haaland", "67'")],
        "assists": [("Savinho", "32'"), ("De Bruyne", "67'")]
    },
    "29.01.2025_Arsenal_Chelsea": {
        "score": "2-2",
        "goals": [("Palmer", "14'"), ("Havertz", "35'"), ("Saka", "47'"), ("Palmer", "93'")],
        "assists": [("Jackson", "14'"), ("Odegaard", "35'"), ("Odgaard", "47'"), ("Fernandez", "93'")]
    },
    "29.01.2025_Bayern_Barcelona": {
        "score": "1-3",
        "goals": [("Kane", "27'"), ("Raphinha", "39'"), ("Raphinha", "49'"), ("Raphinha", "83'")],
        "assists": [("Musiala", "27'"), ("Pedri", "39'"), ("Gavi", "49'"), ("Lewandovski", "83'")]
    },
    "29.01.2025_Inter_Real Madrid": {
        "score": "2-4",
        "goals": [("Mbappe", "10'"), ("Bellingham", "24'"), ("Martinez", "31'"), ("Thuram", "48'"),("Vini Jr", "66'"), ("Mbappe", "89'"),],
        "assists": [("Bellingham", "10'"), ("Vini Jr", "24'"), ("Calhanoglu", "31'"), ("Martinez", "48'"),("Rodrygo", "66'"), ("Valverde", "89'"),]
    },
    "29.01.2025_Liverpool_Atletico Madrid": {
        "score": "3-1",
        "goals": [("Nunez", "34'"), ("Salah", "54'"), ("Alvarez", "61'"), ("Salah", "72'")],
        "assists": [("Salah", "34'"), ("Gakpo", "54'"), ("Griezmann", "61'"), ("Diaz", "72'")]
    },
    "29.01.2025_Man City_Leverkusen": {
        "score": "1-1",
        "goals": [("Boniface", "77'"), ("Haaland", "82'")],
        "assists": [("Frimpong", "77'"), ("Doku", "82'")]
    },
    "30.01.2025_Arsenal_Man City": {
        "score": "3-1",
        "goals": [("Odegaard", "2'"), ("Havertz", "15'"), ("Haaland", "39'"), ("Partey", "83'")],
        "assists": [("Martinelli", "2'"), ("Odegaard", "15'"), ("Savinho", "39'"), ("Saka", "83'")]
    },
    "30.01.2025_Barcelona_Atletico Madrid": {
        "score": "2-0",
        "goals": [("Lewandovski", "32'"), ("Raphinha", "67'")],
        "assists": [("Raphinha", "32'"), ("Dani Olmo", "67'")]
    },
    "30.01.2025_Inter_Bayern": {
        "score": "0-1",
        "goals": [("Kane", "57'")],
        "assists": [("Olise", "57'")]
    },
    "31.01.2025_Chelsea_Leverkusen": {
        "score": "2-2",
        "goals": [("Palmer", "23'"), ("Boniface", "34'"), ("Frimpong", "41'"), ("Sancho", "93'")],
        "assists": [("Jackson", "23'"), ("Xhaka", "34'"), ("Grimaldo", "41'"), ("Fernandez", "93'")]
    },
    "31.01.2025_Real Madrid_Liverpool": {
        "score": "2-1",
        "goals": [("Mbappe", "6'"), ("Rudiger", "32'"), ("Salah", "77'")],
        "assists": [("Bellingham", "6'"), ("Modric", "32'"), ("Gakpo", "77'")]
    },
    "08.02.2025_Arsenal_Leverkusen": {
        "score": "1-0",
        "goals": [("Saka", "67'")],
        "assists": [("Partey", "67'")]
    },
    "08.02.2025_Real Madrid_Man City": {
        "score": "3-2",
        "goals": [("Vini Jr", "21'"), ("Rodrygo", "34'"), ("Haaland", "41'"), ("Doku", "54'"), ("Vini Jr", "78'")],
        "assists": [("Mbappe", "21'"), ("Vini Jr", "34'"), ("De Bruyne", "41'"), ("Gvardiol", "54'"), ("Bellingham", "78'")]
    },
    "08.02.2025_Inter_Chelsea": {
        "score": "2-0",
        "goals": [("Martinez", "37'"), ("Thuram", "32'")],
        "assists": [("Dumfries", "37'"), ("Martinez", "32'")]
    },
    "08.02.2025_Atletico Madrid_Bayern": {
        "score": "1-3",
        "goals": [("Sorloth", "21'"), ("Kane", "34'"), ("Kane", "67'"), ("Olise", "84'")],
        "assists": [("Griezmann", "21'"), ("Musiala", "34'"), ("Davies", "67'"), ("Muller", "84'")]
    },
    
}


# Utakmice

matches = {
    "28.01.2025": [("Arsenal", "Bayern", "12:00"), ("Barcelona", "Chelsea", "15:00"), ("Inter", "Liverpool", "17:30"), ("Leverkusen", "Real Madrid", "19:15"),("Man City", "Atletico Madrid", "21:30")],
    "29.01.2025": [("Arsenal", "Chelsea", "11:30"), ("Bayern", "Barcelona", "14:00"), ("Inter", "Real Madrid", "17:00"), ("Liverpool", "Atletico Madrid", "19:30"),("Man City", "Leverkusen", "21:15")],
    "30.01.2025": [("Arsenal", "Man City", "15:00"), ("Barcelona", "Atletico Madrid", "18:00"), ("Inter", "Bayern", "20:30")],
    "31.01.2025": [("Chelsea", "Leverkusen", "16:30"), ("Real Madrid", "Liverpool", "19:00")],
    "08.02.2025": [("Arsenal", "Leverkusen", "12:00"), ("Real Madrid", "Man City", "15:00"), ("Inter", "Chelsea", "17:30"), ("Atletico Madrid", "Bayern", "19:15"),("Barcelona", "Liverpool", "21:30")], 
    }

current_date = datetime.now()


# Ažuriranje tabele

def update_date_label():
    date_label.config(text=current_date.strftime("%d.%m.%Y"))
    update_table()


def update_table():
    table.delete(*table.get_children())
    date_str = current_date.strftime("%d.%m.%Y")
    if date_str in matches:
        for match in matches[date_str]:
            table.insert("", "end", values=match)
    else:
        table.insert("", "end", values=("Nema utakmica", "", ""))


# Prikaz detalja

def open_match_details(event):
    selected_item = table.selection()
    if not selected_item:
        return

    values = table.item(selected_item, "values")
    if len(values) < 3:
        return

    team1, team2, time = values

    date_str = current_date.strftime("%d.%m.%Y")
    match_key = f"{date_str}_{team1}_{team2}"

# Dohvati podatke o utakmici
    details = match_details.get(match_key, {"score": "N/A", "goals": [], "assists": []})

# Novi tab za prikaz detalja
    detail_tab = Toplevel(root)
    detail_tab.title(f"{team1} vs {team2} - Detalji")
    detail_tab.geometry("400x400")

# Prikaz rezultata

    Label(detail_tab, text=f"Rezultat: {details['score']}", font=("Arial", 14, "bold")).pack(pady=10)

# Prikaz golova

    Label(detail_tab, text="Golovi:", font=("Arial", 12, "bold")).pack()
    if details["goals"]:
        for goal, minute in details["goals"]:
            Label(detail_tab, text=f"{goal} - {minute}").pack()
    else:
        Label(detail_tab, text="Nema podataka o golovima").pack()

# Prikaz asistencija

    Label(detail_tab, text="Asistencije:", font=("Arial", 12, "bold")).pack()
    if details["assists"]:
        for assist, minute in details["assists"]:
            Label(detail_tab, text=f"{assist} - {minute}").pack()
    else:
        Label(detail_tab, text="Nema podataka o asistencijama").pack()


# Promjena datuma

def next_day():
    """unaprijed za jedan dan"""
    global current_date
    current_date += timedelta(days=1)
    update_date_label()

def previous_day():
    """unazad za jedan dan"""
    global current_date
    current_date -= timedelta(days=1)
    update_date_label()


# Strelice

arrowright_button = tk.Button(root, text="→", font=("Arial", 14), bg="#223441", fg="#ffffff",command=next_day)
arrowright_button.grid(column=3,row=0,sticky=tk.W)

arrowleft_button = tk.Button(root, text="←", font=("Arial", 14), bg="#223441", fg="#ffffff",command=previous_day)
arrowleft_button.grid(column=1,row=0,sticky=tk.E)


# Datum

date_frame=Frame(root,bg="#223441",width=300,height=50)
date_frame.grid(row=0,column=2,sticky=tk.N,padx=10)

date_label=tk.Label(root,bg="#223441",fg="#ffffff",font=("Times",18))
date_label.grid(column=2,row=0)

today_date = datetime.now().strftime("%d.%m.%Y")
date_label.config(text=today_date)


# Tabela

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12), rowheight=30, background="#f0f0f0", fieldbackground="#ffffff")
style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#223441", foreground="black")
style.map("Treeview", background=[("selected", "#1f77b4")], foreground=[("selected", "white")])

table_frame = LabelFrame(root, text="Utakmice", font=("Arial", 16, "bold"), padx=10, pady=10)
table_frame.grid(row=1, column=1, columnspan=3, pady=20)

table = ttk.Treeview(table_frame, columns=("Team1", "Team2", "Time"), show="headings", height=8)
table.heading("Team1", text="Tim 1")
table.heading("Team2", text="Tim 2")
table.heading("Time", text="Vrijeme")
table.column("Team1", anchor=CENTER, width=300)
table.column("Team2", anchor=CENTER, width=300)
table.column("Time", anchor=CENTER, width=200)

table.pack()

#Otvaranje novog taba
table.bind("<Double-1>", open_match_details)

# Prvo ažuriranje tabele
update_table()

# Pokretanje petlje
root.mainloop()
