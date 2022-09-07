# mailtoall
This is a python program to send emails to multiple users at once.
This program will take all the emails from a csv file and send a custom designed email to them.

# Lets set up your gmail account
- first go to your google account > Security > 2-Step verification and turn it on.
- now in the Security main page you will be able to see App password.
- now click App password , Enter your gmail password.
- Now select the app and select the device and click generate.
- Now copy that 16 digit code and keep it with youself.

# Some prerequisite
- you need to have python in your machine.
- you need to run the following command. <br>
for windows : `pip install -r requirements.txt` <br>
for macOS : `pip3 install -r requirements.txt`

# How to send emails

- `cp sample_config.py config.py`
- edit the config.py file with your required data.
- edit the index.html with your required mailing data.
- `python mail_to_all.py`

## Note:
config.py is ignored in git commits, so your credentials won't be visible to anyone if you do any PR and all.