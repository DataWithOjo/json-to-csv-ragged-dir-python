import glob
import json
import csv
import os


def flatten_json(y):
    """Recursively flatten nested JSON/dict."""
    out = {}

    def flatten(x, name=""):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f"{name}{a}_")
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, f"{name}{i}_")
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def convert_json_to_csv(json_path):
    # Read and flatten JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Make sure it's a list of objects
    if isinstance(data, dict):
        data = [data]

    # Flatten all records
    flat_data = [flatten_json(record) for record in data]

    # Determine CSV path
    csv_path = os.path.splitext(json_path)[0] + ".csv"

    # Write CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_data[0].keys())
        writer.writeheader()
        writer.writerows(flat_data)

    print(f"Converted: {json_path} to {csv_path}")


def main():
    # Find all .json files recursively inside ./data/
    json_files = glob.glob("data/**/*.json", recursive=True)

    if not json_files:
        print("No JSON files found.")
        return

    for json_path in json_files:
        try:
            convert_json_to_csv(json_path)
        except Exception as e:
            print(f"Failed to convert {json_path}: {e}")


if __name__ == "__main__":
    main()
