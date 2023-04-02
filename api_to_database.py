import requests
import psycopg2
import time
from datetime import datetime

api_key = 'API Key'
city = 'Enter A city here'

# Connect to the local PostgreSQL database
conn = psycopg2.connect(database="database name", user="db username", password="db password", host="localhost", port="your port")

while True:
    # make api call
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    cod = weather_data.json()['cod']
    city = weather_data.json()['name']
    country = weather_data.json()['sys']['country']
    wind = weather_data.json()['wind']['speed']
    test_data1 = city
    test_data2 = temp
    test_data3 = cod
    test_data4 = country
    test_data5 = wind
    now =  datetime.now()

    #Create a cursor object
    cur = conn.cursor()

    #Insert the data into the database
    cur.execute("INSERT INTO python (city, temp, cod, country, wind_speed, date ) VALUES (%s, %s, %s, %s, %s,%s)",
                (test_data1, test_data2, test_data3, test_data4,test_data5,now))

    #Commit the transaction
    conn.commit()

    #Close the cursor
    cur.close()

    #Pause for 10 seconds or any desired amount of time. Note 10 seconds might be too much for this kind of data
    time.sleep(10)
