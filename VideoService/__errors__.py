########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
from typing import List, Dict, Union

#####  INTERNAL IMPORTS


########################################
#####  CODE                        #####
########################################

##### ERROR CLASS

# Data related errors
class DataBaseNotFound(Exception):...
class FolderNotFound(Exception):...

# Variable assignation errors
class WrongTagsStructure(ValueError):...
class WrongOrderStructure(ValueError):...
class WrongFilterStructure(ValueError):...

##### CHECK STRUCTURES OF SEARCHING VARIABLES

def check_tags(lst: List[str]) -> bool:
    return all(isinstance(item, str) for item in lst)

def check_order_settings(lst: List[ Union[ str, bool]]) -> bool:
    if len(lst) != 2:
        return False
    return isinstance(lst[0], str) and isinstance(lst[1], bool)

def check_filter_settings(filter_settings: Dict[str, Dict[str, Union[List[Union[str, int]], bool]]]) -> bool:
    required_structure = {
        "_filter_by_date": {"filter": list, "active": bool},
        "_filter_by_length": {"filter": list, "active": bool},
        "_filter_by_tags": {"filter": list, "active": bool},
    }
    
    # Check that the top-level keys match the required structure
    if not isinstance(filter_settings, dict):
        return False
    
    if filter_settings.keys() != required_structure.keys():
        return False
    
    for key, value in filter_settings.items():
        if not isinstance(value, dict):
            return False
        if set(value.keys()) != {"filter", "active"}:
            return False
        
        filter_type = value["filter"]
        if not isinstance(filter_type, list):
            return False
        
        if key == "_filter_by_date" and (len(filter_type) > 2 or not all(isinstance(item, str) for item in filter_type)):
            return False

        elif key == "_filter_by_length" and (len(filter_type) > 2 or not all(isinstance(item, int) for item in filter_type)):
            return False
        
        elif key == "_filter_by_tags" and not all(isinstance(item, str) for item in filter_type):
            return False
        
        if not isinstance(value["active"], bool):
            return False
    
    return True