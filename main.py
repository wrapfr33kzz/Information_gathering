import email_header 
import insta_info
import Insta_respond
import ip
import ip_info
import phone_info
import os

print("""

██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

░██████╗░░█████╗░████████╗██╗░░██╗███████╗██████╗░██╗███╗░░██╗░██████╗░
██╔════╝░██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║████╗░██║██╔════╝░
██║░░██╗░███████║░░░██║░░░███████║█████╗░░██████╔╝██║██╔██╗██║██║░░██╗░
██║░░╚██╗██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║╚████║██║░░╚██╗
╚██████╔╝██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║██║░╚███║╚██████╔╝
░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░

""")

ip.public_ip()
print("""
\t 1. Email Header Analysis
\t 2. Instagram Information
\t 3. Instagram Username Check
\t 4. IP Information
\t 5. Phone Number Information
\t 6. Port Scan
\t 7. Exit
""")
option = int(input("Enter What You Want: "))
print("\n")
if option == 1:
    email_header.email()
    print("You want exit or use another options(yes/no)")
    choose = input("yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 2:
    insta_info.info()
    print("You want exit or use another options(yes/no)")
    choose = input("yes Or no: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose ==  "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 3:
    Insta_respond.insta_check()
    print("You want exit or use another options(yes/no)")
    choose = input("yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 4:
    ip_info.ip_info()
    print("You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 5:
    phone_info.phone_info()
    print("You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "No" or "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 6:
    ip = input("Enter ip address: ")
    s_p = int(input("Enter starting port number: "))
    e_p = int(input("Enter ending port number: "))
    os.system(f'python port_scanner.py {ip} {s_p} {e_p}')
    print("You want exit or use another options(yes/no)")
    choose = input("Yes Or No: ")
    if choose == "yes":
        os.system("cls")
        os.system('python project.py')
    elif choose == "no":
        os.system("cls")
        print("Thank you for using..!!")

elif option == 7:
    os.system("^")

else:  
    print("Wrong option Try angin..!!")
    os.system('python project.py')


