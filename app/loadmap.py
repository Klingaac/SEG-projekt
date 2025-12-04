import json
import marble_class
import track_class

mapFile = "map1.json"

with open(mapFile, "r", encoding="utf-8") as f:
    mapData = json.load(f)

    data = mapData["data"]

    marbles = mapData.get("marbles", {})
    tracks = mapData.get("tracks", {})

    # create all marbles and tracks from file via assigning them their classes
    for i, marble in enumerate(marbles):
        x = marble.get("x")
        y = marble.get("y")
        marble_class.marble(x, y)

    for i, track in enumerate(tracks):
        x1 = track.get("x1")
        y1 = track.get("y1")
        x2 = track.get("x2")
        y2 = track.get("y2")
        width = track.get("width") 
        track_class.track(x1, y1, x2, y2, width)

    print("works")
