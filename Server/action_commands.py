import os 
def camera_action(action):
    res = ''
    if action == "snapshot":
        os.system("fswebcam -r 640x480 --no-banner ./static/images/current_pic.jpg")
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

def ReadTargetPoint(event,img):
    var posX = event.offsetX?(event.offsetX):event.pageX-img.offsetLeft;
    var posY = event.offsetY?(event.offsetY):event.pageY-img.offsetTop;
    document.getElementById("NameX").value = posX;
    document.getElementById("NameY").value = posY;
    res = { 'type': "image", 'action': action, 'success': 'true' } 
    return true



