input_songs = ['Track A','Track B','Track C','Track D']

input_songs.remove('Track C')
input_songs.insert(0,'Track X')

input_songs.insert(1,input_songs.pop())

print(" ".join(input_songs))