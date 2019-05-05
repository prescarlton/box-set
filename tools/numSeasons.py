import os

owned_seasons = []
for _, seasons, _ in os.walk('../shows/Supernatural (2005)'):
    for season in seasons:
        num_episodes = sum([len(folder) for r, d, folder in os.walk('../shows/Supernatural (2005)/%s' % (season))])
        print('season:'+season)
        print("episodes:"+str(num_episodes))
        if num_episodes > 0:
            owned_seasons.append(season)
print(owned_seasons)
