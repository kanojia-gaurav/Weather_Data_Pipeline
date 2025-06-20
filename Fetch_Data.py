import pandas as pd
from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import os
import s3fs
import csv
import utils.utils as utils

# print(datetime.now())

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

# print(utils.appid)
# print(current_dir)

for data in City:
    folder_path = os.path.join(output_path, data)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, f"{data}_weather_{datetime.now()}.csv")
    print(file_path)
    # with open(file_path, mode="w", newline="") as file:
    #     writer = csv.writer(file)
    #     print(writer)
        # writer.writerow(headers)  # write header





# def run_openweather_etl():

#     for data in City:
#         api = f"https://api.openweathermap.org/data/2.5/weather?q={data}&appid={utils.appid}"
#         print(data)
#         response = requests.request("GET",api, headers=headers, data={})
#         myData = response.json()

#         df = pd.json_normalize(myData)
#         print(df)


# print(run_openweather_etl())