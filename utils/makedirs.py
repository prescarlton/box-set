import os
shows = []
badchars = ['/', '\\', '?', '>', '<', '|', '"', '*']
with open('../shows.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line[0] != '[' and line != '\n':
        show = line
        for oof in badchars:
            show = show.replace(oof, '')
        shows.append(show.strip())

for show in shows:
    if not os.path.exists('../shows/'+show):
        os.makedirs('../shows/'+show)
