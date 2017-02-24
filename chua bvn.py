#clothes = ["Jeans", "T-Shirt", "Skirt"]

###function, phan mau xanh la la ten ham: lap lai doan code giong nhau
##def print_clothes():
##    for index in range(len(clothes)):
##        print(clothes[index], end = "")
##        if index != len(clothes) - 1:
##            print(", ", end = "")
##        else:
##            print()
##
##while True:
##    choice = input("What do you want (CRUD)?")
##    if choice.upper() == "D":
##        position = int(input("Position?")) - 1
##        print(position)
##        del clothes[position]
##        print_clothes()
##    elif choice.upper() == "C":
##        new_cloth = input("New item?")
##        clothes.append(new_cloth)
##        print_clothes()


#function, phan mau xanh la la ten ham: thay the
##clothes_1_2 = ["Jeans", "T-Shirt", "Skirt"]
##
##def print_clothes(clothes):
##    for index in range(len(clothes)):
##        print(clothes[index], end = "")
##        if index != len(clothes) - 1:
##            print(", ", end = "")
##        else:
##            print()
##            
##def shop(clothes):
##    while True:
##        choice = input("What do you want (CRUD)?")
##        if choice.upper() == "D":
##            position = int(input("Position?")) - 1
##            print(position)
##            del clothes[position]
##            print_clothes(clothes)
##        elif choice.upper() == "C":
##            new_cloth = input("New item?")
##            clothes.append(new_cloth)
##            print_clothes(clothes)
##shop(clothes_1_2)


##clothes_1_2 = ["Jeans", "T-Shirt", "Skirt", "T-Shirt", "T-Shirt"]
##def count_t_shirt():
##    count = 0
##    for cloth in clothes_1_2:
##        if cloth== "T-Shirt":
##            count +=1
##    return count
##no_t_shirt= count_t_shirt()
##print(no_t_shirt)
##
##def dummy():
##    i=7
##    return i #bat cu return j ra cung vao x, ke ca return 3 hay return i
##x=dummy()
##print(x)
### hoac: print(dummy())
##
##def print_clothes(clothes):
##    for index in range(len(clothes)):
##        print(clothes[index], end = "")
##        if index != len(clothes) - 1:
##            print(", ", end = "")
##        else:
##            print()
##            
##def shop(clothes):
##    while True:
##        choice = input("What do you want (CRUD)?")
##        if choice.upper() == "D":
##            position = int(input("Position?")) - 1
##            print(position)
##            del clothes[position]
##            print_clothes(clothes)
##        elif choice.upper() == "C":
##            new_cloth = input("New item?")
##            clothes.append(new_cloth)
##            print_clothes(clothes)
##shop(clothes_1_2)

##clothes_1_2 = ["Jeans", "T-Shirt", "Skirt", "T-Shirt", "T-Shirt"]
##find_list=["jeans","hoody","bra"]
##
##def count_item(clothes,item):
##    count = 0
##    for cloth in clothes:
##        if cloth.lower()== item.lower():
##            count +=1
##    return count
##n=count_item(clothes_1_2,"t-shirt")
##print(n)
##
####def dummy():
####    i=7
####    return i #bat cu return j ra cung vao x, ke ca return 3 hay return i
####x=dummy()
####print(x)
##### hoac: print(dummy())
##
##def print_clothes(clothes):
##    for index in range(len(clothes)):
##        print(clothes[index], end = "")
##        if index != len(clothes) - 1:
##            print(", ", end = "")
##        else:
##            print()
##            
##def shop(clothes):
##    while True:
##        choice = input("What do you want (CRUD)?")
##        if choice.upper() == "D":
##            position = int(input("Position?")) - 1
##            print(position)
##            del clothes[position]
##            print_clothes(clothes)
##        elif choice.upper() == "C":
##            new_cloth = input("New item?")
##            clothes.append(new_cloth)
##            print_clothes(clothes)
##shop(clothes_1_2)

clothes_1 = ["Jeans", "T-Shirt", "Skirt", "T-Shirt", "T-Shirt","jeans", "jeans","bra"]
find_list=["jeans","hoody","bra"]

def count_item(clothes, item):
    count = 0
    for cloth in clothes_1:
            if cloth.lower()== item.lower():
                count +=1
    return count
for cloth in find_list:
##    print(cloth, ":", count_item(find_list,cloth), sep="")
##    n= count_item(find_list,cloth)
##    if n >2:
##        print("sale")
##    elif n>=1:
##        print("nhap them")
##    elif n==0:
##        print("het hang")
##    

#cach 2:
    print("{0}:{1}". format(cloth,count_item(clothes_1,cloth)))
    
