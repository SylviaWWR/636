# ============== Selwyn Campground MAIN PROGRAM ==============
# Student Name: Weiran Wang
# Student ID : buzhidao
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import camp_data    # camp_data.py MUST be in the SAME FOLDER as this file!
                    # camp_data.py contains the data
import datetime     # We are using date times for this assessment, and it is
                    # available in the column_output() function, so do not delete this line

# Data variables
#col variables contain the format of each data column and help display headings
#db variables contain the actual data
col_customers = camp_data.col_customers
db_customers = camp_data.db_customers
col_bookings = camp_data.col_bookings
db_bookings = camp_data.db_bookings
UNPS = camp_data.UNPS #list of unpowered sites
PS = camp_data.PS #list of powered sites


def next_id(db_data):
    #Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys())+1

def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['name'],
                             db_customers[customer]['phone'],
                             db_customers[customer]['email']))
    format_columns = "{: >4} | {: <18} | {: <15} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    column_output(display_list, col_customers, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output



def list_campsites():
    # List the ID, name, occupancy
    col_name_phone = {"First Name":str,"Last Name":str,"Phone":str}
    db_name_phone = []
    for passenger in db_passengers:
        db_name_phone.append((passenger[1],passenger[2],passenger[4]))
    print()
    column_output(db_name_phone,col_name_phone,"{: <10}  {: <10}  {: <15}")

def list_campers_by_date():
    # List the Date, name, site, occupancy
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_customer():
    # Add a customer to the db_customers database, use the next_id to get an id for the customer.
    # Remember to add all required dictionaries.
    
    # TODO
    # Know the type, columns of a customer
    # e.g. 1660(this is id):{'name':"Heidi",'email':"HDelaney@gmail.com",'phone':"(028) 294-2819"}
    # Get the value of each column from user's input
    # ...
    # For ID column, use next_id to get one
    # id = ?
    # Validate input value
    # Add to db
    db_data_customer = camp_data.db_customers
    print("==== Add Customer ===")
    # Input and validate name
    name = input("Please input your name: ")
    while name == "":
        name = input("Name cannot be empty, please re-enter your name: ")
    # Input and validate email
    email = input("Please input your email: ")
    emailValid = "@" in email
    while not emailValid:
        email = input("Looks like you've input an invalid email. " 
                      "Please re-enter: ")
        emailValid = "@" in email
    # Input and validate phone_number_area_code
    phone_number_area_code = input("Please input your phone number area code: ")
    areaCodeValid = (len(phone_number_area_code) > 0 and 
                     len(phone_number_area_code) < 4 and 
                     phone_number_area_code.isdigit())
    while not areaCodeValid:
        phone_number_area_code = input("Looks like you've input an invalid area code. " 
                                       "Please re-enter your area code (up to 3 digit): ")
        areaCodeValid = (len(phone_number_area_code) > 0 and 
                         len(phone_number_area_code) < 4 and 
                         phone_number_area_code.isdigit())
    # Input and validate phone_number
    phone_number = input("Please input your phone number: ")
    phoneNumberValid = len(phone_number) == 7 and phone_number.isdigit()
    while not phoneNumberValid:
        phone_number = input("Looks like you've input an invalid phone number. "
                             "Please re-enter your 7 digit phone number: ")
        phoneNumberValid = len(phone_number_area_code) < 4 and phone_number_area_code.isdigit()
    # Write the entry to customer dictionary
    db_data_customer[next_id(camp_data.db_customers)] = { 'name': name, 'email': email, 'phone': "(" + phone_number_area_code + ") " + phone_number[:3] + '-' + phone_number[3:]}

def add_booking():
    # Add a booking
    # Remember to validate customer ids and sites

    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)



# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN CAMPGROUND ===")
    print(" 1 - List Customers")
    print(" 2 - List Campsites")
    print(" 3 - List Campers (Specific Date")
    print(" 4 - Add Customer")
    print(" 5 - Add Booking")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ").upper().strip()

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
while response != "X":
    if response == "1":
        list_customers()
    elif response == "2":
        list_campsites()
    elif response == "3":
        list_campers_by_date()
    elif response == "4":
        add_customer()
    elif response == "5":
        add_booking()
    else:
        print("\n***Invalid response, please try again (enter 1-5 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Campground Administration! ===\n")
