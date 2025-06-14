# Syntax
# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

user_input = input("Enter a name: ")
match user_input:
  case 'sovann':
    print("Hello sovann")
  case 'thavarak':
    print("Hello thavarak")
  case 'thanak':
    print("Hello thanak")
  case _:
    print("Who are you?")

# Example
day = int(input("Enter a day: "))
match day:
  case 1:
    print("Monday")
    print("Start of the week")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
# Output
# Thursday


