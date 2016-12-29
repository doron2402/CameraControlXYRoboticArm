# app.py or app/__init__.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
	return render_template('about.html')
# Now we can access the configuration variables via app.config["VAR_NAME"].

@app.route('/commands/<type>/<action>', methods=['POST'])
def commands(type, action):
    # name=request.form['yourname']
    # email=request.form['youremail']
    res = { 'type': type, 'action': action }
    return jsonify(**res)



if __name__ == "__main__":
    app.run()
