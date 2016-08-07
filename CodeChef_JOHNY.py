for i in range(int(input())):
    n= int(input())
    songs=[int(x) for x in input().strip().split(" ")]
    orig=int(input())
    val=songs[orig-1]
    songs.sort()
    print(songs.index(val)+1)