# empty dictionary to store all show information
shows = {}

with open('../tv.txt', 'r') as f:
    show_names = f.readlines()

show_names.sort()

for index, show in enumerate(show_names):
    show = show.strip()
    show_name = show.split('//')[0]
    year = show.split('//')[1]
    num_seasons = int(show.split('//')[2])
    show_names[index] = show.strip()
    if show_name in shows:
        if shows[show_name]["year"] == year:
            continue

    shows[show_name] = {
        "year": year,
        "seasons": num_seasons
    }


for show in shows:
    with open('../shows.txt', 'a') as f:
        f.write("%s (%d) \n" % (show, int(shows[show]["year"])))
        for i in range(shows[show]["seasons"]):
            f.write("[%d]" % (i+1))
        f.write("\n")
        f.write("\n")
