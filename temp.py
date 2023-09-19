# Ask the user what acronym they want to add
# Ask the user for the acronym definition
# open the file
# write the new acronym and definition to the file

acronym = input("What acronym do you want to add? \n")
definition = input("What does the acronym mean? \n")

with open("acronyms.txt", "r") as file:
    for line in file:
        print(line)
            
