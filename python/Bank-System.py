class User:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} TL yatırıldı. Yeni bakiyeniz: {self.balance} TL"
        return "Geçersiz tutar!"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"{amount} TL çekildi. Kalan bakiyeniz: {self.balance} TL"
        elif amount > self.balance:
            return "Yetersiz bakiye!"
        return "Geçersiz tutar!"

    def __str__(self):
        return f"Hesap Sahibi: {self.name}, Hesap No: {self.account_number}, Bakiye: {self.balance} TL"


class Bank:
    def __init__(self):
        self.users = {}

    def create_account(self, name, account_number, initial_balance=0):
        if account_number in self.users:
            return "Bu hesap numarası zaten kayıtlı!"
        self.users[account_number] = User(name, account_number, initial_balance)
        return "Hesap başarıyla oluşturuldu!"

    def find_user(self, account_number):
        return self.users.get(account_number, None)

    def list_accounts(self):
        if not self.users:
            print("Banka hesabı bulunmuyor.")
        else:
            for user in self.users.values():
                print(user)


def main():
    bank = Bank()

    while True:
        print("\n1. Hesap Aç\n2. Para Yatır\n3. Para Çek\n4. Bakiye Sorgula\n5. Hesapları Listele\n6. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Adınız: ")
            account_number = input("Hesap Numarası: ")
            initial_balance = float(input("Başlangıç bakiyesi (isteğe bağlı): ") or 0)
            print(bank.create_account(name, account_number, initial_balance))
        elif choice == "2":
            account_number = input("Hesap Numarası: ")
            user = bank.find_user(account_number)
            if user:
                amount = float(input("Yatırılacak Tutar: "))
                print(user.deposit(amount))
            else:
                print("Hesap bulunamadı!")
        elif choice == "3":
            account_number = input("Hesap Numarası: ")
            user = bank.find_user(account_number)
            if user:
                amount = float(input("Çekilecek Tutar: "))
                print(user.withdraw(amount))
            else:
                print("Hesap bulunamadı!")
        elif choice == "4":
            account_number = input("Hesap Numarası: ")
            user = bank.find_user(account_number)
            if user:
                print(user)
            else:
                print("Hesap bulunamadı!")
        elif choice == "5":
            bank.list_accounts()
        elif choice == "6":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
