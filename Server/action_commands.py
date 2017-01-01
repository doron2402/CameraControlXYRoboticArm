import os 
def camera_action(action):
    res = ''
    if action == "snapshot":
        os.system("sh ./commands/webcam.sh")
        res = { 'type': 'camera', 'action': action, 'success': 'true' } 
    else:
        res = { 'type': 'camera', 'action': action, 'error': 'unknown action' }

    return res

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
