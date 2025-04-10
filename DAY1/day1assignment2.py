# intersection of two dictionry data type 
#Given:
#D1 = {'ok': 1, 'nok': 2}
#D2 = {'ok': 2, 'new':3 }
#output:{'ok': 1}
d1={'ok':1,'nok':2}
d2={'ok':1,'new':3}
#result varible is use to store the output dictionry
result={}
#for loop to iterate the dictionry for the keys from d1
#result varible only store the elements which are present both d1 and d2
for i in d1.keys():
    if i in d2:
        result[i]=d1[i];

print(result)
#output
#result={'ok': 1}
# Conclusion: 
# Time complexity: O(n)
# Space complexity: O(n)