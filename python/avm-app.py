class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.quantity} adet x {self.price} TL"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        for product in self.products:
            if product.name == name:
                product.quantity += quantity
                return f"{name} güncellendi. Yeni miktar: {product.quantity}"
        self.products.append(Product(name, price, quantity))
        return f"{name} sepete eklendi."

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return f"{name} sepetten çıkarıldı."
        return f"{name} sepette bulunamadı!"

    def list_cart(self):
        if not self.products:
            print("Sepet boş.")
        else:
            print("\nSepet İçeriği:")
            for i, product in enumerate(self.products, 1):
                print(f"{i}. {product}")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.products)
        return f"Toplam Tutar: {total} TL"


def main():
    cart = Cart()

    while True:
        print("\n1. Ürün Ekle\n2. Ürün Çıkar\n3. Sepeti Listele\n4. Toplam Tutarı Görüntüle\n5. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Ürün Adı: ")
            price = float(input("Ürün Fiyatı (TL): "))
            quantity = int(input("Ürün Miktarı: "))
            print(cart.add_product(name, price, quantity))
        elif choice == "2":
            name = input("Çıkarılacak Ürün Adı: ")
            print(cart.remove_product(name))
        elif choice == "3":
            cart.list_cart()
        elif choice == "4":
            print(cart.calculate_total())
        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
