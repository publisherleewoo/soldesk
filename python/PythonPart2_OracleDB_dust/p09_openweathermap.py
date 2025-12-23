# https://openweathermap.org/
# api key = baff8f3c6cbc28a4024e336599de28c4
# https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4

# JSON(JavaScript Object Notation)

from http.client import HTTPSConnection
import json
from oracledb import connect

hc = HTTPSConnection("api.openweathermap.org")
hc.request(
    "GET",
    "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr",
)
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()


con = connect("leewoo/3214@195.168.9.53:1521/xe")

weatherData = json.loads(txt)
description = weatherData["weather"][0]["description"]
humidity = weatherData["main"]["humidity"]
temp = weatherData["main"]["temp"]
hc.close()



print(description, humidity, temp)

sql = "insert into owm_weather values (sysdate,'%s',%.2f,%d)" % (
    description,
    humidity,
    temp,
)

cur = con.cursor()
cur.execute(sql)
con.commit()

cur.close()
con.close()

