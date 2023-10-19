a = int(input("masukkan angka : "))

if a < 3 :
    print("Maaf Size Kurang")

else :
    for i in range (1, a+1) :
        if i > 1 and i < a :
            for j in range ( 1, a+1) :
                if j > 1 and j < a :
                    # kalopakecontinue disini
                    print(" ", end=" ") 
                else :
                    print(j, end=" ")
        else :
            for j in range ( 1, a+1) :
                print (j, end=" ")
        print(" ")
    print(" ")

    for k in range (1, a+1) :
        if k < a//2+1 :
            for l in range (1, a+1) :
                if l > 1 and l < a :
                    print (" ", end=" ")
                else :
                    print (l, end=" ")
        elif k == a//2+1 :
            for m in range (1,a+1) :
                print(m, end=" ")
        else :
            for n in range (1, a+1) :
                if n < a :
                    print(" ", end=" ")
                else :
                    print(n,end=" ")
        print(" ")        
    print(" ")
    for o in range (1,a+1) :
        if o == 1 :
            for p in range (1,a+1) :
                print(p, end=" ")
        elif o > 1 : 
            for q in range (1,a+1) :
                if q < a :
                    print(" ", end=" ")
                else :
                    print(q, end=" ")
        print(" ")