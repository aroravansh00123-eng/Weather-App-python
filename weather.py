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
while True:
    print("""FOLLOWING THINGS WORKS IN GIVEN PROGRAM
            1. Weather According to your CITY
            2. 5 Day Weather Forecast according to your CITY
            3. AI-weather advice according to your CITY
        """)
    choice=int(input("ENTER THE CHOICE"))
    if choice==1:
        city = input("Enter city name: ")
        apikey="4ecaf8f9a6bc8a5b94e85bead4b2745b"  #enter your api key
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
    elif choice==2:
        city=input("ENTER YOUR CITY")
        apikey="4ecaf8f9a6bc8a5b94e85bead4b2745b"
        url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == "200":

                print("\n========== 5 DAY WEATHER FORECAST ==========")
                print(f"City    : {data['city']['name']}")
                print(f"Country : {data['city']['country']}")
                print("============================================")

                days = 0

                for item in data["list"]:

                    if "12:00:00" in item["dt_txt"]:
                        print(f"\nDate        : {item['dt_txt']}","Day-",days)
                        print(f"Temperature : {item['main']['temp']} °C")
                        print(f"Feels Like  : {item['main']['feels_like']} °C")
                        print(f"Humidity    : {item['main']['humidity']}%")
                        print(f"Pressure    : {item['main']['pressure']} hPa")
                        print(f"Weather     : {item['weather'][0]['description'].title()}")
                        print(f"Wind Speed  : {item['wind']['speed']} m/s")
                        print("--------------------------------------------")

                        days += 1

                    if days == 5:
                        break

            else:
                print("❌ City not found!")

        except Exception as e:
            print("Error:", e)