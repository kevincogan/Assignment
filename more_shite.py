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