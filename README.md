Daikibo Telemetry Data Processing Project
📌 Project Title

Daikibo Telemetry Data Preparation for Tableau Analysis

🎯 Project Objective

This project processes raw JSON telemetry data and converts it into a structured CSV format suitable for visualization and analysis in Tableau.

The script also creates a calculated measure called Unhealthy to track device health duration.

🛠️ Technologies Used

Python 3

Pandas

JSON module

Tableau (for visualization)

📂 Project Files

daikibo-telemetry-data.json → Raw telemetry data

data_processing.py → Python script for processing data

daikibo_telemetry_prepared.csv → Output file for Tableau

README.md → Project documentation

⚙️ How the Script Works

Loads telemetry data from a JSON file.

Converts nested JSON data into a structured Pandas DataFrame.

Creates a new calculated column called Unhealthy:

If device status = "unhealthy" → assigns 10 minutes

Otherwise → assigns 0 minutes

Exports the cleaned dataset into a CSV file.

The CSV file can be imported directly into Tableau.

🧮 Business Logic

For every device record:

If status = unhealthy

Then Unhealthy = 10

Else Unhealthy = 0

This allows calculation of total unhealthy duration per:

Factory

Device Type

Time Period

▶️ How to Run the Project
Step 1: Install Required Library
pip install pandas
Step 2: Run the Script
python data_processing.py
Step 3: Output

The file below will be generated:

daikibo_telemetry_prepared.csv
📊 Tableau Usage

Open Tableau.

Connect to Text/CSV file.

Select daikibo_telemetry_prepared.csv.

Use the Unhealthy column to create:

Total unhealthy time

Factory-wise analysis

Device-type analysis

🚀 Future Improvements

Add error handling for missing fields

Automate unhealthy duration calculation based on timestamps

Deploy as automated data pipeline

Add dashboard templates

👤 Author

Faruk M
