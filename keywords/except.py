# --- except: if an exception happens, do this ----
try:
  print(x)
except NameError:
  print("Variable x is not defined. this would have been a NameError.")
except:
  print("Something else went wrong")
