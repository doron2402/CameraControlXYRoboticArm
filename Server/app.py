# app.py or app/__init__.py
from flask import Flask, render_template, jsonify
import os 

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
	# check device status we can ping the robot and check if its "alive"
	return render_template('about.html')
# Now we can access the configuration variables via app.config["VAR_NAME"].

@app.route('/commands/<type>/<action>', methods=['POST'])
def commands(type, action):
    print("Command Type %s" % type)
    print("Command Action %s" % action)
    if action == "picture":
        print("Amit is the king!!!")
        os.system("sh Server/command/webcam.sh")
    else:
        # example of running a linux command line
        os.system("ls -lsf")
        os.system("echo 'Doron is my king!!!'")
        
    res = { 'type': type, 'action': action }
    return jsonify(**res)



if __name__ == "__main__":
    app.run()
