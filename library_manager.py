import json
import os

def load_library():
    """Load library data from JSON file if exists"""
    try:
        with open('library.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_library(library):
    """Save library data to JSON file"""
    with open('library.json', 'w') as f:
        json.dump(library, f, indent=4)

def display_menu():
    """Display the main menu options"""
    print("\nPersonal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for books")
    print("4. Display all books")
    print("5. Show statistics")
    print("6. Exit")

def add_book(library):
    """Add a new book to the library with input validation"""
    print("\nAdd New Book")
    book = {
        'title': input("Enter book title: ").strip(),
        'author': input("Enter author: ").strip(),
        'year': None,
        'genre': input("Enter genre: ").strip(),
        'read': False
    }
    
    # Validate publication year
    while True:
        try:
            book['year'] = int(input("Enter publication year: "))
            if book['year'] < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid year. Please enter a positive integer.")
    
    # Validate read status
    read_input = input("Have you read this book? (yes/no): ").lower()
    book['read'] = read_input in ['yes', 'y']
    
    library.append(book)
    print(f"'{book['title']}' added successfully!")

def remove_book(library):
    """Remove a book by title (case-insensitive)"""
    title = input("\nEnter title of book to remove: ").strip().lower()
    initial_count = len(library)
    
    library[:] = [book for book in library 
                 if book['title'].lower() != title]
    
    removed_count = initial_count - len(library)
    if removed_count > 0:
        print(f"Removed {removed_count} book(s)")
    else:
        print("No books found with that title")

def search_books(library):
    """Search books by title or author with partial matching"""
    print("\nSearch Options:")
    print("1. By Title")
    print("2. By Author")
    choice = input("Enter search type (1-2): ")
    
    search_term = input("Enter search term: ").lower()
    results = []
    
    for book in library:
        if choice == '1' and search_term in book['title'].lower():
            results.append(book)
        elif choice == '2' and search_term in book['author'].lower():
            results.append(book)
    
    if results:
        print(f"\nFound {len(results)} matching book(s):")
        display_books(results)
    else:
        print("No matching books found")

def display_books(books):
    """Display books in formatted list"""
    for i, book in enumerate(books, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} "
              f"({book['year']}) - {book['genre']} - {status}")

def show_statistics(library):
    """Calculate and display library statistics"""
    total = len(library)
    read_count = sum(book['read'] for book in library)
    percentage = (read_count / total * 100) if total > 0 else 0
    
    print("\nLibrary Statistics")
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

def main():
    """Main program loop"""
    library = load_library()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            print("\nYour Library:")
            display_books(library)
        elif choice == '5':
            show_statistics(library)
        elif choice == '6':
            save_library(library)
            print("\nLibrary saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6")

if __name__ == "__main__":
    main()