access_data = {(103,209):"Alice",(104,210):"Bob",(105,211):"Charlie",(106,212):"Diana"}

auth_input = tuple(map(int,input("Enter the pair of biometric ids: ").split(" ")))

print(access_data.get(auth_input) or access_data.get((auth_input[1],auth_input[0])))