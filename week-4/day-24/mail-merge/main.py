#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# save letter template text into variable
with open("./Input/Letters/starting_letter.txt") as letter_template:
    letter_text = letter_template.read()
# save addressee names into list
with open("./Input/Names/invited_names.txt") as invitee_data:
    invitees = invitee_data.readlines()

# loop through invitees and prepare a personalised invite ready to send
for person in invitees:
    person_strip = person.strip("\n")
    invite = letter_text.replace("[name]", person_strip)
    with open("./Output/ReadyToSend/"+person_strip+".txt", mode="w") as personalised_invite:
        personalised_invite.write(invite)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp