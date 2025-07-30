# JSON to CSV Converter from Ragged Directories

This project is a simple Python utility that recursively searches through a ragged directory structure, identifies all `.json` files, flattens their nested structures, and converts them into `.csv` files.

## 🚀 Project Summary

- 📂 Recursively searches the `data/` folder for `.json` files.
- 📉 Flattens nested JSON structures (e.g. GeoJSON-style coordinate points).
- 📄 Outputs one CSV per JSON file, preserving headers and structure.

## 🛠️ Technologies Used

- Python 3
- `glob` for file searching
- `json` for parsing
- `csv` for writing
- Docker for packaging

## 📦 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/json-to-csv-ragged-dir.git
cd json-to-csv-ragged-dir
docker build --tag=exercise-4 .
docker-compose up
