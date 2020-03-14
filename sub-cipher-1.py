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
	#print(stored_letters)
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
	if len(one_letter_word) != 0:
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
	two_letter_freq = []
	upper_list = []
	lower_list = []
	used_list = []
	attempt1 = attempt.strip().split()
	i = 0
	while i != len(attempt1):
		if len(attempt1[i]) == 2 and attempt1[i] != attempt1[i].upper():
			#print(attempt1[i])
			two_letter_freq.append(attempt1[i])
			f = frequency_analysis(two_letter_freq)
			fr = sorted(f,key=f.get, reverse=True)
		i = i + 1

	#print(fr)
	n = 0
	for word in fr:
		first = word[0]
		second = word[1]
		if (first == first.upper()) or (second == second.upper()):
			upper_list.append(word)
		else:
			lower_list.append(word)
	new_list = upper_list + lower_list
	#print(new_list)

	i = 0
	while i != len(new_list):
		letter_1 = new_list[i][0]
		letter_2 = new_list[i][1]
		#print(new_list[i])
		two_letters = "of to in it is be as at so we he by or on do if me my up an go no us am"
		if letter_1 == (letter_1).upper() and new_list[i] != new_list[i].upper():
			regex = re.escape(letter_1.lower()) + r"\w"
			result = re.findall(regex , two_letters)
			#print(result)

			j = 0
			while result[j] in used_list:
				j = j + 1

			char = (result[j][1]).upper()
			used_list.append(result[j])
			attempt = attempt.replace(letter_2, char)
			string = " ". join(new_list)
			new_list = (string.replace(letter_2, char)).strip().split()
			if char not in used_letters:
				used_letters.append(char)


		elif letter_2 == (letter_2).upper() and new_list[i] != new_list[i].upper():
			regex = r"\w" + re.escape(letter_2.lower())
			result = re.findall(regex , two_letters)
			#print(result)

			j = 0
			while result[j] in used_list:
				j = j + 1

			char = (result[j][0]).upper()
			used_list.append(result[j])
			attempt = attempt.replace(letter_1, char)
			string = " ". join(new_list)
			new_list = (string.replace(letter_1, char)).strip().split()
			if char not in used_letters:
				used_letters.append(char)

		i = i + 1
	#print(used_list)
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

def three_letter_word_double_case(attempt):
	attempt1 = attempt.strip().split()
	three_letter_list = []
	used_list = []
	three_letters = "the and for are but not you all any can had her was one our out day get has him his how man new now old see two way who boy did its let put say she use"
	i = 0
	while i != len(attempt1):
		if len(attempt1[i]) == 3 and attempt1[i] != attempt1[i].upper() and (attempt1[i]).isalpha():
			three_letter_list.append(attempt1[i])
			freq_3 = frequency_analysis(three_letter_list)
			most_freq = sorted(freq_3,key=freq_3.get, reverse=True)
		i = i + 1

	#print(fr)
	n = 0
	upper_list = []
	lower_list = []
	for word in most_freq:
		first = word[0]
		second = word[1]
		third = word[2]
		#print(word)
		if (first == first.upper()) or (second == second.upper()) or (third == third.upper()) and word.isalpha():#########
			upper_list.append(word)
		else:
			lower_list.append(word)
	new_list = upper_list + lower_list
