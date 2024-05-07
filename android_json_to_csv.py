"""
sms_json_to_csv.py

This script converts JSON data containing SMS messages into a CSV file format, adding human-readable date columns. It is designed to facilitate the transformation of SMS data for further analysis or integration into other systems.

Features:
- Loads JSON data from a specified file path.
- Extracts unique headers from the JSON data.
- Converts Unix timestamps to human-readable date formats.
- Writes the transformed data to a CSV file with additional date columns.

Usage:
1. Ensure the JSON file containing SMS data is located at the same file path as this script
2. Run the script, providing the necessary file paths for input and output.
3. The script will generate a CSV file with the transformed data.

Note: This script assumes that the JSON data follows a specific structure with consistent field names for dates ('date' and 'date_sent').

Author: Prashant V. Gaikar (@1729prashant)
Date: 24-APR-2024

For more information, see the README.md file.
"""


import json
import csv
import os

from datetime import datetime

def load_json(file_path):
    """
    Load JSON data from the given file path.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            error_line = e.lineno
            print(f"Error decoding JSON at line {error_line}: {lines[error_line - 1].strip()}")
        return None


def get_headers(json_data):
    """
    Extract unique headers from JSON data.

    Args:
        json_data (list of dict): JSON data containing messages.

    Returns:
        list: Sorted list of unique headers.
    """
    headers_set = set()
    for msg in json_data:
        headers_set.update(msg.keys())
    return sorted(list(headers_set))


def convert_unix_to_human(timestamp, line_number):
    """
    Convert Unix timestamp to human-readable date format.

    Args:
        timestamp (str): Unix timestamp in milliseconds.
        line_number (int): Line number of the timestamp.

    Returns:
        str: Human-readable date string.
    """
    try:
        if timestamp:  # Check if timestamp is not empty
            # Convert milliseconds to seconds and then to datetime
            return datetime.utcfromtimestamp(float(timestamp) / 1000).strftime('%d/%m/%Y %H:%M:%S')
        else:
            return ''
    except ValueError:
        print(f"Error converting timestamp at line {line_number}")


def write_json_to_csv(json_data, headers, file_path):
    """
    Write JSON data to a CSV file.

    Args:
        json_data (list of dict): JSON data containing messages.
        headers (list): List of headers.
        file_path (str): The path to the CSV file.
    """
    # Add extra columns for human-readable dates
    headers = ['date_human', 'date_sent_human'] + headers
    
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()  # Write header row
        
        # Sort data by the "date" key
        sorted_data = sorted(json_data, key=lambda x: x.get('date', float('inf')), reverse=True)
        
        for msg in sorted_data:
            # Convert Unix timestamps to human-readable format
            msg['date_human'] = convert_unix_to_human(msg.get('date', ''), msg['__line__'])
            msg['date_sent_human'] = convert_unix_to_human(msg.get('date_sent', ''), msg['__line__'])
            # Write data row
            writer.writerow({header: msg.get(header, '') for header in headers})
    print(f"CSV file written successfully: {file_path}")


def main():
    """
    Main function to execute the program.
    """
    current_directory = os.getcwd() + "/"
    print("Program running in: ", current_directory)

    json_path = current_directory
    json_filename = "sms_restore.json"
    csv_filename = "sms_restore.csv"
    file_path = json_path + json_filename
    
    json_data = load_json(file_path)
    if json_data:
        for i, msg in enumerate(json_data, start=1):
            msg['__line__'] = i  # Add line number to each message
        headers = get_headers(json_data)
        csv_file_path = json_path + csv_filename
        write_json_to_csv(json_data, headers, csv_file_path)

if __name__ == "__main__":
    main()
