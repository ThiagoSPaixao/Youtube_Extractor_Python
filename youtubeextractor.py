from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def download_video(video_url, selected_quality):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(res=selected_quality, file_extension='mp4', progressive=True).first()

        # Modificando o nome do arquivo para incluir a resolução
        video_filename = f"{yt.title}_{selected_quality}.mp4"

        print(f"Baixando vídeo ({selected_quality})...")
        video_stream.download(filename=video_filename)
        print("Download de vídeo concluído!")

        messagebox.showinfo("Download Concluído", f"Download de vídeo concluído!\nTítulo do vídeo: {yt.title}")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar vídeo: {e}")

def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Modificando o nome do arquivo para incluir a resolução
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

def baixar_video():
    video_url = entry.get()
    if video_url:
        # Criar uma nova janela para a seleção de qualidade
        quality_window = tk.Toplevel(root)
        quality_window.title("Selecione a Qualidade")

        label_quality = tk.Label(quality_window, text="Selecione a Qualidade:")
        label_quality.pack(pady=10)

        # Função para iniciar o download com a qualidade selecionada
        def iniciar_download():
            selected_quality = quality_var.get()
            if selected_quality:
                quality_window.destroy()  # Fechar a janela de seleção de qualidade
                download_video(video_url, selected_quality)
            else:
                messagebox.showwarning("Aviso", "Selecione a qualidade antes de iniciar o download.")

        # Adicionar menu de opções para seleção de qualidade
        quality_var = tk.StringVar()
        quality_options = [f"{stream.resolution}p" for stream in YouTube(video_url).streams.filter(file_extension='mp4', progressive=True)]
        quality_menu = ttk.Combobox
        quality_menu = ttk.Combobox(quality_window, textvariable=quality_var, values=quality_options)
        quality_menu.pack(pady=10)

        # Botão para iniciar o download com a qualidade selecionada
        download_button = tk.Button(quality_window, text="Iniciar Download", command=iniciar_download)
        download_button.pack(pady=10)

    else:
        messagebox.showwarning("Aviso", "Insira o link do vídeo do YouTube.")

def baixar_audio():
    video_url = entry.get()
    if video_url:
        download_audio(video_url)
    else:
        messagebox.showwarning("Aviso", "Insira o link do vídeo do YouTube.")

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

    button_video = tk.Button(root, text="Baixar Vídeo", command=baixar_video)
    button_video.pack(pady=10)

    button_audio = tk.Button(root, text="Baixar Áudio", command=baixar_audio)
    button_audio.pack(pady=10)

    root.mainloop()
