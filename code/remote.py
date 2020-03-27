import os
import softwareManagement

# Show basic cmd
def show(user,ip):
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
        os.system("ssh {var}@{var2} date".format(var=user,var2=ip))
    elif (num==2):
        os.system("ssh {var}@{var2} cal".format(var=user,var2=ip))
    elif (num==3):
        os.system("ssh {var}@{var2} date | awk '{print $4}'".format(var=user,var2=ip))
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
    def show_user():
        os.system("tput setaf 2")
        # this fn is for show all user in your system
        os.system("sudo cat /etc/passwd | grep -A 100 1000  | awk -F : '{print $1}' ; tput setaf 7")

    def user_add(user_name):
        user_name=input("Enter user name: ")
        os.system("sudo adduser {var}".format(var=user_name))                    # i have to make more convenient
        os.system("sudo passwd {var}".format(var=user_name))

    def user_remove():
        user_name=input("Enter user name which you want to delete: ")
        os.system("sudo userdel -r {var}".format(var=user_name))

    def user_modify():
        def set_comment(user_name):
            comment=input("Enter comment: ")
            os.system("sudo usermod -c {com_var} {var}".format(com_var=comment,var=user_name))

        def change_home_dir(user_name):
            dir_name=input("Enter directory name: ")
            os.system("sudo usermod -d {dir_var} {var}".format(dir_var=dir_name,var=user_name))
            os.system("sudo mkdir /home/{dir_var}".format(dir_var=dir_name))

        print("==========================================")
        os.system("tput setaf 1")
        print("""\t\t1: set comment
    \t\t2: change home directory """)
        os.system("tput setaf 7")
        print("==========================================")
        num=int(input("Enter your choice: "))
        user_name=input("Enter user name: ")
        if(num==1):
            set_comment(user_name)
        elif(num==2):
            change_home_dir(user_name)
        else:
            print("wrong choice")

    def change_passwd():
        user_name=input("Enter user name which you want to change password: ")
        os.system("sudo passwd {var}".format(var=user_name))

    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: Show all user
    \t\t2: user add
    \t\t3: user remove
    \t\t4: user modification
    \t\t5: change password""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter number which you want: "))
    #user_name=input("Enter user name: ")
    if(num==1):
        show_user()
    elif(num==2):
        user_add()
    elif(num==3):
        user_remove()
    elif(num==4):
        user_modify()
    elif(num==5):
        change_passwd()
    else:
        print("wrong input")

def docker_configuration():
    data="""[docker]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0"""
    with open("docker.repo","w") as fp:
        for content in data:
            fp.write(content)

    os.system("sudo mv -i docker.repo /etc/yum.repos.d/")
    os.system("sudo yum install docker-ce --nobest")

def configure_server():
    def configure_httpd():
        os.system("sudo yum install httpd")

    def configure_ssh():
        os.system("sudo yum install openssh-server")
        os.system("firewall-cmd --zone=public --permanent --add-service=ssh")
        os.system("firewall-cmd --reload")

    print("==========================================")
    os.system("tput setaf 1")
    print("""\t\t1: configure httpd server
    \t\t2: configure ssh server""")
    os.system("tput setaf 7")
    print("==========================================")
    num=int(input("Enter your choice: "))
    if(num==1):
        configure_httpd()
    elif(num==2):
        configure_ssh()
    else:
        print("wrong choice")
if __name__ == '__main__':
    pass
