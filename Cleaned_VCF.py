import vobject
import argparse

def format_contact(contact):
    """
    Formats a single contact entry into the desired output structure.
    """
    fn = contact.fn.value if hasattr(contact, 'fn') else "N/A"
    n = contact.n.value if hasattr(contact, 'n') else "N/A"
    tel = contact.tel.value if hasattr(contact, 'tel') else "N/A"
    email = contact.email.value if hasattr(contact, 'email') else "N/A"
    photo = contact.photo.value if hasattr(contact, 'photo') else "N/A"
    categories = contact.categories.value if hasattr(contact, 'categories') else "N/A"

    # Handle custom fields like "item1.TEL"
    custom_tel = ""
    for attr in contact.contents:
        if attr.startswith("item") and "TEL" in attr:
            custom_tel = f"item1.TEL:{contact.contents[attr][0].value}"
            break

    return f"""
----------------------------------
{fn}
{n}
{email if email != "N/A" else ""}
{"TEL;TYPE=CELL:" + tel if tel != "N/A" else ""}
{custom_tel if custom_tel else ""}
{"PHOTO:" + photo if photo != "N/A" else ""}
{"CATEGORIES:" + categories if categories != "N/A" else ""}
----------------------------------
"""

def main():
    """
    Main function to load the .vcf file and format all contacts.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Format contacts from a .vcf file.")
    parser.add_argument("file", help="Path to the .vcf file containing contacts")
    args = parser.parse_args()

    # Load the .vcf file
    with open(args.file, "r", encoding="utf-8") as f:
        vcard_data = f.read()

    # Parse the vCard data
    vcards = vobject.readComponents(vcard_data)

    # Format and print all contacts
    for vcard in vcards:
        formatted_contact = format_contact(vcard)
        print(formatted_contact)

