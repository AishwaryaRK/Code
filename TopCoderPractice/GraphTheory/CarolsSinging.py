import itertools


class CarolsSinging:
    def choose(self, lyrics):
        people_knowing_songs = []
        for song_people in list(map(list, zip(*lyrics))):
            people = []
            for i, person in enumerate(song_people):
                if person == 'Y':
                    people.append(i)
            people_knowing_songs.append(people)

        people_knowing_songs.sort(key=len)
        print(people_knowing_songs)

        for i, people in enumerate(people_knowing_songs):
            other_people = set(itertools.chain.from_iterable(people_knowing_songs[:i] + people_knowing_songs[i + 1:]))
            if set(people).issubset(other_people):
                people_knowing_songs.pop(i)

        return len(people_knowing_songs)


print(CarolsSinging().choose(["YNN", "YNY", "YNY", "NYY", "NYY", "NYN"]))
