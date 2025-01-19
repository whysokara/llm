import re

File_Path = "/Users/kara/Desktop/llm/docs/Shakespeare.txt"

with open(File_Path,"r", encoding="utf-8") as file:
    raw_text = file.read()
print(f"Total number of characters in file {File_Path.split("/")[-1]} is {len(raw_text)}")
# print(raw_text[:99])

## Pre processing
preprocessed = re.split(r'([,.:;?_!"()\']|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()] ## remove all spaces and trim
# print(preprocessed)

## Creating a Vocabulary
words = sorted(set(preprocessed))
# print(len(words))

## make a dictionary where every integer is mapped to a unique word
vocab={token:i for i,token in enumerate(words)}
# print(vocab)

## print first 10 words
for i,j in enumerate(vocab.items()):
	print(j)
	if(i>9):
		break
