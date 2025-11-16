library_catalog = {
    'b1': {'title': ['Dune'], 'author': ['Frank Herbert'], 'genres': ['Sci-Fi, Adventure']},
    'b2': {'title': ['Dune'], 'author': ['Frank Herbert'], 'genres': ['Sci-Fi, Adventure']},
    'b3': {'title': ['1984'], 'author': ['George Orwell'], 'genres': ['Dystopian, Political Fiction']},
    'b4': {'title': ['The Hobbit'], 'author': ['J.R.R. Tolkien'], 'genres': ['Fantasy, Adventure']},
    'b5': {'title': ['1984'], 'author': ['George Orwell'], 'genres': ['Dystopian, Political Fiction']},
}

unique_books = {}

for key, value in library_catalog.items():
    if value not in unique_books.values():
        unique_books[key] = value

print("Unique books:")
print(unique_books)

print("Total unique books:", len(unique_books))

sorted_titles = sorted(book['title'][0] for book in unique_books.values())
print("Sorted titles:", sorted_titles)
