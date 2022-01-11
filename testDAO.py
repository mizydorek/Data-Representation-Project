from actorDAO import actorDAO

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
    'actordob': '1945-04-02',
    'actorgender': 'Male',
    'actorcountryid': 'Mexico'
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
# actors = actorDAO.getAll()
# print(actors)

################
# findActorByID
# actor = actorDAO.findActorById(1)
# print(actor)

################
# find actor by text
# actors = actorDAO.findActorByText('toma')
# print(actors)

################
# findCountry
# countries = actorDAO.getCountries()
# print(countries)
# country = actorDAO.findCountryById(241)
# print(country)
# country = actorDAO.findCountryByName("Germany")
# print(country)

################
# update actor
# actor = actorDAO.updateActor(actorupdate)
# print(actor)


################
# create actor
# actor = actorDAO.createActor(new)
# print(actor)



# findCountry = countryDAO.findByID('Poland')
# print(findCountry)


