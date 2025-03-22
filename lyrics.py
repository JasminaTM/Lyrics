import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

BASE_URL = "https://api.lyrics.ovh/v1/"

def get_lyrics():
    artist = artist_entry.get().strip()
    song = song_entry.get().strip()
    
    if not artist or not song:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")
        return

    url = f"{BASE_URL}{artist}/{song}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lyrics_text.config(state=tk.NORMAL)
        lyrics_text.delete(1.0, tk.END) 
        lyrics_text.insert(tk.END, data["lyrics"])
        lyrics_text.config(state=tk.DISABLED)
    else:
        messagebox.showerror("Not Found", "Lyrics not found. Check the artist and song name.")

root = tk.Tk()
root.title("Lyrics Finder 🎶")
root.geometry("500x500")
root.config(bg="#f0f0f0")

tk.Label(root, text="Artist Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
artist_entry = tk.Entry(root, font=("Arial", 12))
artist_entry.pack(pady=5, padx=10, fill=tk.X)

tk.Label(root, text="Song Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
song_entry = tk.Entry(root, font=("Arial", 12))
song_entry.pack(pady=5, padx=10, fill=tk.X)

fetch_button = tk.Button(root, text="Get Lyrics 🎵", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=get_lyrics)
fetch_button.pack(pady=10)

lyrics_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), height=15)
lyrics_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
lyrics_text.config(state=tk.DISABLED)

root.mainloop()
