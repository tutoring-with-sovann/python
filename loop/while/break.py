# Scenario: Imagine you’re searching for your favorite book in a library. You check each shelf, but if you find the book, you stop looking.

shelf = 1
favorite_book = 3
while shelf <= 5:
    if shelf == favorite_book:
        print(f"Found my book on shelf {shelf}!")
        break  # Stop searching once book is found
    print(f"Checking shelf {shelf}...")
    shelf += 1
    
# Explanation: The break stops the loop when the book is found on shelf 3, mimicking how you’d stop searching in real life.