import os
import softwareManagement

# Show basic cmd
def show():
    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: Date
    \t\t2: Calendar
    \t\t3: Time""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter your choice: "))
    os.system("tput setaf 2")
    if (num==1):
        os.system("date")
    elif (num==2):
        os.system("cal")
    elif (num==3):
        os.system("date | awk '{print $4}'")
    else:
        print("wrong input")
    os.system("tput setaf 7")

#package management
def package_management():
    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: Install
    \t\t2: Remove""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter what you want to do: "))
    package_name=input("Enter pacakage name: ")
    if (num==1):
        os.system("sudo yum install {var}".format(var=package_name))
    elif (num==2):
        os.system("sudo yum remove {var}".format(var=package_name))
    else:
        print("wrong input")
    os.system("tput setaf 7")

#service management
def service_management():
    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: show
    \t\t2: start
    \t\t3: stop""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter the number which you want: "))
    service_name=input("Enter service name: ")
    if (num==1):
        os.system("systemctl status {var}".format(var=service_name))
    elif (num==2):
        os.system("systemctl start {var}".format(var=service_name))
    elif (num==3):
        os.system("systemctl stop {var}".format(var=service_name))
    else:
        print("wrong input")
    #os.system("tput setaf 1")

# Software management
def software_management():
    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: open software
    \t\t2: close software""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter the number which you want: "))
    software_name=input("Enter software name: ")
    softwareManagement.software_manage(num,software_name)

# Configuration
def configuration():
    
    def yum():
        data="""[dvd1]
baseurl=file:///run/media/anoop/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0
[dvd2]
baseurl=file:///run/media/anoop/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0"""

        with open("yum.repo", "w") as f1:
            for content in data:
                f1.write(content)

        os.system("sudo mv yum.repo /etc/yum.repos.d")
        os.system("yum repolist")
        os.system("tput setaf 2")
        print("Successful")

    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: configure Yum""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter number which you want: "))
    if (num==1):
        yum()
    os.system("tput setaf 7")

# user management
def user_management():
#    def user_add()
    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: user add
    \t\t2: user remove
    \t\t3: user modification""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter number which you want: "))
    user_name=input("Enter user name: ")
    if(num==1):
        user_add(user_name)
    elif(num==2):
        user_remove(user_name)
    elif(num==3):
        user_remove(user_name)
    else:
        print("wrong input")


def menu():
    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: Show
    \t\t2: Package management
    \t\t3: Service management
    \t\t4: Software management
    \t\t5: Configuration
    \t\t6: User management""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter what services you want: "))
    if (num==1):
        show()
    elif (num==2):
        package_management()
    elif (num==3):
        service_management()
    elif (num==4):
        software_management()
    elif (num==5):
        configuration()
    elif (num==6):
        user_management()
    else:
        print("wrong input")

menu()
