while True:
    name=input("enter your name or roll number and see your result : ")
    rajesh={"math":56,"english":45,"hindi":67}
    rohit={"math":65,"english":54,"hindi":76}
    rohan={"math":67,"english":66,"hindi":77}
    arun={"math":90,"english":88,"hinidi":66}
    a=("congratulation your result is \n ")
    b="rajesh"
    c="rohit"
    d="rohan"
    e="arun"

    if (name=="rajesh" or 1001):
        print(a,b,rajesh)

    elif(name=="rohit"or 1002):

        print(a,c,rohit)

    elif(name=="rohan"or 1003):
        print(a,d,rohan)

    elif(name=="arun"or 1004):
        print(a,e,arun)
        
    elif(name=="all"or"all result"):
        security=int(input("plese enter the paswword and take your answer"))
        if (roll_number==8952898310):
            print(rajesh,rohit ,rohan,arun)
        else:
            print("you are frode")
            
    else:
        print("not found your mark sheet")
