# union of two dictionry data type 
d1={'ok':1,'nok':2}
d2={'ok':1,'new':3}
# function defination 
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
#output
#result={'nok': 2}
# Conclusion: The above code D1 - D2 results in a dictionary that contains only the keys values
# that are in D1 but not in D2
# Time complexity: O(n)
# Space complexity: O(n)