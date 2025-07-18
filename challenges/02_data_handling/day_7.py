"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import os
import json
import csv

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
        return data
    
def save_as_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Converted {len(data)} records to {filename}")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))
    print(".......")


def main():

    data = load_csv_data(INPUT_FILE)
    if not data:
        return
    save_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main()
