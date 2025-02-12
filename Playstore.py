  GNU nano 6.2                                                                                                     playstore.py                                                                                                               
from bs4 import BeautifulSoup
from datetime import datetime
import argparse
import re

def parse_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    activities = {}

    # Find all activity cells
    content_cells = soup.find_all("div", class_="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1")
    print(f"Found {len(content_cells)} activity cells.")  # Debugging

    for cell in content_cells:
        # Extract the activity text
        activity_text = cell.get_text(strip=True)
        if not activity_text:
            print("Skipping cell: No activity text found.")  # Debugging
            continue

        # Debug: Print the raw activity text
        print(f"Raw activity text: {activity_text}")  # Debugging

        # Use regex to extract the activity type, app name, and timestamp
        match = re.match(r"^(Installed|Updated|Uninstalled|Visited|Searched for|Received a notification)\s*([A-Z].+?)([A-Za-z]{3} \d{1,2}, \d{4}, \d{1,2}:\d{2}:\d{2} [AP]M PST)$", activity_text)
        if not match:
            print(f"Skipping cell: Could not parse activity text: {activity_text}")  # Debugging
            continue

        activity_type, app_name, timestamp_str = match.groups()

        # Convert the timestamp to a datetime object
        try:
            timestamp = datetime.strptime(timestamp_str, "%b %d, %Y, %I:%M:%S %p PST")
        except ValueError:
            print(f"Skipping cell: Could not parse timestamp: {timestamp_str}")  # Debugging
            continue

        # Extract the app link
        app_link = cell.find("a")["href"] if cell.find("a") else None

        # Add the activity to the dictionary, grouped by activity type
        if activity_type not in activities:
            activities[activity_type] = []
        activities[activity_type].append({
            "app": app_name,
            "link": app_link,
            "timestamp": timestamp
        })

    return activities

def save_activities(activities, output_file):

