#You are tasked with creating a function that generates a user login. The function receives a firstName (string), a lastName (string), and a userID (integer).
#The login format is as follows:
#The first three letters of the firstName.
#The first three letters of the lastName.
#The last two digits of the userID.
#The entire login must be in lowercase. If a name has fewer than three letters, use the entire name.

def func(firstname, lastname, userid):
    needed = ""
    short_needed = ""
    if len(firstname) >= 3:
        needed = firstname[0:2].lower() + lastname[0:2].lower() + str(userid)[-2:]
        print(needed)
    elif len(firstname) < 3:
        short_needed = firstname.lower + lastname[0:2].lower( ) + str(userid)[-2:]
        print(short_needed)

func(firstname = "Michael", lastname = "Scott", userid = 1965)