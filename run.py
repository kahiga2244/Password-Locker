from Username import User
from Credentials import Credentials


# creating an account
def create_user(fname,sname,password):
    """
    function to create a new user account
    """
    new_user = User(fname,sname,password)
    return new_user

def create_app(app,app_password):
    """
    Function to create new app and password
    """
    new_app = Credentials(app,app_password)
    return new_app


# saving user and app
def save_user(user):
    """
    Function to save our user details
    """
    user.save_user()


def save_app(credentials):
    """
    Function to save new app details
    """
    credentials.save_app()


# delete user
def del_account(user):
    """
    Function that deletes a user account
    """
    user.delete_account()

def del_app(credentials):
    """
    Function that deletes app logged
    """
    credentials.delete_app()

# finding a user by first name
def find_user(first_name):
    """
    Function that finds user by their first name and returns their first name
    """
    return User.find_by_fname(first_name)


def find_app(app):
    """
    Function that finds an app
    """
    return Credentials.find_app(app)

# checking if a user exists
def user_existance(first_name):
    """
    Function that checks if a user exist and returns a boolean
    """
    return User.user_exist(first_name)

def app_existance(app):
    """
    Function that checks if an app exists and returns a boolean
    """
    return Credentials.app_exist(app)

# displaying users
def display_users():
    """
    Function that does actual display of users
    """
    return User.display_user()

def display_app():
    """
    Function that displays a list of apps saved
    """
    return Credentials.display_app()

def generate_password():
    """
    Function that generates random passwords
    """
    generate_password = Credentials.gen_password()
    return generate_password

## main function
def main():
    print("Welcome to Password Vault, to login please enter your name")
    user_name = input().upper()

    # print("Password:")
    # password = input()


    while True:            
        print("-"*5)
        print("Create App password using any of these short codes:\n 'OWN' to use your own password\n 'GP' to use generated password")

        password_choice = input().lower().strip()

        if password_choice == 'own':
                print("Enter your password")
                password = input().strip()
                break
        elif password_choice == 'gp':
                password = generate_password()
                break

        else :
                print("Please enter a valid password")

    
    print(f"Welcome {user_name}!")

    while True:
        print("Use this short codes: \nNC - to save new account credentials\n VC - to view credentials\n DEL - to delete credentials\nEXIT to leave app")

        short_code = input().upper()

        if short_code == 'NC':
            print("*"*100)
            print("New app Name:\n")
            app = input()

            while True:            
                print("-"*10)
                print("Enter App password:\n use short codes:\n'OWN' to use your own password\n 'GP' to use generated password\n 'EXIT'to exit")

                password = input().lower().strip()

                if password == 'own':
                        print("Enter your password")
                        app_password = input().strip()
                        break
                elif password == 'gp':
                        app_password = generate_password()
                        break

                else :
                        print("Please enter a valid password")


            save_app(create_app(app,app_password)) # create and save new app and password

            print(f"New {app} account created\n")
            print(f"Password: {app_password}")

        elif short_code == 'VC':
            if app_existance():
                print("Here is a list of your saved apps & their passwords")

                for credentials in display_app():
                    print(f"{credentials.app} - Password: {credentials.app_password}")
                else :
                    print("You have NO saved Apps")

        elif short_code == 'DEL':
            """
            Delete app credentials
            """
            print("Type in the app you want to delete")
            app = input()

            print("Confirm password")
            app_password = input()

            delete = credentials.delete_app()
            return delete
            
        elif short_code == 'EXIT':
            print("Successfully Logged out of Password Vault")
            break
        else :
            print("Please enter a valid short code?")
if __name__ == '__main__':
    main()