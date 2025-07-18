"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests

FILENAME = "weather_logs.csv"
API_KEY = "Get Your own key here" 
# keys are usually hidden in .env file but that is for later

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
   city = input("Enter your city name: ").strip()
   date = datetime.now().strftime("%Y-%m-%d")

   with open(FILENAME, "r", newline='', encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
          if row["Date"] == date and row['City'].lower() == city.lower():
              print("Entry for this city and date exists")
              return
          
   try:
       url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
       response = requests.get(url)
       data = response.json()

       if response.status_code != 200:
           print(f"API Error ")
           return
       temp = data["main"]["temp"]
       condition = data["weather"][0]["main"]

       with open(FILENAME, "a", newline='', encoding="utf-8") as f:
           writer = csv.writer(f)
           writer.writerow([date, city.title(), temp, condition])
           print(f"Logged: {temp} {condition} in {city.title()} on {date}")
   except Exception as e:
       print("Failed to make API call")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No Entries")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")


def main():
    while True:
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View weather log")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case _: print("Invalid choice")


if __name__ == "__main__":
    main()