from asyncio.windows_events import NULL
import string


class timezone:
    id = int
    abbreviation = string
    offsetUTC = float

pst = timezone()
est = timezone()
eet = timezone()

pst.id = 1
pst.abbreviation = "PST"
pst.offsetUTC = -8

est.id = 2
est.abbreviation = "EST"
est.offsetUTC = -5

eet.id = 3
eet.abbreviation = "EET"
eet.offsetUTC = 2.0

tzList = [pst,est,eet]
for tz in tzList:
    if tz.id == 2:
        print("I found the TZ with ID ",tz.id,", it is "+tz.abbreviation+" and is UTC",tz.offsetUTC)
        break