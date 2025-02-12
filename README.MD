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
