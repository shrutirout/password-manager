def encrypt (data ,shift):
   encrypted = ""
   for i in range (len(data)):
     char = data[i]
     if (char.isupper()):
         encrypted += chr((ord(char) + shift - 65) % 26 +65)
     elif (char.islower()):
         encrypted += chr((ord(char) + shift -97) % 26 +97)
     elif (char.isdigit()):
         number = (int(char) +shift) % 10
         encrypted += str(number)
     else:
         encrypted += char
   return encrypted

def decrypt(data ,shift):
    decrypted = ""
    for i in range (len(data)):
      char = data[i]
      if (char.isupper()):
         decrypted += chr((ord(char) - shift - 65) % 26 +65)
      elif (char.islower()):
         decrypted += chr((ord(char) - shift -97) % 26 +97)
      elif (char.isdigit()):
         number = (int(char) -shift) % 10
         decrypted += str(number)
      else:
         decrypted += char
    return decrypted

menu = ""
while menu != '1' or menu != '2':
    menu = input("would you like to save a new password or view your old ones?"
                "\n1. Input new password"
                "\n2. View password"
                "\n3. Exit")
    if menu== '1':
        softwareName = input("enter the name of software you are using:")
        username = input("enter the username for this software: ")
        password = input("enter your password for this software: ")
        shift = 2
        file = open("secure password.txt", "a")
        file.write(encrypt(softwareName,shift)+";|"+encrypt(username,shift)+";|"+encrypt(password,shift)+"\n")
        file.close()
    if menu=='2':
        file = open("secure password.txt" , "r")
        print("Software\tUsername\tPassword")
        for i in file:
            shift = 2
            data = i.split(";|")
            print(decrypt(data[0],shift)+"\t\t"+decrypt(data[1],shift)+"\t\t"+decrypt(data[2],shift))
    if menu =='3':
        exit()
