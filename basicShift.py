#Cypher Encryption(basic numerical shift)
message = input("Message: ")
shift = int(input("Shift: "))
def encrypt(msg):
  alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ") #26 alphabets. 0-25
  specialCharacters = ", < . > / ? ' ; : [ { ] } \ | = + - _ 0 ) 9 ( 8 * 7 & 6 ^ 5 % 4 $ 3 2 @ 1 ! ) ]".split(" ")
  temp = []
  for i in msg:
    if i in specialCharacters or i == " ":
      temp.append(i) #Nothing should change
    else:
      if i.isupper():
        index = alphabet.index(i.lower())
        fixedIndex = index+shift
        fixedIndex = (fixedIndex + 26) % 26

        i2 = alphabet[fixedIndex].upper()
        temp.append(i2) #List with letters of the message but like, shifted(uppercase)
      else:
        index = alphabet.index(i)
        fixedIndex = index+shift
        fixedIndex = (fixedIndex + 26) % 26

        i2 = alphabet[fixedIndex]
        temp.append(i2) #List with letters of the message but like, shifted
  print("".join(temp))
encrypt(message)
