class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title} ({self.year}) - Yönetmen: {self.director}, Tür: {self.genre}"


class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, director, year, genre):
        self.movies.append(Movie(title, director, year, genre))
        return f"'{title}' filmi eklendi."

    def delete_movie(self, index):
        if 0 <= index < len(self.movies):
            removed_movie = self.movies.pop(index)
            return f"'{removed_movie.title}' filmi silindi."
        return "Geçersiz film numarası!"

    def list_movies(self, filter_by=None, value=None):
        filtered_movies = self.movies
        if filter_by == "genre":
            filtered_movies = [movie for movie in self.movies if movie.genre.lower() == value.lower()]
        elif filter_by == "year":
            filtered_movies = [movie for movie in self.movies if movie.year == value]

        if not filtered_movies:
            print("Eşleşen film bulunamadı.")
        else:
            print("\nFilmler:")
            for i, movie in enumerate(filtered_movies, 1):
                print(f"{i}. {movie}")

    def list_all_movies(self):
        if not self.movies:
            print("Film listesi boş.")
        else:
            print("\nTüm Filmler:")
            for i, movie in enumerate(self.movies, 1):
                print(f"{i}. {movie}")


def main():
    movie_manager = MovieManager()

    while True:
        print("\n1. Film Ekle\n2. Film Sil\n3. Tüm Filmleri Listele\n4. Filmleri Filtrele (Tür)\n5. Filmleri Filtrele (Yıl)\n6. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            title = input("Film Adı: ")
            director = input("Yönetmen: ")
            year = int(input("Yıl: "))
            genre = input("Tür: ")
            print(movie_manager.add_movie(title, director, year, genre))
        elif choice == "2":
            movie_manager.list_all_movies()
            index = int(input("Silmek istediğiniz filmin numarası: ")) - 1
            print(movie_manager.delete_movie(index))
        elif choice == "3":
            movie_manager.list_all_movies()
        elif choice == "4":
            genre = input("Filtrelemek istediğiniz tür: ")
            movie_manager.list_movies(filter_by="genre", value=genre)
        elif choice == "5":
            year = int(input("Filtrelemek istediğiniz yıl: "))
            movie_manager.list_movies(filter_by="year", value=year)
        elif choice == "6":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
