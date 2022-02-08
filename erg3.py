"""
3. Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο
γράμματα και τον κενό χαρακτήρα (space). Χωρείστε αυτό το κείμενο σε λέξεις
σύμφωνα με το κενό και ξεκινείστε να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα
των γραμμάτων τους είναι 20. Βγάλτε τα στατιστικά για το μήκος των λέξεων που
έμειναν, πχ. 10 λέξεις του ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις
των 3 γραμμάτων κτλ. Τα ζεύγη δεν χρειάζεται να είναι από συνεχόμενες λέξεις.
"""
import re
#Read txt file into string, replace new lines with space
with open("two_cities_ascii.txt", "r") as file:
    text = file.read().replace("\n", " ")
#Replace special characters with space
text = re.sub("[^A-Za-z ]","",text)
words = text.split()

#For k=20, I assume that there exist equal numbers of words that have
#20-n and n characters accordingly (for n={1,2,3...19}), and therefore if added together
#the sum is 20.

#I will count the number of words for every n={1,2,3...19} in a list
word_rec = []
for n in range(19):
	word_rec.append(0)

for word in words:
	chars = len(word)
	if chars <= 19:
		word_rec[chars-1] += 1


#An equal number of 20-n char and n char words must be removed
#word_rem list is a list of items to be removed from words
word_rem = []
for k in range(9):
	if word_rec[k] < word_rec[18-k]:
		word_rem.append(word_rec[k])
	elif word_rec[k] > word_rec[18-k]:
		word_rem.append(word_rec[18-k])
word_rem.append(word_rec[9])
for count in word_rem[8::-1]:
	word_rem.append(count)

#word_rem are removed from the total sum word_rec
for k in range(19):
	word_rec[k] = word_rec[k] - word_rem[k]

for i in range(10):
	print(word_rec[i],"words of ",i+1," letters remained \n")
