from datetime import datetime

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
event_year = input("Enter event year: ")
event_month = input("Enter event month: ")
event_day = input("Enter event day: ")

# String cleaning (Version 2)
cleaned_first = first_name.strip()
cleaned_last = last_name.strip()
cleaned_section = section.strip()
cleaned_event = event_name.strip()

proper_full_name = f"{cleaned_first} {cleaned_last}".title()
uppercase_full_name = f"{cleaned_first} {cleaned_last}".upper()
uppercase_section = cleaned_section.upper()
clean_event_name = cleaned_event.title()

# Date formatting using datetime (Version 3)
try:
    year_int = int(event_year.strip())
    day_int = int(event_day.strip())
    month_input = event_month.strip()
    
    if month_input.isdigit():
        month_int = int(month_input)
        event_date_obj = datetime(year_int, month_int, day_int)
    else:
        event_date_obj = datetime.strptime(f"{month_input} {day_int}, {year_int}", "%B %d, %Y")
        
    readable_date = event_date_obj.strftime("%B %d, %Y").replace(" 0", " ")
except ValueError:
    readable_date = f"{event_month} {event_day}, {event_year}"

# Required Output Summary
print("\nStudent Event Registration Summary")
print(f"Name: {proper_full_name}")
print(f"Name Code: {uppercase_full_name}")
print(f"Section: {uppercase_section}")
print(f"Event: {clean_event_name}")
print(f"Event Date: {readable_date}")
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")