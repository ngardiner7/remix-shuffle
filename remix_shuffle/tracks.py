from remix_shuffle.spotify import client

PAGE_SIZE = 50

def get_user_saved_tracks():
    user_library = []
    start = 0
    while True:
        saved_track_response = client.get_user_saved_tracks(start, PAGE_SIZE)
        if saved_track_response is not None:
            for track in saved_track_response.get("items"):
                # If i want to swap out remixes will require some string manipulation. This ignores any song with remix in the name
                if "remix" not in track.get("track").get("name").lower():
                    user_library.append({'track_id': track.get("track").get("id")
                                    , 'track_name': track.get("track").get("name")
                                    # I'm assuming the primary artist is always in slot one, probably a bad assumption
                                    , 'artist_name': track.get("track").get("artists")[0]["name"]
                                    , 'artist_id': track.get("track").get("artists")[0]["id"]
                                    })
        # Worried that there are scenarios where this could break if #saved_tracks % PAGE_SIZE = 0
        if len(saved_track_response.get("items")) < PAGE_SIZE:
            break
        start += len(saved_track_response.get("items"))

    return user_library

def track_has_remix(track_name, albums):
    for album in albums:
        if "remix" in album.get('album_name').lower() and track_name in album.get('album_name'):
            return True
    return False

def get_remix_count(saved_tracks):
    counter = 0
    for track in saved_tracks:
        if track_has_remix(track.get('track_name'), track.get('albums')):
            counter += 1

    return counter
