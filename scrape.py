import requests
import json

def fetch_aes_data():
    url = "https://www.advancedeventsystems.com/api/landing/events/36812/teams"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        # Save data to a file
        with open("aes_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print("Data successfully fetched and saved to aes_data.json")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    fetch_aes_data()
