from fastapi import FastAPI
from frcm.restapi.utils import parse_location
from frcm.weatherdata.utils import weatherdata_parse
import datetime
import dateutil.parser

app = FastAPI()

@app.get("/fireguard")
async def root():
    return {"message": "FireGuard Cloud Service"}


# Authenticates user. Unnessecary?
@app.get("/fireguard/authenticate")
async def authenticate ():
    pass


# Default for services selection. Returns JSON containing info on available services, input variables required and return values.
@app.get("/fireguard/services")
async def services ():
    return {
        "message": "FireGuard services",
        "rawdata": {
            "temp": "float", 
            "humidity": "float",
            "wind_speed": "float",
            "timestamp": "str",
            "return": ""
        },
        "area": {
            "gps": {
                "lon": "float", 
                "lat": "float",
                "return": ""
            },
            "postcode": {
                "postal_code": "int",
                "return": ""
            },
            "address": {
                "adr": "str",
                "return": ""
            }
        }
    }


# Calculates fire risk based on raw data supplied by the user.
@app.get("/fireguard/services/rawdata")
async def raw_data(temp: float, humidity: float, wind_speed: float, timestamp: str):
    weatherdata_parse()


# Default for area selection. Returns expected input variables for the area service functions.
@app.get("/fireguard/services/area")
async def area():
    return {
        "message": "Område tjeneste frå FireGuard, brannrisiko basert på værdata frå lokasjonar.",
        "area": {
            "gps": {
                "lon": "float", 
                "lat": "float",
                "return": ""
            },
            "postcode": {
                "postal_code": "int",
                "return": ""
            },
            "address": {
                "adr": "str",
                "return": ""
            }
        }
    }


# Calculates fire risk based on GPS coordinates supplied by the user.
@app.get("/fireguard/services/area/gps")
async def gps (lon: float, lat: float):
    parse_location()


# Calculates fire risk based on postcode. Uses separate API to determine coordinates for the post code.
@app.get("/fireguard/services/area/postcode")
async def postcode (postal_code: int):
    pass


# Calculates fire risk based on address. Uses separate API to determine coordinates for the address.
@app.get("/fireguard/services/area/address")
async def address (adr: str):
    pass