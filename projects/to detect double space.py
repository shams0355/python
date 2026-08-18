records_of_cnics=["71501-7329759-5","45122-5632659-5","56996-5458556-8"]
while True:
 ask=input("CNIC NUMBER (0000-0000000-0)\nEnter your cnic number::-  ")#71501-7329759-5
 a=ask.find("-")
 b=ask.find("-",a+1)
 if len(ask)==15:
    if a==5 and b==13:
        if ask in records_of_cnics:
            print("WELCOME BOSS TO YOUR ACCOUNT\n\"YOU ARE LOGED IN\"")
            break
        else:
            print("YOUR RECORD IS NOT FOUNDED")
    else:
        print("PLEASE WRITE IN CORRECT FORMAT (0000-0000000-0)")
 else:
    print("the number should not be less or more than 15 characters including the hyphons(-)")

