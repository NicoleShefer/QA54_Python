#Task 1. Shopping cart

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













