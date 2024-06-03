import csv

def get_user_input(filename='responses.csv'):
    print("Welcome to the 2024MW Hotel Grouper!")
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    print("\nChoose the date block you are booking for (July 1-22, 2024):")
    dates = ['1-3', '4-6', '7-9', '10-12', '13-15', '16-18', '19-21']
    for idx, date in enumerate(dates, 1):
        print(f"{idx}. July {date}")

    date_choice = int(input("Enter your choice: "))
    selected_date = dates[date_choice - 1]

    print("\nEnter your top three hotel choices from the list (only names):")
    hotels = [
        "Motel 6", "Travelodge", "Super 8", "Microtel Inn & Suites",
        "Red Roof Inn", "Best Western", "Holiday Inn Express",
        "Hyatt Place", "Marriott Hotels", "Hilton Garden Inn", "Other"
    ]
    hotel_prices = {
        "Motel 6": "$60", "Travelodge": "$65", "Super 8": "$70", "Microtel Inn & Suites": "$75",
        "Red Roof Inn": "$80", "Best Western": "$100", "Holiday Inn Express": "$110",
        "Hyatt Place": "$120", "Marriott Hotels": "$130", "Hilton Garden Inn": "$140", "Other": "N/A"
    }
    for idx, hotel in enumerate(hotels, 1):
        print(f"{idx}. {hotel} ({hotel_prices[hotel]})")

    hotel_choices = []
    for i in range(1, 4):
        choice = int(input(f"Choice {i}: "))
        if choice == 11:  # Other option
            other_hotel = input("Enter the name of the other hotel: ")
            hotel_choices.append(other_hotel)
        else:
            hotel_choices.append(hotels[choice - 1])

    # Save the data to CSV
    save_data_to_csv(filename, [name, email, selected_date, hotel_choices])
    return {
        'name': name,
        'email': email,
        'dates': selected_date,
        'hotel_choices': hotel_choices
    }

def save_data_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def read_data_from_csv(filename='responses.csv'):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

def display_user_info(user_info):
    print("\nHere is the information you entered:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

def display_all_data():
    data = read_data_from_csv()
    if not data:
        print("No data available.")
        return
    
    print("\nAll collected data:")
    for row in data:
        print(f"Name: {row[0]}, Email: {row[1]}, Date: {row[2]}, Hotels: {row[3]}")

    print("\nSummary by hotel:")
    hotel_summary = {}
    for row in data:
        for hotel in row[3].strip("[]").replace("'", "").split(", "):
            if hotel in hotel_summary:
                hotel_summary[hotel]['count'] += 1
                hotel_summary[hotel]['dates'].append(row[2])
                hotel_summary[hotel]['names'].append(row[0])
            else:
                hotel_summary[hotel] = {
                    'count': 1,
                    'dates': [row[2]],
                    'names': [row[0]]
                }

    for hotel, details in hotel_summary.items():
        print(f"\nHotel: {hotel}")
        print(f"Selected {details['count']} times")
        print(f"Dates selected: {details['dates']}")
        print(f"Names: {details['names']}")

def main():
    user_info = get_user_input()
    display_user_info(user_info)
    display_all_data()

if __name__ == "__main__":
    main()
