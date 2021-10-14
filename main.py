def convertEnglishWordToPigLatinWord(word: str) -> str:

	alphabet: [str] = ['e', 'a', 'r', 'i', 'o', 't', 'n', 's']

	for letter in alphabet:
		if word[-1].lower() != letter:
			return word[:-1] + letter
	

	return word + "o" if word[-1].lower() != "o" or word[-1].lower() != "a" else word + "p"

print(convertEnglishWordToPigLatinWord("Language"))
print(convertEnglishWordToPigLatinWord("word"))
print(convertEnglishWordToPigLatinWord("Roneeta"))