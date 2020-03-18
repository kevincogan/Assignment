import re
characters = "1234567890@%#'$[]/()*:,!;-_\n.?}{`<>+&‘—”“’" + '"=£éàêöæñ'

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
def single_letter(attempt):
	attempt_count = attempt.lower()
	for char in characters:
		if char in attempt_count:
			attempt_count = attempt_count.replace(char, "")
#			print(char)

	freq_single_letters = frequency_analysis(attempt_count)
	sorted_freq_letters = sorted(freq_single_letters,key=freq_single_letters.get, reverse=True)
	sorted_freq_letters.remove(" ")
#	print(freq_single_letters)
#	print("-----------------------------------------------")
#	print(sorted_freq_letters)


	count = 0
	for letter in attempt_count:
		if letter.isalpha():
			count = count + 1
#	print("Total: " + str(count))
#	i = 0
#	while i < 7:
#		print(sorted_freq_letters[i] + ":" + " " + str((freq_single_letters[sorted_freq_letters[i]]/ count)*100))
#		i = i + 1

	if (((((freq_single_letters[sorted_freq_letters[0]]/ count)*100) - (freq_single_letters[sorted_freq_letters[1]]/ count)*100)) >= 1):
		attempt = attempt.replace(sorted_freq_letters[0], "E")
		used_letters.append("E")

	if (((((freq_single_letters[sorted_freq_letters[1]]/ count)*100) - (freq_single_letters[sorted_freq_letters[2]]/ count)*100)) >= 1):
		attempt = attempt.replace(sorted_freq_letters[1], "T")
		used_letters.append("T")

#	if ((stored_letters[freq_letters[2]] - stored_letters[freq_letters[3]]) >= 20 ):
#		attempt = attempt.replace(freq_letters[2], "A")
#		used_letters.append("A")
#	if ((stored_letters[freq_letters[3]] - stored_letters[freq_letters[4]]) >= 25 ):
#		attempt = attempt.replace(freq_letters[3], "O")
#		used_letters.append("O")

	#print(count)
	return attempt

#Frequency analysis on one letter words [i, a]. "I" is more likely if it is at the start of a sentence.
#The first while loop does a frequency analysis on all capital letters the determine "I" as it should be the most frequent.

def single_letter_word(attempt):
	attempt1 = attempt.strip().split()
	one_letter_word = []
	i = 0
	while (i != len(attempt1)):
		if len(attempt1[i]) == 1 and attempt1[i - 1][len(attempt[i]) -1] == "." and attempt1[i].isalpha():
			one_letter_word.append(attempt1[i])
		i = i + 1

	if len(one_letter_word) != 0:
		freq_of_one_letter_words = frequency_analysis(one_letter_word)
		most_freq = sorted(freq_of_one_letter_words,key=freq_of_one_letter_words.get, reverse=True)
		attempt = attempt.replace(most_freq[0], "I")
		if "I" not in used_letters:
			used_letters.append("I")
	#print(most_freq)
	#print(one_letter_word)

	if len(most_freq) > 1:
		attempt = attempt.replace(most_freq[1], "A")
		if "A" not in used_letters:
			used_letters.append("A")

#		i = 0
#		while (i != len(attempt1)):
#			if len(attempt1[i]) == 1:
#				if (attempt1[i]).islower():
#					attempt = attempt.replace(attempt1[i], "A")
#					if "A" not in used_letters:
#						used_letters.append("A")

#			i = i + 1
#		if "E" in used_letters:
#			attempt = attempt.replace("e", "E")
#		if "T" in used_letters:
#			attempt = attempt.replace("t", "T")
	return attempt

def two_letter_word(attempt):
	two_letter_freq = []
	upper_list = []
	lower_list = []
	attempt1 = attempt.strip().split()
	i = 0
	while i != len(attempt1):
		if len(attempt1[i]) == 2 and not attempt1[i].isupper() and attempt1[i].isalpha():
			#print(attempt1[i])
			two_letter_freq.append(attempt1[i])
		i = i + 1
	f = frequency_analysis(two_letter_freq)
	fr = sorted(f,key=f.get, reverse=True)

	#print(fr)
#	n = 0
#	for word in fr:
#		first = word[0]
#		second = word[1]
#		if (first == first.upper()) or (second == second.upper()) and word != word.upper():
#			upper_list.append(word)
#		else:
#			lower_list.append(word)
#	new_list = upper_list + lower_list
#	#print(new_list)
#
	i = 0
	while i != len(fr):
		letter_1 = fr[i][0]
		letter_2 = fr[i][1]
		print(fr[i])
		two_letters = "of to in it is be as at so we he by or on do if me my up an go no us am"

