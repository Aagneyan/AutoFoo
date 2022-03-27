from fuzzywuzzy import process, fuzz
import pandas as pd

# import speech_recognition as sr

######################################
# Global dataframes used by the code #
######################################
song_df = pd.read_csv('Song Library.csv')
ids = song_df['ID'].tolist()
songs = song_df['TITLE'].tolist()
artists = song_df['ARTIST'].tolist()
locations = song_df['LOCATION'].tolist()
albums = song_df['ALBUM'].tolist()
genres = song_df['GENRE'].tolist()

# REDACTED. THIS FUNCTION SHOULD NOT BE CALLED
'''
def attached_searcher(text):
    song_name = ''
    artist_name = ''
    words = [i.lower() for i in text.split()]
    x = len(words)
    for i in range(0, len(words)):
        if words[i] == 'by':
            x = i
            break
        song_name += words[i]
        song_name += ' '
    song_name = song_name[:-1]
    for i in range(x + 1, len(words)):
        artist_name += words[i]
        artist_name += ' '
    artist_name = artist_name[:-1]
    print("Song name: " + song_name + " Artist name: " + artist_name)
    query = song_name if artist_name == '' else " ".join([song_name, artist_name])

    t_songs = [" ".join([str(i), s, a]) for i, s, a in zip(ids, songs, artists)]

    recommendations = process.extract(query, t_songs)

    return recommendations[0][0].split()[0] if recommendations[0][1] >= 75 else "Nothing"
'''


# DEFAULT search function : "PLAY song_name BY artist_name"
def song_then_artist_searcher(text):
    # print("I got : ", text)
    song_name = ''
    artist_name = ''
    words = [i.lower() for i in text.split()]
    x = len(words)
    for i in range(0, len(words)):
        if words[i] == 'by':
            x = i
            break
        song_name += words[i]
        song_name += ' '
    song_name = song_name[:-1]
    for i in range(x + 1, len(words)):
        artist_name += words[i]
        artist_name += ' '
    artist_name = artist_name[:-1]
    # print("Song name: " + song_name + " Artist name: " + artist_name)
    t_songs = [" ".join([str(i), s]) for i, s in zip(ids, songs)]
    r1 = process.extract(song_name, t_songs, scorer=fuzz.ratio)
    # print(r1)
    # if r1[0][1] < 75:
    #   return "Nothing"

    numbs = [int(x[0].split()[0]) for x in r1]
    # print(numbs)
    new_df = song_df.set_index('ID').loc[numbs].reset_index(inplace=False)
    # print(new_df)
    new_artists = new_df["ARTIST"].tolist()
    a_songs = [" ".join([str(i), s.lower()]) for i, s in zip(numbs, new_artists)]
    # print(a_songs)
    recommendations = process.extract(artist_name, a_songs)
    # print("My recommendations")
    # print(recommendations)
    song_id_to_return = recommendations[0][0].split()[0]
    return song_id_to_return


######################################
#       Use for debugging only       #
######################################

'''r = sr.Recognizer()

with sr.Microphone() as source2:
    audio2 = r.listen(source2)
    text = r.recognize_google(audio2)
    text = text.lower()'''

# print("You said : ", text)
# rec1 = attached_searcher(text)
# print(fuzz.partial_token_set_ratio("Joseph and suneo", "172 Josse and tsueno"))
# rec2 = song_then_artist_searcher("something by someone")
# print(rec1)
# print(rec2)
