import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{'[✓]' if self.completed else '[ ]'} {self.name}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def list_tasks(self):
        print("\nGörevler:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, completed = line.strip().split("|")
                    self.tasks.append(Task(name, completed == "True"))


def main():
    manager = TaskManager()

    while True:
        print("\n1. Görev Ekle\n2. Görev Tamamla\n3. Görev Sil\n4. Görevleri Listele\n5. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Görev adı: ")
            manager.add_task(name)
        elif choice == "2":
            manager.list_tasks()
            index = int(input("Tamamlanan görevin numarası: ")) - 1
            manager.complete_task(index)
        elif choice == "3":
            manager.list_tasks()
            index = int(input("Silinecek görevin numarası: ")) - 1
            manager.delete_task(index)
        elif choice == "4":
            manager.list_tasks()
        elif choice == "5":
            manager.save_tasks()
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