#Case 1: left is upper and right is lower.
		if letter_1 == (letter_1).upper() and fr[i] != fr[i].upper():
			regex = re.escape(letter_1.lower()) + r"\w"
			result = re.findall(regex , two_letters)
			print(result)
			if len(result) != 0:
				j = 0
				while result[j][1].upper() in used_letters and j < len(result) -1:
					j = j + 1

				if result[j][1].upper() not in used_letters:
					char = result[j][1].upper()
					used_list.append(result[j])
					attempt = attempt.replace(letter_2, char)
					string = " ". join(fr)
					fr = (string.replace(letter_2, char)).strip().split()
					if char not in used_letters:
						used_letters.append(char)

#Case 2: lower on the left and upper on the right.
		elif letter_2 == (letter_2).upper() and fr[i] != fr[i].upper():
			regex = r"\w" + re.escape(letter_2.lower())
			result = re.findall(regex , two_letters)
			print(result)

			if len(result) != 0:
				j = 0
				while result[j][0].upper() in used_letters and j < len(result) -1:
					j = j + 1

				if result[j][0].upper() not in used_letters:
					char = (result[j][0]).upper()
					used_list.append(result[j])
					attempt = attempt.replace(letter_1, char)
					string = " ". join(fr)
					fr = (string.replace(letter_1, char)).strip().split()
					if char not in used_letters:
						used_letters.append(char)

		i = i + 1
	#print(used_list)
	return attempt

################################################################

def double_two_letters(attempt):
	attempt1 = attempt.strip().split()
	j = 0
	double_letters = []
	same_letters_list = ["ll ss ee oo tt ff pp rr mm cc nn dd gg ii bb aa zz xx uu hh"]
	for word in attempt1:
		i = 0
		while i < len(word) -1:
			first_letter = word[i]
			second_letter = word[i + 1]
			togther_letters = first_letter + second_letter
			if first_letter == second_letter and togther_letters != togther_letters.upper():
				double_letters.append(word)
				break
			i = i + 1

	if len(double_letters) != 0:
		for word in double_letters:
			i = 0
			while i < len(word) -1:
				first_letter = word[i]
				second_letter = word[i + 1]
				togther_letters = first_letter + second_letter
				if first_letter == second_letter and togther_letters != togther_letters.upper():

					while same_letters_list[j][0].upper() in used_letters and j < len(same_letters_list) -1:
						j = j + 1

					if same_letters_list[j][0].upper() not in used_letters:
						char = same_letters_list[j][0].upper()
						used_list.append(same_letters_list[j][0] + same_letters_list[j][0])
						attempt = attempt.replace(first_letter, char)
						#string = " ". join(new_list)
						#new_list = (string.replace(letter_1, char)).strip().split()
						if char not in used_letters:
							used_letters.append(char)
		
					break
				i = i + 1
	return attempt






################################################################

def three_letter_ending_in_E(attempt):
	the = []
	attempt1 = attempt.strip().split()
	i = 0
	while i != len(attempt1):
		word = attempt1[i]
		if len(attempt1[i]) == 3 and not attempt1[i].isupper() and attempt1[i].isalpha():
			#print(attempt1[i])
			if word[2] == "E": 
				the.append(word) 
			#regex = r"..E$" #+ re.escape(letter_2.lower())
			#result = re.findall(regex , attempt1[i])
		i = i + 1

	freq = frequency_analysis(the)
	most_freq = sorted(freq,key=freq.get, reverse=True)
	#print(most_freq)
	if len(most_freq) != 0:
		if most_freq[0][0] not in used_letters:
			attempt = attempt.replace(most_freq[0][0], "T")
			used_letters.append("T")
		if most_freq[0][1] not in used_letters:
			attempt = attempt.replace(most_freq[0][1], "H")
			used_letters.append("H")
		if len(most_freq) > 1:
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
	f = open("shite.txt", "r")
	encrypted_message = f.read()
	attempt = encrypted_message.lower()
	used_letters = []
	used_list = []
	#print(freq_single_letters)	


#Finding single letter words,[i,a], and check frequency pattern such as if there is full stop as "i" is more likely to appear at the beginning of sentences.
	attempt = single_letter(attempt)
	attempt = single_letter_word(attempt)
	#attempt = three_letter_ending_in_E(attempt)
	#attempt = three_letter_word_double_case(attempt)
	#attempt = two_letter_word(attempt)
	##attempt = ending_in_ing(attempt) #Redundant as three_letter_endings does this except for all cases.
	#attempt = three_letter_endings(attempt)
	#attempt = double_two_letters(attempt)

	print(attempt)
	print(used_list)
	print(used_letters)