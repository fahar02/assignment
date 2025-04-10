# union of two dictionry data type 
# union of keys, #value does not matter
#Given:
#D1 = {'ok': 1, 'nok': 2}
#D2 = {'ok': 2, 'new':3 }
d1={'ok': 1, 'nok': 2}
d2={'ok': 2, 'new':3 }
result={**d1,**d2}
print(result)
#output
#result={'ok': 1, 'nok': 2, 'new': 3}
# Conclusion: The above code combines two dictionaries by keys, ignoring the values.
# Time complexity: O(n)
# Space complexity: O(n)
