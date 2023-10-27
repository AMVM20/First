
    #Primer Codigo
print("hello world")

    #Segundo codigo
name = input("What's your name? ")
# Remove whitespace from str (string)
    #name = name.strip()
# Capitalize the string (Only the first word)
    #name = name.capitalize()
# Capitalize all the words in the str 
    #name = name.title()
 # you can concatenate functions 
name=name.strip().title();
print("your name is",name)


#split strings (split user's name into first and last name)
fist,last=name.split();
print('your last name is',last) 