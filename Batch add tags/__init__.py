from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *


# We're going to add a menu item below. First create a function to
# be called when the menu item is activated.

def batFunction() -> None:
    # read config
    config = mw.addonManager.getConfig(__name__)
    # tag to add
    tag = config['tag_name']
    # field name
    field_name = config['field_name']
    # read words
    files_path = config['words_path']
    # words added to list
    t = open(files_path, encoding='UTF-8')
    wordlist = []
    for line in t:
        wordlist.append(line.strip())
    # Count the number of updates
    number = 0
    for word in wordlist:
        ids = mw.col.find_notes(field_name + ":" + word)
        for i in ids:
            note = mw.col.get_note(i)
            tags = note.tags
            if tags.__contains__(tag):
                continue
            else:
                note.add_tag(tag)
                note.flush()
                number += 1
    # show a message box
    showInfo("Upgrade card count: %d" % number)


# create a new menu item, "test"
action = QAction("Batch add tags", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, batFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
