# AR Intercom
Live chat application started as a personal project to earn networking and more python skills.
This small application can help two different users to perform a live chat since they are in the same Local Area Network.

# Preview
This is the login window interface on version 2

![Login interface screenshot](https://github.com/AntaresMugisho/Ar_Intercom/blob/main/ui_login.jpg?raw=true)

# Usage of beta version : console app
One user should run the main.py (Server), one other the client.py (Client) files.
They must be connected at the same network (WiFi).

# Deployment
To make a standalone application of this, clone this repository and checkout the branch
**beta**, **v1** or **v2** respectively to select beta version (console app), version 1 or version 2.
Make sure you have Python 3.9 installed on your computer, 
then follow the steps bellow according to your operating system.

## On Windows
1. Install requirements.txt `pip install -r requirements.txt`
2. Run `python setup.py build` in your terminal
3. The executable file must be generated. Search it in __build/exe.win*/Ar_Intercom.exe__

