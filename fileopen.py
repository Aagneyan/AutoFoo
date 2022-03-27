import subprocess

path_to_foobar = 'C:\\Program Files (x86)\\foobar2000\\foobar2000.exe'
path_to_song = 'D:\\Music\\Rock and Pop\\Linkin Park\\Linkin Park - A Thousand Suns\\16 Blackbirds (Bonus Track).wav'

subprocess.call([path_to_foobar, path_to_song])