import os 
def camera_action(action):
    res = ''
    if action == "snapshot":
        os.system("fswebcam -r 640x480 --no-banner ./static/images/current_pic.jpg")
        res = { 'type': 'camera', 'action': action, 'success': 'true' } 
    else:
        res = { 'type': 'camera', 'action': action, 'error': 'unknown action' }

    return res

'''
def zoom_action(action):
    if action == "in":
        res = { 'type': 'zoom', 'action': action, 'success': 'true' }
    elif action == "out":
        res = { 'type': 'zoom', 'action': action, 'success': 'true' }
    else:
        res = { 'type': 'zoom', 'action': action, 'error': 'unknown action' }  

    return res

def move_action(action):
    if action == "up":
        res = { 'type': "move", 'action': action, 'success': 'true' }
    elif action == "down":
        res = { 'type': "move", 'action': action, 'success': 'true' }
    elif action == "right":
        res = { 'type': "move", 'action': action, 'success': 'true' }
    elif action == "left":
        res = { 'type': "move", 'action': action, 'success': 'true' } 
    else:
        res = { 'type': "move", 'action': action, 'error': 'unknown action' } 
    return res
'''

def program_action(action):
    if action == "start":
        res = { 'type': "program", 'action': action, 'success': 'true', 'msg':'Please choose coordinates', 'Smess':'Running' }
    elif action == "pause":
        res = { 'type': "program", 'action': action, 'success': 'true', 'msg':'Waiting for command', 'Smess':'Paused'  }
    elif action == "stop":
        res = { 'type': "program", 'action': action, 'success': 'true', 'msg':'Stand by' , 'Smess':'Stoped' }
    else:
        res = { 'type': "program", 'action': action, 'error': 'unknown action' } 
    return res