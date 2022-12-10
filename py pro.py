Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def autoconv():
...  h=["eur","usd","pound","cad","cny","rub"]
...  print("Currency Converter*n")
...  fro=input("Input source currency code to convert to INR"
...  "\n(Euro=eur,USD=usd,Pound Sterling=pound,"
...  "\nCanadian Dollar=cad,Chinese Yuan=cny,Russian Ruble=rub): ")
...  while fro not in h:
...  print("Invalid Currency")
...  fro=input("Enter again: ")
...  val=float(input("Input value: "))
...  verted=0
...  if fro=="eur":
...  verted=val*84.34
...  elif fro=="usd":
...  verted=val*81.52
...  elif fro=="pound":
...  verted=val*96.92
...  elif fro=="cad":
...  verted=val*60.77
...  elif fro=="cny":
...  verted=val*11.45
...  elif fro=="rub":
...  verted=val*1.34
...  print("{} INR = {:.2f} {}".format(val,verted,fro))
... choice="Y"
... while choice=="Y": autoconv()
