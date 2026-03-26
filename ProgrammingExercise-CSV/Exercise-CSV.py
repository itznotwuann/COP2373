import csv


# Function to create the grades.csv file
def create_grades_file():
    # Ask instructor how many students
    num_students = int(input("How many students do you want to enter? "))

    # Open file in write mode
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student
        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write student record to CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv file has been created.\n")


# Function to read and display the CSV file
def display_grades():
    # Open file in read mode
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        print("\nStudent Grades:\n")

        # Print each row in table format
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


# Main function to run program
def main():
    create_grades_file()
    display_grades()


# Run the program
main()