db = {}

email_exit = -1


def main_sector():
    main_option = int(input("Press 1 to Register:\nPress 2 to Login\nPress 3 Exit:"))

    if main_option == 1:
        registration()
    elif main_option == 2:
        login()
    elif main_option == 3:
        recording_all_data()
        exit(1)
    else:
        print("Invalid Option")
        main_sector()


def registration():
    user_email = input("Enter your email:")
    email_get = Email_exit(user_email)

    if email_get != None:
        print("Email already exit:")
        registration()
    else:
        user_name = input("Enter your username:")
        user_password = input("Enter your password:")
        user_phone = int(input("Enter your phone:"))
        user_age = int(input("Enter your age:"))

        id = len(db)

        to_insert = {id: {"email": user_email, "u_name": user_name, "password": user_password, "phone": user_phone,
                          "age": user_age}}
        db.update(to_insert)


def login():
    user_found = -1
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")

    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"] == l_user_password:
            user_found = i
    if user_found != -1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("Not Found ")


def user_profile(user_found):
    print("Welcome:", db[user_found]["u_name"])

    option = int(input("Press 1 to exit:\nPress 2 to update user information:"))
    if option == 1:
        recording_all_data()
    elif option == 2:
        update_information(user_found)
    else:
        user_profile(user_found)


def Email_exit(email):
    lenght = len(db)
    for i in range(lenght):
        if db[i]["email"] == email:
            return i


def recording_all_data():

    data = ""
    for key, value in db.items():
        data += f"{key}: {value}\n"
    with open("nistdb.txt", 'w') as file:
        file.write(data)


def loading_all_data():
    with open("nistdb.txt", 'r') as file:
        for line in file:
            key = int(line[0])
            value = line[2:].strip()
            db[key] = eval(value)


def update_information(i):
    options = int(input("1 to update email\n2 to update user name\n3 to change password\n4 to chane phone number: "))
    if options == 1:
        mail = input("Enter email: ")
        db[i]["email"] = mail
        recording_all_data()
        print(f"Success! Your new mail is ", db[i]["email"])
    elif options == 2:
        usr_name = input("Enter user name: ")
        db[i]["uname"] = usr_name
        recording_all_data()
        print(f"Success! Your new user name is ", db[i]["uname"])
    elif options == 3:
        passwd = input("Enter password: ")
        db[i]["password"] = passwd
        recording_all_data()
        print(f"Success! Your new password is ", db[i]["password"])
    elif options == 4:
        phone_no = input("Enter phone number: ")
        db[i]["phone"] = phone_no
        recording_all_data()
        print(f"Success! Your new phone number is ", db[i]["email"])
    else:
        print("Invalid Options")
        update_information(i)


if __name__ == '__main__':
    loading_all_data()
    print(db)
    while True:
        try:
            main_sector()
        except ValueError:
            print("Not Character!!!\nPlease enter integer number.\n")