################################################
	i = 0
	k = 0
	while k != 2: #####iterated twice over the list.
		i = 0
		while i != len(new_list):
			letter_1 = new_list[i][0]
			letter_2 = new_list[i][1]
			letter_3 = new_list[i][2]
			#print(new_list[i])

	#Double case: One capital on the left and centre.
			if letter_1 == (letter_1).upper() and letter_2 == (letter_2).upper() and new_list[i] != new_list[i].upper():
				regex = re.escape(letter_1.lower()) + re.escape(letter_2.lower()) + r"\w"
				result = re.findall(regex , three_letters)
				#print(result)

				j = 0
				while result[j] in used_list:
					j = j + 1

				char = (result[j][2]).upper()
				used_list.append(result[j])
				attempt = attempt.replace(letter_3, char)
				string = " ". join(new_list)
				new_list = (string.replace(letter_3, char)).strip().split()
				if char not in used_letters:
					used_letters.append(char)

	#Double case: One capital on the left and far right.
			elif letter_1 == (letter_1).upper() and letter_3 == (letter_3).upper() and new_list[i] != new_list[i].upper():
				regex = re.escape(letter_1.lower()) + r"\w" + re.escape(letter_3.lower())
				result = re.findall(regex , three_letters)
				#print(result)

				j = 0
				while result[j] in used_list:
					j = j + 1

				char = (result[j][1]).upper()
				used_list.append(result[j])
				attempt = attempt.replace(letter_2, char)
				string = " ". join(new_list)
				new_list = (string.replace(letter_2, char)).strip().split()
				if char not in used_letters:
					used_letters.append(char)

	#Double case: One capital in the centre and far right.
			elif letter_2 == (letter_2).upper() and letter_3 == (letter_3).upper() and new_list[i] != new_list[i].upper():
				regex =  r"\w" + re.escape(letter_2.lower()) + re.escape(letter_3.lower())
				result = re.findall(regex , three_letters)
				#print(result)

				if len(result) != 0:
					j = 0
					while result[j] in used_list and len(result[j]) < 0:
						j = j + 1
					if result[j] not in used_list:
						char = (result[j][0]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_1, char)
						string = " ". join(new_list)
						new_list = (string.replace(letter_1, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)
			i = i + 1
		k = k + 1

	#print(upper_list)
	#print(lower_list)
	#print(used_list)
	#print(new_list)	
	return attempt


def three_letter_word_single_case(attempt):
	attempt1 = attempt.strip().split()
	three_letter_list = []
	three_letters = "the and for are but not you all any can had her was one our out day get has him his how man new now old see two way who boy did its let put say she use"
	i = 0
	while i != len(attempt1):
		if len(attempt1[i]) == 3 and attempt1[i] != attempt1[i].upper():
			three_letter_list.append(attempt1[i])
			freq_3 = frequency_analysis(three_letter_list)
			most_freq = sorted(freq_3,key=freq_3.get, reverse=True)
		i = i + 1

	#print(fr)
	n = 0
	upper_list = []
	lower_list = []
	for word in most_freq:
		first = word[0]
		second = word[1]
		third = word[2]
		#print(word)
		if (first == first.upper()) or (second == second.upper()) or (third == third.upper()) and word.isalpha():#########
			upper_list.append(word)
		else:
			lower_list.append(word)
	new_list = upper_list + lower_list
################################################
	i = 0
	while i != len(new_list):
		letter_1 = new_list[i][0]
		letter_2 = new_list[i][1]
		letter_3 = new_list[i][2]
		#print(new_list[i])

#Single case: One capital on the left.
		if letter_1 == (letter_1).upper() and new_list[i] != new_list[i].upper():
			regex = re.escape(letter_1.lower()) + r"\w\w"
			result = re.findall(regex , three_letters)
			#print(result)
#
#			j = 0
#			while result[j] in used_list:
#				j = j + 1
#
#			char = (result[j][1]).upper()
#			used_list.append(result[j])
#			attempt = attempt.replace(letter_2, char)
#			string = " ". join(new_list)
#			new_list = (string.replace(letter_2, char)).strip().split()
#			if char not in used_letters:
#				used_letters.append(char)

#Single case: One capital in the centre.
		elif letter_1 == (letter_1).lower() and letter_2 == (letter_2).upper() and letter_3 == (letter_3).lower() and new_list[i] != new_list[i].upper():
			regex = r"\w" + re.escape(letter_2.lower()) + r"\w"
			result = re.findall(regex , three_letters)
			#print(result)
#
#			j = 0
#			while result[j] in used_list:
#				j = j + 1
#
#			char = (result[j][1]).upper()
#			used_list.append(result[j])
#			attempt = attempt.replace(letter_2, char)
#			string = " ". join(new_list)
#			new_list = (string.replace(letter_2, char)).strip().split()
#			if char not in used_letters:
#				used_letters.append(char)


#		elif letter_2 == (letter_2).upper() and new_list[i] != new_list[i].upper():
#			regex = r"\w" + re.escape(letter_2.lower())
#			result = re.findall(regex , three_letters)
#			#print(result)
#
#			j = 0
#			while result[j] in used_list:
#				j = j + 1
#
#			char = (result[j][0]).upper()
#			used_list.append(result[j])
#			attempt = attempt.replace(letter_1, char)
#			string = " ". join(new_list)
#			new_list = (string.replace(letter_1, char)).strip().split()
#			if char not in used_letters:
#				used_letters.append(char)

		i = i + 1

	#print(upper_list)
	#print(lower_list)
	#print(new_list)



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
	attempt = three_letter_ending_in_E(attempt)
	attempt = two_letter_word(attempt)
	attempt = three_letter_word_double_case(attempt)

	print(attempt)
	print(used_letters)