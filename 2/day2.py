import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:      
    lines = f.read().splitlines()
  return lines


def register_round_info(game_rounds):
  game = {}
  for round_number in range(len(game_rounds)):
    game[round_number] = game_rounds[round_number].strip()
  return game

def find_offenders(game_dict,max_dice):
  too_high = 0
  id_sum = 0
  for game,draws in game_dict.items():
    too_high = 0
    for round,color in draws.items():
      minimum_dice = {'red': 0, 'green': 0, 'blue': 0}
      for draw in color.split(','):
        current_draw = draw.strip().split(' ')
        too_high += check_if_too_many(current_draw,max_dice)
    if too_high < 1: id_sum += game
  return id_sum

def check_if_too_many(draw,max_dice):
  if int(draw[0]) > max_dice[draw[1]]:
    return 1
  return 0

def find_minimal_set(game_dict):
  power_sum = 0
  for game,draws in game_dict.items():
    minimum_dice = {'red': 0, 'green': 0, 'blue': 0}
    for round,color in draws.items():
      for draw in color.split(','):
        current_draw = draw.strip().split(' ')
        if int(current_draw[0]) > minimum_dice[current_draw[1]]:
          minimum_dice[current_draw[1]] = int(current_draw[0])
    power = minimum_dice['red']*minimum_dice['green']*minimum_dice['blue']
    power_sum += power
  return power_sum

def create_game_dict(game_list):
  games = {}
  for game in game_list:
    game_id = int(game.split(':')[0].split(' ')[-1])
    game_rounds = game.split(':')[1].split(';')
    games[game_id] = register_round_info(game_rounds)
  return games

def main():
  max_dice = {'red': 12, 'green': 13, 'blue': 14}
  game_list = readfile()
  game_dict = create_game_dict(game_list)
  print("Total sum: ", find_offenders(game_dict,max_dice))
  print("Power sum:", find_minimal_set(game_dict))
  print(2**1)
main()