class City:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def __str__(self):
        return f"{self.name}: {self.temperature}°C"


class WeatherManager:
    def __init__(self):
        self.cities = {}

    def add_city(self, name, temperature):
        if name in self.cities:
            return f"{name} zaten eklenmiş. Sıcaklık güncelleniyor..."
        self.cities[name] = City(name, temperature)
        return f"{name} şehri eklendi."

    def update_temperature(self, name, temperature):
        if name in self.cities:
            self.cities[name].temperature = temperature
            return f"{name} için sıcaklık {temperature}°C olarak güncellendi."
        return f"{name} bulunamadı!"

    def get_advice(self, temperature):
        if temperature < 0:
            return "Soğuk, sıkı giyinin."
        elif 0 <= temperature <= 15:
            return "Serin, mont almayı unutmayın."
        else:
            return "Hava güzel, rahat giyin."

    def list_cities(self):
        if not self.cities:
            print("Hiç şehir eklenmemiş.")
        else:
            print("\nŞehirler ve Sıcaklıkları:")
            for city in self.cities.values():
                print(city)


def main():
    weather_manager = WeatherManager()

    while True:
        print("\n1. Şehir Ekle\n2. Sıcaklık Güncelle\n3. Şehirleri Listele\n4. Tavsiye Al\n5. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Şehir Adı: ")
            temperature = float(input("Sıcaklık (°C): "))
            print(weather_manager.add_city(name, temperature))
        elif choice == "2":
            name = input("Şehir Adı: ")
            temperature = float(input("Yeni Sıcaklık (°C): "))
            print(weather_manager.update_temperature(name, temperature))
        elif choice == "3":
            weather_manager.list_cities()
        elif choice == "4":
            name = input("Şehir Adı: ")
            city = weather_manager.cities.get(name)
            if city:
                print(f"{city} - {weather_manager.get_advice(city.temperature)}")
            else:
                print(f"{name} bulunamadı!")
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
