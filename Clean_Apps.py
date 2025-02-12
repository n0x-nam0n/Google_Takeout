import json

def format_entry(entry):
    """
    Formats a single app installation entry into the desired output structure.
    """
    return f"""
________________________________________
----------------------------------------
            "{entry['install']['doc']['title']}"
         "documentType": "{entry['install']['doc']['documentType']}",
                "title": "{entry['install']['doc']['title']}"
----------------------------------------
                "model": "{entry['install']['deviceAttribute']['model']}",
              "carrier": "{entry['install']['deviceAttribute']['carrier']}",
         "manufacturer": "{entry['install']['deviceAttribute']['manufacturer']}",
    "deviceDisplayName": "{entry['install']['deviceAttribute']['deviceDisplayName']}"
"firstInstallationTime": "{entry['install']['firstInstallationTime']}"   
       "lastUpdateTime": "{entry['install']['lastUpdateTime']}"
---------------------------------------
_______________________________________
"""

def main():
    """
    Main function to load the JSON data and format all installed programs.
    """
    # Load the JSON data
    with open("Installs.json", "r") as f:
        app_history = json.load(f)

    # Format and print all installed programs
    for entry in app_history:
        formatted_entry = format_entry(entry)
        print(formatted_entry)

if __name__ == "__main__":
    main()
