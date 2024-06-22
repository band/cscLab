import ast

def read_books_from_file(filename):
    books = {}
    with open(filename, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and split the line into key and value
            key, value = line.strip().split(': ', 1)
            
            # Remove the quotes around the key
            key = key.strip('"')
            if key.isdigit():
                # Use ast.literal_eval to safely evaluate the string as a Python literal
                value = ast.literal_eval(value)
                if isinstance(value, tuple):
                    books[key] = value[0]
                else:
                    books[key] = value
    return books

# Usage
filename = 'some-books-202406.txt'  # Replace with your actual filename
books = read_books_from_file(filename)

# Print the resulting dictionary to verify
for key, value in books.items():
    print(f"{key}: {value}")

