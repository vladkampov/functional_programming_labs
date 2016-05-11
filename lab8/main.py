import pickle
from prettytable import PrettyTable


class Film:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating


def get_main_menu_choice():
    """
    Get main menu input from console.
    """
    return input("""
Choose one of menu items:
1. List all films.
2. Add new film.
3. Delete film.
4. List film by mask.
5. Find film by name.
6. Find film by directors name.
7. Find by rating.
8. Exit\n
Enter value: """)


def pretty_print(films_list):
    if films_list:
        table = PrettyTable(["Title", "Director", "Year", "Rating"])
        for film in films_list:
            table.add_row([film.title, film.director, film.year, film.rating])
        table.sort_key("Title")
        print(table)
    else:
        print("No such film.\n")


def main():
    """
    Main interface function. Provides menu functionality.
    """
    try:
        with open("db.pkl", "rb") as pickle_file:
            films = pickle.load(pickle_file)
    except:
        films = []

    while True:
        try:
            choice = int(get_main_menu_choice())
            assert(1 <= choice <= 8)

            if choice == 1:
                pretty_print(films)
            elif choice == 2:
                title = input("Enter film title: ")
                director = input("Enter film director: ")
                year = input("Enter film year: ")
                rating = input("Enter film rating: ")
                films.append(Film(title, director, year, rating))
                print("\nFilm has been successfully added.\n")
            elif choice == 3:
                title = input("Enter film title: ")
                films = [film for film in films if film.title != title]
                print("\nFilm has been successfully deleted.\n")
            elif choice == 4:
                mask = input("Enter mask for film title: ")
                divided = mask.split('*')
                if len(divided) > 1:
                    start, end = divided[0], divided[1]
                    result = [film for film in films
                              if film.title.startswith(start) and film.title.endswith(end)]
                else:
                    result = [film for film in films if film.title == mask]
                pretty_print(result)
            elif choice == 5:
                title = input("Enter film title: ")
                result = [film for film in films if film.title == title]
                pretty_print(result)
            elif choice == 6:
                director = input("Enter film director: ")
                result = [film for film in films if film.director == director]
                pretty_print(result)
            elif choice == 7:
                rating = input("Enter film rating: ")
                result = [film for film in films if film.rating == rating]
                pretty_print(result)
            elif choice == 8:
                with open("db.pkl", "wb") as pickle_file:
                    pickle.dump(films, pickle_file)
                return

        except ValueError:
            print("Wrong value! Enter number.")
        except AssertionError:
            print("Enter value between 1 and 7.")
        except Exception as e:
            print(e.args[0])
            return

if __name__ == "__main__":
    main()
