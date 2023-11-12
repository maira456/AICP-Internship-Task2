# Start of the day
journeys = {
       "09:00": {"up": 0, "down": 0, "revenue": 0},
       "12:00": {"up": 0, "down": 0, "revenue": 0},
       "14:00": {"up": 0, "down": 0, "revenue": 0},
       "15:00": {"up": 0, "down": 0, "revenue": 0}
}

# Purchase tickets
def purchase_tickets():
  print(""" Welcome to the ticket Purchase Station.
             Our Journey times:""")
  for journey_time in journeys.keys():
      print(journey_time)
  journey_time = input("Enter the journey time (in HH:MM format): ")
  num_passengers = int(input("Enter the number of passengers: "))

    # Check if the journey time is valid
  if journey_time not in journeys.keys():
        print("Invalid time.")
        return

  journey = journeys[journey_time]

    # Check if there are enough tickets available
  if num_passengers * 2 > 80 * 6:
        print("Not enough seats available.")
        return

    # Calculate the total price including group discount
  price_per_ticket = 25
  total_price = num_passengers * price_per_ticket

  if num_passengers >= 10 and num_passengers <= 80:
        free_tickets = num_passengers // 10
        total_price -= free_tickets * price_per_ticket

    # Update the screen display and the data for the totals
  journey["up"] += num_passengers
  journey["revenue"] += total_price
  
  print("Tickets purchased successfully.")
  print(f"Total amount paid: ${total_price}")

# End of the day report
def end_of_day():
    total_passengers = 0
    total_revenue = 0
    max_passengers = 0
    max_journey_time = ""

    print("End of the day report:")

    for journey_time, journey in journeys.items():
        total_passengers += journey["up"]
        total_revenue += journey["revenue"]

        print("Journey Time:", journey_time)
        print("Passengers:", journey["up"])
        print("Revenue collected:", journey["revenue"])
        print("---------------------------------")

        if journey["up"] > max_passengers:
            max_passengers = journey["up"]
            max_journey_time = journey_time

    print("Total passengers for the day:", total_passengers)
    print("Total revenue collected for the day: $", total_revenue)
    print("Journey with the most passengers:", max_journey_time, "with", max_passengers, "passengers.")

# Main execution
print("Start of the day.")



while True:
    ch = input("""1.Purchase Ticket 
    2.See the end day
    3.Quit(q)
    please enter code for your choice.   """)

    if ch == '1':
        purchase_tickets()
    elif ch == '2':
        end_of_day()
        break
    elif ch.lower() == 'q':
        break
    else:
        print("Invalid choice.")
