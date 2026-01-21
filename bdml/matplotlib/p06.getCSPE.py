# http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayPayFree/1/5/201501/
# 날짜,노선,역,타고타,안내고타,내고내리,안내고내리

from http.client import HTTPConnection
from json import loads


f = open("./cspf.csv","a", encoding="utf-8")
hc = HTTPConnection('openapi.seoul.go.kr:8088')

for y in range(2015,2026):
    for m in range(1,13):
        when = "%d%02d" %(y,m)
        hc.request("GET","/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/621" + "/"+when+"/")
        resBody =hc.getresponse().read()

        data = loads(resBody)

        for a in data["CardSubwayPayFree"]["row"]:
            # print(a)
            f.write("%s," % a["USE_MM"])
            f.write("%s," % a["SBWY_ROUT_LN_NM"])
            f.write("%s," % a["STTN"])
            f.write("%.0f," % a["RMIO_GTON_NOPE"])
            f.write("%.0f," % a["FREECHRG_GTON_NOPE"])
            f.write("%.0f," % a["RMIO_GTOFF_NOPE"])
            f.write("%.0f\n" % a["FREECHRG_GTOFF_NOPE"])
        print(when)
        
hc.close()
f.close()


