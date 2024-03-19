from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        audio_filename = f"{yt.title}_audio.mp3"

        print("Baixando áudio...")
        audio_stream.download(filename=audio_filename)
        print("Download de áudio concluído!")

        messagebox.showinfo("Download Concluído", f"Download de áudio concluído!\nTítulo do vídeo: {yt.title}")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar áudio: {e}")

def exibir_assinatura():
    print("\n" + "="*40)
    print("Desenvolvido por ThiagoSPaixao")
    print("GitHub: https://github.com/ThiagoSPaixao")
    print("="*40 + "\n")

if __name__ == "__main__":
    exibir_assinatura()

    root = tk.Tk()
    root.title("YouTube Downloader")

    label_assinatura = tk.Label(root, text="Desenvolvido por ThiagoSPaixao\nGitHub: https://github.com/ThiagoSPaixao", font=('Helvetica', 10, 'bold'))
    label_assinatura.pack(pady=10)

    label = tk.Label(root, text="Insira o link do YouTube:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    button_audio = tk.Button(root, text="Baixar Áudio", command=lambda: download_audio(entry.get()))
    button_audio.pack(pady=10)

    root.mainloop()
