#!/usr/bin/env python3
import os
import shutil

def add_user(username, password):
    os.system(f"sudo useradd -m -p $(openssl passwd -1 {password}) {username}")
    print(f"User '{username}' added successfully.")

def modify_user(username, option, value):
    if option == "password":
        os.system(f"echo '{username}:{value}' | sudo chpasswd")
    elif option == "comment":
        os.system(f"sudo usermod -c '{value}' {username}")
    print(f"User '{username}' modified successfully.")

def delete_user(username):
    os.system(f"sudo userdel -r {username}")
    print(f"User '{username}' deleted successfully.")

def add_group(groupname):
    os.system(f"sudo groupadd {groupname}")
    print(f"Group '{groupname}' added successfully.")

def delete_group(groupname):
    os.system(f"sudo groupdel {groupname}")
    print(f"Group '{groupname}' deleted successfully.")

def list_groups():
    os.system("cut -d: -f1 /etc/group")

def disable_user(username):
    os.system(f"sudo usermod -L {username}")
    print(f"User '{username}' disabled successfully.")

def enable_user(username):
    os.system(f"sudo usermod -U {username}")
    print(f"User '{username}' enabled successfully.")

def change_password(username, new_password):
    os.system(f"echo '{username}:{new_password}' | sudo chpasswd")
    print(f"Password for '{username}' changed successfully.")

def user_info(username):
    os.system(f"getent passwd {username}")

# Example usage
if __name__ == "__main__":
    while True:
        print("\nLinux User and Group Management")
        print("1. Add User")
        print("2. Modify User")
        print("3. Delete User")
        print("4. Add Group")
        print("5. Delete Group")
        print("6. List Groups")
        print("7. Disable User")
        print("8. Enable User")
        print("9. Change User Password")
        print("10. User Info")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username to add: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif choice == "2":
            username = input("Enter username to modify: ")
            option = input("Enter option (password/comment): ")
            value = input("Enter new value: ")
            modify_user(username, option, value)
        elif choice == "3":
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == "4":
            groupname = input("Enter group name to add: ")
            add_group(groupname)
        elif choice == "5":
            groupname = input("Enter group name to delete: ")
            delete_group(groupname)
        elif choice == "6":
            list_groups()
        elif choice == "7":
            username = input("Enter username to disable: ")
            disable_user(username)
        elif choice == "8":
            username = input("Enter username to enable: ")
            enable_user(username)
        elif choice == "9":
            username = input("Enter username to change password: ")
            new_password = input("Enter new password: ")
            change_password(username, new_password)
        elif choice == "10":
            username = input("Enter username for info: ")
            user_info(username)
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

