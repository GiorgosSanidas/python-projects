mylist = []
stop = False


while stop == False:
    item = input("Dwse stoixeio pou thelis na valeis sthn lista (h dose telos gia exodo):")
    if item == "telos":
        stop = True
    else:
        mylist.append(item)

print("H lista sou einai:", mylist)

while True:

    menu = int(input("Dwse epilogh 1.provoli olon ton proionton 2.anazitisi proiontos 3.diagrafi proiontos 4.taxinomisi listas(alfavitika) 5.exodos:"))

    if menu ==1: 
        print("H lista sou einai:", mylist)

    elif menu ==2 : 
        search = input("Dwse to proion pou thes na psaxis:")
        if search in mylist:
            print("to proion iparhi sti lista!!")
        else:
            print("to proion den iparxi sti lista")

    elif menu ==3: 
        delete= input("Dwse to proion pou thelis na diagrapsoume:")
        if delete in mylist:
            mylist.remove(delete)
            print("diagrafike: ", delete)
        else:
            print("to proion den vrethike sti lista")

    elif menu ==4:
        mylist.sort()
        print("Lista taxinomimeni alfavitika:", mylist)

    elif menu ==5: 
        print("exodos apo to programma")
        break

    else:
        print("eisai amea mhn patas otinane eipame apo to 1 eos to 5")




    
