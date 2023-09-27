class Album:
    def __init__(self, albumName, albumArtist, numberOfSongs):
        self.albumName = albumName
        self.albumArtist = albumArtist
        self.numberOfSongs = numberOfSongs

    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"

if __name__ == '__main__':
    # Creating albums1 list and adding 5 albums
    albums1 = [
        Album("Album1", "Artist1", 10),
        Album("Album2", "Artist2", 12),
        Album("Album3", "Artist3", 11),
        Album("Album4", "Artist4", 14),
        Album("Album5", "Artist5", 13)
    ]

    print("Albums1:")
    for album in albums1:
        print(album)

    # Sorting albums1 by numberOfSongs
    albums1.sort(key=lambda x: x.numberOfSongs)
    print("\nSorted by numberOfSongs:")
    for album in albums1:
        print(album)

    # Swapping element at position 1 with position 2
    albums1[1], albums1[2] = albums1[2], albums1[1]
    print("\nAfter swapping position 1 and 2:")
    for album in albums1:
        print(album)

    # Creating albums2 and adding 5 albums
    albums2 = [
        Album("Album6", "Artist6", 9),
        Album("Album7", "Artist7", 10),
        Album("Album8", "Artist8", 11),
        Album("Album9", "Artist9", 12),
        Album("Album10", "Artist10", 13)
    ]

    print("\nAlbums2:")
    for album in albums2:
        print(album)

    # Copying albums from albums1 to albums2
    albums2.extend(albums1)

    # Adding two albums to albums2
    albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
    albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

    # Sorting albums2 alphabetically according to the album name
    albums2.sort(key=lambda x: x.albumName)
    print("\nSorted by album name:")
    for album in albums2:
        print(album)

    # Searching for the album “Dark Side of the Moon” in albums2
    for idx, album in enumerate(albums2):
        if album.albumName == "Dark Side of the Moon":
            print(f"\nIndex of 'Dark Side of the Moon' in albums2: {idx}")
            break
