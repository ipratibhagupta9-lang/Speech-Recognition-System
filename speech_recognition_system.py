import whisper
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import threading

# Load Whisper model
status_text = "Loading Whisper Model..."
model = whisper.load_model("base")


def upload_audio():
    file_path = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[
            ("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg *.aac"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        progress.start(10)
        status.config(text="Transcribing... Please wait")

        def run():
            try:
                result = model.transcribe(file_path)

                text_box.delete("1.0", tk.END)
                text_box.insert(tk.END, result["text"])

                progress.stop()
                status.config(text="Completed Successfully ✅")

            except Exception as e:
                progress.stop()
                status.config(text="Error ❌")
                messagebox.showerror("Error", str(e))

        threading.Thread(target=run).start()


def save_text():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "No transcription available.")
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")]
    )

    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

        messagebox.showinfo("Saved", "File saved successfully.")


def clear_text():
    text_box.delete("1.0", tk.END)
    status.config(text="Ready")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("AI Speech Recognition System")
root.geometry("900x650")
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="🎤 AI Speech Recognition System",
    font=("Segoe UI", 22, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Upload any audio file and convert Speech into Text",
    font=("Segoe UI", 11),
    fg="#d0d0d0",
    bg="#1e1e2f"
)
subtitle.pack()

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

upload_btn = tk.Button(
    frame,
    text="📂 Upload Audio",
    font=("Segoe UI", 12, "bold"),
    bg="#00b894",
    fg="white",
    width=18,
    command=upload_audio
)
upload_btn.grid(row=0, column=0, padx=10)

save_btn = tk.Button(
    frame,
    text="💾 Save Text",
    font=("Segoe UI", 12, "bold"),
    bg="#0984e3",
    fg="white",
    width=18,
    command=save_text
)
save_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(
    frame,
    text="🗑 Clear",
    font=("Segoe UI", 12, "bold"),
    bg="#d63031",
    fg="white",
    width=18,
    command=clear_text
)
clear_btn.grid(row=0, column=2, padx=10)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=750,
    mode="indeterminate"
)
progress.pack(pady=15)

text_box = scrolledtext.ScrolledText(
    root,
    font=("Consolas", 12),
    wrap=tk.WORD,
    width=95,
    height=22,
    bg="#2d3436",
    fg="white",
    insertbackground="white"
)
text_box.pack(padx=20)

status = tk.Label(
    root,
    text="Ready",
    bg="#1e1e2f",
    fg="#55efc4",
    font=("Segoe UI", 11)
)
status.pack(pady=10)

footer = tk.Label(
    root,
    text="Developed for CODTECH AI Internship",
    bg="#1e1e2f",
    fg="gray",
    font=("Segoe UI", 10)
)
footer.pack(side="bottom", pady=10)

root.mainloop()