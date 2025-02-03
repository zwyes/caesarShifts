#Cypher Encryption(Code shift)
message = input("Message: ")
password = input("Password: ") #"1321" # Applies password to encryption. Character1 gets +first digit, character2 gets +second digit, and this loops.
def encrypt(msg):
  alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ") #26 alphabets. 0-25
  specialCharacters = ", < . > / ? ' ; : [ { ] } \ | = + - _ 0 ) 9 ( 8 * 7 & 6 ^ 5 % 4 $ 3 2 @ 1 ! ) ] ’ —".split(" ")
  temp = []
  #Setup code
  code = []
  for i in password*1000:
    code.append(i)
  pos = 0
  for i in msg:
    if i in specialCharacters or i == " ":
      temp.append(i) #Nothing should change
    else:
      if i.isupper():
        index = alphabet.index(i.lower())
        fixedIndex = index+int(code[int(pos)])
        fixedIndex = (fixedIndex + 26) % 26

        i2 = alphabet[fixedIndex].upper()
        temp.append(i2) #List with letters of the message but like, shifted(uppercase)
      else:
        index = alphabet.index(i)
        fixedIndex = index+int(code[int(pos)])
        fixedIndex = (fixedIndex + 26) % 26

        i2 = alphabet[fixedIndex]
        temp.append(i2) #List with letters of the message but like, shifted
      pos += 1
  print("".join(temp))
encrypt(message)
