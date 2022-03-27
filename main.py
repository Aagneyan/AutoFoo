import random
import subprocess
import time
import search_methods
import pandas as pd
import speech_recognition as sr

music_player_location = 'C:\\Program Files (x86)\\foobar2000\\foobar2000.exe'  # or 'D:\\Program Files\\VLC\\vlc.exe'


######################################################################################
#        This function finds the path of the song depending on the audio input       #
######################################################################################


def song_pathfinder(spoken):
    pd.set_option('display.max_colwidth', None)
    words = [i.lower() for i in spoken.split()]
    artist_name = ''
    song_df = pd.read_csv('Song Library.csv')
    songs = song_df['TITLE']
    artists = song_df['ARTIST']
    locations = song_df['LOCATION']
    albums = song_df['ALBUM']
    genres = song_df['GENRE']

    if words[1] != "anything":
        search_text = spoken.split(' ', 1)[1]
        song_id = search_methods.song_then_artist_searcher(search_text)
        # print("Song id returned : ", song_id)
        da_song = song_df.LOCATION.loc[song_df['ID'] == int(song_id)].to_string()
        da_song = da_song.replace('\u2026', '')
        print("Playing ", da_song)
        return song_df.LOCATION.loc[song_df['ID'] == int(song_id)].to_string(index=False)

    if words[1] == "anything":
        # 'anything from' proceeded by genre
        if words[2] == 'from':
            genre_name = words[3]
            songs_in_genre = []
            song_names_from_genre = []
            artist_name_from_genre = []
            for s_name, a_name, loc, genre in zip(songs, artists, locations, genres):
                if genre_name.lower() == genre.lower():
                    songs_in_genre.append(loc)
                    song_names_from_genre.append(s_name)
                    artist_name_from_genre.append(a_name)
            num = random.randint(0, len(songs_in_genre))
            print("Playing " + song_names_from_genre[num] + ' by ' + artist_name_from_genre[num])
            return songs_in_genre[num]

        # 'anything by' proceeded by artist name
        if words[2] == 'by':
            for i in range(3, len(words)):
                artist_name += words[i].lower()
                artist_name += ' '
            artist_name = artist_name[:-1]
            songs_by_artist = []
            song_names_by_artist = []
            for s_name, loc, artist in zip(songs, locations, artists):
                if artist.lower() == artist_name:
                    songs_by_artist.append(loc)
                    song_names_by_artist.append(s_name)
            num = random.randint(0, len(songs_by_artist))
            print("Playing " + song_names_by_artist[num] + ' by ' + artist_name)
            return songs_by_artist[num]

        # 'anything in' proceeded by album name
        if words[2] == 'in':
            album_name = ''
            for i in range(3, len(words)):
                album_name += words[i]
                album_name += ' '
            album_name = album_name[:-1]
            songs_in_album = []
            song_names_in_album = []
            for s_name, loc, album in zip(songs, locations, albums):
                if album_name.lower() == album.lower():
                    songs_in_album.append(loc)
                    song_names_in_album.append(s_name)
            num = random.randint(0, len(songs_in_album))
            print("Playing " + song_names_in_album[num] + ' in ' + album_name)
            # time.sleep(1.4)
            return songs_in_album[num]

    return "SNF"


######################################################################################
#                                    Driver code                                     #
######################################################################################

def listen_to_request():
    # Parallel_Processing.listen_thread.join(15)
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Listening...")
            audio2 = r.listen(source2)
            text = r.recognize_google(audio2)
            text = text.lower()
            print("You said : " + text)
            time.sleep(1)
            # print("calling function")
            song_location = song_pathfinder(text)
            # print(song_location)
            if song_location != "No Song":
                subprocess.call([music_player_location, song_location])
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occurred")


# song_pathfinder("play strike by far out")
listen_to_request()
