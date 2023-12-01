from aqt import QMessageBox, QWidget
from aqt import mw
#from anki.collection import Collection

# col = Collection("C:/Users/Tien/AppData/Roaming/Anki2/11/collection.anki2")

def replace_text(select_tag_value, field_name_value, was_replace_content_value, replace_content_value):
    self = QWidget()
    was_replace_content_value = str(was_replace_content_value)
    replace_content_value = str(replace_content_value)
    if(select_tag_value == "" and field_name_value == ""):
        QMessageBox.information(self, "Warning", "Tag Names and Field Names are required!",
                            QMessageBox.Yes)
        return
    
    if(was_replace_content_value == ""):
        QMessageBox.information(self, "Warning", "Enter what you want to replace!",
                            QMessageBox.Yes)
        return
    
    # empty function
    if(was_replace_content_value == "totally-all-content" and replace_content_value == ""):
        count = 0
        count = replace_without_matching(count, select_tag_value, field_name_value, replace_content_value)
        
        QMessageBox.information(self, "Result", "Empty field content count: %d" % count,
                            QMessageBox.Yes)
    # add function
    elif(was_replace_content_value == "this-field-is-blank"):
        count = 0
        count = replace_without_matching(count, select_tag_value, field_name_value, replace_content_value)
        
        QMessageBox.information(self, "Result", "Update cards count: %d" % count,
                            QMessageBox.Yes)
    # replace function
    else:
        count = 0
        # get card id list
        card_id_list = mw.col.find_cards("tag:" + select_tag_value)
        for card_id in card_id_list:
            # get field content
            note = mw.col.get_card(card_id).note() 
            str_field_content = ""
            try:
                str_field_content = note[field_name_value]
            except:
                QMessageBox.information(self, "Warning", "The filtered card does not have the specified Field, please select another one!",
                            QMessageBox.Yes)
                return
            if(was_replace_content_value in str_field_content):
                note[field_name_value] = str_field_content.replace(was_replace_content_value, replace_content_value)
                note.flush()
                count += 1
        QMessageBox.information(self, "Result", "Update cards count: %d" % count,
                            QMessageBox.Yes)
        
def replace_without_matching(count, select_tag_value, field_name_value, replace_content_value):
    self = QWidget()
    # get card id list
    card_id_list = mw.col.find_cards("tag:" + select_tag_value)
    for card_id in card_id_list:
        # get field content
        #str_field_content = col.get_card(card_id).note()[field_name_value]
        note = mw.col.get_card(card_id).note() 
        try:
            note[field_name_value] = replace_content_value
        except:
            QMessageBox.information(self, "Warning", "The filtered card does not have the specified Field, please select another one!",
                        QMessageBox.Yes)
            return
        note.flush()
        count += 1
    return count
# Features updated in the next version: Fills the specified field contents based on the matching of the external file list and fields