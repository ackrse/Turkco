class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.title}' ödünç alındı."
        return f"'{self.title}' zaten ödünç alınmış."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.title}' geri teslim edildi."
        return f"'{self.title}' zaten kütüphanede."

    def __str__(self):
        status = "Ödünç Alınmış" if self.is_borrowed else "Mevcut"
        return f"Kitap: {self.title}, Yazar: {self.author}, Durum: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        return f"'{title}' kütüphaneye eklendi."

    def list_books(self, show_borrowed=False):
        if not self.books:
            print("Kütüphanede kitap yok.")
            return

        print("\nKütüphane Kitapları:")
        for i, book in enumerate(self.books, 1):
            if show_borrowed or not book.is_borrowed:
                print(f"{i}. {book}")

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            return self.books[index].borrow()
        return "Geçersiz kitap numarası!"

    def return_book(self, index):
        if 0 <= index < len(self.books):
            return self.books[index].return_book()
        return "Geçersiz kitap numarası!"


def main():
    library = Library()

    while True:
        print("\n1. Kitap Ekle\n2. Kitapları Listele\n3. Kitap Ödünç Al\n4. Kitap Geri Ver\n5. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            title = input("Kitap Adı: ")
            author = input("Yazar Adı: ")
            print(library.add_book(title, author))
        elif choice == "2":
            show_borrowed = input("Ödünç alınmış kitapları da listelemek ister misiniz? (E/H): ").strip().lower() == "e"
            library.list_books(show_borrowed)
        elif choice == "3":
            library.list_books()
            index = int(input("Ödünç almak istediğiniz kitabın numarası: ")) - 1
            print(library.borrow_book(index))
        elif choice == "4":
            library.list_books(show_borrowed=True)
            index = int(input("Geri vermek istediğiniz kitabın numarası: ")) - 1
            print(library.return_book(index))
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
