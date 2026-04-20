import csv
import numpy as np


# Function to load exam grades from grades.csv into a numpy array
def load_grades(filename):
    exam_data = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            # Store only the exam grades (columns 2, 3, and 4)
            exam_scores = [int(row[2]), int(row[3]), int(row[4])]
            exam_data.append(exam_scores)

    return np.array(exam_data)


# Function to display the first few rows of the dataset
def display_first_rows(data, num_rows=5):
    print("\nFirst few rows of the dataset:")
    print(data[:num_rows])


# Function to calculate and print statistics for each exam
def exam_statistics(data):
    print("\nStatistics for Each Exam:\n")

    for i in range(data.shape[1]):
        exam_column = data[:, i]

        print(f"Exam {i + 1}")
        print(f"Mean: {np.mean(exam_column):.2f}")
        print(f"Median: {np.median(exam_column):.2f}")
        print(f"Standard Deviation: {np.std(exam_column):.2f}")
        print(f"Minimum: {np.min(exam_column)}")
        print(f"Maximum: {np.max(exam_column)}")

        passed = np.sum(exam_column >= 60)
        failed = np.sum(exam_column < 60)

        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print()


# Function to calculate and print overall statistics for all exams combined
def overall_statistics(data):
    all_grades = data.flatten()

    print("\nOverall Statistics for All Exams Combined:\n")
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades)}")
    print(f"Maximum: {np.max(all_grades)}")

    total_passed = np.sum(all_grades >= 60)
    total_grades = len(all_grades)
    pass_percentage = (total_passed / total_grades) * 100

    print(f"Overall Pass Percentage: {pass_percentage:.2f}%")


# Main function to run the program
def main():
    filename = "../ProgrammingExercise-12/grades.csv"

    try:
        grades_array = load_grades(filename)

        display_first_rows(grades_array)
        exam_statistics(grades_array)
        overall_statistics(grades_array)

    except FileNotFoundError:
        print("Error: grades.csv was not found.")
        print("Make sure your grades.csv file is in the same folder as this program.")

    except ValueError:
        print("Error: The CSV file contains invalid grade data.")


# Run the program
main()