N=int(input())

words=set()

for i in range(N):
    words.add(input())

new_sortedWords=sorted(words,key=lambda x: (len(x),x))

for word in new_sortedWords:
    print(word)