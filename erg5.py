"""
Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. Αρχικά, κάντε την κατάλληλη
επεξεργασία ώστε να σας μείνει κείμενο με μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά)
και τον κενό χαρακτήρα (space). Αρχικά, χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό.
Στις λέξεις που έχετε υπολογίστε τα ακόλουθα στατιστικά:
α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις; Αν κάποιες εμφανίζονται το ίδιο πλήθος και βγαίνουν
παραπάνω από δέκα, κρατείστε όποιες νομίζετε εσείς ή στην τύχη.
β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που
αρχίζουν οι περισσότερες λέξεις;
γ) Επαναλάβετε το ίδιο για τρία γράμματα.
"""
import re
#---Functions---
#Function that searches a list of lists for the key. Returns the index of the sublist if found,
#or -1 if not found
def search(key, list):
	pos = -1
	for sublist in list:
		if sublist[0] == key:
			pos = list.index(sublist)
			break
	return pos
#Sorting criteria is the number of times a word appears
def MyFunc(sublist):
	return sublist[1]
#Finding the top n amount of words by finding the frequency and then sorting
def top(words, n):
	common_words = []
	for word in words:
		pos = search(word, common_words)
		if pos == -1:
			common_words.append([word, 1])
		else:
			common_words[pos][1] += 1
	common_words.sort(key=MyFunc, reverse=True)
	print(n," most common: ",common_words[:n])

#---Program---
#Read txt file into string, replace new lines with space
with open("two_cities_ascii.txt", "r") as file:
    text = file.read().replace("\n", " ")
#Remove special characters
text = re.sub("[^A-Za-z ]","",text)
text = text.lower()
words = text.split()

#For whole words
print("Searching top words...")
top(words,10)

#For 2-letter combinations
print("Searching top 2-letter combinations...")
letters2 = []
for i in range(len(words)):
	letters2.append(words[i][:2])
top(letters2,3)

#For 3-letters combinations
print("Searching top 3-letter combinations...")
letters3 = []
for i in range(len(words)):
	letters3.append(words[i][:3])
top(letters3,3)
