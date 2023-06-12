print("WELCOME TO OUR ENCRYPTION ARENA!!!")


def ceaser():
    task = input("Enter \"e\" to ENCRYPT & \"d\" to DECRYPT""\n").lower()
    msg = list(input("Type your message\n"))
    key = int(input("Enter the shift number i.e the Key\n"))
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    enc = []
    dec = []

    if task == "e" or task == "encrypt":
        for val in msg:
            for letter in letters:
                if letter == val:
                    ind = letters.index(letter)
                    encode = (ind + key) % 26
                    enc.append(letters[encode])
        print("Here is the text after encryption: \t", ''.join(enc))
        # print(enc)
    elif task == "d" or task == "decrypt":
        for val in msg:
            for letter in letters:
                if letter == val:
                    ind = letters.index(letter)
                    tx = ind - key
                    if tx < 0:
                        decode = (tx + 26) % 26
                    else:
                        decode = tx % 26
                    dec.append(letters[decode])
        print("Here is the text after decryption: \t", ''.join(dec))

ceaser()
again = input("Type 'yes' if you want to go again otherwise type 'no'\n")
if again == "yes":
    ceaser()
elif again == "no":
    print("Thank You, Bye Bye, Take Care!!!")
else:
    print("Wrong Key! See you again!!!")
