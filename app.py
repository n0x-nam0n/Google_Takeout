from flask import Flask, request, render_template, send_file
import os
import json
import tempfile
from clean_app_history import main as clean_app_history

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" not in request.files:
            return "No file uploaded", 400
        file = request.files["file"]
        if file.filename == "":
            return "No file selected", 400

        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
            file.save(temp_file.name)
            temp_file_path = temp_file.name

        # Run the cleaning script on the uploaded file
        try:
            # Call the cleaning function
            clean_app_history(temp_file_path)

            # Read the cleaned output
            with open("cleaned_app_history.json", "r") as cleaned_file:
                cleaned_data = cleaned_file.read()

            # Return the cleaned data as a downloadable file
            return send_file(
                "cleaned_app_history.json",
                as_attachment=True,
                download_name="cleaned_app_history.json",
            )
        except Exception as e:
            return f"Error processing file: {str(e)}", 500
        finally:
            # Clean up temporary files
            os.remove(temp_file_path)
            if os.path.exists("cleaned_app_history.json"):
                os.remove("cleaned_app_history.json")

    return render_template("upload.html")

@app.route("/clean-calendar", methods=["POST"])
def clean_calendar():
    if "file" not in request.files:
        return "No file uploaded", 400
    file = request.files["file"]
    if file.filename == "":
        return "No file selected", 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".ics") as temp_file:
        file.save(temp_file.name)
        temp_file_path = temp_file.name

    try:
        # Call the calendar cleaning function
        from clean_calendar import main as clean_calendar
        clean_calendar(temp_file_path)

        with open("cleaned_calendar.txt", "r") as cleaned_file:
            cleaned_data = cleaned_file.read()

        return send_file(
            "cleaned_calendar.txt",
            as_attachment=True,
            download_name="cleaned_calendar.txt",
        )
    except Exception as e:
        return f"Error processing file: {str(e)}", 500
    finally:
        os.remove(temp_file_path)
        if os.path.exists("cleaned_calendar.txt"):
            os.remove("cleaned_calendar.txt")

if __name__ == "__main__":
    app.run(debug=True) 
