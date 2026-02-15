# Function to ask the user how many tickets they want
def ask_tickets(remaining):
    # Prompt the user and return the number of tickets they want
    tickets = int(input(f"How many tickets do you want? (1-4) - {remaining} tickets left: "))
    return tickets

def main():
    tickets_left = 20  # total number of tickets available
    total_buyers = 0   # accumulator to count how many people bought tickets

    # Loop until all tickets are sold
    while tickets_left > 0:
        wanted = ask_tickets(tickets_left)  # ask the user how many tickets they want

        # Check if the requested number is valid (1-4)
        if wanted < 1 or wanted > 4:
            print("Sorry, you can only buy 1 to 4 tickets at a time.")
        # Check if there are enough tickets left
        elif wanted > tickets_left:
            print("Not enough tickets left for that many.")
        else:
            tickets_left -= wanted          # subtract purchased tickets from total
            total_buyers += 1               # add 1 to the buyers accumulator
            print(f"Thanks! Tickets remaining: {tickets_left}\n")  # show remaining tickets

    # All tickets are sold, show summary
    print("All tickets are sold out!")
    print(f"Total buyers: {total_buyers}")

# Run the program
main()
