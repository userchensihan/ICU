from geoip2 import database
import sys
def yLngLatLocation(IP):
    r=database.Reader('./GeoLite2-City.mmdb').city(IP).location
    print(f"{r.latitude}\n{r.longitude}")
if __name__=="__main__":
    yLngLatLocation(sys.argv[1])
