#This code takes the user's name and prints out its initials. This code was created by Julian.

full_name = str(input("Please type your full name: "))
user_initials = full_name[0]

for i in range(len(full_name)):
    if full_name[i] == " ":
        user_initials = user_initials + full_name[i+1]

user_initials = user_initials.upper()
print ("Initials: " + user_initials)
