#Functions to parse/process json
from typing import Dict, List, Any

def parse_json(response: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Parses some request response to json

    Parameters:
    -----------
        response (Dict[Any, Any]): A dictionary representing the raw response data to be parsed.

    Returns:
    -----------
        Dict[Any, Any]: A dictionary containing the JSON data extracted from the response. 
    """
    try:
        response = response.json()
        return response
    except Exception as e:
        print(f"Exception occurred when parsing response to json. Error: {e}")
        return None

def flatten_json(nested_dict: Dict[Any, Any], parent_key="", sep=".") -> Dict[Any, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary by concatenating nested keys.

    Parameters:
    -----------
        nested_dict (Dict[Any, Any]): The dictionary with nested structures to flatten.
        parent_key (str, optional): The initial key used as a prefix for each new key in the flattened dictionary. Defaults to an empty string.
        sep (str, optional): The separator used to join keys from different levels. Defaults to '.'.

    Returns:
    -----------
        Dict[Any, Any]: A new dictionary with keys representing the concatenated path of the original nested keys.
    """

    return

def extract_keys(json_list: List[Any], keys: List[Any]) -> List[Dict[Any, Any]]:
    """
    "Rebrands" a list of json-objects by only selecting given keys

    Parameters:
    -----------
        json_list (List[Any]): List of json objects
        keys (List[Any]): List of keys to extract 

    Returns:
    --------
        List[Dict[Any, Any]]: A new dictionary with keys provided in keys-parameter
    """
    return [{k: item.get(k) for k in keys} for item in json_list]