# You can Store anything in Dictionary
dictionary = {
    "name":"Ishan",
    "from":"Gujrat",
    "marks":[98,99,100],
    "age":17
}

# an Empty Dictionary
information = {}

# Entering some Information in Dictionary named infomration
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
place = input("Enter your Belong Place : ")

# Initializing entered Information from the dictionary named information
information["name"] = name
information["age"] = age
information["place"] = place

# Printing the inforamtion stored in information
print(information)

# Searching and Printing th information from the dictionary named information
search = '''
Enter what you want to Search :
1. Name
2. Age
3. Belonging Place
'''
print(search)

# Entering the choice from user that what he want to search from the dictionary name information
choice = input("Enter Search Item Here : ")

# printing the Choice that user entered to search
print(information[choice])
