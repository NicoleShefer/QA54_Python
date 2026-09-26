# Task 1.
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
        return
    print(lst[::-1])

print_list_reverse([1, 2, 3, 4, 5])       # [5, 4, 3, 2, 1]
print_list_reverse([])                     # Wrong list
print_list_reverse(None)                   # Wrong list
print_list_reverse("12345")                # Wrong list

#================================================================================

# Task 2.
def is_valid_point(point):
    if point is None or point == ():
        return None
    if not isinstance(point, tuple):
        return False
    if len(point) != 2:
        return False
    for item in point:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return False
    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))

#================================================================================

# Task 3.
def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong args")
        return
    if isinstance(start, bool) or isinstance(finish, bool):
        print("Wrong args")
        return
    if not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
        return
    if start < 0 or finish < 0 or start >= len(lst) or finish >= len(lst):
        print("Wrong args")
        return
    if start > finish:
        print("Wrong args")
        return

    result = lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:]
    print(result)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)

#================================================================================

# Task 4.
def get_students_by_grade(students):
    if students is None or not isinstance(students, dict) or len(students) == 0:
        return {}

    result = {}
    for name, grade in students.items():
        if grade not in result:
            result[grade] = []
        result[grade].append(name)
    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))
print(get_students_by_grade(None))
print(get_students_by_grade({}))
print(get_students_by_grade([1, 2]))


