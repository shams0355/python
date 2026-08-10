code=1218
attemps=0
while attemps<3:
 ask=int(input("Enter your code::"))
 if ask==code:
    print("acess granted\nWelcome to the system")
    break
 else:
    attemps+=1
    if attemps<3:
     print("access denied\nPlease try again")
if attemps==3:
      print("You have exceeded the maximum number of attempts\nPlease try again later")    