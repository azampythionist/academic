import time

def menu():
 while True:
  print("\n==================")
  print("1. Balance Enquiry")
  print("2. Withrawal")
  print("3. Deposit")
  print("4. Money Transfer")
  print("5. Exit")
  print("==================\n")
  op=int(input("Enter your option :"))
  if op==5:
   print("Thank you..... visit again")
   break
  elif op==1:
   ch=input("Do u want a receipt ? y/n :")
   if ch.upper()=="Y":
    print("processing.....")
    time.sleep(5)
    print("Collect ur receipt")
    break
   else :
    print("Your Account Balance is 10,000")
    break
  elif op==2:
   c=int(input("Enter the amount: "))
   if c==100:
    print("Transaction is under process....")
    time.sleep(5)
    print("Collect ur cash.")
    break
   elif c==200:
    print("Transaction is under process....")
    time.sleep(5)
    print("Collect ur cash.")
    break
   elif c==500:
    print("Transaction is under process....")
    time.sleep(5)
    print("Collect ur cash.")
    break
   else:
    print("Invalid amount or insufficient balance.")
    break
  elif op==3:
    de=int(input("Enter the amount to be deposited :"))
    ok=input("PRESS ok/cancel :")
    if ok.upper()=="OK":
      print("Processing....")
      time.sleep(5)
      print("Amount deposited successfully.")
      break
    else:
      break
    
  elif op==4:
    mt=int(input("Enter the account number to transfer the money :"))
    if mt==9819657431:
     m=int(input("Enter the amount to be transferred :"))
     ok = input("PRESS ok/cancel :")
     if ok.upper() == "OK":
      print("Processing....")
      time.sleep(5)
      print("Money transferred successfully.")
      break
     else:
      break
    if mt==9137118744:
     m=int(input("Enter the amount to be transferred :"))
     ok = input("PRESS ok/cancel :")
     if ok == "ok":
      print("Processing....")
      time.sleep(5)
      print("Money transferred successfully.")
      break
     else:
      break
    if mt==9322521586:
     m=int(input("Enter the amount to be transferred :"))
     ok = input("PRESS ok/cancel :")
     if ok == "ok":
      print("Processing....")
      time.sleep(5)
      print("Money transferred successfully.")
      break
     else:
      break
  return
  
bal=0
while True:
 print("\n\n----------Welcome to KGN bank----------")
 acc=int(input("Enter your Account no :"))
 if acc==9819657431:
  print("\n===========================")
  print("Name: Khan Azam")
  print("DOB: 06/06/2000")
  print("UID: 543351991897")
  print("===========================\n")
  pin=int(input("Enter ur pin :"))
  if pin==7866:
   bal=5000
   print(menu())
  else :
   print("incorrect pin")
 elif acc==9137118744 :
  print("\n===========================")
  print("Name: Pushpendra Sharma")
  print("DOB: 26/12/1990")
  print("UID: 919181816999")
  print("===========================\n")
  pin=int(input("Enter ur pin :"))
  if pin==1234:
   print(menu())
  else :
   print("incorrect pin")
 elif acc==9322521586:
  print ("\n===========================")
  print("Name: Khan Faisal")
  print("DOB: 05/06/2003")
  print("UID: 987654321699")
  print("===========================\n")
  pin = int(input("Enter ur pin :"))
  if pin ==9876:
   print(menu())
  else:
   print("incorrect pin")

 else :
  print("Account number does nt exists.")
  print("plz....enter valid acc no")
