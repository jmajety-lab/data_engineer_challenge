from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load the cleaned CSV data with geo-locations
try:
    df = pd.read_csv('worldbank_countries_with_geo_data.csv')
    df = df.replace({np.nan: None})  # Replace NaNs with None
except Exception as e:
    logging.error(f"Error loading data: {e}")
    raise HTTPException(status_code=500, detail="Data loading error")

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to the World Bank Country Data API"}

@app.get("/countries/")
def get_countries():
    try:
        countries_data = df.to_dict(orient='records')
        logging.debug(f"Countries data: {countries_data[:5]}")  # Log first 5 records for debugging
        return countries_data
    except Exception as e:
        logging.error(f"Error retrieving countries: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/countries/{country_name}")
def get_country(country_name: str):
    try:
        country = df[df['name'].str.lower() == country_name.lower()]
        if country.empty:
            return {"error": "Country not found"}
        return country.to_dict(orient='records')[0]
    except Exception as e:
        logging.error(f"Error retrieving country {country_name}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/map")
def get_map():
    return FileResponse("index.html")
