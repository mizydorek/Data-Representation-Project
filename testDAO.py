from movieDAO import movieDAO

test = {
    'fname': 'Paul',
    'lname': 'Neptune',
    'age': 31
}
test2 = {
    'fname': 'Tom',
    'lname': 'Dragon',
    'age': 35
}
test3 = {
    'id': 9,
    'fname': 'Mateo',
    'lname': 'King',
    'age': 74
}

actorupdate = {
    'id': 1,
    'actorname': 'Tom Cruise',
    'actordob': '1962-07-03',
    'actorgender': 'Female',
    'actorcountryid': 'Germany'
}

new = {
    'actorname': 'Maciek',
    'actordob': '1983-08-09',
    'actorgender': 'Male',
    'actorcountryid': 241
}



# display all - test!!!
# tests = movieDAO.getAll()
# print(tests)
# tests = movieDAO.createTest(test2)
# print(tests)
# tests = movieDAO.findByNameTest(10)
# print(tests)
# tests = movieDAO.updateTest(test3)
# print(tests)
# tests = movieDAO.deleteTest(14)
# print(tests)


################
# Actors db
################
# display all
# actors = movieDAO.getAll()
# print(actors)

################
# findActorByID
# actor = movieDAO.findActorById(1)
# print(actor)

################
# findCountry
# countries = movieDAO.getCountries()
# print(countries)
# country = movieDAO.findCountryById(241)
# print(country)
# country = movieDAO.findCountryByName("Germany")
# print(country)


################
# update actor
actor = movieDAO.updateActor(actorupdate)
print(actor)


################
# create actor
# actor = movieDAO.createActor(new)
# print(actor)




# for test in tests:
#     print(test)
    
# findCountry = countryDAO.findByID('Poland')
# print(findCountry)


# create - test!!!
# test = {
#     'fname': 'Paul',
#     'lname': 'Neptune',
#     'age': 31
# }
# result = movieDAO.createTest(test)

# print(result)

# result = movieDAO.columnsName('test')
# print(result)


