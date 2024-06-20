import wikipedia
#print(wikipedia.summary("Wikipedia",  sentences=1))
#print(wikipedia.search("Albert Einstein"))
# albert = wikipedia.page("Albert Einstein", auto_suggest=False)
# print(albert)
# print(albert.title, albert.content)

# Karla is coding here:
# print(albert.content)
print(wikipedia.summary("Jack Sparrow", auto_suggest=False))
characters_hints = wikipedia.summary("Jack Sparrow", auto_suggest=False)
characters_hints.split(",")
print(characters_hints)

#  To dos with the summary:
# 1. Create the hints (split on dot?)
# 2. Implement the hints in the game (Hint can be a list, end the game when list is empty)
# 2.1 You could have a list of harcoded hints ["Hint 1", "Hint 2", "Hint 3"]
# 3. Replace Albert Einstein, remove, hash
