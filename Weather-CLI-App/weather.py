import tkinter as tk
import requests

# Create the main window
root = tk.Tk()

# Create Entry for city name
city_entry = tk.Entry(root)
city_entry.pack()

# Create a Label for output
result_label = tk.Label(root, text="")
result_label.pack()

# Function to fetch weather
def get_weather():
    city = city_entry.get()   # Get city from Entry widget
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=af2987041d0d0c1094dd035eea4e69c0&units=metric")
    if response.status_code == 200:
        # Parse JSON and update result_label
        result_label.config(text="Weather info here")
        data = response.json() 
        temperature = data['main']['temp'] 
        weather_description = data['weather'][0]['description'] 
        Humidity= data['main']['humidity'] 
        Wind_Speed = data['wind']['speed'] 
        result_label.config(f"The current temperature in {city} :\nTempertaure: {temperature}°C \n Condition: {weather_description}\n Humidity: {Humidity}% \n Wind Speed: {Wind_Speed} m/s")
    else:
        result_label.config(text="City not found.")

# Create a Button to trigger the function
btn = tk.Button(root, text="Get Weather", command=get_weather)
btn.pack()

root.mainloop()
