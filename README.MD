
Clean_Contacts.py

This will create two files:

cleaned_contacts.json (structured data)
cleaned_contacts.csv (flat table format)

Key features:

Handles missing values properly
Preserves photo links
Maintains group memberships
Keeps all phone numbers and emails
Converts addresses to structured format
Retains special notes and birthdays
The script automatically:
Combines name components
Standardizes phone number formats
Validates email addresses
Removes empty fields
Handles encoding issues

Usage:

python Clean_Contacts.py -t (location of contacts.csv)

-----------------------------------------------------------------------------------------------



Playstore.py

1.Grouping by Activity Type:
Activities are now stored in a dictionary (activities) where the key is the activity type (e.g., Installed, Visited) and the value is a list of activities of that type.
2. Output Format:
The script now groups all activities of the same type together in the output file.
Each activity type is followed by its associated apps, links, and timestamps.
3. Debugging:
Added debug messages to help identify issues during parsing.

Example Output:Activity: 
Visited
App: Gardenscapes
Link: https://play.google.com/store/apps/details?id=com.playrix.gardenscapes
Timestamp: 2023-05-23 09:29:47
App: Gardenscapes
Link: https://play.google.com/store/apps/details?id=com.playrix.gardenscapes
Timestamp: 2023-05-23 09:29:47
----------------------------------------
Activity: Installed
App: Google Messages
Link: https://play.google.com/store/apps/details?id=com.google.android.apps.messaging
Timestamp: 2024-02-04 05:15:20
App: WeatherService
Link: https://play.google.com/store/apps/details?id=com.coloros.weather.service
Timestamp: 2023-10-27 11:23:13
----------------------------------------
How to Use:
Save the script as parse_playstore.py.
Run the script with your HTML file:   
python parse_playstore.py --input path/to/your/file.html --output output.txt
3. Check the console output for debugging information and the parsed activities in output.txt.
------------------------------------------------------------------------------------------------------------------


Clean_App.py

This will clean up your installed apps under playstore.

1. Added Docstrings: Added docstrings to the format_entry and main functions for better documentation.
2. Simplified Structure: Removed unnecessary functions (clean_app_history and save_cleaned_data) and streamlined the script.
3. Encapsulated Main Logic: Moved the main logic into a main() function for better organization.
4. Improved Readability: Used consistent indentation and spacing for clarity.

How It Works:
1. format_entry Function: Formats a single app installation entry into the specified structure.
2. main Function:
Loads the JSON data from Installs.json.
Iterates through all entries and formats each one using format_entry.
Prints the formatted output for each installed program.
Example Output:
For each installed program, the output will look like this:
How to Use:
Save the script as clean_app_history.py.
2. Ensure Installs.json is in the same directory.
Run the script:
4. The formatted output for all installed programs will be printed to the console.
-------------------------------------------------------------------------------------------------------------
