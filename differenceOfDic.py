# union of two dictionry data type 
d1={'ok':1,'nok':2}
d2={'ok':1,'new':3}
# function defination to perform the union of two dic
def uni(l1,l2):
    # removing the key which is persent in l1 and l2
    for i in l2.keys():
        if i in l1:
            del l1[i]
    #returning the resultant dic to the function call        
    return l1
       
#function call   
result=uni(d1,d2)
print(result)