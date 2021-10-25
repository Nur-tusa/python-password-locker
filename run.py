from locker import User, Credentials

def function():
    # print("PASSWORD LOCKER APP") 
    function()

#1.creat new user
def create_new_users(username,password):
    """
    Function to create a new user with a username and password
    """
    new_user = User(username,password)
    return new_user
#2.save new user
def save_user(user):
    """
    Function to save a new user
    """
    return user.save_user()
    #3.display the users
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
    #4.login user
def login_user(username,password):
    """
    function that checks whether a user exist .
    """
  #credentials 
    check_user = Credentials.verify_user(username,password)
    return check_user
 #5.creat new credential
def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for  user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
    #6.save new credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    return credentials. save_details()
    #7.display credential
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()
#   8.delet credential
def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    return credentials.delete_credentials()
#   9.find credential
def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
    # 10.check credentials
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)



def copy_password(account):
    """
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

def passlocker():
    print("PASSWORD LOCKER APP")


    print("Hello Welcome to your Accounts' Password Store...\n Please enter one of the following to proceed to next step and use lowrcase(smallletters).\n ca ---  Create New Account for password-locker \n li ---  Have An existing Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("fill this questions below to register")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" CR - creat your  own pasword:\n")
            password_Choice = input().lower().strip()
            if password_Choice == 'cr':
                password = input("Enter Password\n")
                break

            else:
                print("Invalid password please check properly")
        save_user(create_new_users(username,password))
        print("*" * 100)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*" * 100)
    elif short_code == "li":
        print("*" * 100)
        print("Enter your User name and your Password to log in:")
        print('*' * 100)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes to navigate and use lowercase :\n CC - Create  credential \n DC - Display Credentials \n FC - Find  credential \n  D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("." * 20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
             
                else:
                    print("Invalid password please check properly")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully!")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of accounts: ")
                 
                print('*' * 100)
                print('_' * 100)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_' * 100)
                print('*' * 100)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 100)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 100)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*100)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist ")

        
        elif short_code == 'ex':
            print("Thanks for using passwords locker. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
            print("please enter correct in put to continue")

if __name__ == '__main__':
    passlocker()