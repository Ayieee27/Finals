from utils.user import User as user
from utils.dice_game import DiceGame

account = []

class UserManager:
    @staticmethod
    def load_users(username, password):
        if UserManager.validate_username(username) and UserManager.validate_password(password):
            DiceGame.menu(username)
        else:
            print("Invalid Login Credentials.")

    @staticmethod
    def save_users(username, password):
        account.append(user(username, password))
        print("Registered Successfully!")

    @staticmethod
    def validate_username(username):
        for users in account:
            if users.username == username:
                return True
        return False

    @staticmethod
    def validate_password(password):
        for users in account:
            if users.password == password:
                return True
        return False

    def register(self):
        username = None
        password = None
        print("\nRegister an Account!")
        while True:
            username = input("Username: ")
            if len(username) == 0:
                break
            elif len(username) < 4:
                print("Username must be at least 4 characters long.")
            else:
                break
        while True:
            password = input("Password: ")
            if len(password) == 0:
                return
            elif len(password) < 8:
                print("Password must be at least 8 characters long.")
            else:
                break
        UserManager.save_users(username, password)

    def login(self):
        while True:
            if len(account) == 0:
                print("Register first!")
                break
            else:
                print("\nLogin to an Account!")
                username = input("Username: ")
                password = input("Password: ")
                UserManager.load_users(username, password)
                break

    @staticmethod
    def count_of_account():
        size = len(account)
        if size <= 0:
            print("Empty")
        else:
            print(size)