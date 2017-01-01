# app.py or app/__init__.py
from flask import Flask, render_template, jsonify
import os 

app = Flask(__name__)
app.config.from_object('config')


def camera_action(action):
    res = ''
    if action == "snapshot":
        os.system("sh ./commands/webcam.sh")
        res = { 'type': 'camera', 'action': action, 'success': 'true' } 
    else:
        res = { 'type': 'camera', 'action': action, 'error': 'unknown action' }

    return res

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
    
    # Camera
    if type == "camera":
        res = camera_action(action)
    # Zoom
    elif type == "zoom":
        if action == "in":
            res = { 'type': type, 'action': action, 'success': 'true' }
        elif action == "out":
            res = { 'type': type, 'action': action, 'success': 'true' }
        else:
            res = { 'type': type, 'action': action, 'error': 'unknown action' }  
    # Move
    elif type == "move":
        if action == "up":
            res = { 'type': type, 'action': action, 'success': 'true' }
        elif action == "down":
            res = { 'type': type, 'action': action, 'success': 'true' }
        elif action == "right":
            res = { 'type': type, 'action': action, 'success': 'true' }
        elif action == "left":
            res = { 'type': type, 'action': action, 'success': 'true' } 
        else:
            res = { 'type': type, 'action': action, 'error': 'unknown action' } 
    else:
        res = { 'type': type, 'action': action, 'error': 'unknown type' }    

    return jsonify(**res)



if __name__ == "__main__":
    app.run()
