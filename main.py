# import pytesseract
# from PIL import Image

# # Відкриття зображення
# image = Image.open('screenshot.png')

# # Застосування OCR за допомогою pytesseract
# extracted_text = pytesseract.image_to_string(image)

# print(extracted_text.lower())

# from tkinter import Tk, messagebox
# from tkinter import ttk

# # Створюємо вікно
# window = Tk()
# # frm = ttk.Frame(window, padding=10)
# window.geometry("800x800")

# # Приховуємо вікно
# window.withdraw()




import pytesseract
from PIL import Image

# Встановіть шлях до файлика з українською мовою
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Встановіть мову на українську
custom_config = r'--oem 3 --psm 6 -l ukr'

# Відкрийте зображення
image = Image.open('screenshot.png')

# Виконайте OCR з використанням української мови
extracted_text = pytesseract.image_to_string(image, config=custom_config)
print(extracted_text.lower())

# # Виводимо діалогове вікно з повідомленням
# messagebox.showinfo('Повідомлення', extracted_text.lower())

# # Закриваємо вікно
# window.destroy()



# # Відображаємо вікно
# window.mainloop()

import tkinter as tk

def select_text():
    selected_text = text_widget.selection_get()
    print("Selected Text:", selected_text)

# Створюємо вікно
window = tk.Tk()

# Створюємо поле для введення тексту
text_widget = tk.Text(window)
text_widget.insert(tk.END, extracted_text.lower())

text_widget.pack()

# Кнопка для виділення тексту
button = tk.Button(window, text="Виділити текст", command=select_text)
button.pack()

# Відображаємо вікно
window.mainloop()
