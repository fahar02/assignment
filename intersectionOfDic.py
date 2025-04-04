# union of two dictionry data type 
d1={'ok':1,'nok':2}
d2={'ok':1,'new':3}
# function defination to perform the union of two dic
def inter(l1,l2):
    #temp varible to store both l1 and l2
    r={}
    # resultant varible
    s={}
    # storing l1 into temp dic
    for i in l1.keys():
        r[i]=l1.get(i)
    #storing l2 into temp dic
    for i in l2.keys():
        r[i]=l2.get(i)
    for i in r.keys():
        if i in l1 and i in l2:
            s[i]=l1.get(i)
     #returning the resultant dic to the function call               
    return s
#function call
result=inter(d1,d2)
print(result)