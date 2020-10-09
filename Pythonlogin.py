name = {"Johny" : 'Stone',"Max": "Johson"}
def registry(incoming_name, incoming_surname):
    name[incoming_name] = incoming_surname
    print(("""Name {} Surname {} you registered""").format(incoming_name,incoming_surname))

    ask = input("Would you like to login? y/n >>>")
    if ask == 'y':
        access_control(incoming_name, incoming_surname)
    else:
        exit()

def access_control(incoming_name,incoming_surname):
    s_d = False
    for i in name:
        name_g = i
        surname_g = name[i]
        if incoming_surname == surname_g and incoming_name == name_g:
            print(("""
                    Acces succesful.
                    Welcome {} {} 
                    """).format(name_g,surname_g)) 
            s_d = True
    if s_d == False:
        print("""Account not found ,  Would you like to register?
                y/n
                """)
        ask = input(">>>")     
        if ask == 'y':
            name_ask = input("""
                       Name:
            """)  
            surname_ask = input("""
                        Surname:
            """)
            registry(name_ask,surname_ask)
        else:
            print("Exiting")
            exit()    
                       
def user():
    name = input('Name >>>')
    surname = input('Surname >>>')  
    access_control(name,surname)

user()                         

            