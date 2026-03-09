# COP 2373 Programming Exercise
# Program that validates a phone number, social security number, and zip code
# using regular expressions.

import re


# ---------------------------------------------------------
# Function: validate_phone
# Checks if the phone number matches common US formats
# ---------------------------------------------------------
def validate_phone(phone):
    # regex for formats like 123-456-7890 or (123) 456-7890
    pattern = r"^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$"

    if re.match(pattern, phone):
        return True
    else:
        return False


# ---------------------------------------------------------
# Function: validate_ssn
# Checks if SSN is in the format 123-45-6789
# ---------------------------------------------------------
def validate_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"

    if re.match(pattern, ssn):
        return True
    else:
        return False


# ---------------------------------------------------------
# Function: validate_zip
# Checks for a 5 digit zip or zip+4 format
# ---------------------------------------------------------
def validate_zip(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"

    if re.match(pattern, zip_code):
        return True
    else:
        return False


# ---------------------------------------------------------
# Function: run_tests
# Runs a few sample tests to show valid and invalid inputs
# ---------------------------------------------------------
def run_tests():

    print("\n--- Testing Examples ---")

    # phone tests
    phone_tests = ["123-456-7890", "(813) 555-1234", "1234567890"]

    for p in phone_tests:
        print("Phone:", p, "Valid:", validate_phone(p))

    # ssn tests
    ssn_tests = ["123-45-6789", "111223333"]

    for s in ssn_tests:
        print("SSN:", s, "Valid:", validate_ssn(s))

    # zip tests
    zip_tests = ["33563", "90210-1234", "123"]

    for z in zip_tests:
        print("Zip:", z, "Valid:", validate_zip(z))


# ---------------------------------------------------------
# Main function
# Gets user input and displays results
# ---------------------------------------------------------
def main():

    print("Data Validation Program\n")

    # get user input
    phone = input("Enter a phone number (ex: 123-456-7890): ")
    ssn = input("Enter a social security number (ex: 123-45-6789): ")
    zip_code = input("Enter a zip code (ex: 12345 or 12345-6789): ")

    print("\n--- Validation Results ---")

    # check phone
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is NOT valid.")

    # check ssn
    if validate_ssn(ssn):
        print("SSN is valid.")
    else:
        print("SSN is NOT valid.")

    # check zip
    if validate_zip(zip_code):
        print("Zip code is valid.")
    else:
        print("Zip code is NOT valid.")

    # run additional tests
    run_tests()


# run program
if __name__ == "__main__":
    main()