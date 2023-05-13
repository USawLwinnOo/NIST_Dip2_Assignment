class Voting:
    def __init__(self):
        print("Working in Voting special method or constructor ")
        self.students = {0: {"name": "James", "v_mark": 0, "voter": []},
                         1: {"name": "John", "v_mark": 0, "voter": []},
                         2: {"name": "Rooney", "v_mark": 0, "voter": []},
                         3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                         4: {"name": "Messi", "v_mark": 0, "voter": []}
                         }
        self.db: dict = {}
        self.id: int = 0
        self.l_id: int = 0
        self.points: int = 0

    def main_option(self):
        option = 0
        try:
            option = int(input("Press 1 to Register\nPress 2 to Login\nPress 3 to Exit"))
        except Exception as err:
            # print(err)
            print("Pls insert only Integer eg:1,2,3")

        if option == 1:
            self.register()
            self.storing_data()
        elif option == 2:
            self.login()
            self.storing_data()
        elif option == 3:
            self.storing_data()
            exit(1)
        else:
            print("Invalid Option")
            self.main_option()

    def register(self):
        print("This is register option ")
        pass_match = False
        try:
            r_email = input("Enter your email address to register!")
            r_name = input("Enter your name to register!")
            r_phone = input("Enter your phone to register!")
            r_address = input("Enter your address:")
            r_money = input("Enter Your Money!")

            while pass_match is False:
                r_pass1 = input("Enter your password to register!")
                r_pass2 = input("Retype your password:")

                if r_pass1 != r_pass2:
                    print("Your passwords not match")

                else:
                    print("Your passwords was recorded!")
                    self.id = len(self.db)
                    data_form: dict = {self.id: {"email": r_email, "name": r_name, "phone": r_phone,
                                                 "address": r_address, "password": r_pass1, "money": r_money}}

                    self.db.update(data_form)

                    pass_match = True
        except Exception as err:
            print("Invalid User Input!Try Again Sir!")
            self.register()

        print("Registration success :", self.db[self.id]["name"])

        r_option = False
        while r_option is False:
            try:
                user_option = int(input("Press 1 to Login!\nPress 2 Main Option:\nPress3 to Exit!:"))
                if user_option == 1:
                    self.login()
                    break
                elif user_option == 2:
                    self.main_option()
                    break
                elif user_option == 3:
                    exit(1)
                else:
                    print("Pls read again for option!")

            except Exception as err:
                print("Invalid Input!", err)

    def login(self):
        print("This is login option ")
        length = len(self.db)
        try:
            l_email = input("Enter your email to Login:")
            l_pass = input("Enter your pass to Login:")
            self.l_id = -1
            for i in range(length):
                if l_email == self.db[i]["email"] and l_pass == self.db[i]["password"]:
                    self.l_id = i
                    break
            if self.l_id != -1:
                self.user_sector(self.l_id)
                print("Username or Password incorrect!")
                self.login()

        except Exception as err:
            print(err, "\nInvalid input:")

    def buy_points(self, l_id):

        money = int(self.db[l_id]["money"])
        print(f"Your total amount is ${money}.Buy some points to vote.")

        try:
            points = int(input("1 point cost $50. Please enter amount of point to buy :"))
            balance = money - (50 * points)
            if money < (50 * points):
                print("Not insufficient balance")

            elif money > (50 * points):
                print(f"You have {points} points and balance is ${balance}")

            else:
                print(f"You have {points} points and balance is $0")
            self.points += points
            self.db[l_id]["money"] = balance

        except Exception as err:
            print(err, "\n Invalid input!")

    def user_sector(self, l_id):
        print("Welcome", self.db[l_id]["name"])

        try:
            print(f"You have {self.points} points to vote")

            if self.points == 0:
                print("No points.Buy again!")
                print("Yor balance is ${}.".format(self.db[l_id]["money"]))
                opt = int(input("Press 1 to Buy: \nPress 2 to Force Quit:"))
                if opt == 1:
                    self.buy_points(self.l_id)
                else:
                    self.storing_data()
                    exit(1)

            else:
                print("Please select one!")

                for i in range(len(self.students)):
                    print("Id:{} - Name {} - Current Vote Mark: {}".format(i, self.students[i]["name"],
                                                                           self.students[i]["v_mark"]
                                                                           ))

                v_id = int(input("Just Enter Id number to vote:"))

                self.students[v_id]["v_mark"] += 1
                self.points -= 1
                self.students[v_id]["voter"].append(self.db[l_id]["name"])

                print("Congratulation you are voted!")
                print("{} now voting mark is : {}".format(self.students[v_id]["name"], self.students[v_id]["v_mark"]))

                for i in range(len(self.students[v_id]["voter"])):
                    print("Voter: ", self.students[v_id]["voter"][i])

        except Exception as err:
            print(err)

        while True:
            try:
                vote_option = int(input("Press 1 to Vote Again!\nPress 2 to get Main Option!\nPress 3 to Force Quit:"))

                if vote_option == 1:
                    self.user_sector(self.l_id)
                    break
                elif vote_option == 2:
                    self.main_option()
                    break
                elif vote_option == 3:
                    self.storing_data()
                    exit(1)

                else:
                    print("Invalid option after vote!")
            except Exception as err:
                print(err)

    def storing_data(self):
        with open("db.txt", 'w') as file:
            use_data = ""
            for i in range(len(self.db)):
                email = self.db[i]["email"]
                name = self.db[i]["name"]
                phone = self.db[i]["phone"]
                address = self.db[i]["address"]
                password = self.db[i]["password"]
                use_data += f"{i} {email} {name} {phone} {address} {password}+"
            vote_data = ""
            for a in range(len(self.students)):
                voter = self.students[a]["voter"]
                vote_data += str(f"{a} {voter} ")
            file.write(use_data)
            file.write(vote_data)

