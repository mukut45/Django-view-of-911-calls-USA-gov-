import pandas as pd
from django.shortcuts import render
import os

def top_zip_codes(request):
    # Load the dataset from the CSV file
    file_path = os.path.join(os.path.dirname(__file__), r"D:\Information Technology\Django projects\core\911.csv")  # Adjust path if needed sometime
    df = pd.read_csv(file_path)

    # Compute the top 10 zip codes
    top_zipcodes = df["zip"].value_counts().head(10).reset_index()
    top_zipcodes.columns = ["zip_code", "count"]
    print(top_zipcodes)
    
    # Convert DataFrame to a list of dictionaries for the template
    zip_data = top_zipcodes.to_dict(orient="records")
    return render(request, "calls/top_zip_codes.html", {"top_zipcodes": zip_data})

# Now, creating a home page view for "911 call data analysis"
def home(request):
    return render(request, 'calls/home.html')

# writing a view for the top township
def top_townships(request):
    file_path = os.path.join(os.path.dirname(__file__), r"D:\Information Technology\Django projects\core\911.csv")  # Adjust path if needed sometime
    df = pd.read_csv(file_path)
    top_4_township = df["twp"].value_counts().head(4)  # Get top 4 townships
    print(top_townships)
    township_data = top_4_township.to_dict()  # Convert to dictionary for template rendering

    return render(request, 'calls/top_townships.html', {'townships': township_data})

# writing a view for "most common resion"

def common_reason(request):
    file_path = os.path.join(os.path.dirname(__file__), r"D:\Information Technology\Django projects\core\911.csv")  # Adjust path if needed sometime
    df = pd.read_csv(file_path)
    df["Reason"] = df["title"].apply(lambda x: x.split(":")[0])  # Extract Reason
    common_reason = df["Reason"].value_counts()  # Count occurrences
    most_common = common_reason.idxmax()  # Most common reason
    reason_data = common_reason.to_dict()  # Convert to dictionary for template

    return render(request, 'calls/common_reason.html', {
        'most_common': most_common,
        'reasons': reason_data
    })

# Writing a view of EMS calls by day

def ems_calls_by_day(request):
    # Load the dataset (Ensure the path is correct)
    file_path = r"D:\Information Technology\Django projects\core\911.csv"
    df = pd.read_csv(file_path)

    # Extract Reason from the 'title' column
    df["Reason"] = df["title"].apply(lambda x: x.split(":")[0])  # Extracts 'Reason'

    # Convert 'timeStamp' to datetime format
    df["timeStamp"] = pd.to_datetime(df["timeStamp"])

    # Extract the day of the week
    df["DayOfWeek"] = df["timeStamp"].dt.day_name()

    # Filter for EMS calls
    ems_calls = df[df["Reason"] == "EMS"]

    # Count EMS calls by day
    calls_by_day = ems_calls["DayOfWeek"].value_counts().to_dict()

    return render(request, 'calls/ems_calls_by_day.html', {'calls_by_day': calls_by_day})

# Writing the view for the month with the maximum fire calls
def max_fire_calls_month(request):
    # Load the dataset (Ensure the file path is correct)
    file_path = r"D:\Information Technology\Django projects\core\911.csv"
    df = pd.read_csv(file_path)

    # Extract Reason from the 'title' column
    df["Reason"] = df["title"].apply(lambda x: x.split(":")[0])  

    # Ensure 'timeStamp' is in datetime format
    df["timeStamp"] = pd.to_datetime(df["timeStamp"])

    # Extract the month name
    df["Month"] = df["timeStamp"].dt.month_name()

    # Filter dataset for 'Fire' calls
    fire_calls = df[df["Reason"] == "Fire"]

    # Count Fire calls by month
    fire_calls_by_month = fire_calls["Month"].value_counts()

    # Find the month with the highest Fire calls
    max_fire_month = fire_calls_by_month.idxmax()  # Most fire calls occurred in this month
    max_fire_calls = fire_calls_by_month.max()  # Number of fire calls in that month

    return render(request, 'calls/max_fire_calls_month.html', {
        'max_fire_month': max_fire_month,
        'max_fire_calls': max_fire_calls
    })

def traffic_calls_map(request):
    # Define the path to your saved Folium map HTML file
    #map_file_path = os.path.join(os.path.dirname(__file__), 'templates/calls/Traffic_Calls_Map2.html')

    return render(request, 'calls/Traffic_Calls_Map2.html')  # Load existing map file