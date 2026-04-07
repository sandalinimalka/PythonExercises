class Publication:
    def __init__(self, name: str):
        self.name = name

class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name is {self.name}")
        print(f"Author is {self.author}")
        print(f"Page count is {self.page_count}")

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
            super(). __init__(name)
            self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine name is {self.name}")
        print(f"Chief editor is {self.chief_editor}")

#Main Program
book = Book('Compartment No. 6', 'Rosa Liksom', 192)
magazine = Magazine('Donald Duck', 'Aki Hyyppä')

book.print_information()
print()
magazine.print_information()

