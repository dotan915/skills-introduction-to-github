import tkinter as tk
from tkinter import ttk
import requests

class TextTranslatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Text Translator (MyMemory)")
        self.create_widgets()

    def create_widgets(self):
        # Nhãn + ô nhập văn bản
        label1 = tk.Label(self.root, text="Enter text to translate:")
        label1.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Chọn ngôn ngữ nguồn
        label2 = tk.Label(self.root, text="Choose source language:")
        label2.grid(row=1, column=0, padx=10, pady=10)

        self.source_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.source_lang.set("en")
        self.source_lang.grid(row=1, column=1, padx=10, pady=10)

        # Chọn ngôn ngữ đích
        label3 = tk.Label(self.root, text="Choose target language:")
        label3.grid(row=2, column=0, padx=10, pady=10)

        self.target_lang = ttk.Combobox(self.root, values=["en", "es", "fr", "vi", "ja", "zh"])
        self.target_lang.set("vi")
        self.target_lang.grid(row=2, column=1, padx=10, pady=10)

        # Nút dịch
        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Nhãn kết quả
        self.result_label = tk.Label(self.root, text="Translated text will appear here.", wraplength=400, justify="left")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        text_to_translate = self.entry.get()
        src = self.source_lang.get()
        tgt = self.target_lang.get()

        if not text_to_translate.strip():
            self.result_label.config(text="Please enter some text.")
            return

        url = "https://api.mymemory.translated.net/get"
        params = {"q": text_to_translate, "langpair": f"{src}|{tgt}"}

        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            translated_text = data["responseData"]["translatedText"]
            self.result_label.config(text=translated_text)
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextTranslatorApp(root)
    root.mainloop()
