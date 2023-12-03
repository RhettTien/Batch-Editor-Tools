from aqt import QMessageBox, QWidget
from aqt import mw


def replace_text(
    select_tag_value, 
    field_name_value, 
    was_replace_content_value, 
    replace_content_value
    ):
    self = QWidget()
    
    was_replace_content_value = str(was_replace_content_value)
    replace_content_value = str(replace_content_value)
    
    if(select_tag_value == "" and field_name_value == ""):
        QMessageBox.warning(self, "Warning", "Tag Names and Field Names are required!",QMessageBox.StandardButton.Yes)
        return
    
    if(was_replace_content_value == ""):
        QMessageBox.warning(self, "Warning", "Enter what you want to replace!",QMessageBox.StandardButton.Yes)
        return
    
    # empty function
    if(was_replace_content_value == "totally-all-content"):
        # get card id list
        card_id_list = mw.col.find_cards("tag:" + select_tag_value)
        count = 0
        for card_id in card_id_list:
            # get field content
            #str_field_content = col.get_card(card_id).note()[field_name_value]
            note = mw.col.get_card(card_id).note() 
            try:
                note[field_name_value] = replace_content_value
            except:
                QMessageBox.critical(self, "Wrong!", "The filtered card does not have the specified Field, please select another one!",QMessageBox.StandardButton.Yes)
                return
            note.flush()
            count += 1
            
        QMessageBox.information(self, "Result", "Empty field content count: %d" % count,QMessageBox.StandardButton.Yes)

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
                QMessageBox.critical(self, "Wrong!", "The filtered card does not have the specified Field, please select another one!",QMessageBox.StandardButton.Yes)
                return
            if(was_replace_content_value in str_field_content):
                note[field_name_value] = str_field_content.replace(was_replace_content_value, replace_content_value)
                note.flush()
                count += 1
        QMessageBox.information(self, "Result", "Update cards count: %d" % count,QMessageBox.StandardButton.Yes)
        
# Features updated in the next version: Fills the specified field contents based on the matching of the external file list and fields
