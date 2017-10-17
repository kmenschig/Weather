import os

API_KEY = os.environ['WUNDERGROUND_KEY']

os.chdir(os.path.dirname(os.path.abspath(__file__)))
cwd=os.getcwd()


vapor_pressure = {
    "a0": 6.107799961,
    "a1": 4.436518521E-01,
    "a2": 1.428945805E-02,
    "a3": 2.650648471E-04,
    "a4": 3.031240396E-06,
    "a5": 2.034080948E-08,
    "a6": 6.136820929E-11
}


stations = [
    {
        "country": "Brazil",
        "country_short": "br",
        "station_id": "ISTATEOF5"
    },
    {
        "country": "Colombia",
        "country_short": "co",
        "station_id": "IMANIZAL5"
    },
    {
        "country": "Germany",
        "country_short": "dl",
        "station_id": "IKNBERZD2"
    },
    {
        "country": "Germany",
        "country_short": "dl",
        "station_id": "IKNMESCH2"
    },
    {
        "country": "Germany",
        "country_short": "dl",
        "station_id": "ICOLOGNE184"
    },
    {
        "country": "Great Britain",
        "country_short": "gb",
        "station_id": "IDUKINFI2"
    },
    {
        "country": "Mexico",
        "country_short": "mx",
        "station_id": "ITULTITL2"
    },
    {
        "country": "Mexico",
        "country_short": "mx",
        "station_id": "IESTADOD2"
    },
    {
        "country": "Mexico",
        "country_short": "mx",
        "station_id": "ICIUDADD170"
    },
    {
        "country": "Philippines",
        "country_short": "ph",
        "station_id": "ICALABAR26"
    }
]
