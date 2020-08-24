# 20% of my songs are remixes
# I have 1196 songs left
# of those 1196 songs, 233 are remixes (~20%)


from remix_shuffle import tracks
from remix_shuffle import albums
from remix_shuffle.spotify import client

saved_tracks = tracks.get_user_saved_tracks()
albums.get_albums_for_saved_tracks(saved_tracks)
print len(saved_tracks)
print tracks.get_remix_count(saved_tracks)


# test code
# saved_tracks = [{
#     'track_id' : '1Lim1Py7xBgbAkAys3AGAG',
#     'track_name' : 'Lean Onk',
#     'artist_name' : 'Major Lazer',
#     'artist_id' : '738wLrAtLtCtFOLvQBXOXp'
# }]

# albums.get_albums_for_saved_tracks(saved_tracks)
