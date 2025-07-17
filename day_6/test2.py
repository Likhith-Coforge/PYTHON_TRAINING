text = "amazing python language" # declaring user_input_text

text = text.replace(" ","") # removing all the empty spaces from the input

upper_text = text.upper() # converting the entire string into uppercase

replace_A = upper_text.replace("A","XXX") # replace every "A" with "XXX"

print(replace_A[::3][::-1]) # extract every third character and reverse the final result

