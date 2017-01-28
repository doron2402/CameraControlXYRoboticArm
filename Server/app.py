# app.py or app/__init__.py
from flask import Flask, render_template, jsonify
import os 
from action_commands import *

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

@app.route('/commands/<type>/<action>', methods=['POST']['GET'])
def commands(type, action):
    print("Command Type %s" % type)
    print("Command Action %s" % action)
    
    # Camera
    if type == "camera":
        res = camera_action(action)

    # Camera
    elif type == "program":
        res = program_action(action)
    # Zoom
    #elif type == "zoom":
     #   res = zoom_action(action)
    # Move
    #elif type == "move":
    #    res = move_action(action)
    #else:
    #    res = { 'type': type, 'action': action, 'error': 'unknown type' }    

    return jsonify(**res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

