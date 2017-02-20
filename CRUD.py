##choice=input("welcome,what do you want(C,R,U,D,S)?")
##want=["C","R","U","D","S"]
##clothes=["tshirt","sweater"]
##while choice in want:
##    if choice=="C":
##        new_cloth=input("new item?")
##        clothes.append(new_cloth)
##        print("your",new_cloth,"are created")
##        choice=input("welcome,what do you want(C,R,U,D,S)?")  
##
##    elif choice=="R":
##        for i in range (len(clothes)):
##            print(clothes[i],",",end=" ")
##        print()
##        choice=input("welcome,what do you want(C,R,U,D,S)?")
##    elif choice=="U":
##        clothes[1]=input("new item?")
##        print(clothes)

#cach2:
want=["C","R","U","D","S"]
clothes=["tshirt","sweater"]
while True:
    choice=input("welcome,what do you want(C,R,U,D,S)?")
    if choice=="C":
        new_cloth=input("new item?")
        clothes.append(new_cloth)
        print("your",new_cloth,"are created")
    elif choice=="R":
        for i in range (len(clothes)):
            print(clothes[i],",",end=" ")
        print()
    elif choice=="U":
       position=int(input("update position?"))
       new_clothes=input("new item?")
       clothes[position]=new_clothes
       print("our item: ", end=" ")
       for i in range (len(clothes)-1):
           print(clothes[i],",",end=" ")
       print()
    else:
       position=int(input("delele positions?")
       clothes.pop(position) #cai nay k hieu sao bi bao loi
       print("our item: ", end=" ")
       for i in range (len(clothes)-1):
           print(clothes[i],",",end=" ")
       print()
        
    
