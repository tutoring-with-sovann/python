def printExample(value: string) -> None:
  # Call underlying system to print something to the output.
  # Question: Can you assign a variable to a return value of print?
  # Yes, if both of them are None.
  pass

# Let's look at this 'p' variable. 
# When I wrote 'p: None', that means 'p' has the data type of 'None' which is nothing.
# It doesn't hold any actual value.
p: None = printExample('This is a string');


nativePrint: None = print("Halo")