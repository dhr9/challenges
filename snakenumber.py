multiplier = 6
max_length = 10000
# possible_ending_numbers = {}
# for i in range(10):
  # possible_ending_numbers[int((str(multiplier * i))[-1])] = 1

# possible_ending_numbers = possible_ending_numbers.keys()
# possible_ending_numbers.sort()
# possible_ending_numbers_ = []
possible_ending_numbers = [i for i in range(1, 10)]
# for number in possible_ending_numbers:
  # if number != 0:
    # possible_ending_numbers_.append(number)
# possible_ending_numbers = possible_ending_numbers_

def get_product_remainder(a, b, carry):
  result = str(a*b + carry)
  x, y = '0', '0'
  try:
    x, y = result[0], result[1]
  except:
    x = result
  return (int(y), int(x))

def is_snake_number(num, multiplier):
  return ((10 ** (len(str(num)) - 1)) * (num%10)) + ((num - (num%10))/10) == multiplier*num

def recurse(num, carry):
  while len(str(num)) <= max_length:
    if is_snake_number(num, multiplier):
      return num
    product, carry = get_product_remainder(int(str(num)[0]), multiplier, carry)
    if product == 0:
      num, carry = int(str(carry) + '0' + str(num)), 0
    else:
      num = int(str(product) + str(num))
  return False

snake_numbers = []
for first_number in possible_ending_numbers:
  print(first_number)
  snake_number = recurse(first_number, 0)
  print(snake_number)
  if snake_number != False:
    snake_numbers.append(snake_number)

print(snake_numbers)
