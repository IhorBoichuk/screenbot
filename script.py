import os
import shutil

import pytesseract
from PIL import Image
import tkinter as tk
from langchain.llms import OpenAI
import glob


pattern = r"/home/taras/Pictures/*.png"

matching_files = glob.glob(pattern)

for file_path in matching_files:
    src = file_path
    

# Генеруємо новий шлях з новим ім'ям файлу
dst = "./screenshot.png"

# Переносимо та перейменовуємо файл
shutil.move(src, dst)

# Встановіть шлях до файлика з українською мовою
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Встановіть мову на українську
custom_config = r'--oem 3 --psm 6 -l ukr'

# Відкрийте зображення
image = Image.open('screenshot.png')

# Виконайте OCR з використанням української мови
extracted_text = pytesseract.image_to_string(image, config=custom_config)
text = extracted_text.lower()


# Створюємо поле для введення тексту
def create_text_field(text):
    text_widget.insert(tk.END, text)
    text_widget.pack()


llm = OpenAI(temperature=0.0)

def gener_answer(text):
    create_text_field(llm(text))



# Створюємо вікно
window = tk.Tk()
text_widget = tk.Text(window)



def select_text():
    selected_text = text_widget.selection_get()
    gener_answer(str(selected_text))
    
    
create_text_field(extracted_text.lower())

# Кнопка для виділення тексту
button = tk.Button(window, text="Виділити текст", command=select_text)
button.pack()

# Відображаємо вікно
window.mainloop()


img_file_path = "/home/taras/screenbot/screenshot.png"
os.remove(img_file_path)
