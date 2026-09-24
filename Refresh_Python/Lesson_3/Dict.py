books = \
    {
    "Lev Tolstoy" : "Anna Karenina" ,
    "Anton Chekhov" : "The Cherry Orchard"
    }

books_2 = \
    {
    "Lev Tolstoy" , "Anton Chekhov"
    }

print(books_2)


response = \
    {
    "StatusCode" : "200" ,
    "User" : {
        "Id" : 1,  "Name" : "Nicole"
             }
    }

print(response["User"]["Name"])


data = [ 1 , 2 , 33 ]
print(isinstance(data, list))
print(isinstance(data, tuple))


value = 22
print(isinstance(value, (int)))

value = 22.3
print(isinstance(value, (float)))

team_ages = \
{
    "Nicole" : 20,
    "Alex" : 40,
    "Tatiana" : 54,
    "Andrey" : 44
}

print(team_ages.keys())
print(team_ages.values())

team_names = "Nicole" ,  "Alex", "Tatiana" , "Andrey"
team_numbers = [20 , 40 , 54 , 44 ]
team_ages = {name:age for name, age in zip(team_names, team_numbers)}
print(team_ages)




