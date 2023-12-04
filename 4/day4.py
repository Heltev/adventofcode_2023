import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:      
    lines = f.read().splitlines()
  return lines

def get_winners(line):
  winners = line.split(':')[1].strip().split('|')[0].strip().split(' ')
  return [int(x) for x in winners if x != '']

def get_elf_numbers(line):
  elf_numbers = line.split(':')[1].strip().split('|')[1].strip().split(' ')
  return [int(x) for x in elf_numbers if x != '']

def get_card_power(winners,elf_numbers):
  power = -1
  for number in elf_numbers:
    if number in winners:
      power += 1
  if power >= 0: 
    return 2**power
  else: return 0 

def get_winning_numbers(winners,elf_numbers):
  num_winners = 0
  for number in elf_numbers:
    if number in winners:
      num_winners += 1
  return num_winners

def get_card_id(card):
  return int(card.split(':')[0].split()[1])

def main():
  lines = readfile()
  total_power = 0
  total_cards = 0
  card_multiplier = {}
  for line in lines:
    card_id = get_card_id(line)
    card_multiplier[card_id] = 1
  for card in lines:
    card_id = get_card_id(card)
    winners = get_winners(card)
    elf_numbers = get_elf_numbers(card)
    winning_numbers = get_winning_numbers(winners,elf_numbers)
    for x in range(card_id+1,card_id+winning_numbers+1):
      card_multiplier[x] += card_multiplier[card_id]
    card_power = get_card_power(winners,elf_numbers)
    total_power += card_power
  total_cards = 0
  for k,v in card_multiplier.items(): total_cards += v
  print("Total power:", total_power)
  print("Number of cards:",total_cards)
main()