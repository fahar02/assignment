input = [1,2,3, [1,2,3,[3,4],2]]
lst=[*input[:3],*input[-1][:3],*input[-1][3],input[-1][-1]]
print(lst)