from flask import Flask
app = Flask(__name__)
from flask import request, jsonify, abort
import json

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h1>'

d = {}

# post
# in template fomr unique name from terraform and passs it to cloudinit using file functions
# in cloudinit write POST - with that usnique key

# GET
# use the unique key to fetch the updated status
@app.route('/status',methods = ['POST', 'GET'])
def status():
   if request.method == 'POST':
      user = request.get_json()
      d.update(user)
      response ={}
      response['status_code'] = 201
      response['message'] = 'status updated'
      return jsonify(response)
   elif request.method == 'GET':
      args = request.args.to_dict()
      response ={}
      if args['key'] in d:
         response[args['key']]= d[args['key']]
      else:
         abort(400, description="Bad Request : key not found")
      return jsonify(response)

@app.errorhandler(400)
def page_not_found(error):
   return jsonify(error=str(error)), 400


# use jsonify 
if __name__ == "__main__":
    app.run(debug=True, port=8080)
