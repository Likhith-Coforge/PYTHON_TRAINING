l=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

result = set(l[0]) & set(l[1]) & set(l[2]) & set(l[3])

print(list(result))