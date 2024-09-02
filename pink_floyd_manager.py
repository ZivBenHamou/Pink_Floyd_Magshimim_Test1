import os  # Importing the os module to handle file-related operations

# Function to load the database from a text file
def load_database(filename):
    database = {}  # Initialize an empty dictionary to store album and song data
    current_album = None  # Variable to keep track of the current album while reading the file

    # Check if the file exists, if not - print a message and return an empty dictionary
    if not os.path.exists(filename):
        print(f"File '{filename}' not found!")
        return {}

    # Open the file and read it line by line
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove any leading or trailing whitespace from the line

            # Check if the line indicates the start of a new album
            if line.startswith("#"):
                current_album = line[1:]  # Remove the '#' symbol and store the album name
                database[current_album] = []  # Add the album to the dictionary with an empty list for songs

            # Check if the line indicates the start of a new song
            elif line.startswith("*"):
                song_data = line[1:].split("::")  # Split the song details by '::'

                # Build a dictionary for the song using the extracted details
                song_info = {
                    "title": song_data[0],  # The song title
                    "writer": song_data[1],  # The songwriter
                    "length": song_data[2],  # The duration of the song
                    "lyrics": song_data[3] if len(song_data) > 3 else ""  # The lyrics of the song
                }
                # Add the song to the list of songs for the current album
                database[current_album].append(song_info)

            # If the line doesn't indicate a new album or song, it's likely part of the song's lyrics
            elif current_album and database[current_album]:
                # Append the current line to the lyrics of the last added song
                database[current_album][-1]["lyrics"] += "\n" + line

    return database  # Return the built database

# Function to list all albums
def list_albums(database):
    print("Albums:")
    for album in database.keys():  # Iterate over all albums in the database
        print(f"- {album}")  # Print the name of each album

# Function to list all songs in a specified album
def list_songs_in_album(database):
    album_name = input("Enter album name: ").strip()  # Get the album name from the user
    for album in database:  # Iterate over all albums to find the specified one
        if album.lower() == album_name.lower():  # Compare without case sensitivity
            print(f"Songs in '{album}':")
            for song in database[album]:  # Iterate over all songs in the album
                print(f"- {song['title']}")  # Print the title of each song
            return
    print("Album not found.")  # If the album wasn't found, print an appropriate message

# Function to get the length of a specified song
def get_song_length(database):
    song_name = input("Enter song name: ").strip()  # Get the song name from the user
    for album in database.values():  # Iterate over all albums
        for song in album:  # Iterate over all songs in each album
            if song["title"].lower() == song_name.lower():  # Find the song by its title
                print(f"Length of '{song['title']}': {song['length']}")  # Print the length of the song
                return
    print("Song not found.")  # If the song wasn't found, print an appropriate message

# Function to get the lyrics of a specified song
def get_song_lyrics(database):
    song_name = input("Enter song name: ").strip()  # Get the song name from the user
    for album in database.values():  # Iterate over all albums
        for song in album:  # Iterate over all songs in each album
            if song["title"].lower() == song_name.lower():  # Find the song by its title
                print(f"Lyrics of '{song['title']}']:\n{song['lyrics']}")  # Print the lyrics of the song
                return
    print("Song not found.")  # If the song wasn't found, print an appropriate message

# Function to find the album in which a specified song is located
def find_album_by_song(database):
    song_name = input("Enter song name: ").strip()  # Get the song name from the user
    for album, songs in database.items():  # Iterate over all albums and their songs
        for song in songs:
            if song["title"].lower() == song_name.lower():  # Find the song by its title
                print(f"The song '{song['title']}' is in the album '{album}'.")  # Print the album name
                return
    print("Song not found.")  # If the song wasn't found, print an appropriate message

# Function to search for songs by their title
def search_song_by_name(database):
    search_term = input("Enter search term: ").strip().lower()  # Get a search term from the user
    print("Matching songs:")
    for album, songs in database.items():  # Iterate over all albums and their songs
        for song in songs:
            if search_term in song["title"].lower():  # Search for the term in the song title
                print(f"- {song['title']} (Album: {album})")  # Print the song title and its album

# Function to search for songs by their lyrics
def search_song_by_lyrics(database):
    search_term = input("Enter search term: ").strip().lower()  # Get a search term from the user
    print("Songs containing the term:")
    for album, songs in database.items():  # Iterate over all albums and their songs
        for song in songs:
            if search_term in song["lyrics"].lower():  # Search for the term in the song lyrics
                print(f"- {song['title']} (Album: {album})")  # Print the song title and its album

# Main function to manage the program's menu
def main():
    database = load_database("Pink_Floyd_DB.txt")  # Load the database from the file

    while True:
        print("\nPink Floyd Discography Manager")
        print("1. List Albums")
        print("2. List Songs in Album")
        print("3. Get Song Length")
        print("4. Get Song Lyrics")
        print("5. Find Album by Song")
        print("6. Search Song by Name")
        print("7. Search Song by Lyrics")
        print("8. Exit")
        choice = input("Choose an option: ")  # Get the user's choice

        if choice == "1":
            list_albums(database)  # List all albums
        elif choice == "2":
            list_songs_in_album(database)  # List all songs in a specified album
        elif choice == "3":
            get_song_length(database)  # Get the length of a specified song
        elif choice == "4":
            get_song_lyrics(database)  # Get the lyrics of a specified song
        elif choice == "5":
            find_album_by_song(database)  # Find the album where a specified song is located
        elif choice == "6":
            search_song_by_name(database)  # Search for songs by title
        elif choice == "7":
            search_song_by_lyrics(database)  # Search for songs by lyrics
        elif choice == "8":
            print("Exiting the program.")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid choices

if __name__ == "__main__":
    main()  # Run the main function
