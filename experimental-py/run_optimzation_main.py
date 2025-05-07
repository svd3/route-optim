import csv
import requests
import json
import argparse
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
def parse_arguments():
    parser = argparse.ArgumentParser(description="Run route optimization.")
    parser.add_argument("--csv-file-path", required=True, help="Path to the input CSV file containing waypoints.")
    return parser.parse_args()

args = parse_arguments()
CSV_FILE_PATH = args.csv_file_path
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")  # Load API key from .env file

def read_csv(file_path):
    """Reads the CSV file and returns a list of waypoints."""
    waypoints = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            waypoints.append(row)
    return waypoints

def call_route_optimization_api(waypoints):
    """Calls the Google Maps Route Optimization API."""
    # TODO: Implement the optimization logic here.
    # This should include processing the waypoints, calling the route optimization API,
    # and handling the response to determine the optimal route.
    pass

def main():
    waypoints = read_csv(CSV_FILE_PATH)
    if not waypoints:
        print("No waypoints found in the CSV file.")
        return

    for i, waypoint in enumerate(waypoints):
        if (i < 10):
            print(f"Waypoint {i+1}\n: {waypoint}")

    call_route_optimization_api(waypoints)
    print("Route optimization API called successfully.")

if __name__ == "__main__":
    main()