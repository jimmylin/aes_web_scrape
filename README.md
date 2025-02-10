# AES Volleyball Tournament Scraper

## Overview
This project provides a set of Python scripts to scrape tournament registration data from Advanced Event Systems (AES). The goal is to monitor team registrations for volleyball tournaments and alert organizers when divisions are filling up. 

The first step in this process is scraping team registration data from AES and exporting it to a Google Sheet for further analysis.

## Features
- Fetches team registration data from AES API.
- Converts the data into a structured CSV file.
- Uploads the CSV data to a Google Sheet.
- Supports parameterized tournament ID input.

## Requirements
To run this project, ensure you have the following installed:

- Python 3.7+
- Required Python libraries:
  ```sh
  pip install requests gspread oauth2client
  ```
- A Google Cloud service account with access to Google Sheets.
- A `credentials.json` file for Google Sheets API authentication.

## Setup
### 1. Google Sheets API Authentication
To enable Google Sheets integration, follow these steps:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or use an existing one).
3. Enable the Google Sheets API.
4. Create a service account and download the `credentials.json` file.
5. Share your Google Sheet with the service account email.

### 2. Running the Script
Execute the script by passing a tournament ID as an argument:
```sh
python scrape.py <tournament_id>
```
For example:
```sh
python scrape.py 36812
```

## Output
- The script fetches data and saves it to `aes_data.json`.
- It converts the data into `aes_data.csv`.
- The data is then uploaded to a Google Sheet named **AES Data**.

## Future Enhancements
- Implement real-time monitoring of tournament registrations.
- Add email or Slack notifications when divisions reach capacity.
- Store historical registration data for trend analysis.

## Troubleshooting
- If the script fails to fetch data, check the AES API URL.
- Ensure your `credentials.json` file is correctly configured.
- Verify that the Google Sheet name matches the one in the script.
- If the script cannot find the tournament data, confirm the tournament ID is correct.

