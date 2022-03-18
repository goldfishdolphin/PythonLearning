def make_album(artist_name, album_title, songs= None):
    # Make a dictionary of artist and album title.
    album = {'artist':artist_name , 'title':album_title }
    if songs:
        album['Number of songs'] = songs
    return album

print(make_album('madona', 'halo', songs=10))
print(make_album('james blunt', 'beautiful', songs=11))
print(make_album('bryan adams', 'summer of 69', songs=12))

