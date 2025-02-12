
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

...
How to Use:
Save the script as parse_playstore.py.
Run the script with your HTML file:   
python parse_playstore.py --input path/to/your/file.html --output output.txt
3. Check the console output for debugging information and the parsed activities in output.txt.
