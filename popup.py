# -*- This python file uses the following encoding : coding:utf-8 -*-

from plyer.utils import platform
from plyer import notification
import os, sys


# Only tested on Windows 10 and MacOS X

def popup(sender):
    if sys.platform == "win32":
        try:
            notification.notify(
                title="Nouveau message",
                message=f"Un message de {sender}",
                app_name="AR Intercom Beta",
                app_icon="popup." + ('ico' if platform == 'win' else 'png'))

        except Exception as e:
            print(e)

    else:
        msg = f"Un message de {sender}"
        try:
            popup_mac(msg, "AR Intercom")
        except Exception as e:
            print(e)

def popup_mac(message, title=None, subtitle=None, soundname=None) :
    """
        Display an OSX notification with message title an subtitle
        sounds are located in /System/Library/Sounds or ~/Library/Sounds
    """
    titlePart = ''
    if (not title is None) :
        titlePart = 'with title "{0}"'.format(title)
    subtitlePart = ''
    if (not subtitle is None) :
        subtitlePart = 'subtitle "{0}"'.format(subtitle)
    soundnamePart = ''
    if (not soundname is None) :
        soundnamePart = 'sound user_code "{0}"'.format(soundname)

    appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message, titlePart, subtitlePart,
                                                                                soundnamePart)
    os.system("osascript -e '{0}'".format(appleScriptNotification))

# Popup test
if __name__ == '__main__':
    from plyer import notification

    notification.notify(
        title="HEADING HERE",
        message=" DESCRIPTION HERE",

        # displaying time
        timeout=2
    )


    #popup("Antares")
