
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


def check(data):
    if data == None:
        return "?"
    return data.strip().replace(",", " ")


f = open("./lnp.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")

for start in range(1, 760002, 1000):
    t = "%d/%d" % (start, start + 999)

    hc.request(
        "GET", "/575a4655496b636839386f58586542/xml/ListNecessariesPricesService/" + t
    )

    resBody = hc.getresponse().read()

    lnpsData = fromstring(resBody)
    for l in lnpsData.iter("row"):
        f.write(check(l.find("M_NAME").text) + ",")
        f.write(check(l.find("A_NAME").text).strip() + ",")
        f.write(check(l.find("A_PRICE").text) + ",")
        f.write(check(l.find("P_DATE").text) + ",")
        f.write(check(l.find("M_TYPE_NAME").text) + ",")
        f.write(check(l.find("M_GU_NAME").text) + "\n")
    print(t)

hc.close()
f.close()
