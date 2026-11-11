from movies import add_movie, view_movies, load_movies

movies = load_movies()




def show_menu():
    print("   Movie Watchlist")
    print("1. Add a new movie")
    print("2. View all movies")
    print("3. Exit")

while True:
    show_menu()

    choice = input("Choose an option: ")
    if choice =="1":
        add_movie(movies)
    elif choice == "2":
        view_movies(movies)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again!")