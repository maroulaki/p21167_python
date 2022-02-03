import random
FYLLO=[i for i in range(1,11)]
XRWMA=["C","S","H","D"]
FIGOURES=["J","Q","K"]
FYLLO=FYLLO+FIGOURES

DECK=[]
for i in XRWMA:
	for j in FYLLO:
		DECK.append([i,j])
random.shuffle(DECK)

def get_card_value(c):
	if c[1] in FIGOURES:
		return 10
	else:
		return c[1]
		
def sum_cards(LST):
	score=0
	for c in LST:
		score+=get_card_value(c)
	return score
	
#moirase xartia
comp_cards=[DECK[0],DECK[1],DECK[2]]
my_cards=[DECK[3],DECK[4]]

comp_score=sum_cards(comp_cards)
print comp_cards,comp_score
my_score=sum_cards(my_cards)
print my_cards,my_score

if my_score>comp_score:
	print "kerdises!"
elif comp_score>my_score:
	print "exases :("
else:
	print "pame pali..."
