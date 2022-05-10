import json
print("whether you want to do login and signup: ")
print("1.login")
print("2.signup")
chose=int(input("enter your option: "))
if chose==2:
    usern=input("enter user name: ")
    email=input("enter your email: ")
    if True:
        list=[]
        user=input("enter your strong password: ")
        if len(user)>=6 and len(user)<=16:
            if ("A" in user or "Z" in user) or ("a" in user or "z" in user):
                if "2" in user or "1"in user or "3" in user or "4"in user or "5" in user or "6"in user or "7" in user or "8"in user or "9" in user or "0"in user :
                    if "@" in user or "$" in user or "&" in user:
                        print("strong password: ")
                        confirm=input("enter agin to confirm your password: ")
                        if user==confirm:
                            x={}
                            x["name"]=usern
                            x["email"]=email
                            x["password"]=user
                            list.append(x)
                            k=json.dumps(list,indent=1)
                            f1=open("log.json","a")
                            f1.write(k)
                            f1.write("\n")
                            f1.write("\n")
                            f1.close()
                            print() 
                            print(list)                          
                        else:
                            print("Not same password: ")
                    else:
                        print("special character: ")
                else:
                    print("also added number: ")
            else:
                print("upper and lower case both we want: ")
        else:
            print("week password: ")
elif chose==1:
    name2=input("enter user name: ")
    password=input("enter your password: ")
    t=open("log.json","r")
    j=t.read()
    if name2 in j:
        if password in j:
            print("you log in successfully")
        else:
            print("please enter correct password")
    else:
        print("please first signup then login")
            
    