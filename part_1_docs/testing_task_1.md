### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# is equal to operator on line 21 should be "=="
# else is missing ":"
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# "dif" should be "def"
# missing comma in-between card1 + card2
# "card" on line 31 should be card1
# 31 onwards requires indentation
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total needs to be equal to a value
# indentation error on line 44 means that loop will only iterate once
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
