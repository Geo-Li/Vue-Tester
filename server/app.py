from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlalchemy

Demo_User = [
    # {
    #     'title': 'On the Road',
    #     'author': 'Jack Kerouac',
    #     'read': True
    # },
    {
        'Name': 'Harry Potter',
        'Password': 'admin1',
        'read': False
    },
    {
        'Name': 'Tester',
        'Password': 'admin2',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/login', methods=['GET'])
def all_users():
    return jsonify({
        'status': 'success',
        'login': Demo_User
    })

@app.route('/login', methods=['GET', 'POST'])
def all_users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Demo_User.append({
            'name': post_data.get('username'),
            'password': post_data.get('password')
            # 'title': post_data.get('title'),
            # 'author': post_data.get('author'),
            # 'read': post_data.get('read')
        })
        response_object['message'] = 'User added!'
    else:
        response_object['login'] = Demo_User
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()
    