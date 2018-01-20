import itertools as it
import functools as ft


# 1. probability of having at least one six when we roll two dice
# solution 1
sample = [(dice1,dice2) for dice1 in range(1,7) for dice2 in range(1,7)]
event = [roll for roll in sample if roll[0] == 6 or roll[1] == 6]

print(len(event), "/", len(sample))


# 2. probability of having no sixes when we roll two dice
event = [roll for roll in sample if roll[1] != 6 and roll[0] != 6]

print(len(event), "/", len(sample))


# 3. probability of having sum 6 when we roll two dice
event = [roll for roll in sample if roll[0]+roll[1]== 6]

print(len(event), "/", len(sample))

# 4. probabiity of having sum 10 if we roll three dice
r = range(1,7)
sample = [(i,j,k) for i in r for j in r for k in r]
event = [roll for roll in sample if sum(roll)==10]

print(len(event), "/", len(sample))

# 5. probability of rolling sum 13 if we roll four dice
r = range(1,7)
sample = [(i,j,k,l) for i in r for j in r for k in r for l in r]
event = [roll for roll in sample if sum(roll)==13]

print(len(event), "/", len(sample))


# 6. probability of having one six when we roll four dice    
def numsix(roll):    
    return len([dice for dice in roll if dice == 6])
  
event = [roll for roll in sample if numsix(roll)==1]

print(len(event), "/", len(sample))


# 7. probability of having four sixes when we roll eight dice
sample = [[i] for i in range(1,7)]
for i in range(7):
    sample = [x + [i] for x in sample for i in range (1,7)]
    
event = [roll for roll in sample if numsix(roll)==4]

print(len(event), "/", len(sample))


# 8. probability of drawing four aces
cards = list(it.product(range(1,5), range(1,14)))
sample = list(it.combinations(cards, 5))

def numval(hand, val):
    return len([card for card in hand if card[1] == val])

def numace(hand):
    return numval(hand, 1)

event = [hand for hand in sample if numace(hand)==4]

print(len(event), "/", len(sample))

# 9. probability of drawing 2 aces and two jacks
def numjack(hand):
    return numval(hand,11)

event = [hand for hand in sample if numace(hand)==2 and numjack(hand)==3]

print(len(event), "/", len(sample))

# 10. probability of all having the same suit
def numsuit(hand, suit):
    return len([card for card in hand if card[0]==suit])

event = [hand for hand in sample if numsuit(hand, hand[0][0]) == 5]

print(len(event), "/", len(sample))


cards = list(it.product(range(1,5), range(1,14)))
sample = list(it.combinations(cards, 5))
event = [hand for hand in sample if numsuit(hand, 0) == 5]

# 11. probability of a pair
event = [hand for hand in sample if sum([numval(hand,hand[i][1])  for i in range(5)]) == 7]

print(len(event), "/", len(sample))





# 12. Probability that a is at the front
# sample[i] = j has either the interpretation
#
# 1. i has position j in the queue, or
# 2. j has position i in the queue.
#
# Both are used in the examples below.
sample = list(it.permutations(range(6)));
             
event = [queue for queue in sample if queue[0] == 0]     

print(len(event), "/", len(sample))        

# 13. Probability that a is not at the back             
event = [queue for queue in sample if queue[-1] != 0]

print(len(event), "/", len(sample))        


# 14. Probability that a is in front of b
event = [queue for queue in sample if queue[0] < queue[1]]

print(len(event), "/", len(sample))        

# 14. Probability that a is in front of b
event = [queue for queue in sample if queue[0] < 2 and queue[1] < 2]

print(len(event), "/", len(sample))  
    
# 15. Probability that a and b are both in front of c and d
event = [queue for queue in sample if queue[0] < queue[2] and \
                                      queue[0] < queue[3] and \
                                      queue[1] < queue[2] and \
                                      queue[1] < queue[3]]

print(len(event), "/", len(sample))  

























