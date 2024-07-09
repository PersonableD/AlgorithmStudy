N=int(input())
words=[]

for i in range(N):
    num=input()
    words.append(num)

unique_words = list(set(words))

unique_words.sort(key=lambda x: (len(x),x))

for word in unique_words:
    print(word)