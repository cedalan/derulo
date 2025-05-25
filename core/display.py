#Functions to display parsed data
from typing import Dict, Any, List, Union

def print_json_as_list(data: Union[List[Dict], Dict[Any, Any]]):
    """
    Prints provided parsed json as a list in the terminal.

    Parameters:
    -----------
    data: data to print to terminal.
    """

    if not isinstance(data, List) and not isinstance(Dict):
        print("Data has to be list or dictionary!")
        return
    
    if not data:
        print("Data is none! Aborting display")
        return
    
    if isinstance(data, List):
        _print_json_list_as_list(data)
    
    else:
        _print_json_dict_as_list(data)
    
def _print_json_list_as_list(data: List[Dict]):
    """
    Inner function to display parsed json in terminal in case where argument is list
    """
    return

def _print_json_dict_as_list(data: Dict[Any, Any]):
    """
    Inner function to display parsed json in terminal in case where argument is dict.
    """
    return