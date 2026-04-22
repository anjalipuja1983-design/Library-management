from add_books import add_book
from issue_book import issue
from show_book import show
from return_book import return_book

def library():
    while True:
        print("\n1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice.isdigit():
            choice = int(choice)
            if choice==1:   add_book()     
            elif choice==2: show()
            elif choice==3: issue()
            elif choice==4: return_book()
            elif choice==5: 
                print("Thank you")
                break
            else:
                print("Invalid choice")
        else:
            print("Invalid input")
            
library()
