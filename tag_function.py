from aqt import QMessageBox, QWidget
from aqt import mw

from . import xlrd_local


def add_tag(select_tag_value, add_tag_value, field_name_value, file_path_value):
    select_tag_value = str(select_tag_value)
    add_tag_value = str(add_tag_value)
    field_name_value = str(field_name_value)
    file_path_value = str(file_path_value)
    self = QWidget()
    
    if(field_name_value == "" or add_tag_value == ""):
        QMessageBox.warning(self, "Warning", "The Field Name or the Tag cannot be null!",QMessageBox.StandardButton.Yes)
        return
        
    # wrong file path
    if(len(file_path_value) < 2):
        QMessageBox.warning(self, "Warning", "Must select a word list file to execute!",QMessageBox.StandardButton.Yes)
        return
    
    # wrong file type
    file_type = file_path_value[file_path_value.rfind(".")+1:]
    if(file_type != "xls" and file_type != "xlsx" and file_type != "txt"):
        QMessageBox.critical(self, "Wrong!", "Please select the correct file format!\r\n.txt .xls .xlsx",QMessageBox.StandardButton.Yes)
        return

    # fill words list
    word_list = []
    if file_type == "txt":
        # txt
        t = open(file_path_value, encoding='UTF-8')
        # words added to list
        for line in t:
            line = line.strip().replace('\n', '').replace('\r', '')
            word_list.append(line)
    else:
        # xls, xlsx
        workbook = xlrd_local.open_workbook(file_path_value)
        sheet = workbook.sheet_by_index(0)
        for i in range(0, sheet.nrows):
            word = sheet.row_values(i)[0].strip()
            if(word != ""):
                word_list.append(word)

    # note id
    id_list = []
    if(select_tag_value == ""):
        # according field name and words list
        for word in word_list:
            # get note id
            note_id = mw.col.find_notes(field_name_value + ":" + word)
            if(len(note_id) >= 1):
                # multiple cards
                for i in range(len(note_id)):
                    id_list.append(note_id[i])
    else:
        # according field name and words list
        for word in word_list:
            # get note id
            note_id = mw.col.find_notes(field_name_value + ":" + word)
            if(len(note_id) >= 1):
                # multiple cards
                for i in range(len(note_id)):
                    # whether there is a specified tag
                    tags = mw.col.get_note(note_id[i]).tags
                    if(select_tag_value in tags):
                        id_list.append(note_id[i])
        
    # add tag
    # Count the number of updates
    number = 0
    # Iterate through the note id list
    for i in id_list:
        note = mw.col.get_note(i)
        tags = note.tags
        # turn to list type
        tags_list = []
        for j in range(len(tags)):
            tags_list.append(tags[j])
        print(tags_list)
        if add_tag_value not in tags_list:
            note.add_tag(add_tag_value)
            note.flush()
            number += 1
            
    # mw.col.close()
    # show a message box
    QMessageBox.information(self, "Result", "Update cards count: %d" % number + "\r\nReopen the window to refresh the changes.",QMessageBox.StandardButton.Yes)
    