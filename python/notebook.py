from datetime import datetime

class Note:
    def __init__(self, content, date=None):
        self.content = content
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.date}] {self.content}"


class Notebook:
    def __init__(self, filename="notebook.txt"):
        self.notes = []
        self.filename = filename
        self.load_notes()

    def add_note(self, content):
        note = Note(content)
        self.notes.append(note)
        self.save_notes()
        return "Not eklendi."

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            removed_note = self.notes.pop(index)
            self.save_notes()
            return f"'{removed_note.content}' silindi."
        return "Geçersiz not numarası!"

    def list_notes(self):
        if not self.notes:
            print("Not defteri boş.")
        else:
            print("\nNotlar:")
            for i, note in enumerate(self.notes, 1):
                print(f"{i}. {note}")

    def save_notes(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for note in self.notes:
                file.write(f"{note.date}|{note.content}\n")

    def load_notes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    date, content = line.strip().split("|", 1)
                    self.notes.append(Note(content, date))
        except FileNotFoundError:
            pass  # Dosya yoksa notları yükleme.


def main():
    notebook = Notebook()

    while True:
        print("\n1. Not Ekle\n2. Not Sil\n3. Notları Listele\n4. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            content = input("Not İçeriği: ")
            print(notebook.add_note(content))
        elif choice == "2":
            notebook.list_notes()
            index = int(input("Silmek istediğiniz notun numarası: ")) - 1
            print(notebook.delete_note(index))
        elif choice == "3":
            notebook.list_notes()
        elif choice == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
