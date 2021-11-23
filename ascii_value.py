word = input("Enter your word: ")

short_list = sorted(word, key=lambda word:ord(word))
result = ""
print(result.join(short_list) )
