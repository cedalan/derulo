#Functions to display parsed data
from typing import Dict, Any, List, Union

def _print_header():
    """
    Prints a formatted header for the JSON output
    """
    width = 40
    print("\n" + "=" * width + "\n")

def _print_footer():
    """
    Prints a formatted footer for the JSON output
    """
    width = 40
    print("\n" + "=" * width + "\n")

def print_json_as_list(data: Union[List[Dict], Dict[Any, Any]]):
    """
    Prints provided parsed json as a list in the terminal.

    Parameters:
    -----------
    data: data to print to terminal.
    """
    if not isinstance(data, List) and not isinstance(data, Dict):
        print("Data has to be list or dictionary!")
        return
    
    if not data:
        print("Data is empty! Aborting display")
        return
    
    _print_header()
    
    if isinstance(data, List):
        _print_json_list_as_list(data)
    else:
        _print_json_dict_as_list(data)
    
    _print_footer()

def _print_json_list_as_list(data: List[Dict]):
    """
    Inner function to display parsed json in terminal in case where argument is list
    """
    


def _print_json_dict_as_list(data: Dict[Any, Any], indent=2, level=0):
    """
    Inner function to display parsed json in terminal in case where argument is dict.
    """
    for key, value in data.items():
        prefix = " " * indent * level
        if isinstance(value, dict):
            print(f"{prefix}{key}:")
            _print_json_dict_as_list(value, level=level+1)
        else:
            print(f"{prefix}{key}:")