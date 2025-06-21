import json
from datetime import datetime, timezone
import requests
import os
import utils.utils as utils
import boto3


City = [
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Ahmedabad",
    "Surat",
    "Pune",
    "Jaipur"
]

current_dir = os.path.dirname(os.path.abspath(__file__))
# weather_folder = os.path.join(current_dir, "weather")

output_path = os.path.join(current_dir, "output")
os.makedirs(output_path, exist_ok=True)

headers = {
    "Accept" :"application/json",
    "Content-Type" : "application/json" 
}

# python function to store the date on local computer
def run_openweather_etl():
    now = datetime.now(timezone.utc)
    timestamp = int(now.timestamp())

    for city in City:
        print(city)
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={utils.appid}"
        response = requests.get(api, headers=headers)

        if response.status_code == 200:
            myData = response.json()
            folder_path = os.path.join(output_path, city)
            os.makedirs(folder_path, exist_ok=True)

            file_name = f"{city}_weather_{now.year}_{now.month}_{now.day}_{timestamp}.json"
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'w') as file:
                json.dump(myData, file, indent=4)

        else:
            print(f"Failed to fetch data for {city}: {response.status_code}")


# run_openweather_etl()


s3 = boto3.client('s3')
bucket_name = 'weather-project-gaurav'

#python function to store data on the S3 bucket
def run_openweather_etl_S3():
    now = datetime.now(timezone.utc)
    timestamp = int(now.timestamp())

    for city in City:
        print(city)
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={utils.appid}"
        response = requests.get(api, headers=headers)

        if response.status_code == 200:
            myData = response.json()
            s3_key = f"LandingZone/{city}/{city}_weather_{now.year}_{now.month}_{now.day}_{timestamp}.json"

            s3.put_object(
                Bucket=bucket_name,
                Key=s3_key,
                Body=json.dumps(myData, indent=4),
                ContentType='application/json'
            )
            print(f"Uploaded: {s3_key}")
        else:
            print(f"Failed to fetch data for {city}: {response.status_code}")

run_openweather_etl_S3()
