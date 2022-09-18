from pushbullet import Pushbullet
import os
import shutil

def sending_message():
    api_keys = 'api_key.txt'
    # extracting date of recording - might not need this in your case
    file = sorted([x for x in os.listdir('C:\\Users\\sskr2\\Documents\\personal-projects') if x[-4:] == '.mp4'])[0]
    shutil.move(f'C:\\Users\\sskr2\\Documents\\personal-projects\\{file}', f'C:\\Users\\sskr2\\Documents\\personal-projects\\security\\{file}')

    # extracting sample message
    with open(api_keys, mode = 'r') as f:
        text = f.read()
        auth_token = str(text[20:54])
    
    # configuring message
    message =f'Camera has picked up suspicious activity at {file[:-4]}. Please Review Google drive' 
    
    pb = Pushbullet(auth_token)
    push = pb.push_note('Attention!: ', message)
    
    return push