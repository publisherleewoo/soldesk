# https://openweathermap.org/
# api key = baff8f3c6cbc28a4024e336599de28c4
# https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4

# JSON(JavaScript Object Notation)

from http.client import HTTPSConnection
import json

hc = HTTPSConnection("api.openweathermap.org")
hc.request(
    "GET",
    "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr",
)
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()

weatherData = json.loads(txt)

hc.close()


