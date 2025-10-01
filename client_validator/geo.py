# geo.py
# Fetch GEO coordinates for a given address using OpenStreetMap Nominatim API
import requests
import logging


def fetch_geo_coordinates(address):
    # Old Nominatim code commented out below
    # if not address:
    #     return None
    # url = "https://nominatim.openstreetmap.org/search"
    # params = {
    #     "q": address,
    #     "format": "json",
    #     "limit": 1
    # }
    # try:
    #     response = requests.get(
    #         url,
    #         params=params,
    #         headers={"User-Agent": "client-validator/1.0"},
    #         timeout=5
    #     )
    #     response.raise_for_status()
    #     data = response.json()
    #     if data:
    #         lat = data[0].get("lat")
    #         lon = data[0].get("lon")
    #         return {"latitude": lat, "longitude": lon}
    #     else:
    #         logging.warning(f"No GEO data found for address: {address}")
    #         return None
    # except requests.Timeout:
    #     logging.error(
    #         f"Timeout fetching GEO coordinates for address: {address}")
    #     return None
    # except Exception as e:
    #     logging.error(f"Failed to fetch GEO coordinates: {e}")
    #     return None

    # New OpenCage API integration
    if not address:
        return None
    api_key = "cff2c176b4ee4afca1bb960f53d62156"
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": address,
        "key": api_key,
        "limit": 1,
        "no_annotations": 1
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            geometry = data["results"][0].get("geometry", {})
            lat = geometry.get("lat")
            lon = geometry.get("lng")
            if lat is not None and lon is not None:
                return {"latitude": lat, "longitude": lon}
            else:
                logging.warning(f"No GEO data found for address: {address}")
                return None
        else:
            logging.warning(f"No GEO data found for address: {address}")
            return None
    except requests.Timeout:
        logging.error(
            f"Timeout fetching GEO coordinates for address: {address}")
        return None
    except Exception as e:
        logging.error(f"Failed to fetch GEO coordinates: {e}")
        return None
