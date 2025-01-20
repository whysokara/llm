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
print(len(words))

## make a dictionary where every integer is mapped to a unique word
vocab={token:i for i,token in enumerate(words)}
# print(vocab)

## print first 10 words
for i,j in enumerate(vocab.items()):
	print(j)
	if(i>9):
		break

# Before we make a tokenizer, 
# we have to keep in mind some of the words might not be in the vocabulary. Hence we should add a special token for them called <|unk|>. 

words.extend(["<|unk|>"])
vocab={token:i for i,token in enumerate(words)}
print(len(words))

## Building a tokenizer
class Tokenizer:
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = { i:s for s,i in vocab.items()}
  def encode(self, text):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]  
    preprocessed = [item if item in self.str_to_int else '<|unk|>' for item in preprocessed]
    token_ids=[self.str_to_int[s] for s in preprocessed]
    return token_ids
  def decode(self, token_ids):
    tokens=[self.int_to_str[i] for i in token_ids]
    return tokens


text = 'Hello how are thee my lad'
text

tokenizer = Tokenizer(vocab)
print(tokenizer.encode(text))

## Decoder
print(tokenizer.decode(tokenizer.encode(text)))






