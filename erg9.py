"""
9. Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό μήκους 7.
Υπολογίστε ποια είναι η μεγαλύτερη ακολουθία από συνεχόμενα 0 και από συνεχόμενα 1.
"""
with open("two_cities_ascii.txt", "r") as file:
    text = file.read().replace("\n", " ")
#Getting ASCII codes of each character, and converting them to 7-bit binary codes
ascii_text = []
for char in text:
	ascii_text.append(ord(char))
bin_codes = []
for ascii_code in ascii_text:
	binary = bin(ascii_code)[2:]
	while len(binary) < 7:
		binary = "0" + binary
	bin_codes.append(binary)
#Joining the binary codes into a string
binary_text = "".join(bin_codes)

#Longest 0 sequence.
#If max characters in a sequence of "0" are 1:
#Sometimes a string in zeroes list will have a length of 1 and won't be a "0"(due to split method)
#In that case, I will check if there is a sequence of "0" with the length of 1,
#or if there are no "0" at all.
zeroes = binary_text.split("1")
str0 = max(zeroes, key=len)
if len(str0) == 1:
	if str0 != "0":
		max_0 = True
		for zero in zeroes:
			if (len(zero) == 1) and (zero == "0"):
				max_0 = False
				break
		if max_0:
			longest0 = 0
		else:
			longest0 = 1
else:
	longest0 = len(str0)
#Longest 1 sequence
ones = binary_text.split("0")
str1 = max(ones, key=len)
if len(str1) == 1:
	if str1 != "0":
		max_0 = True
		for one in ones:
			if (len(one) == 1) and (one == "1"):
				max_0 = False
				break
		if max_0:
			longest1 = 0
		else:
			longest1 = 1
else:
	longest1 = len(str1)
print("Longest 0 sequence: ",longest0,"\nLongest 1 sequence: ", longest1)
