import requests
print("""
    ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                                                                                                    ║
    ║                                                                                                                                                                    ║
    ║                                                                                                                                                                    ║
    ║                                                    ██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗                                                      ║
    ║                                                    ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗                                                     ║
    ║                                                    ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝                                                     ║
    ║                                                    ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗                                                     ║
    ║                                                    ╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║                                                     ║
    ║                                                     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                     ║
    ║                                                                                                                                                                    ║
    ║                                                                        █████╗ ██████╗ ██████╗                                                                      ║
    ║                                                                       ██╔══██╗██╔══██╗██╔══██╗                                                                     ║
    ║                                                                       ███████║██████╔╝██████╔╝                                                                     ║
    ║                                                                       ██╔══██║██╔═══╝ ██╔═══╝                                                                      ║
    ║                                                                       ██║  ██║██║     ██║                                                                          ║
    ║                                                                       ╚═╝  ╚═╝╚═╝     ╚═╝                                                                          ║
    ║                                                                                                                                                                    ║
    ║                                                        Real-Time Weather • Temperature • Wind • Humidity                                                           ║
    ║                                                                                                                                                                    ║
    ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_weather(city):
    url = f"{BASE_URL}/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print("\n========== WEATHER REPORT ==========")
            print(f"City        : {data['name']}")
            print(f"Country     : {data['sys']['country']}")
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Feels Like  : {data['main']['feels_like']} °C")
            print(f"Humidity    : {data['main']['humidity']}%")
            print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather'][0]['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")
            print("====================================")

        else:
            print(f" {data.get('message', 'City not found!')}")

    except requests.exceptions.Timeout:
        print("❌ Request timed out. Check your internet connection.")

    except requests.exceptions.RequestException as e:
        print(" Network error:", e)


def get_forecast(city):
    url = f"{BASE_URL}/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print(f" {data.get('message', 'City not found!')}")
            return

        print("\n========== 5 DAY WEATHER FORECAST ==========")
        print(f"City    : {data['city']['name']}")
        print(f"Country : {data['city']['country']}")
        print("============================================")

        days = 0

        for item in data["list"]:

            # Get one forecast around noon for each day
            if "12:00:00" in item["dt_txt"]:

                print(f"\nDay {days + 1}")
                print(f"Date        : {item['dt_txt']}")
                print(f"Temperature : {item['main']['temp']} °C")
                print(f"Feels Like  : {item['main']['feels_like']} °C")
                print(f"Humidity    : {item['main']['humidity']}%")
                print(f"Pressure    : {item['main']['pressure']} hPa")
                print(
                    f"Weather     : "
                    f"{item['weather'][0]['description'].title()}"
                )
                print(f"Wind Speed  : {item['wind']['speed']} m/s")
                print("--------------------------------------------")

                days += 1

                if days == 5:
                    break

    except requests.exceptions.Timeout:
        print(" Request timed out.")

    except requests.exceptions.RequestException as e:
        print(" Network error:", e)


def weather_advice(city):
    url = f"{BASE_URL}/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print(f" {data.get('message', 'City not found!')}")
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["main"]

        print("\n========== WEATHER ADVICE ==========")
        print(f"City        : {data['name']}")
        print(f"Temperature : {temperature} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {weather}")

        if temperature >= 35:
            advice = " It's very hot. Stay hydrated and avoid unnecessary outdoor activity."

        elif temperature >= 25:
            advice = " The weather is warm. Keep yourself hydrated."

        elif temperature <= 10:
            advice = " It's cold. Wear warm clothes."

        elif weather == "Rain":
            advice = " It may rain. Carry an umbrella or raincoat."

        elif weather == "Thunderstorm":
            advice = " Thunderstorms are possible. Avoid exposed outdoor areas."

        elif weather == "Clouds":
            advice = " It's cloudy. Keep an umbrella nearby in case conditions change."

        else:
            advice = " Weather looks comfortable. Have a good day!"

        print(f"\nAdvice      : {advice}")
        print("====================================")

    except requests.exceptions.Timeout:
        print(" Request timed out.")

    except requests.exceptions.RequestException as e:
        print(" Network error:", e)


def main():

    while True:

        print("""
╔════════════════════════════════════════╗
║          🌦️ WEATHER APPLICATION        ║
╠════════════════════════════════════════╣
║  1. Current Weather                   ║
║  2. 5-Day Weather Forecast            ║
║  3. Weather Advice                    ║
║  4. Exit                              ║
╚════════════════════════════════════════╝
        """)

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print(" Please enter a number from 1 to 4.")
            continue

        if choice == 4:
            print(" Exiting Weather Application...")
            break

        if choice in [1, 2, 3]:

            city = input("Enter your city name: ").strip()

            if not city:
                print("City name cannot be empty.")
                continue

            if choice == 1:
                get_weather(city)

            elif choice == 2:
                get_forecast(city)

            elif choice == 3:
                weather_advice(city)

        else:
            print(" Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
