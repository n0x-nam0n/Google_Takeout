from icalendar import Calendar
import argparse

def format_event(event):
    """
    Formats a single calendar event into the desired output structure.
    """
    return f"""
CALNAME:{event.get('X-WR-CALNAME', 'N/A')}

START:{event.get('DTSTART').dt.strftime('%Y%m%dT%H%M%SZ')}
  END:{event.get('DTEND').dt.strftime('%Y%m%dT%H%M%SZ')}
STAMP:{event.get('DTSTAMP').dt.strftime('%Y%m%dT%H%M%SZ')}

USERID:{event.get('UID', 'N/A')}
CREATED:{event.get('CREATED').dt.strftime('%Y%m%dT%H%M%SZ') if event.get('CREATED') else 'N/A'}
DESCRIPTION:{event.get('DESCRIPTION', 'N/A')}
LAST-MODIFIED:{event.get('LAST-MODIFIED').dt.strftime('%Y%m%dT%H%M%SZ') if event.get('LAST-MODIFIED') else 'N/A'}
LOCATION:{event.get('LOCATION', 'N/A')}
SEQUENCE:{event.get('SEQUENCE', 'N/A')}
STATUS:{event.get('STATUS', 'N/A')}
SUMMARY:{event.get('SUMMARY', 'N/A')}
"""

def main():
    """
    Main function to load the .ics file and format all calendar events.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Format calendar events from an .ics file.")
    parser.add_argument("file", help="Path to the .ics file containing calendar events")
    args = parser.parse_args()

    # Load the .ics file
    with open(args.file, "rb") as f:
        cal = Calendar.from_ical(f.read())

    # Format and print all events
    for component in cal.walk():
        if component.name == "VEVENT":
            formatted_event = format_event(component)
            print(formatted_event)

if __name__ == "__main__":
    main() 
