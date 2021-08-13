input_dict = {'A' : 1965, 'B' : 1965,
              'C' : 1964, 'D' : 1964, 'E' : 1964,
              'F' : 1965, 'G' : 1965, 'H' : 1966,
              'I' : 1967, 'J' : 1967, 'K' : 1968,
              'L' : 1969, 'M' : 1969,
              'N' : 1970}

track = {}

for value in input_dict.values() :
    if value not in track :
        track[value] = 0
    else :
        track[value] += 1

print(max(track, key=track.get))
