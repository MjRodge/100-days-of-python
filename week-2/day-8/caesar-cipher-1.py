alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    
    #shift alphabet by chosen number, assign to new array 
    modified_alphabet = alphabet.copy()
    for x in range(0, shift):
      letter_shift = modified_alphabet.pop(0)
      modified_alphabet.append(letter_shift)
    
    #find index of encoded letters for chosen encryption text
    ref_array = []
    for l in text:
      ref_array.append(alphabet.index(l))
    print(ref_array)
    
    #create the encoded text 
    cipher_text = ""
    for y in ref_array:
      cipher_text += modified_alphabet[y]

    print(cipher_text)
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    print(alphabet)
    print(modified_alphabet)
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)