def is_null(value: any) -> bool:
   """
   Check if a value is None.

   Args:
      value (any): The value to check.

   Returns:
      bool: True if the value is None, False otherwise.
   """
   if value is None:
     return True
   return False

def get_value_or_none(value: any, attr: str) -> any:
   """
   Returns the value of an attribute of an object or None if the object or attribute is null.

   Args:
      value (any): The object to retrieve the attribute from.
      attr (str): The name of the attribute to retrieve.

   Returns:
      any: The value of the attribute or None if the object or attribute is null.
   """
   if is_null(value):
      return None
   if is_null(getattr(value, attr)):
      return None
   return getattr(value, attr)

def create_dict(value: any, attrs: list[str]) -> dict:
   """
   Create a dictionary from a given object and a list of attributes.

   Args:
       value (any): The object to create a dictionary from.
       attrs (list[str]): The list of attributes to include in the dictionary.

   Returns:
       dict: A dictionary containing the specified attributes and their values from the given object.
   """
   if is_null(value):
      return {}
   
   if is_null(attrs) or len(attrs) == 0:
      return value.to_dict()
   
   results: dict[str, any] = {}
   for attr in attrs:
      results[attr] = get_value_or_none(value, attr)
   return results

def to_list_base(array: list | None) -> list:
   """
   Converts a list of objects to a list of dictionaries.

   Args:
      array (list | None): The list of objects to be converted.

   Returns:
      list: A list of dictionaries representing the objects in the input list.
   """
   if is_null(array) or len(array) == 0:
     return []
   return [item.to_dict() for item in array]

def to_list_with_attr(array: list | None, attr: str) -> list:
   """
   Returns a list of attribute values for a given attribute from a list of objects.

   Args:
      array (list | None): The list of objects to extract attribute values from.
      attr (str): The name of the attribute to extract from each object.

   Returns:
      list: A list of attribute values for the given attribute from each object in the input list.
   """
   if is_null(array) or len(array) == 0:
      return []
   return [get_value_or_none(item, attr) for item in array]

def to_list_with_attrs(array: list | None, attrs: list[str]) -> list:
   """
   Converts a list of objects to a list of dictionaries containing only the specified attributes.

   Args:
       array (list): The list of objects to convert.
       attrs (list[str]): The list of attributes to include in the resulting dictionaries.

   Returns:
       list: A list of dictionaries containing only the specified attributes.
   """
   if is_null(array) or len(array) == 0:
      return []
   
   results: list[dict] = [{}]
   for item in array:
      dic: dict = create_dict(item, attrs)
      results.append(dic)
   return results


# Interface Layer ------------------------------------------------------------------


def to_list(array: list | None, attr: str | list[str] | None = None) -> list:
    """
    Convert a list of objects to a list of dictionaries or attribute values.
    
    Parameters:
    - array: The list of objects to convert.
    - attr: The attribute(s) to extract. If None, convert the entire object to a dictionary.
            If a single string, extract just that attribute from each object.
            If a list of strings, extract those attributes from each object.

    Returns:
    - A list of dictionaries or attribute values.
    """

    # If no attr is provided, convert the entire object to a dictionary
    if attr is None:
        return to_list_base(array)

    # If a single attribute is provided, extract just that attribute
    elif isinstance(attr, str):
        return to_list_with_attr(array, attr)

    # If a list of attributes is provided, extract those attributes
    elif isinstance(attr, list):
        return to_list_with_attrs(array, attr)

    else:
        raise ValueError("Invalid attr type. Expected None, str, or list[str].")

def get_value(value: any, attr: str) -> any:
    """
    Returns the value of an attribute of an object or None if the object or attribute is null.

    Parameters:
    - value: The object to retrieve the attribute from.
    - attr: The name of the attribute to retrieve.

    Returns:
    - The value of the attribute or None if the object or attribute is null.
    """
    return get_value_or_none(value, attr)