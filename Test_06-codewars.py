'''Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance.
Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts
a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word
(the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy
glues together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find
out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length
doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
'''

#First var:
def song_decoder(song):
    song = song.upper()
    song_res = ''
    if song[0] + song[1] + song[2] != 'WUB':
        if song[1] + song[2] + song[3] != 'WUB':
            if song[2] + song[3] + song[4] != 'WUB':
                song_res += song[0] + song[1] + song[2]
            else:
                song_res += str(song[0]) + str(song[1])
        else:
            song_res += str(song[0])
    else:
        song_res = ''
    print('song_res = ', song_res)
    for i in range(3, len(song) - 2):
        if song[i] + song[i + 1] + song[i + 2] != 'WUB' and song[i - 1] + song[i] + song[i + 1] != 'WUB' and song[
            i - 2] + song[i - 1] + song[i] != 'WUB':
            if song[i - 3] + song[i - 2] + song[i - 1] == 'WUB':
                if len(song_res) == 0:
                    song_res += str(song[i])
                else:
                    song_res += ' ' + song[i]
            else:
                song_res += song[i]
    if song[-3] + song[-2] + song[-1] != 'WUB':
        if song[-4] + song[-3] + song[-2] != 'WUB':
            if song[-5] + song[-4] + song[-3] != 'WUB':
                song_res += song[-2] + song[-1]
            else:
                song_res += ' ' + song[-2] + song[-1]
        else:
            song_res += ' ' + song[-1]
    return song_res

#Second var:


song = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'

print(song_decoder(song))
#print(song_decoder2(song))
