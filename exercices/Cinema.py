# You are building a seat reservation system for a small cinema. 
# Each seat is identified by a tuple (row, number) — for example ("A", 5) or ("C", 8). The cinema has 4 rows (A, B, C, D) and 8 seats per row. 
# The program runs in the terminal with a menu.
# Requirements:
# Store all bookings in a dictionary where the key is a seat tuple (row, number) and the value is the guest's name.
# The seating plan displays a grid of the cinema, marking booked seats with [X] and free ones with [ ].
# Booking asks for a row, a seat number, and a guest name. Reject the booking if the seat is already taken or doesn't exist.
# Cancelling asks for a row and seat number, and removes the booking if it exists.
# Search by name finds all seats booked under a given name (a guest could book multiple seats).
# Available seats lists all free seat tuples in order.

class Cinema:
    def __init__(self):
        self.booking = {}
        self.rows = ['A', 'B', 'C', 'D']
        self.seats_per_row = 8

    def display_seating_plan(self):
        print("Seats Plan:")
        for row in self.rows:
            row_display = f"{row}"
            for seat in range(1, self.seats_per_row + 1):
                if (row, seat) in self.booking:
                    row_display += " [X]"
                else: 
                    row_display += " [ ]"
            print(row_display)
    
    def book_a_seat(self, row, seat_nr, name):
        if (row, seat_nr) in self.booking:
            print("The seat is already taken")
        elif row not in self.rows or seat_nr < 1 or seat_nr > self.seats_per_row:
            print("Error: Seat doesn't exist")
        else:
            self.booking[(row, seat_nr)] = name
            print(f"Seat {row}-{seat_nr} successfully booked for {name}")
    
    def cancel_booking(self, row, seat_nr):
        if (row, seat_nr) in self.booking:
            del self.booking[(row, seat_nr)]
            print(f"Booking for seat {row}-{seat_nr} has been cancelled")
        else:
            print("Error: No booking found for that seat")

    def search_by_name(self, name):
        booked_seats = [seats for seats, guest in self.booking.items() if guest == name]
        if booked_seats:
            print(f"Seats booked for {name}: {booked_seats}")
        else: 
            print(f"No reservations found for {name}")

    def available_seats(self):
        free_seats = [(row, seat_nr) for row in self.rows for seat_nr in range(1, self.seats_per_row + 1) if (row, seat_nr) not in self.booking]
        print(f"Available seats: {free_seats}")

    def display_menu(self):
        while True:
            print("\nMenu:")
            print("1. Display seating plan")
            print("2. Book a seat")
            print("3. Cancel a booking")
            print("4. Search by name")
            print("5. Available seats")
            print("6. Exit")
            
            choice = int(input("Select an option: "))

            match choice:
                case 1:
                    self.display_seating_plan()
                case 2: 
                    self.book_a_seat(input("Enter row (A-D): ").upper(), int(input("Enter seat number (1-8): ")), input("Enter your name: "))
                case 3:
                    self.cancel_booking(input("Enter row (A-D): ").upper(), int(input("Enter seat number (1-8): ")))
                case 4:
                    self.search_by_name(input("Enter guest name: "))
                case 5:
                    self.available_seats()
                case 6:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option. Please try again.")
        
    def main(self):
        self.display_menu()

if __name__ == "__main__":
    cinema = Cinema()
    cinema.main()
        
