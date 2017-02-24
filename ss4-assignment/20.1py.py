string="ThiS is String with Upper and lower case Letters"
alphabet=["a","b","c","e","g","h","i","l","n","o","p","r","s","t","u","w"]
def count(string,find_letter):
    count=0
    for letter in string:
        if letter.lower()==find_letter.lower():
            count+=1
    return count

for letter in alphabet:
    n=count(string,letter)
    if n>0:
        print("{0} {1}".format(letter,n))
