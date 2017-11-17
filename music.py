from gmusicapi import Mobileclient
import vlc
import json
import random

class music:
    def __init__(self):
        api = Mobileclient()
        api.login('roman.grout@gmail.com', 'romgroGMAIL95', Mobileclient.FROM_MAC_ADDRESS)


       # library = api.get_all_songs()


        stations = api.get_all_stations()


        station = random.choice(stations)

        tracks = api.get_station_tracks(station["id"])

        print(json.dumps(tracks, sort_keys=True, indent=4, separators=(',', ': ')))

        url = api.get_stream_url(tracks[0]['nid'], device_id=None, quality=u'hi')
        print(url)

        p = vlc.MediaPlayer(url)
        p.play()


