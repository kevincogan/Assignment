encrypted_message = "Xlkbirtsg ozdh ziv xszmtrmt zoo levi gsv dliow. Yv hfiv gl xsvxp gsv xlkbirtsg ozdh uli blfi xlfmgib yvuliv wldmolzwrmt li ivwrhgiryfgrmt gsrh li zmb lgsvi Kilqvxg Tfgvmyvit vYllp. Gsrh svzwvi hslfow yv gsv urihg gsrmt hvvm dsvm ervdrmt gsrh Kilqvxg Tfgvmyvit urov.  Kovzhv wl mlg ivnlev rg.  Wl mlg xszmtv li vwrg gsv svzwvi drgslfg dirggvm kvinrhhrlm. Kovzhv ivzw gsv ovtzo hnzoo kirmg zmw lgsvi rmulinzgrlm zylfg gsv vYllp zmw Kilqvxg Tfgvmyvit zg gsv ylggln lu gsrh urov.  Rmxofwvw rh rnkligzmg rmulinzgrlm zylfg blfi hkvxrurx irtsgh zmw ivhgirxgrlmh rm sld gsv urov nzb yv fhvw.  Blf xzm zohl urmw lfg zylfg sld gl nzpv z wlmzgrlm gl Kilqvxg Tfgvmyvit, zmw sld gl tvg rmeloevw."
encrypted_message = encrypted_message.lower()
stored_letters = {}

for char in encrypted_message:
	if char not in stored_letters:
		stored_letters[char] = 1

	else:
		stored_letters[char] += 1

print(stored_letters)
#print(sorted(stored_letters,key=stored_letters.get, reverse=True))
attempt = encrypted_message.replace("v", "e")
attempt = attempt.replace("g", "t")
attempt1 = attempt.strip().split()
two_letter_word: ["an", "as", "at", "it", "to", "in", "is", "on", "am", "be"]

#Frequency analysis on one letter words [i, a]. "I" is more likely if it is at the start of a sentence.
i = 0
while (i != len(attempt1)):
	if len(attempt1[i]) == 1:
		if "." in attempt[i -1]:
			attempt = attempt.replace(attempt1[i], "\033[31mi\033[0m")
		else:
			attempt = attempt.replace(attempt1[i], "\033[31ma\033[0m")
	i = i + 1




#attempt = attempt.replace("r", "\033[31mo\033[0m")
#attempt = attempt.replace("q", "\033[31mz\033[0m")

print(attempt)