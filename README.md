# ExcelToJson

This repository contains a Python script that converts an Excel file to a JSON file with each dictionary having an 'id' field. The script uses Pandas and Openpyxl libraries. The Excel file structure should have cells A1 and B1 containing the data that needs to be combined.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

1. Pandas
2. Openpyxl


You can install them using pip:
```bash
pip install pandas openpyxl


# Usage

clone and Run the script.


The script will convert the Excel data to a JSON file named output.json in your project directory. The JSON file will have the following characteristics:
Persian letters and UTF-8 encoding are supported.

The Excel data structure like this:
[excell structure](Screenshot.png "Optional tooltip")

Each dictionary in the JSON file will have an 'id' field, with a unique integer value assigned to it.