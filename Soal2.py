la = [[1,2,3], [4,5,6], [7,8,9]]
lb1 = [] #masukkin list counter angka 1 
lb2 = [] #masukkin list counter angka 2
lb3 = [] #masukkin list counter angka 3


def CC(list_awal):
    for x in la[0]:  #make sure value x ada di list [1,2,3]  
        if x == 3: 
            a = lb1.append(x) #append angka 3 ke list lb1
    for y in la[1]: #make sure value y ada di list [4,5,6]  
        if y == 6:
            a = lb1.append(y) #append angka 6 ke list lb1
    for z in la[2]: #make sure value z ada di list [7,8,9]  
        if z == 9:
            a = lb1.append(z) #append angka 9 ke list lb1

    for o in la[0]:
        if o == 2: 
            b = lb2.append(o)
    for p in la[1]:
        if p == 5:
            b = lb2.append(p)
    for q in la[2]:
        if q == 8:
            b = lb2.append(q)


    for r in la[0]:
        if r == 1: 
            c = lb3.append(r)
    for s in la[1]:
        if s == 4:
            c = lb3.append(s)
    for t in la[2]:
        if t == 7:
            c = lb3.append(t)
    return a,b,c

print(CC(la)) #error karena yg keluar none, none, none.

# Errornya mungkin karena cara saya append isi dari list awal ke list baru [lb1, lb2, lb3]. 
# Return value yg saya berikan pun kemungkinan salah. 

print(lb1) 
print(lb2)
print(lb3)

#bisa keluar kalo gak pake def function. 
