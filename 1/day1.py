import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:      
    lines = f.read().splitlines()
  # for character in lines[-1]:
  #   if character.isnumeric(): print(character)
  #   #print(int(lines[-1][-1]))
  return lines

def simple_find_digits(lines):
  sum = 0
  for line in lines:
    number_string = ''
    index = 0
    while len(number_string) == 0:
      if line[index].isnumeric():
        number_string += line[index]
      index += 1
    index = len(line)-1
    while len(number_string) == 1:
      if line[index].isnumeric():
        number_string += line[index]
      index -=1
    sum += int(number_string)
  return sum

def find_outer_digits(line):
  index_found_from_left = -1
  index_found_from_right = -1
  number_string = ''
  index = 0
  while len(number_string) == 0:
    if line[index].isnumeric():
      number_string += line[index]
      index_found_from_left = index
    index += 1
  index = len(line)-1
  while len(number_string) == 1:
    if line[index].isnumeric():
      number_string += line[index]
      index_found_from_right = index
    index -=1
  return number_string, index_found_from_left,index_found_from_right
    
def get_number_strings():
  return ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']

def find_integer_string(line):
  index_left = 1000000
  index_right = -1
  number_left = ''
  number_right = ''
  for number in get_number_strings():
    for index in range(len(line)):
      if line.find(number,index) >= 0:
        if line.find(number,index) < index_left:
          index_left = line.find(number,index)
          number_left = convert_from_string_to_int(number)
        if line.find(number,index) > index_right:
          index_right = line.find(number,index)
          number_right = convert_from_string_to_int(number)
  return index_left,index_right,number_left,number_right

def convert_from_string_to_int(string):
  if string == 'one': return '1'
  elif string == 'two': return '2'
  elif string == 'three': return '3'
  elif string == 'four': return '4'
  elif string == 'five': return '5'
  elif string == 'six': return '6'
  elif string == 'seven': return '7'
  elif string == 'eight': return '8'
  elif string == 'nine': return '9'

def check_if_digits(line):
  for character in line:
    if character.isnumeric():
      return 1
  return -1

def fancy_find_digits(lines):
  sum = 0
  for line in lines:
    number_string = ''
    any_digits = check_if_digits(line)
    if any_digits > 0:
      outer_digits, index_left,index_right = find_outer_digits(line)
    else:
      index_left = 1000000
      index_right = -1
    index_found_from_left, index_found_from_right,number_characters_from_left,number_characters_from_right = find_integer_string(line)
    if index_left < index_found_from_left:
      number_string += outer_digits[0]
    else:
      number_string += number_characters_from_left
    if index_right > index_found_from_right:
      number_string += outer_digits[1]
    else:
      number_string += number_characters_from_right
    sum += int(number_string)
  return sum


def main():
  lines = readfile()
  print(simple_find_digits(lines))
  print(fancy_find_digits(lines))
  
main()