import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np

#ładowanie modelu
model = tf.keras.models.load_model('fruit_recognition_model.h5')

#lista nazw klas owoców (zgodna z indeksami zwracanymi przez model)
class_names = ['Apple', 'Banana', 'Carambola', 'Guava', 'Kiwi', 'Mango', 'Muskmelon', 'Orange', 'Peach', 'Pear', 'Persimmon', 'Pitaya', 'Plum', 'Pomegranate', 'Tomatoes']

#tworzenie okna aplikacji
window = tk.Tk()
window.title("Rozpoznawanie owoców - Projekt Pogromców Danych")
window.geometry("500x500")

#obsługa zdarzenia
def classify_image():
    global image_display
    
    #wybieranie obrazu
    file_path = filedialog.askopenfilename()
    
    #przetwarzanie obrazu
    image = Image.open(file_path)
    image = image.resize((258, 320))
    image = np.array(image) / 255.0 
    image = np.expand_dims(image, axis=0)
    
    #klasyfikacja obrazu przy użyciu modelu
    predictions = model.predict(image)
    label_index = np.argmax(predictions)
    label = class_names[label_index]
    confidence = predictions[0][label_index] * 100
    
    #wyświetlanie wynikówa
    result_label.config(text=f"Owoc: {label}\n\nPewność: {confidence:.2f}%")
    
    #wyświetlanie obrazu
    image_display = ImageTk.PhotoImage(file=file_path) 
    image_label.config(image=image_display)
    image_label.image = image_display

#interfejs użytkownika
upload_button = tk.Button(window, text="Wybierz obraz", command=classify_image)
upload_button.pack(pady=10)

image_label = tk.Label(window)
image_label.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

#uruchomienie aplikacji
window.mainloop()