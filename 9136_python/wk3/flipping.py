 # Enter your code here for prompting the user for input.
# Enter your code here for the new flipped_binary_string that is to be displayed.
# Enter your code here for displaying the populated flipped_binary_string.

binary_string = "1010"

flipped_binary_string = ""
for i in binary_string:
    if i == "1":
        flipped_binary_string += "0"
    else:
        flipped_binary_string += "1"
print(flipped_binary_string)
