import json


def add_movie(movies):
    while True:
        title = input("Movie title: ")
        if title.strip():
            break
        else:
            print("Title cannot be empty!")

    while True:
        try:
            release_year = int(input("Release year: "))

            if release_year > 1888:
                break
            else:
                print("Please enter a valid release year.")

        except ValueError:
            print("Please enter a number!")
    while True:
        genre = input("Genre: ").split(",")

        genre = [g.strip() for g in genre if g.strip()]

        if genre:
            break
        else:
            print("Genre cannot be empty!")
    while True:
        imdb_url = input("IMDb URL: ").strip()

        if imdb_url.startswith("https://www.imdb.com/title/"):
            break
        else:
            print("Please enter a valid IMDb URL!")

    movie = {
        "title": title,
        "release_year": release_year,
        "genre": [g.strip() for g in genre],
        "imdb_url": imdb_url
    }

    movies.append(movie)
    save_movies(movies)

    print("Movie added successfully!")

def view_movies(movies):

    if not movies:
        print("There are no movies in your watchlist.")
        return


    for index, movie in enumerate(movies, start=1):
        print(f"\n{index}. {movie['title']}")
        print(f"   Release year: {movie['release_year']}")
        print(f"   Genre: {', '.join(movie['genre'])}")
        print(f"   IMDb: {movie['imdb_url']}")

def save_movies(movies):
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)

def load_movies():
    try:
        with open("movies.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []