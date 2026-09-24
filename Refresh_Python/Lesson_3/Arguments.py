def total(*args):
    print(type(args) , args)
    return sum(args)

print(total(1,2,3,4,5,6))
print(total(1,12,23,4,4,3))
print(total())
print()

def print_scores(students , *scores):
    print(f"students: {students}, scores: {scores}")

print_scores("Nicole", 30,20,40)
print_scores("Alex", 20,10,30)

def check_status_codes(*codes):
    for code in codes:
        assert code == 200

print(check_status_codes(200, 200 , 200))
print(check_status_codes(200, 400, 200))




