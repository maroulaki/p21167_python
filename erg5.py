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
#Finding the top n amount of words by finding the frequency for each word. Every time
#the most common word is found, it removed so that the next one will be found in the
#next repetition.
def top(words, n):
	common_words = {}
	for word in words:
		exists = common_words.get(word, 0)
		if exists != 0:
			common_words.update({word: exists + 1})
		else:
			common_words.update({word: 1})
	print(n," most common: ")
	for i in range(n):
		top_word = max(common_words, key=common_words.get)
		print(top_word," : ",common_words.get(top_word),"\n")
		common_words.pop(top_word)

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
