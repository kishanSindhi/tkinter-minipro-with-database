import tkinter as tk
from tkinter import font
from tkinter.constants import FALSE, LEFT, NW, W
import requests as re
from PIL import Image, ImageTk

# 0a8f79d0b1ef3fb5b8c94833d0067ca1
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        city = weather["name"]
        condition = weather["weather"][0]["description"]
        temperature = float(weather["main"]["temp"]) - 214
        temp = format(temperature, ".2f")
        final_str = f"City {city}\nCondition {condition}\nTemperature{temp}"
    
    except:
        final_str = f"There was a problem in fetching the data.."
    
    return final_str

def search(city):
    weather_key = "0a8f79d0b1ef3fb5b8c94833d0067ca1"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID":weather_key, "q":city, "unit":"imperial"}
    response = re.get(url, params)
    weather = response.json()

    result["text"]=format_response(weather)

root = tk.Tk()
root.title("Weather App")
root.geometry("600x500")
root.resizable(False, FALSE)
img = Image.open("gui\\1.jpg")
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)
bg_lable = tk.Label(root, image=img_photo).place(x=0, y=0, width=600, height=500)

heading_title = tk.Label(bg_lable, text="Search Your city...", fg="red", bg="#b0e0e6", font="timesnewroman 18 bold")
heading_title.place(x=75, y=20)

frame_1 = tk.Frame(bg_lable, bg="#42c2f4", bd=5)
frame_1.place(x=75, y=60, width=450, height=50)

txt_box = tk.Entry(frame_1, font="timesnewroman 25 bold", width=17)
txt_box.grid(row=0, column=0, sticky=W)

btn = tk.Button(frame_1, text="Search", fg="#42c2f4", font="timesnewroman 16", command=lambda: search(txt_box.get()))
btn.grid(row=0, column=1, padx=25)
btn.bind("<Return>",lambda: search(txt_box.get()))

frame_2 = tk.Frame(bg_lable, bg="#42c2f4")
frame_2.place(x=75, y=130, width=450, height=300)

result = tk.Label(frame_2, font=40, bg="white", justify=LEFT, anchor=NW)
result.place(relheight=1, relwidth=1)
root.mainloop()