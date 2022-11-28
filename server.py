from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

d = {"k": "v"}

# post
# in template fomr unique name from terraform and passs it to cloudinit using file functions
# in cloudinit write POST - with that usnique key

# GET
# use the unique key to fetch the updated status
@app.route('/login',methods = ['POST', 'GET'])
def status():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

# use jsonify 
if __name__ == "__main__":
    app.run(debug=True, port=37999)
