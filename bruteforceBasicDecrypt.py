#Cypher Decryption Forcer(Basic shift, All 25 shifts)
message = input("Message: ")

def decrypt(msg):
  alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ") #26 alphabets. 0-25
  specialCharacters = ", < . > / ? ' ; : [ { ] } \ | = + - _ 0 ) 9 ( 8 * 7 & 6 ^ 5 % 4 $ 3 2 @ 1 ! ) ]".split(" ")
  temp = []
  shift = 1
  while shift <= 25:
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
    print("(" + "".join(temp) + ") Shift: +" + str(shift) + "(-" + str(26-shift) + ")")
    temp = []
    shift += 1

decrypt(message)
