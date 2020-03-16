import re
f = open("shite.txt", "r")
encrypted_message = f.read()
encrypted_message = encrypted_message
attempt = encrypted_message
used_letters = []
used_list = []

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
	attempt1 = attempt.strip().split()
	i = 0
	while i != len(attempt1):
		if len(attempt1[i]) == 2 and attempt1[i] != attempt1[i].upper() and attempt1[i].isalpha():
			#print(attempt1[i])
			two_letter_freq.append(attempt1[i])
		i = i + 1
	f = frequency_analysis(two_letter_freq)
	fr = sorted(f,key=f.get, reverse=True)

	#print(fr)
	n = 0
	for word in fr:
		first = word[0]
		second = word[1]
		if (first == first.upper()) or (second == second.upper()) and word != word.upper():
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

#Case 1: left is upper and right is lower.
		if letter_1 == (letter_1).upper() and new_list[i] != new_list[i].upper():
			regex = re.escape(letter_1.lower()) + r"\w"
			result = re.findall(regex , two_letters)
			#print(result)
			if len(result) != 0:
				j = 0
				while result[j][1].upper() in used_letters and j < len(result) -1:
					j = j + 1

				if result[j][1].upper() not in used_letters:
					char = result[j][1].upper()
					used_list.append(result[j])
					attempt = attempt.replace(letter_2, char)
					string = " ". join(new_list)
					new_list = (string.replace(letter_2, char)).strip().split()
					if char not in used_letters:
						used_letters.append(char)

#Case 2: lower on the left and upper on the right.
		elif letter_2 == (letter_2).upper() and new_list[i] != new_list[i].upper():
			regex = r"\w" + re.escape(letter_2.lower())
			result = re.findall(regex , two_letters)
			#print(result)

			if len(result) != 0:
				j = 0
				while result[j][0].upper() in used_letters and j < len(result) -1:
					j = j + 1

				if result[j][0].upper() not in used_letters:
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

