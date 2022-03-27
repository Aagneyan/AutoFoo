import os
from csv import writer

from mutagen.flac import FLAC
from mutagen.mp3 import MP3


def songlist():
    f1 = open("Song Library.csv", 'w', newline='')
    wr = writer(f1)
    wr.writerow(['ID', 'TITLE', 'ARTIST', 'ALBUM', 'GENRE', 'YEAR', 'LOCATION'])
    f1.close()
    id = 1
    for dirpath, dirnames, filenames in os.walk("D:\\Music"):
        for filename in [f for f in filenames if f.endswith(".flac")]:
            song_location = dirpath
            song_location += '\\'
            song_name = filename
            song_location += song_name
            print(song_location)
            song = FLAC(song_location)
            with open("Song Library.csv", 'a', encoding='utf-8', newline='') as f_object:
                writer_obj = writer(f_object)
                song_title = song.get('TITLE', 'UNKNOWN')
                song_artist = song.get('ARTIST', 'UNKNOWN')
                song_album = song.get('ALBUM', 'UNKNOWN')
                song_genre = song.get('GENRE', 'UNKNOWN')
                song_year = song.get('YEAR', 'UNKNOWN')
                s_name = "UNKNOWN" if str(song_title[0]) == 'U' else str(song_title[0])
                ar_name = "UNKNOWN" if str(song_artist[0]) == 'U' else str(song_artist[0])
                al_name = "UNKNOWN" if str(song_album[0]) == 'U' else str(song_album[0])
                g_name = "UNKNOWN" if str(song_genre[0]) == 'U' else str(song_genre[0])
                y_name = "UNKNOWN" if str(song_year[0]) == 'U' else str(song_year[0])
                writer_obj.writerow([str(id),
                                     s_name,
                                     ar_name,
                                     al_name,
                                     g_name,
                                     y_name,
                                     str(song_location)])
                id = id + 1
        for filename in [f for f in filenames if f.endswith(".mp3")]:
            song_location = dirpath
            song_location += '\\'
            song_name = filename
            song_location += song_name
            print(song_location)
            song = MP3(song_location)
            with open("Song Library.csv", 'a', encoding='utf-8', newline='') as f_object:
                writer_obj = writer(f_object)
                song_title = song.get('TITLE', 'UNKNOWN')
                song_artist = song.get('ARTIST', 'UNKNOWN')
                song_album = song.get('ALBUM', 'UNKNOWN')
                song_genre = song.get('GENRE', 'UNKNOWN')
                song_year = song.get('YEAR', 'UNKNOWN')
                s_name = "UNKNOWN" if str(song_title[0]) == 'U' else str(song_title[0])
                ar_name = "UNKNOWN" if str(song_artist[0]) == 'U' else str(song_artist[0])
                al_name = "UNKNOWN" if str(song_album[0]) == 'U' else str(song_album[0])
                g_name = "UNKNOWN" if str(song_genre[0]) == 'U' else str(song_genre[0])
                y_name = "UNKNOWN" if str(song_year[0]) == 'U' else str(song_year[0])
                writer_obj.writerow([str(id),
                                     s_name,
                                     ar_name,
                                     al_name,
                                     g_name,
                                     y_name,
                                     str(song_location)])
                id = id + 1


songlist()
