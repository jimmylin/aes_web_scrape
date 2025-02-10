import requests
import json
import csv
import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

def fetch_aes_data(tournament_id):
    url = f"https://www.advancedeventsystems.com/api/landing/events/{tournament_id}/teams"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        # Print the JSON structure to debug
        print(json.dumps(data, indent=4))
        
        # Save data to a file
        with open("aes_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print("Data successfully fetched and saved to aes_data.json")
        print("Response Data Type:", type(data))
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def convert_to_csv(data, filename="aes_data.csv"):
    if isinstance(data, dict):
        data = data.get("value", [])  # Extract the list from the "value" key
    
    if not isinstance(data, list) or not data:
        print("Unexpected data format, cannot convert to CSV.")
        return
    
    # Extract only relevant fields
    processed_data = []
    for team in data:
        processed_data.append({
            "teamId": team.get("teamId"),
            "name": team.get("name"),
            "clubId": team.get("clubId"),
            "clubName": team.get("clubName"),
            "teamCode": team.get("teamCode"),
            "acceptedType": team.get("acceptedType", {}).get("displayName"),
            "divisionDescription": team.get("divisionDescription")
        })
    
    keys = processed_data[0].keys() if processed_data else []
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(processed_data)
    
    print(f"Data successfully written to {filename}")

def write_to_google_sheets(csv_filename, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    
    sheet = client.open(sheet_name).sheet1
    
    with open(csv_filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        sheet.clear()
        sheet.update(data)
    
    print(f"Data successfully written to Google Sheets: {sheet_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape.py <tournament_id>")
        sys.exit(1)
    
    tournament_id = sys.argv[1]
    data = fetch_aes_data(tournament_id)
    if data:
        convert_to_csv(data)
        #TODO Set up Google Cloud Project and test this
        #write_to_google_sheets("aes_data.csv", "AES Data")
