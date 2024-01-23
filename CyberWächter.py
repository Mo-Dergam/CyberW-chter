#Passwortgenerator:
import string
import random 
def Password12():
  i = int(input("aus wie stellig soll ihr passwort sein:"))
  Z = input("Soll dein Passwort zahlen enthalten: (Ja/Nein)")
  GB = input("Soll dein passwort großbuchtaben haben: (Ja/Nein)")
  KB = input("Soll dein passwort Kleinbuchtaben haben: (Ja/Nein)")
  S = input("soll dein passwort sonderzeichen haben: (Ja/Nein)")
 # Ja, Nein, Nein, Nein
  if Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "nein":
    Password1 = string.digits
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Ja, Ja, Nein, Nein
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "nein":
    Password1 = string.digits + string.ascii_uppercase
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Ja, Ja, Ja, Nein
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "nein":
    Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Ja, Ja, Ja, Ja
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Ja, Ja, Ja
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Nein, Ja, Ja
  elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Nein, Nein, Ja
  elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Ja, Ja, Nein, Ja
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.digits + string.ascii_uppercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Ja, Nein, Ja, Ja
  elif Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.digits + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Ja, Nein, Nein, Ja
  elif Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.digits + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Ja, Ja, Nein
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "nein":
    Password1 = string.ascii_uppercase + string.ascii_lowercase 
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Ja, Nein, Ja
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.ascii_uppercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Ja, Nein, Nein
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "nein":
    Password1 =  string.ascii_uppercase
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
 # Nein, Nein, Ja, Nein
  elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "nein":
    Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print(password, end = '')
Password12()


# while wi < i:
 
#  wi +=1

 

# w = 0
# z = 0
# Passwort1 = []
# Passwort2 = []
# while w < i:
#   import random

#             # Zufällige Auswahl aus einer Liste von Zeichen
#   zeichenliste = ['A', 'B', 'C', 'D', 'E', 'D','F']
#   zufallszeichen = random.choice(zeichenliste)
#   Passwort1.append(zufallszeichen)
#   w +=1

# while z < i:
#   import random
#   zahl = random.randint(0, 10)
#   Passwort2.append(zahl)
#   z +=1


# Passwort3 = Passwort1 + Passwort2
# import random             
# random.shuffle(Passwort3)
# for P in Passwort3: 
#  print(P , end='')