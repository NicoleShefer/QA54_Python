# ---------- Task 1 ----------
def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"


# ---------- Task 2 ----------
def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"


# ---------- Task 3 ----------
def calculate_total_price(price, quantity):
    try:
        return float(price) * float(quantity)
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"


# ---------- Task 4 ----------
def read_temperature():
    value = input("Enter temperature: ")
    try:
        temperature = float(value)
    except ValueError:
        print("Invalid temperature")
    else:
        print("Temperature was entered successfully")
        return temperature
    finally:
        print("Program finished")


# ---------- Task 5 ----------
def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")
    return discount


# ---------- Check ----------
if __name__ == "__main__":
    # Task 1
    products = ["coffee", "tea", "milk"]
    assert get_product(products, 0) == "coffee"
    assert get_product(products, 7) == "Product index is out of range"

    # Task 2
    settings = {"language": "English", "theme": "dark"}
    assert get_settings_value(settings, "theme") == "dark"
    assert get_settings_value(settings, "font") == "Setting was not found"

    # Task 3
    assert calculate_total_price("12.5", "4") == 50.0
    assert calculate_total_price("coffee", "4") == "Value must be a number"
    assert calculate_total_price(None, 4) == "Invalid data type"

    # Task 4
    import builtins

    original_input = builtins.input
    builtins.input = lambda prompt="": "21.5"
    assert read_temperature() == 21.5
    builtins.input = lambda prompt="": "abc"
    assert read_temperature() is None
    builtins.input = original_input

    # Task 5
    assert validate_discount(50) == 50
    for bad, message in [(-5, "Discount cannot be negative"),
                         (150, "Discount cannot be greater than 100")]:
        try:
            validate_discount(bad)
            assert False, "ожидалась ошибка"
        except ValueError as e:
            assert str(e) == message

    print("Все проверки пройдены")