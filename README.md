This repo contains the code for my AutoFoo project

How it works :
  1. Run main.py and say the name of the song you want to play. EG : "play numb by linkin park"
  2. search_methods.py attempts to search for your requested song by looking through all the entries in "Song Library.csv" file
  3. "Song Library.csv" stores all your music data such as a SongID, Song Name, Artist, Album, Genre, Year and its location in your local disk. (Run songlistloader.py if this csv file is empty or to update new entries into the csv file)
  4. search_methods uses Fuzzy String Matching to find your song. So the quality of the metadata stored in your .mp3 or .FLAC files (or the data stored in Song Library.csv) heavily impacts the accuracy of the string matching.
  5. Once found, the search_methods will return the songID and the curresponding location of your song.
  6. main.py opens your music player (the location of which you need to specify within the file) and plays it for you.
  7. Requirements.txt contains a list of all the packages used in this project. 
 
Python files other than the ones I have mentioned above are currently not fully functional. They are being used to develop a trigger word detection model which removes the need to run main.py manually whenver you want to play a song. 
