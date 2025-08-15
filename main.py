import re
from collections import defaultdict

text = "Mr. and Mrs. Smith have one son and one daughter. The son's name is John. The daughter's name is Sarah. The Smiths live in a house. They have a living room. They watch TV in the living room. The father cooks food in the kitchen. They eat in the dining room. The house has two bedrooms. They sleep in the bedrooms. They keep their clothes in the closet. There is one bathroom. They brush their teeth in the bathroom.The house has a garden. John and Sarah play in the garden. They have a dog. John and Sarah like to play with the dog."

words = [word.lower() for word in re.findall(r'\w+', text, flags=re.UNICODE)]

word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

sorted_word_count = sorted(word_count.items())

for word, count in sorted_word_count:
    print(f"{word}: {count}")