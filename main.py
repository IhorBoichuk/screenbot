import glob
import os
import shutil
import pytesseract
import tkinter as tk
from PIL import Image
from langchain.llms import OpenAI



def find_screenshot():
    pattern = r"/home/taras/Pictures/*.png"
    matching_files = glob.glob(pattern)
    for file_path in matching_files:
        src = file_path
    return src

def move_screenshot():
    src = find_screenshot()
    # Генеруємо новий шлях з новим ім'ям файлу
    dst = "./screenshot.png"
    # Переносимо та перейменовуємо файл
    shutil.move(src, dst)
    

def parse_img():
    # Встановіть шлях до файлика з українською мовою
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    # Встановіть мову на українську
    custom_config = r'--oem 3 --psm 6 -l ukr'

    # Відкрийте зображення
    image = Image.open('screenshot.png')

    # Виконайте OCR з використанням української мови
    extracted_text = pytesseract.image_to_string(image, config=custom_config)
    return extracted_text.lower()


def gener_answer(text, text_widget):
    llm = OpenAI(temperature=0.0)
    create_text_field(llm(text), text_widget)


    
# Створюємо поле для введення тексту
def create_text_field(text, text_widget):

    text_widget.insert(tk.END, text)
    text_widget.pack()


def del_screenshot():
    img_file_path = "/home/taras/screenbot/screenshot.png"
    os.remove(img_file_path)   



def main():

    move_screenshot()
    text = parse_img()

    window = tk.Tk()
    text_widget = tk.Text(window)
    def select_text():
        selected_text = text_widget.selection_get()
        gener_answer(str(selected_text), text_widget)
    text_widget.insert(tk.END, text)
    text_widget.pack() 
    # Кнопка для виділення тексту
    button = tk.Button(window, text="Виділити текст", command=select_text)
    button.pack()  
    # Відображаємо вікно
    window.mainloop() 
    
    del_screenshot()
        
import time        
import os
if __name__=="__main__":
    


    # directory = "/home/taras/Pictures"
    # filename = "Screenshot from 2023-06-19 10-40-06*.png"

    while True:

        pattern = "/home/taras/Pictures/Screenshot from *.png"

        matching_files = glob.glob(pattern)

        if matching_files:
            file_path = matching_files[0]  # Перший знайдений файл
            print("Файл знайдено:", file_path)
            main()
        else:
            print("Файл не знайдено")
            time.sleep(5)  # Затримка у секундах між перевірками

        # file_path = os.path.join(directory, filename)
        
        # if os.path.exists(file_path):
        #     print("Файл знайдено:", file_path)
        #     # Виконайте додаткові дії зі знайденим файлом, якщо потрібно
        #     main()
        
        # print("Файл не знайдено. Зачекайте...")
        # 
