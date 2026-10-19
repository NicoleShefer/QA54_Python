# 1. get_product
def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"


# 2. get_settings_value
def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"


# 3. calculate_total_price
def calculate_total_price(price, quantity):
    try:
        return float(price) * float(quantity)
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"


# 4. read_temperature
def read_temperature():
    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid temperature")
    else:
        print("Temperature was entered successfully")
    finally:
        print("Program finished")


# 5. validate_discount
def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")


# ---------- Check ----------
if __name__ == "__main__":
    products = ["coffee", "tea", "milk"]
    print(get_product(products, 0))
    print(get_product(products, 7))

    settings = {"language": "English", "theme": "dark"}
    print(get_settings_value(settings, "theme"))
    print(get_settings_value(settings, "font"))

    print(calculate_total_price("12.5", "4"))
    print(calculate_total_price("coffee", "4"))
    print(calculate_total_price(None, 4))

    read_temperature()

    try:
        validate_discount(150)
    except ValueError as e:
        print(e)