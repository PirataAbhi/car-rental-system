#importing datetime for date and time
import datetime

#this will display welcome message for user
def banner():
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("                                            Welcome to the bike management system")
    print("------------------------------------------------------------------------------------------------------------------------------------")

#this will create 2D list
def bike_2D_List():
    read_file = open("file.txt", "r")
    my_list = [] 
    for i in read_file:
        i = i.replace("\n", "")
        my_list.append(i.split(","))       
    return my_list

#this will show the bike details in table
def show_the_bike():
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Bike ID \t Bike-Name \t\t Company Name \t\t Colour \t\tQuantity \tPrice")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    file = open("file.txt", "r")
    a = 1
    for line in file:
        print(a, "\t\t"+line.replace(",", "\t\t"))
        a = a+1
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    file.close()

#this will ask user to input the bike id and check for validation    
def bike_id():
    show_the_bike()
    status = True
    while status:
        try:
            valid_bike_id = int(input("Enter the ID of the bike you want to buy: "))
            while valid_bike_id <= 0 or valid_bike_id > len(bike_2D_List()):
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Please provide a valid Bike ID")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
                print("\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                valid_bike_id = int(input("Enter the ID of the bike you want to buy: "))
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
            return valid_bike_id
        except ValueError:
            print("\n")
            print("--------------------------------------------------------------------------------------------")
            print("                          please input as suggested.")
            print("--------------------------------------------------------------------------------------------")
            print("\n")

#this will ask user to input the quantity of bike and check for validation
def valid_bike_quantity(motor_bike_id):
    item_list = bike_2D_List()
    print("\n")
    status = True
    while status:
        try:
            valid_quantity = int(input("Enter the quantity of the bike you want: "))
            while valid_quantity <=0 or valid_quantity > int(item_list[motor_bike_id-1][3]):
                print("\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Invalid input or The bike is currently out of stock.")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
                show_the_bike()
                print("\n")
                print("\n")
                valid_quantity = int(input("Enter the quantity of the bike you want: "))
                print("\n")
            print("\n")
            return valid_quantity
        except ValueError:
            print("\n")
            print("--------------------------------------------------------------------------------------------")
            print("                          please input as suggested.")
            print("--------------------------------------------------------------------------------------------")
            print("\n")

#this will calculate the total cost for the customer
def total_bike_cost(motor_bike_id,the_bike_quantity):
    bike_list = bike_2D_List()
    total_cost = int(bike_list[motor_bike_id-1][4].replace("$",""))* the_bike_quantity
    return total_cost

#this will update the stock
def update_the_stock(bike_list):
    file = open("file.txt", "w")
    for i in bike_list:
        file.write(str(i[0]) +","+ str(i[1]) +","+ str(i[2])+"," + str(i[3]) + "," + str(i[4])+ "\n")
    file.close()
    show_the_bike()

#this will update the quantity of the bike
def final_list_after_sell(motor_bike_id,the_bike_quantity):
     bike_list = bike_2D_List()
     bike_list[motor_bike_id-1][3] = int(bike_list[motor_bike_id-1][3]) - the_bike_quantity   
     update_the_stock(bike_list)
     print("--------------------------------------------------------------------------------------------")
     print("                          Bike has been succesfully sold.")
     print("--------------------------------------------------------------------------------------------")
     print("\n")

#this will display the bill for customer
def customer_bill_display(customer_bill_file_name):
    customer_bill = open(customer_bill_file_name, "r")
    for line in customer_bill:
        print(line)

# this will ask cutomer details
def the_customer_detail():
    print("---------------------------------Customer Information---------------------------------------")
    #assking customer to enter personal information
    customer_name = input("Enter your full name: ")
    customer_address = input("Enter your address: ")
    customer_contactNumber = input("Enter your contact number: ")
    Customer_email = input("Enter you email address: ")
    customer_amount_paid = input("Enter the bike amount you want to pay: $")
    print("--------------------------------------------------------------------------------------------")
    return customer_name,customer_address,customer_contactNumber,Customer_email,customer_amount_paid

#this will create the customer bill
def customer_details(motor_bike_id,the_total_cost,the_bike_quantity,the_cus_deatail):
    #creating bill for customer
    bike_list = bike_2D_List()
    #another_bike_quantity(user_input,motor_bike_id,the_bike_quantity,the_cus_deatail)
    customer_name,customer_address,customer_contactNumber,Customer_email,customer_amount_paid = the_cus_deatail
    a = 1
    #remaning_amount = int(the_total_cost)- int(customer_amount_paid)
    customer_bike = str(bike_list[motor_bike_id-1][0])
    customer_bike_company = str(bike_list[motor_bike_id-1][1])
    customer_bike_color = str(bike_list[motor_bike_id-1][2])
    customer_bike_quantity = str(the_bike_quantity)
    customer_bike__price =str(the_total_cost)
    customer_bill_file_name = str(customer_name + customer_contactNumber + ".txt")
    with open(customer_bill_file_name,"w+") as f:
        f.write("---------------------------------------------------------------------------------------------------------------------\n")
        f.write("                                         Bike Management System\n")
        f.write("                                              Customer Bill\n")
        f.write("---------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n")
        date_and_time = datetime.datetime.now()
        f.write("Date: " + str(date_and_time) + "\n")
        f.write("Name: " + customer_name + "\n")
        f.write("Address: " + customer_address + "\n")
        f.write("Contact Number: " + customer_contactNumber + "\n")
        f.write("E-mail Address: " + Customer_email + "\n")
        f.write("Paid: " + str(customer_amount_paid) + "\n")
        #f.write("Due amount: $" + str(remaning_amount) + "\n" )
        f.write("---------------------------------------------------------------------------------------------------------------------\n")
        f.write("S.N. \t Bike-Name \t\t Company Name \t\t Colour \t\tQuantity \tPrice \n")
        f.write("---------------------------------------------------------------------------------------------------------------------\n")
        f.write(str(a) +"\t"+customer_bike+"\t\t"+customer_bike_company+"\t\t"+customer_bike_color+"\t\t"+customer_bike_quantity+"\t\t"+"$"+ customer_bike__price +"\n")
        f.write("---------------------------------------------------------------------------------------------------------------------\n")
    f.close()
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    #displaying the bill
    customer_bill_display(customer_bill_file_name)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        

#this will create bill for another bikes buyer want
def customer_second_bike_input(the_cus_deatail,motor_bike_id,the_bike_quantity,the_total_cost):
    bike_list = bike_2D_List()
    sn = 2
    customer_name,customer_address,customer_contactNumber,Customer_email,customer_amount_paid= the_cus_deatail
    customer_bike_1 = str(bike_list[motor_bike_id-1][0])
    customer_bike_company_1 = str(bike_list[motor_bike_id-1][1])
    customer_bike_color_1 = str(bike_list[motor_bike_id-1][2])
    customer_bike_quantity_1 = str(the_bike_quantity)
    customer_bike__price_1=str(the_total_cost)
    customer_bill_file_name = str(customer_name + customer_contactNumber + ".txt")
    with open(customer_bill_file_name,"a") as f:
        f.write(str(sn) +"\t"+customer_bike_1 +"\t\t"+customer_bike_company_1+"\t\t"+customer_bike_color_1+"\t\t"+customer_bike_quantity_1+"\t\t"+"$"+ customer_bike__price_1 +"\n")
        f.write("---------------------------------------------------------------------------------------------------------------------\n")
    f.close()

# this will add bike in a stock
def adding_bike_in_stock(motor_bike_id):
    bike_list = bike_2D_List()
    status = True
    while status:
        try:
            dealer_input = int(input("Enter the quantity of the bike you want add in a stock: "))
            while dealer_input <=0:
                print("\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Sorry please input atleast 1 bike.")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
                print("\n")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                dealer_input = int(input("Enter the quantity of the bike you want add in a stock: "))
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\n")
            bike_list[motor_bike_id-1][3] = int(bike_list[motor_bike_id-1][3]) + dealer_input   
            update_the_stock(bike_list)
            return dealer_input
        except ValueError:
            print("\n")
            print("--------------------------------------------------------------------------------------------")
            print("                          please input as suggested.")
            print("--------------------------------------------------------------------------------------------")
            print("\n")
        

#this function display the bill for dealer
def dealer_bill_display(dealer_bike_file_name):
    dealer_bill = open(dealer_bike_file_name, "r")
    for line in dealer_bill:
        print(line)

# asking dealer details
def the_dealer_details():
    print("---------------------------------Dealer Information---------------------------------------")
    #asking dealer to enter personal information
    dealer_name = input("Enter your full name: ")
    shipping_company_name = input("Enter the name of the shipping company: ")
    shipping_cost = input("Enter the shipping cost: $")
    dealer_address = input("Enter your address: ")
    dealer_contactNumber = input("Enter your contact number: ")
    dealer_email = input("Enter you E-mail address: ")
    print("--------------------------------------------------------------------------------------------")
    return dealer_name,shipping_company_name,shipping_cost,dealer_address,dealer_contactNumber,dealer_email

#this will create the bill for dealer
def dealer_details(motor_bike_id,the_dealer_cost,the_dealer_input,the_deal_detail):
    #creating bill for delear
    bike_list = bike_2D_List()
    dealer_name,shipping_company_name,shipping_cost,dealer_address,dealer_contactNumber,dealer_email = the_deal_detail
    a = 1
    dealer_bike = str(bike_list[motor_bike_id-1][0])
    dealer_bike_company = str(bike_list[motor_bike_id-1][1])
    dealer_bike_color= str(bike_list[motor_bike_id-1][2])
    dealer_bike_quantity = str(the_dealer_input)
    dealer_bike_price = str(the_dealer_cost)
    dealer_bike_file_name = str(dealer_name + dealer_contactNumber + ".txt")
    with open(dealer_bike_file_name, "w+") as file:
        file.write("---------------------------------------------------------------------------------------------------------------------\n")
        file.write("                                                 Bike Management System \n")
        file.write("                                                      Dealer Bill \n")
        file.write("---------------------------------------------------------------------------------------------------------------------\n")
        file.write("\n")
        date_and_time = datetime.datetime.now()
        file.write("Date: " + str(date_and_time) + "\n")
        file.write("Name: " + dealer_name + "\n")
        file.write("Shipping Company Name: " + shipping_company_name + "\n")
        file.write("Shipping Cost: $" + shipping_cost + "\n")
        file.write("Address: " + dealer_address+ "\n")
        file.write("Contact Number: " + dealer_contactNumber + "\n")
        file.write("E-mail Address: " + dealer_email + "\n")
        file.write("---------------------------------------------------------------------------------------------------------------------\n")
        file.write("S.N. \t Bike-Name \t\t Company Name \t\t Colour \t\tQuantity \tPrice \n")
        file.write("---------------------------------------------------------------------------------------------------------------------\n")
        file.write(str(a) +"\t"+dealer_bike+"\t\t"+dealer_bike_company+"\t\t"+dealer_bike_color+"\t\t"+dealer_bike_quantity+"\t\t"+"$"+ dealer_bike_price +"\n")
        file.write("---------------------------------------------------------------------------------------------------------------------\n")
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    #displaying dealer bill
    dealer_bill_display(dealer_bike_file_name)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


#this will calculate dealer total cost
def total_dealer_bike_cost(motor_bike_id,dealer_input):
    bike_list = bike_2D_List()
    x = int(bike_list[motor_bike_id - 1][4].replace("$", ""))
    dealer_total_cost = x * dealer_input
    print("\n")
    print("--------------------------------------------------------------------------------------------")
    print("                          Bike has been odered succesfully.")
    print("--------------------------------------------------------------------------------------------")
    return dealer_total_cost
