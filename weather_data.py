import requests
from datetime import date

# Luzern coordinates
latitude = 47.0502
longitude = 8.3093

# Today's date in ISO format
today = date.today().isoformat()


url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&daily=precipitation_sum"
    f"&timezone=Europe%2FBerlin"
    f"&start_date={today}&end_date={today}"
)

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    precipitation = data['daily']['precipitation_sum'][0]
    if precipitation > 0:
        print("It rained today in Luzern.")
    else:
        print("It did not rain today in Luzern.")
else:
    print("Failed to fetch data from weather API.")
