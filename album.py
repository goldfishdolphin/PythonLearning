from re import A


def make_album(artist_name, album_title):
    # Return artist name and title.
    info = f"{artist_name} {album_title}"
    return info.title()

while True:
    print("\n Please enter your favorite artist name and title :")
    print("(Enter 'q' at any time to quit)")

    a_name = input("Artist Name:")
    if a_name == 'q':
        break
    t_name = input("Title Name:")
    if t_name == 'q':
        break

information = make_album(a_name, t_name)
print(information.title())