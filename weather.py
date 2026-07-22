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
city = input("Enter city name: ")
apikey=" "  #enter your api key
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
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
        print("❌ City not found!")

except Exception as e:
    print("Error:", e)