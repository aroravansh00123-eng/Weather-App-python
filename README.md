# 🌦️ Python Weather App

A simple Python-based weather application that fetches and displays **real-time weather information** for a user-selected city.

This project was created to practice Python programming, API integration, JSON data handling, user input, and basic error handling.

---

## 📌 About the Project

The Weather App takes a city name from the user and sends a request to a weather API.

The API returns weather data in JSON format, which the program processes and displays in a simple, readable format.

## 📚 Libraries & Documentation

This project uses the following Python library:

- **Requests** — Used to send HTTP requests to the weather API.
  - Official Documentation: https://requests.readthedocs.io/

- **Python** — Main programming language.
  - Official Documentation: https://docs.python.org/3/

### 🔄 Basic Workflow

```text
User enters city
       ↓
Python sends API request
       ↓
Weather API processes request
       ↓
JSON weather data received
       ↓
Python extracts required information
       ↓
Weather information displayed

#File Structure
Weather-App/
│
├── weather.py
├── README.md
└── requirements.txt