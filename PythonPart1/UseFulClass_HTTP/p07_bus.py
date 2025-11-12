# # http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/5/20151101/

# # 2015,01,01 ~ 2024,12,31 버스 운행정보

# # 2015,01,01,100번(하계동~용산구청),명륜3가,성대입구,108,171

# from datetime import date, timedelta
# from http.client import HTTPConnection
# from json import loads

# hc = HTTPConnection("openapi.seoul.go.kr:8088")

# year = 2019

# start_date = date(year, 1, 1)
# end_date = date(year, 12, 31)

# delta = end_date - start_date
# days_count = delta.days + 1

# for i in range(days_count):
#     current_date = start_date + timedelta(days=i)
#     hc.request("GET","/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/5/"+current_date.strftime('%Y%m%d'))


#     resBody = hc.getresponse().read().decode()
#     print(resBody)
#     data = loads(resBody)

#     row = data["CardBusStatisticsServiceNew"]["row"]
#     hc.close()

#     f = open(
#         "C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/bus"+str(year)+".csv",
#         "a",
#         encoding="utf-8",
#     )
#     for r in row:
#         USE_YMD = r["USE_YMD"]
#         y=str(USE_YMD[0:4])
#         m=str(USE_YMD[4:6])
#         d=str(USE_YMD[6:8])
#         RTE_NM = str(r["RTE_NM"]).replace(",","")
#         SBWY_STNS_NM = str(r["SBWY_STNS_NM"]).replace(",","")
#         GTON_TNOPE = int(r["GTON_TNOPE"])
#         GTOFF_TNOPE = int(r["GTOFF_TNOPE"])
#         # 수정된 코드 (튜플로 묶음)
#         f.write("%s,%s,%s,%s,%s,%d,%d\n" % (y, m, d, RTE_NM, SBWY_STNS_NM, GTON_TNOPE, GTOFF_TNOPE))


# f.close()

from http.client import HTTPConnection
from json import loads

# 1~1000
# 1001~2000
# ...
# 41001~42000
yy = 2023
f = open("C:/PythoneWorkspace/PythonPart1/UseFulClass_HTTP/bus%d.csv" % yy, "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
 
#for yy in range(2015, 2025):
for mm in range(1, 13):
    for dd in range(1, 32):
        for start in range(1, 41002, 1000):
            t = "%d/%d/%d%02d%02d" % (start, start + 999, yy, mm, dd)
            hc.request(
                "GET",
                "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/" + t,
            )
            resBody = hc.getresponse().read()
 
            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData:
                cbssn = busData["CardBusStatisticsServiceNew"]
                stations = cbssn["row"]
                for s in stations:
                    uy = s["USE_YMD"]
                    y = uy[0:4]
                    m = uy[4:6]
                    d = uy[6:8]
                    rn = s["RTE_NM"].replace(",", ".")
                    ssn = s["SBWY_STNS_NM"].replace(",", ".")
                    gont = s["GTON_TNOPE"]
                    gofft = s["GTOFF_TNOPE"]
                    data = "%s,%s,%s,%s,%s,%.0f,%.0f\n" % (y, m, d, rn, ssn, gont, gofft)
                    f.write(data)
                print(t)
hc.close()
f.close()