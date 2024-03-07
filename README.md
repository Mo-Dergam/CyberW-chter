#Passwortgenerator:

import string
import random 
def Password12():
  In = 0
  i = int(input("aus wie stellig soll ihr passwort sein:"))
  Z = input("Soll dein Passwort zahlen enthalten: (Ja/Nein)")
  GB = input("Soll dein passwort großbuchtaben haben: (Ja/Nein)")
  KB = input("Soll dein passwort Kleinbuchtaben haben: (Ja/Nein)")
  S = input("soll dein passwort sonderzeichen haben: (Ja/Nein)")
 # Ja, Nein, Nein, Nein
  if Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "nein":
    Password1 = string.digits
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Ja, Ja, Nein, Nein
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "nein":
    Password1 = string.digits + string.ascii_uppercase
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Ja, Ja, Ja, Nein
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "nein":
    Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Ja, Ja, Ja, Ja
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    # password = ''.join(random.choice(Password1) for _ in range(i))
    print(''.join(random.choice(Password1) for _ in range(i)), end = '')
 # Nein, Ja, Ja, Ja
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Nein, Nein, Ja, Ja
  elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Nein, Nein, Nein, Ja
  elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Ja, Ja, Nein, Ja
  elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.digits + string.ascii_uppercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Ja, Nein, Ja, Ja
  elif Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "ja":
    Password1 = string.digits + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Ja, Nein, Nein, Ja
  elif Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.digits + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Nein, Ja, Ja, Nein
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "nein":
    Password1 = string.ascii_uppercase + string.ascii_lowercase 
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Nein, Ja, Nein, Ja
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "ja":
    Password1 = string.ascii_uppercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Nein, Ja, Nein, Nein
  elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "nein":
    Password1 =  string.ascii_uppercase
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
 # Nein, Nein, Ja, Nein
  elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "nein":
    Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(Password1) for _ in range(i))
    print("Ihr Passwort wird getellt", end = '')
    while In < 5:
      print(".", end = '')
      import time 
      z = 1
      time.sleep(z)
      In += 1
    print()
    print(password)
Password12()

import time
t = 10
time.sleep(t)

quit
