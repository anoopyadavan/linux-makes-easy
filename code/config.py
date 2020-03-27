import os
import local
import remote


choice=input("Where you want to run local or remote: ")
if(choice=='remote'):
    ip=input("Enter ip of remote server: ")
    user_name=input("Enter user name: ")
if(choice=='local' or choice=='remote'):
    while(True):
            def menu():
                print("==========================================")
                os.system("tput setaf 1")
                print("""\t\t\t\t1: Show
                \t\t2: Package management
                \t\t3: Service management
                \t\t4: Software management
                \t\t5: Configuration
                \t\t6: User management
                \t\t7: Docker configuration
                \t\t8: Configure Server
                \t\t9: Exit""")
                os.system("tput setaf 7")
                print("==========================================")
                num=int(input("Enter what services you want: "))
                if (num==1 and choice=='local'):
                    local.show()
                elif (num==2 and choice=='local'):
                    local.package_management()
                elif (num==3 and choice=='local'):
                    local.service_management()
                elif (num==4 and choice=='local'):
                    local.software_management()
                elif(num==5 and choice=='local'):
                    local.configuration()
                elif (num==6 and choice=='local'):
                    local.user_management()
                elif(num==7 and choice=='local'):
                    local.docker_configuration()
                elif(num==8 and choice=='local'):
                    local.configure_server()
                elif (num==1 and choice=='remote'):
                    remote.show(user_name,ip)
                elif (num==2 and choice=='remote'):
                    remote.package_management()
                elif (num==3 and choice=='remote'):
                    remote.service_management()
                elif (num==4 and choice=='remote'):
                    remote.software_management()
                elif(num==5 and choice=='remote'):
                    remote.configuration()
                elif (num==6 and choice=='remote'):
                    remote.user_management()
                elif(num==7 and choice=='remote'):
                    remote.docker_configuration()
                elif(num==8 and choice=='remote'):
                    remote.configure_server()
                elif(num==9):
                    exit()
                else:
                    print("wrong input")

            menu()

else:
    print("wrong choice")

