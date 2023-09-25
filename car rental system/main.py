import functions
#main function
def start():
    functions.banner()
    status = True
    while(status == True):
        print("\n")
        functions.show_the_bike()
        print("\n")
        print("1. To sell the bike.")
        print("2. To order the bike.")
        print("3. To exit")
        print("\n")
        try:
            user_input = int(input("Enter the value of the option: "))
            if (user_input == 1):
                motor_bike_id = functions.bike_id()
                the_bike_quantity = functions.valid_bike_quantity(motor_bike_id)
                the_cus_deatail = functions.the_customer_detail()
                functions.final_list_after_sell(motor_bike_id,the_bike_quantity)
                the_total_cost = functions.total_bike_cost(motor_bike_id,the_bike_quantity)
                functions.customer_details(motor_bike_id,the_total_cost,the_bike_quantity,the_cus_deatail)
                #this will ask user to buy more bikes and display suitable message as the buyer input message
                print("\n")
                continuation = input("Do you want to buy another one?? Press y for yes or n for no. ")
                if continuation == "y":
                    status = True
                    while status == True:
                        motor_bike_id = functions.bike_id()
                        the_bike_quantity = functions.valid_bike_quantity(motor_bike_id)
                        functions.final_list_after_sell(motor_bike_id,the_bike_quantity)
                        the_total_cost = functions.total_bike_cost(motor_bike_id,the_bike_quantity)
                        Customer_second_input= functions.customer_second_bike_input(the_cus_deatail,motor_bike_id,the_bike_quantity,the_total_cost)
                        continueAgain = input("Do you wish to continue again?? ")
                        if continueAgain == "n":
                            print("\n")
                            #functions.customer_details(motor_bike_id,the_total_cost,the_bike_quantity,the_cus_deatail)
                            print("\n")
                            print("--------------------------------------------------------------------------------------------")
                            print("                         Thank you for buying from us.")
                            print("--------------------------------------------------------------------------------------------")
                            print("\n")
                            print("------------------------------------------------------------------------------------------------------------------------------------")
                            print("------------------------------------------------------------------------------------------------------------------------------------")
                            break
                elif continuation == "n":
                    print("\n")
                    print("--------------------------------------------------------------------------------------------")
                    print("                         Thank you for buying from us.")
                    print("--------------------------------------------------------------------------------------------")
                    print("\n")
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                else:
                    print("--------------------------------------------------------------------------------------------")
                    print("                           Please input as suggested.")
                    print("--------------------------------------------------------------------------------------------")
                    
            elif(user_input == 2):
                motor_bike_id = functions.bike_id()
                the_deal_detail = functions.the_dealer_details()
                the_dealer_input= functions.adding_bike_in_stock(motor_bike_id)
                the_dealer_cost = functions.total_dealer_bike_cost(motor_bike_id,the_dealer_input)
                functions.dealer_details(motor_bike_id,the_dealer_cost,the_dealer_input,the_deal_detail)
            
            elif(user_input == 3):
                print("\n")
                print("--------------------------------------------------------------------------------------------------------------------------------")
                print("                                         Thank you for using our bike management system.")
                print("--------------------------------------------------------------------------------------------------------------------------------")
                status = False
            else:
                print("Invalid number.")
        except ValueError:
            print("--------------------------------------------------------------------------------------------")
            print("                           Please input as suggested.")
            print("--------------------------------------------------------------------------------------------")
start()
 

