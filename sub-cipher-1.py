import re
f = open("shite.txt", "r")
encrypted_message = f.read()
encrypted_message = encrypted_message
attempt = encrypted_message
used_letters = []

#This will find the frequency analysis of the input that could be words or letters. The diction is a temporary dictiona that needs to be assigned a variable name in the command area at the very bottom
def frequency_analysis(input):
	distribution_freq = {}
	for char in input:
		if char not in distribution_freq:
			distribution_freq[char] = 1

		else:
			distribution_freq[char] += 1
	return distribution_freq


#Find the frequency of letters in the text and replace them with the most common letters in english [E,T,A,O,I,N]. Check if there is a big enough difference betten the frequency of words in the text as this will make predictions more accurate.
def single_letter(attempt, freq_letters, stored_letters):
	if ((stored_letters[freq_letters[0]] - stored_letters[freq_letters[1]]) >= 5):
		attempt = attempt.replace(freq_letters[0], "E")
		used_letters.append("E")
	if ((stored_letters[freq_letters[1]] - stored_letters[freq_letters[2]]) >= 15):
		attempt = attempt.replace(freq_letters[1], "T")
		used_letters.append("T")
	if ((stored_letters[freq_letters[2]] - stored_letters[freq_letters[3]]) >= 20):
		attempt = attempt.replace(freq_letters[2], "A")
		used_letters.append("A")
	return attempt

#Frequency analysis on one letter words [i, a]. "I" is more likely if it is at the start of a sentence.
#The first while loop does a frequency analysis on all capital letters the determine "I" as it should be the most frequent.

def single_letter_word(attempt, stored_letters):
	attempt1 = attempt.strip().split()
	one_letter_word = []
	i = 0
	while (i != len(attempt1)):
		if len(attempt1[i]) == 1:
			if attempt1[i].isupper():
				one_letter_word.append(attempt1[i])
		i = i + 1
	freq_of_I = frequency_analysis(one_letter_word)
	most_freq = sorted(freq_of_I,key=freq_of_I.get, reverse=True)
	attempt = attempt.lower()
	attempt = attempt.replace(most_freq[0].lower(), "I")
	if "I" not in used_letters:
		used_letters.append("I")

	i = 0
	while (i != len(attempt1)):
		if len(attempt1[i]) == 1:
			if (attempt1[i]).islower():
				attempt = attempt.replace(attempt1[i], "A")
				if "A" not in used_letters:
					used_letters.append("A")
		i = i + 1
	return attempt

def two_letter_word(attempt):
	attempt1 = attempt.strip().split()
	i = 0
	while i != len(attempt1):
		if len(attempt1[i]) == 2:
			#print(attempt1[i])
			letter_1 = attempt1[i][0]
			letter_2 = attempt1[i][1]
			#print(letter_1)
			two_letters = "of to in it is be as at so we he by or on do if me my up an go no us am"
			if letter_1 in used_letters:
				regex = re.escape(letter_1.lower()) + r"."
				result = re.findall(regex , two_letters)
				print(result)

				char = (result[0][1]).upper()
				attempt = attempt.replace(attempt1[i][1], char)
				if char not in used_letters:
					used_letters.append(char)


			elif letter_2 in used_letters:
				regex = r"." + re.escape(letter_2.lower())
				result = re.findall(regex , two_letters)
				print(result)

				char = (result[0][0]).upper()
				attempt = attempt.replace(attempt1[i][0], char)
				if char not in used_letters:
					used_letters.append(char)

		i = i + 1
	return attempt

def three_letter_ending_in_E(attempt):
	the = []
	attempt1 = attempt.strip().split()
	i = 0
	while i != len(attempt1):
		letter_3 = attempt1[i]
		if len(attempt1[i]) == 3:
			#print(attempt1[i])
			if letter_3[2] == "E": 
				the.append(letter_3) 
			#regex = r"..E$" #+ re.escape(letter_2.lower())
			#result = re.findall(regex , attempt1[i])
		i = i + 1
	freq = frequency_analysis(the)
	most_freq = sorted(freq,key=freq.get, reverse=True)
	attempt = attempt.replace(most_freq[0][0], "T")
	used_letters.append("T")
	attempt = attempt.replace(most_freq[0][1], "H")
	used_letters.append("H")
	attempt = attempt.replace(most_freq[1][0], "S")
	used_letters.append("S")
	#print(most_freq)
	return attempt


if __name__ == '__main__':
	stored_letters = frequency_analysis(encrypted_message)
	#print(stored_letters)

#Makes a list of the most frequent words from most frequent to least frequent and removes the non alpha charaters as they are already in the correct position.
	freq_letters = sorted(stored_letters,key=stored_letters.get, reverse=True)
	freq_letters.remove(" ")
	freq_letters.remove(".")
	freq_letters.remove(",")
	freq_letters.remove("-")
	freq_letters.remove("\n")

#Finding single letter words,[i,a], and check frequency pattern such as if there is full stop as "i" is more likely to appear at the beginning of sentences.
	attempt = single_letter_word(attempt,stored_letters )
	attempt = single_letter(attempt, freq_letters, stored_letters)
	#attempt = two_letter_word(attempt)
	attempt = three_letter_ending_in_E(attempt)
	print(attempt)
	print(used_letters)