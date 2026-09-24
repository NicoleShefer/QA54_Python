#Task 1. Shopping cart
"""
def clean_cart(cart):
  if not isinstance(cart, list):
    raise TypeError("Argument 'cart' should be a (list)")

  for item in cart:
    if not isinstance(item, str):
      raise TypeError(
          f"All the elements should be a string. There is found another type: {type(item).__name__}"
      )

  if not cart:
    return []

  while "sold out" in cart:
    cart.remove("sold out")

  return cart


print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
print(clean_cart(["milk", 123, "bread"]))
print(clean_cart({"item": "milk"}))

#======================================================

# Task 2. Temperature report

def temperature_report(temperatures):
  if not isinstance(temperatures, list):
    raise TypeError("Аргумент должен быть списком (list)")

  result = []

  for temp in temperatures:
    if not isinstance(temp, (int, float)):
      raise TypeError(
          f"All the elements should be an int. Type found: {type(temp).__name__}"
      )

    if not (-60 <= temp <= 60):
      raise ValueError(
          f"Incorrect temperature: {temp}. It should be between -60 and 60°C"
      )

    if temp > 25:
      result.append(temp)

  return result


print(temperature_report([21, 28, 19, 31, 25, 27]))
print(temperature_report([21, 150]))

#======================================================

#Task 3. Fix negative balances

def fix_balances(balances):
    if not isinstance(balances, list):
        raise TypeError("balances must be a list")

    for i in range(len(balances)):
        if isinstance(balances[i], bool) or not isinstance(balances[i], (int, float)):

            raise TypeError("all balances must be numbers")
        if balances[i] < 0:
            balances[i] = 0
    return balances

print(fix_balances([120, -30, 50, -5, 0, 200]))

#======================================================

# Task 4. Remove duplicates without set

def unique_items(items):
    if not isinstance(items, list):
        raise TypeError("items must be a list")
    result = []

    for item in items:
        if item not in result:
            result.append(item)
    return result

print(unique_items(["red", "blue", "red", "green", "blue"]))

#======================================================

# Task 5. Longest word

def longest_word(words):
    if not isinstance(words, list):
        raise TypeError("words must be a list")
    if len(words) == 0:
        raise ValueError("words list is empty")
    for w in words:
        if not isinstance(w, str):
            raise TypeError("all elements must be strings")
    best = words[0]
    for w in words:
        if len(w) > len(best):
            best = w
    return best

print(longest_word(["cat", "elephant", "python", "coffee"]))

"""