#Double case 1: One capital on the left and centre.
			if letter_1 == (letter_1).upper() and letter_2 == (letter_2).upper() and new_list[i] != new_list[i].upper():
				regex = re.escape(letter_1.lower()) + re.escape(letter_2.lower()) + r"\w"
				result = re.findall(regex , three_letters)
				#print(result)

				if len(result) != 0:
					j = 0
					while result[j][2].upper() in used_letters and j < len(result) -1:
						j = j + 1

					if result[j][2].upper() not in used_letters:
						char = (result[j][2]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_3, char)
						string = " ". join(new_list)
						new_list = (string.replace(letter_3, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)

#Double case 2: One capital on the left and far right.
			elif letter_1 == (letter_1).upper() and letter_3 == (letter_3).upper() and new_list[i] != new_list[i].upper():
				regex = re.escape(letter_1.lower()) + r"\w" + re.escape(letter_3.lower())
				result = re.findall(regex , three_letters)
				#print(result)

				if len(result) != 0:
					j = 0
					while result[j][1].upper() in used_letters and j < len(result) -1:
						j = j + 1

					if result[j][1].upper() not in used_letters:
						char = (result[j][1]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_2, char)
						string = " ". join(new_list)
						new_list = (string.replace(letter_2, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)

#Double case 3: One capital in the centre and far right.
			elif letter_2 == (letter_2).upper() and letter_3 == (letter_3).upper() and new_list[i] != new_list[i].upper():
				regex =  r"\w" + re.escape(letter_2.lower()) + re.escape(letter_3.lower())
				result = re.findall(regex , three_letters)
				#print(result)

				if len(result) != 0:
					j = 0
					while result[j][0].upper() in used_letters and j < len(result) -1:
						j = j + 1

					if result[j][0].upper() not in used_letters:
						char = (result[j][0]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_1, char)
						string = " ". join(new_list)
						new_list = (string.replace(letter_1, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)
			i = i + 1
			#print(new_list)
			#print(used_list)
			#print(used_letters)
			#print("------------------------------------------------------------------")
		k = k + 1

	#print(upper_list)
	#print(lower_list)
	#print(used_list)
	#print(new_list)	
	return attempt

#currently not in use as not needed
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

def ending_in_ing(attempt):
	ending = []
	attempt1 = attempt.strip().split()
	for word in attempt1:
		if len(word) > 4 and word.isalpha() and word != word.upper():
			start = word[len(word)-3:]
			if "IN" in start or "NG" in start or "G" in start:
				ending.append(start)
				freq_ending = frequency_analysis(ending)
				most_freq = sorted(freq_ending,key=freq_ending.get, reverse=True)

	letter_1 = most_freq[0][0]
	letter_2 = most_freq[0][1]
	letter_3 = most_freq[0][2]

	most_freq = " ".join(most_freq)
#Put a loop her that will find the last three letters for any case not just ING.
	if letter_1 == "I" and letter_2 == "N":
		regex = re.escape(letter_1) + re.escape(letter_2) + r"\w"
		result = re.findall(regex , most_freq )

		char = "G"
		used_list.append("ing")
		attempt = attempt.replace(letter_3, char)
		if char not in used_letters:
			used_letters.append(char)





	elif letter_2 == "N" and letter_3 == "G":
		regex = r"\w" + re.escape(letter_1) + re.escape(letter_2)
		result = re.findall(regex , most_freq )

		char = "I"
		used_list.append("ing")
		attempt = attempt.replace(letter_1, char)
		if char not in used_letters:
			used_letters.append(char)		

	elif letter_1 == "I" and letter_3 == "G":
		regex = re.escape(letter_1) + r"\w" + re.escape(letter_2)
		result = re.findall(regex , most_freq )

		char = "N"
		used_list.append("ing")
		attempt = attempt.replace(letter_2, char)
		if char not in used_letters:
			used_letters.append(char)		

	#print(upper_list)
	#print(lower_list)
	#print(new_list)
	#print(result)
	return attempt

def three_letter_endings(attempt):
	ending = []
	three_freq = "the and ing ent ion her for tha nth int ere tio ter est ers hat ate all eth hes ver his oft ith fth sth oth res ont"
	attempt1 = attempt.strip().split()
	for word in attempt1:
		if len(word) > 4 and word.isalpha():
			start = word[len(word)-3:]
			if start != start.upper():
				ending.append(start)
	#print(ending)
	freq_ending = frequency_analysis(ending)
	most_freq = sorted(freq_ending,key=freq_ending.get, reverse=True)
	#print(most_freq)
#Put a loop her that will find the last three letters for any case not just ING.
	
	i = 0
	while i != len(most_freq):
		letter_1 = most_freq[i][0]
		letter_2 = most_freq[i][1]
		letter_3 = most_freq[i][2]
		#print(most_freq[i])

#Case 1: Upper on the left and in the centre.
		if letter_1 == letter_1.upper() and letter_2 == letter_2.upper() and letter_3 == letter_3.lower():
			regex = re.escape(letter_1.lower()) + re.escape(letter_2.lower()) + r"\w"
			result = re.findall(regex , three_freq )
			#print(result)

			if len(result) != 0:
				j = 0
				while result[j][2].upper() in used_letters and j < len(result) -1:
					j = j + 1

				if result[j] not in used_list:
						char = (result[j][2]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_3, char)

						string = " ". join(most_freq)
						most_freq = (string.replace(letter_3, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)




#Case 2: upper in the centre and on the right.
		elif letter_1 == letter_1.lower() and letter_2 == letter_2.upper() and letter_3 == letter_3.upper():
			regex = r"\w" + re.escape(letter_2.lower()) + re.escape(letter_3.lower())
			result = re.findall(regex , three_freq )
			#print(result)

			if len(result) != 0:
				j = 0
				while (result[j][0]).upper() in used_letters and j < len(result) -1:
					j = j + 1
				#print(j)

				if result[j] not in used_list:
						char = (result[j][0]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_1, char)

						string = " ". join(most_freq)
						most_freq = (string.replace(letter_1, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)

#Case 3: upper on the left and far right.
		elif letter_1 == letter_1.upper() and letter_2 == letter_2.lower() and letter_3 == letter_3.upper():
			regex = re.escape(letter_1.lower()) + r"\w" + re.escape(letter_3.lower())
			result = re.findall(regex , three_freq )
			#print(result)

			if len(result) != 0:
				j = 0
				while result[j][1].upper() in used_letters and j < len(result) -1:
					j = j + 1

				if result[j][1].upper() not in used_letters: ############ change this for others too.
						char = (result[j][1]).upper()
						used_list.append(result[j])
						attempt = attempt.replace(letter_2, char)

						string = " ". join(most_freq)
						most_freq = (string.replace(letter_2, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)		

		i = i + 1
	#print(upper_list)
	#print(lower_list)
	#print(new_list)
	#print(result)
	return attempt


##################################################################
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
	attempt = two_letter_word(attempt)
	#attempt = ending_in_ing(attempt) #Redundant as three_letter_endings does this except for all cases.
	attempt = three_letter_endings(attempt)

	print(attempt)
	print(used_list)
	print(used_letters)