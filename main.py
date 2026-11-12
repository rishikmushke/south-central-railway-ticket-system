from array import*
import numpy as np
class agent:
    def __init__(self,username,password,name,dob):
        self.username=username
        self.password=password
        self.name=name
        self.dob=dob

users=np.array([agent("rishik@123","rishik@123","rishik",'7/11/2007'),
                agent("pooja@123","pooja@123","pooja",'10/10/2007'),
                agent("lucky@123","lucky@123","lucky",'7/11/2007'),
                agent("laddu@123","laddu@123","laddu",'10/10/2007'),
                agent("rishitha@123","rishitha@123","rishithapriya",'7/11/2007')],dtype=object)

class train:
    def __init__(self,name,source,destination,intermediate,tod):
        self.name=name
        self.source=source
        self.destination=destination
        self.intermediate=intermediate
        self.tod=tod

trains=np.array([train("AJANTA EXPRESS","KACHEGUDA","KAMAREDDY","MALKAJGIRI JUNCTION,BOLARUM,MEDCHAL,KAMAREDDY","06:30PM,06:50PM,07:05PM,07:20PM,08:40PM"),
                 train("KACHEGUDA-NIZAMBAD DEMU","KACHEGUDA","KAMAREDDY","SITAFALMANDI,MALKAJGIRI JUNCTION,BOLARUM,MEDCHAL,KAMAREDDY","06:55PM,07:05,07:15PM,07:30PM,07:45PM,10:20PM")
                 ],dtype=object)





print(" ---------------------------")
print("|                           |")
print("|     ---SOUTH CENTRAL--    |")
print("|         --RAILWAY--       |")
print("|                           |")
print("|                           |")
print("|ENTER 1 FOR AGENT LOGIN    |")
print("|ENTER 2 FOR CUSTOMER LOGIN |")
print("|ENTER 3 FOR  REGISTRATION  |")
print(" ---------------------------")
choice=int(input("Enter your choice: "))
if choice==1:
    print("\n---AGENT DETAILS---")
    username=str(input("USERNAME: "))
    password=str(input("PASSWORD: "))
    for agent in users:
        if username==agent.username and password==agent.password:
            print("\n---AGENT DASHBOARD--")
            print("1.TRAIN TICKET BOOKING\n2.TICKET MANAGEMENT\n3.PAYMENT AND BANK DETAILS\n4.TRAIN INFORMATION")
            agentchoice=int(input("\nENTER YOUR CHOICE: "))
            match agentchoice:
                case  1:
                    print("\n---ROUTE DETAILS---")
                    print("1.KACHEGUDA\n2.SITAFALMANDI\n3.MALKAJGIRI JUNCTION\n4.BOLARUM\n5.MEDCHAL\n6.KAMAREDDY\n7.NIZAMBAD JUNCTION")
                    print("\n---TYPE THE NAME OF SOURCE AND DESTINATION CORRECTLY---")
                    source=str(input("ENTER THE SOURCE STATION: "))
                    destination=str(input("ENTER THE DESTINATION: "))
                    print("---TRAIN DETAILS---")
                    for train in trains:
                        if source==train.source and destination==train.destination:
                            print(train.name)
                        else:
                            print("NO train found!!!!")
