import os
import local
import remote
import search
import sys

def ping(ip):
    os.system("ping -c 4 {var}".format(var=ip))

choice=input("Where you want to run local or remote: ").lower()
if(choice=='remote'):
   # ip=input("Enter ip of remote server: ")
    ip="192.168.1.10"
    var=os.popen("ping -c 1 %s | grep received | awk '{print $4}'" % ip).read()
    if(int(var)>0):
        user_name=input("Enter user name: ")
        os.system("ssh-copy-id {var}@{var2} 2>/dev/null".format(var=user_name,var2=ip))
    else:
        print("Wrong ip provided")
        exit()
if(choice=='local' or choice=='remote'):
    while(True):
            def menu():
                print("==========================================")
                os.system("tput setaf 1")
                print("""\t\t\t\t1: Search
                \t\t2: Show
                \t\t3: Package management
                \t\t4: Service management
                \t\t5: Software management
                \t\t6: Configuration
                \t\t7: User management
                \t\t8: Docker configuration
                \t\t9: Configure Server
                \t\t10: File management
                \t\t11: Exit""")
                os.system("tput setaf 7")
                print("==========================================")
                num=int(input("Enter what services you want: "))
                if(num==1):
                    search_key=input("what you want to search: ")
                    search.primary(search_key)
                elif (num==2 and choice=='local'):
                    local.show()
                elif (num==3 and choice=='local'):
                    local.package_management()
                elif (num==4 and choice=='local'):
                    local.service_management()
                elif (num==5 and choice=='local'):
                    local.software_management()
                elif(num==6 and choice=='local'):
                    local.configuration()
                elif (num==7 and choice=='local'):
                    local.user_management()
                elif(num==8 and choice=='local'):
                    local.docker_configuration()
                elif(num==9 and choice=='local'):
                    local.configure_server()
                elif(num==10 and choice=='local'):
                    local.file_management()
                elif (num==2 and choice=='remote'):
                    remote.show(user_name,ip)
                elif (num==3 and choice=='remote'):
                    remote.package_management(user_name,ip)
                elif (num==4 and choice=='remote'):
                    remote.service_management(user_name,ip)
                elif (num==5 and choice=='remote'):
                    remote.software_management(user_name,ip)
                elif(num==6 and choice=='remote'):
                    remote.configuration(user_name,ip)
                elif (num==7 and choice=='remote'):
                    remote.user_management()
                elif(num==8 and choice=='remote'):
                    remote.docker_configuration(user_name,ip)
                elif(num==9 and choice=='remote'):
                    remote.configure_server()
                elif(num==10 and choice=='remote'):
                    remote.file_management()
                elif(num==11):
                    sys.exit()
                else:
                    print("wrong input")
                input("Press Enter to continue")
                os.system("clear")

            menu()

else:
    print("wrong choice")

