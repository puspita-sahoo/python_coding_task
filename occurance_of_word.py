sentence = input("Enter your word: ")
sentence_lower = sentence.lower()
sentence_list = sentence_lower.split()

result = {}
for word in sentence_list:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)
