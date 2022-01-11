from flask import Flask, url_for, request, redirect, abort, jsonify, render_template, redirect
from actorDAO import actorDAO

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = 'Av&(b4&c>Re/PRg=Av&(b4&c>Re/PRg='

# curl http://127.0.0.1:5000/
@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

# display all the actors
# curl http://127.0.0.1:5000/actors
@app.get('/actors')
def getActors():
    print('getActors')
    return jsonify(actorDAO.getAll())

# find actor by id
# curl http://127.0.0.1:5000/actors/1
@app.route('/actors/<int:id>')
def findActorById(id):
    return jsonify(actorDAO.findActorById(id))

# find actor by name
# curl http://127.0.0.1:5000/actors/tom
@app.route('/actors/<string:actorname>')
def findActorByText(actorname):
    return jsonify(actorDAO.findActorByText(actorname))

# display all countries
# curl http://127.0.0.1:5000/countries
@app.route('/countries')
def getCountries():
    return jsonify(actorDAO.getCountries())

# find country by id
# curl http://127.0.0.1:5000/countries/240
@app.route('/countries/<int:id>')
def findCountryById(id):
    return jsonify(actorDAO.findCountryById(id))

# find country id by name 
# curl http://127.0.0.1:5000/countries/Germany
@app.route('/countries/<countryname>')
def findCountryByName(countryname):
    return jsonify(actorDAO.findCountryByName(countryname))

# create a new record
# curl -X POST -d "{\"actorname\":\"test\", \"actordob\":\"Someone\", \"actorgender\":\"Someone\", \"actorcountryid\": 241 }" -H Content-Type:application/json http://127.0.0.1:5000/actors
@app.route('/actors', methods=['POST'])
def createActor():
    if not request.json:
        abort(400)

    actor = {
            'actorname': request.json['actorname'],
            'actordob': request.json['actordob'],
            'actorgender': request.json['actorgender'],
            'actorcountryid': request.json['actorcountryid']
            }

    return jsonify(actorDAO.createActor(actor))

# update the record
# curl -X PUT -d "{\"fname\":\"test\", \"lname\":\"Someone\", \"age\":10}" -H Content-Type:application/json http://127.0.0.1:5000/actors/1
@app.route('/actors/<int:id>', methods=['PUT'])
def update(id):

    found = actorDAO.findActorById(id)
    if (found == {}):
        return jsonify({}), 404
    
    current = found

    if 'actorname' in request.json:
        current['actorname'] = request.json['actorname']

    if 'actordob' in request.json:
        current['actordob'] = request.json['actordob']

    if 'actorgender' in request.json:
        current['actorgender'] = request.json['actorgender']

    if 'actorcountryid' in request.json:
        current['actorcountryid'] = request.json['actorcountryid']

    result = actorDAO.updateActor(current)

    return jsonify(result)

# delete the record
# curl -X DELETE http://127.0.0.1:5000/movies/1
@app.route('/actors/<int:id>', methods=['DELETE'])
def delete(id):

    found = actorDAO.findActorById(id)

    if (found == {}):
        return jsonify({}), 404

    result = actorDAO.deleteActor(id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)