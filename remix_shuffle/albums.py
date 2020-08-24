from remix_shuffle.spotify import client

PAGE_SIZE = 50

def get_albums_for_saved_tracks(saved_tracks):
    albums = []
    for track in saved_tracks:
        track['albums'] = get_albums_for_artist(track.get('artist_id'))


def get_albums_for_artist(artist_id):
    albums = []
    start = 0
    while True:
        album_response = client.get_albums_for_artist(artist_id, start, PAGE_SIZE)
        if album_response is not None:
            for album in album_response.get("items"):
                albums.append({'album_id': album.get("id")
                             , 'album_name': album.get("name")})
            if len(album_response.get("items")) < PAGE_SIZE:
                break
            start += len(album_response.get("items"))

    return albums
