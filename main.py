import os
from colorama import Fore, Back, Style

log = []
accounts = []
islogged = False

def menu():
    os.system('cls')
    print("Welcome to "+Fore.RED+"Complex Chat"+Fore.WHITE+" in Python")
    print("_________________________________")
    print("Commands:\n"+Fore.RED+"1"+Fore.WHITE+".Login\n"+Fore.RED+"2"+Fore.WHITE+".Sign Up\n"+Fore.RED+"3"+Fore.WHITE+".Accounts\n"+Fore.RED+"4"+Fore.WHITE+".Current Session\n"+Fore.RED+"5"+Fore.WHITE+".Enter Chat\n"+Fore.RED+"6"+Fore.WHITE+".Exit")
    nav = int(input("Type: "))
    if nav == 1:
        os.system('cls')
        print(Fore.RED+"Complex Chat"+Fore.WHITE+" - Login")
        print("_________________________________")
        nick = input("Username: ")
        psw = input("Password: ")
        checkreg(nick, psw)  
        os.system('pause')
        menu()
    elif nav == 2:
        os.system('cls')
        print(Fore.RED+"Complex Chat"+Fore.WHITE+" - Create Account")
        print("_________________________________")
        nick = input("Username: ")
        psw = input("Password: ")
        register(nick, psw)
        menu()
    elif nav == 3:
        os.system('cls')
        print(Fore.RED+"Complex Chat"+Fore.WHITE+" - Registered Accounts")
        print("_________________________________")
        print(accounts)
        os.system('pause')
        menu()
    elif nav == 4:
        if islogged == True:
            os.system('cls')
            print(Fore.RED+"Complex Chat"+Fore.WHITE+" - Current Session")
            print("_________________________________")
            print("Username:", sessionid)
            os.system('pause')
            menu()
        else:
            os.system('cls')
            print(Fore.RED+"Complex Chat"+Fore.WHITE+" - WARNING")
            print("_________________________________")
            print("Please log into your account first!")
            os.system('pause')
            menu()
    elif nav == 5:
        chatinit()
    elif nav == 6:
        os.system('cls')
        quit()
    else:
        menu()

def register(nick, psw):
    accounts.append({
        'nick': nick,
        'psw': psw
    })
    list(accounts)

def checkreg(nick, psw):
    if len(accounts) > 0:
        for each in accounts:
            if nick == each['nick'] and psw == each['psw']:
                print("Welcome,", each['nick']+", you are logged in!")
                global sessionid
                sessionid = each['nick']
                global islogged
                islogged = True
                break
            else:
                islogged = False
        if islogged == False:
            print("Invalid username and/or password")
    else:
        print("No accounts registers")

def echo(text):
    splittext = text.split()
    echotext = ""
    for x in range(1,len(splittext)):
        echotext = echotext + splittext[x] + " "
    return echotext

def chatinit():
    if islogged == True:
        chatloop = True

        while chatloop == True:
            os.system('cls')
            print(Fore.RED+"COMPLEX CHAT V1"+Fore.WHITE)
            if len(log) > 0:
                for x in log:
                    if x["from"] == "user":
                        print("["+Fore.GREEN+sessionid+Fore.WHITE+"]:", x['msg'])
                    elif x["from"] == "system":
                        print("["+Fore.YELLOW+"SYSTEM"+Fore.WHITE+"]:", x["msg"])
            print("_________________________________")
            msg = input("Type: ")
            log.append({
                "from": "user",
                "msg": msg
            })
            if msg[0] == "/": #is a command
                if msg == "/end":
                    chatloop = False
                    log.pop()
                elif msg == "/clear":
                    log.clear()
                elif msg == "/ping":
                    msg = "Pong!"
                    log.append({
                        "from": "system",
                        "msg": msg
                    })
                elif msg.startswith("/echo"):
                    msg = echo(msg)
                    log.append({
                        "from": "system",
                        "msg": msg
                    })
                elif msg == "/help":
                    msg = "List of commands:\n/help - This command\n/echo {content} - Echo content\n/ping - Test command\n/clear - Clear log\n/end - Leave chat"
                    log.append({
                        "from": "system",
                        "msg": msg
                    })
                else:
                    msg = "Invalid command"
                    log.append({
                        "from": "system",
                        "msg": msg
                    })
                    
        menu()
    else:
        os.system('cls')
        print(Fore.RED+"Complex Chat"+Fore.WHITE+" - WARNING")
        print("_________________________________")
        print("Please log into your account first!")
        os.system('pause')
        menu()

menu()