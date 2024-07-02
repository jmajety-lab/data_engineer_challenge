# World Bank Country Data API

This repository provides a FastAPI-based web application to serve World Bank country data and display it on an interactive map.

## Features

- Retrieve country data via API endpoints
- Display country data on an interactive map
- Search functionality to locate specific countries on the map

## Prerequisites

- Python 3.7 or higher
- Git

## Installation

1. **Clone the repository:**

   git clone https://github.com/jmajety-lab/data_engineer_challenge.git
   cd data_engineer_challenge

2. **Create and activate a virtual environment:**



    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the dependencies:**


    pip install -r requirements.txt

4. **Ensure the data file is in place:**

    Make sure you have the worldbank_countries_with_geo_data.csv file in the repository directory. This file should contain the cleaned CSV data with geo-locations.


5. **Start the FastAPI server:**


    uvicorn main:app --reload in your terminal

    Open your web browser (Google chrome is recommended) and navigate to http://127.0.0.1:8000/map to see the interactive map.



**Access the application:**

    http://127.0.0.1:8000/map
