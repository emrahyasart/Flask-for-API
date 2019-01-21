from flask import Flask, url_for ,request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



@app.route('/test/<word>', methods=['GET', 'POST'])


def api(word):
    def test_get():
        test_list = ["Kemal", "Emrah", "Paul"]
        return jsonify(test_get=test_list)

    def test_post(word):
        test_list = ["Kemal", "Emrah", "Paul"]
        test_list.append('{}'.format(word))
        return jsonify(test_post=test_list)
    if request.method == 'GET':
        return test_get()
    else:
        return test_post(word)



names = {
  'Emrah': 1,
  'Kemal': 2,
  'Paul': 3
}
def addNameEntry(name, value):
  print(name, value)
  names[name] = value
  print(names)
  return jsonify(result=names)

def delete_entry(key):
    print(key)
    if key in names:
        del names[key]
        return jsonify(names=names)
    else:
        return ("Please enter a valid key")

def update_key_value(key, value):
    print(key, value)
    if key in names:
        names[key] = value
        return jsonify(names=names)
    else:
        return ("Please enter a valid key")


@app.route('/names', methods=['GET', 'POST', 'DELETE', 'PATCH'])

def getNames():

  if request.method == 'POST':
      data = request.json
      print(data)
      print(data['newName'], data['value'])
      return addNameEntry(data['newName'], data['value'])

  elif request.method == 'GET':
      return jsonify(names=names)

  elif request.method == 'DELETE':
      data = request.json
      print(data)
      print(data['key_to_delete'])
      return delete_entry(data["key_to_delete"])

  elif request.method == 'PATCH':
      data = request.json
      print(data)
      print(data["key"], data["value"])
      return update_key_value(data["key"], data["value"])









