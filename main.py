import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.layout = QVBoxLayout()
        
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Masukkan nama kota")
        self.layout.addWidget(self.city_input)
        
        # Label untuk menampilkan hasil
        self.city_label = QLabel("Kota: ")
        self.layout.addWidget(self.city_label)
        
        self.temperature_label = QLabel("Suhu: ")
        self.layout.addWidget(self.temperature_label)
        
        self.weather_description_label = QLabel("Cuaca: ")
        self.layout.addWidget(self.weather_description_label)
        
        self.setLayout(self.layout)

        # Connect the textChanged signal to the update_weather function
        self.city_input.textChanged.connect(self.update_weather)

    def update_weather(self):
        city = self.city_input.text()
        if city:  # Only fetch weather if the input is not empty
            self.get_weather(city)

    def get_weather(self, city):
        api_key = "b55cbdd314ab8df3e05055270c1ccaf0"  # Ganti dengan API key Anda
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},ID&appid={api_key}&units=metric&lang=id"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            self.city_label.setText(f"Kota: {city}")
            self.temperature_label.setText(f"Suhu: {temperature}°C")
            self.weather_description_label.setText(f"Cuaca: {weather_description.capitalize()}")
        else:
            self.city_label.setText("Kota: Kota tidak ditemukan. Silakan coba lagi.")
            self.temperature_label.setText("Suhu: ")
            self.weather_description_label.setText("Cuaca: ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())