# steps: 
		
# 1) get username
# 2) input should be in a lowercase
# 3) convert it into the upper case without using the string .upper() method


user_name = input('Enter your name: ').lower()

resulting_name = ""

resulting_name+=chr(ord(user_name[0])-32)
resulting_name+=chr(ord(user_name[1])-32)
resulting_name+=chr(ord(user_name[2])-32)
resulting_name+=chr(ord(user_name[3])-32)
resulting_name+=chr(ord(user_name[4])-32)
resulting_name+=chr(ord(user_name[5])-32)
resulting_name+=chr(ord(user_name[6])-32)

# and so on till len(user_name)=len(resulting_name)

print(resulting_name)
