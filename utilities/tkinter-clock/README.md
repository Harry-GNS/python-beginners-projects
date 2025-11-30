# 🕒 Simple Digital Clock GUI with Tkinter

This is a basic Python application that displays a real-time digital clock using the `tkinter` GUI library. The clock updates every second and features a clean, bold design.

## 💡 Features

- Real-time clock (updates every second)
- Minimal GUI using `tkinter`
- Custom window size and position
- Dark blue background with bold white font

## 🛠️ Requirements

No external libraries are required beyond the Python Standard Library.

## 🚀 How to Run

1. Clone or download this repository.
2. Run the script with Python:

```bash
python tkinterClock.py
```

## 🧠 How It Works

- The `tkinter` module is used to create the GUI window and label.
- The `time.strftime()` function formats the current time as `HH:MM:SS`.
- The `after()` method schedules the `clock()` function to run every 1000 ms (1 second), updating the label.

## 🧑‍💻 Author

Created by AAlexEsc302 
Feel free to contribute or modify this project!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
