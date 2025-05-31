age = int(input("Enter your age:"))
if age > 0:
    print("You're a kid.")
elif age >= 13:
    print("You're a teenager.")
elif age >= 20:
    print("You're an adult")
elif age >= 45:
    print("You're a middle age person.")
else:
    print("You're a senior.")