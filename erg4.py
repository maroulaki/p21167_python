"""
4. Χρησιμοποιείστε τον κώδικα που έχουμε φτιάξει για “21” (card game) και υπολογίστε
σε πόσα από τα 100 παιχνίδια κερδίζει ο πρώτος παίκτης, σε πόσα ο δεύτερος,
και σε πόσα έχουμε ισοπαλία. Στην συνέχεια, πειράξτε το μοίρασμα ώστε ο πρώτος
παίκτης να ξεκινάει με 10 ή φιγούρα (J,Q, K) και ο δεύτερος ποτέ με 10 ή φιγούρα.
Υπολογίστε τα νέα στατιστικά για 100 τυχαία παιχνίδια, δηλαδή πόσα κερδίζει ο πρώτος
παίκτης, πόσα ο δεύτερος, και σε πόσα έχουμε ισοπαλία. Κάθε φορά το μοίρασμα των
χαρτιών γίνεται από την αρχή και ανακατεύεται η τράπουλα.
"""

#Initialisations
import random
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]

for i in xarti:
    for j in color:
        xartia.append([i,j])
random.shuffle(xartia)

print("Mode 1: Normal Blackjack")
a = 0
b = 0
ties = 0
for i in range(100):
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        b += 1
    else:
        #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            a += 1
        elif sum2>sum1:
            b += 1
        else:
            ties += 1
	#shuffle deck
    xartia.clear()
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)

print("-----Results-----\n Player A: ",a,"\n Player B: ",b,"\n Ties: ",ties)

print("Mode 2: Modified Blackjack")
a = 0
b = 0
ties = 0
for i in range(100):
    player1=[]
    #Must have at least one figure or 10
    #I get the last 10 or figures card from the deck, and append it to the player1,
    #while removing it from the deck
    for card in xartia[::-1]:
        if (card[0] in figures) or card[0]==10:
            player1.append(xartia.pop(xartia.index(card)))
            break
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        b += 1
    else:
        #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            #Must NOT have 10 or figures
         	#I append the last card of the deck that is not 10 or figures
            for card in xartia[::-1]:
                if not(card[0]==10 or (card[0] in figures)):
                    player2.append(xartia.pop(xartia.index(card)))
                    break
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            a += 1
        elif sum2>sum1:
            b += 1
        else:
            ties += 1
		#shuffle deck
        xartia.clear()
        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)
print("-----Results-----\n Player A: ",a,"\n Player B: ",b,"\n Ties: ",ties)
