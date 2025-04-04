# union of two dictionry data type 
d1={'ok':1,'nok':2}
d2={'ok':2,'new':3}
# function defination to perform the union of two dic
def uni(l1,l2):
    # result varible to union
    r={}
    # storing first dic into result
    for i in l1.keys():
        r[i]=l1[i]
    # mergeing dic into result 
    print(r)
    for i in l2.keys():
        if i in r:
            r[i] = r[i] + l2[i]
        else:
            r[i]=l2[i]
    #returning the resultant dic to the function call
    return r
       
#function call   
result=uni(d1,d2)
print(result)