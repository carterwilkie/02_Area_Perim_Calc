def user_choice():

    valid = False
    while not valid:

        response = "File type (integer / text / image): ".lower()

        if response == "text" or response == "t":
            return response
        
        else
            print("Please choose a valid file type!")
            print()


data_type = user_choice()
print("You chose", data_type)

print()
