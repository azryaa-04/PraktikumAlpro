nim = "260401100210"
last_nim = nim[9:]

for i in last_nim:
  if i == "0":
    print(7 * "x", end="")
    print()

    for b in range(4):
      print("x     x")

    print(7 * "x")
    print()

  elif i == "1":
    for s in range(6):
      print("  x  ")

    print()

  elif i == "2":
    print(6 * "x", end="")
    print()

    for d in range(1):
      print("     x")

    print(6 * "x", end="")
    print()

    for d in range(1):
      print("x     ")
      
    print(6 * "x", end="")
    print()
    print()


    