import datetime
import subprocess
import openpyxl

# Get the current time
now = datetime.datetime.now()

# Calculate the start time (one month ago)
start_time = now - datetime.timedelta(days=30)

# Format the start and end times as strings
start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
end_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Get the login history
login_history = subprocess.run(["net", "accounts"], capture_output=True).stdout.decode(
    encoding='cp1252').split("\n")


# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Add a new sheet
sheet = workbook.active
sheet.title = "Login History"

# Add the headings to the sheet
sheet["A1"] = "Username"
sheet["B1"] = "Date"
sheet["C1"] = "Time"
sheet["D1"] = "Action"

# Parse the login history and write the data to the sheet
row = 2
for entry in login_history:
    if "logon" in entry:  # If this is a logon entry
        username, _, _, _, date_str, time_str, _ = entry.split()  # Split the entry into parts
        # Combine the date and time strings
        date_time_str = f"{date_str} {time_str}"
        date_time = datetime.datetime.strptime(
            date_time_str, "%m/%d/%Y %I:%M:%S %p")  # Parse the date and time
        if date_time >= start_time and date_time <= now:  # If the date and time is within the specified range
            sheet[f"A{row}"] = username
            sheet[f"B{row}"] = date_time.date()
            sheet[f"C{row}"] = date_time.time()
            sheet[f"D{row}"] = "Logon"
            row += 1
    elif "logoff" in entry:  # If this is a logoff entry
        username, _, _, _, date_str, time_str, _ = entry.split()  # Split the entry into parts
        # Combine the date and time strings
        date_time_str = f"{date_str} {time_str}"
        date_time = datetime.datetime.strptime(
            date_time_str, "%m/%d/%Y %I:%M:%S %p")  # Parse the date and time
        if date_time >= start_time and date_time <= now:  # If the date and time is within the specified range
            sheet[f"A{row}"] = username
            sheet[f"B{row}"] = date_time.date()
            sheet[f"C{row}"] = date
            sheet[f"D{row}"] = "Logoff"
            row += 1

# Save the workbook
workbook.save("login_history.xlsx")
