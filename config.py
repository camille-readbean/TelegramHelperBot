from telethon.types import BotCommand

# CHANGE BELOW
app_id='17349'
app_hash='344583e45741c457fe1862106095a5eb'
bot_token='CHANGE TO YOUR OWN TOEKN'
username='CHANGE TO YOUR USERNAME'
command_word_web_img='CHANGE TO WHATEVER COMMAND WORD YOU WANNA USE, /<cmd word>'
commands_description_list=[
    BotCommand(
        command=command_word_web_img, 
        description="<DESCRIPTION>"),
]
url_regex=r'(\s?(https?:\/\/)?[A-z0-9-._~]*\.([A-z0-9&]\/?)[!-~]*\s?)'
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.3'
viewport={ 'width' : 1920, 'height' : 1080 }
allowed_users=[
    123456789, # CHANGE TO YOUR USER IDs
]
default_timeout=30000
page_waittime=7000
