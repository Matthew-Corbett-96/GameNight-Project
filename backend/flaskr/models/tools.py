def is_null(value: any) -> bool:
   if value is None:
      return True
   return False

def get_value_or_none(value: any, attr: str) -> any:
   if is_null(value):
      return None
   if is_null(getattr(value, attr)):
      return None
   return getattr(value, attr)

def create_dict(value: any, attrs: list[str]) -> dict:
   if is_null(value):
      return {}
   
   if is_null(attrs) or len(attrs) == 0:
      return value.to_dict()
   
   results: dict[str, any] = {}
   for attr in attrs:
      results[attr] = get_value_or_none(value, attr)
   return results

def to_list(array: list | None) -> list:
   if is_null(array) or len(array) == 0:
      return []
   return [item.to_dict() for item in array]

def to_list(array: list | None, attr: str) -> list:
   if is_null(array) or len(array) == 0:
      return []
   return [get_value_or_none(item, attr) for item in array]

def to_list(array: list | None, attrs: list[str]) -> list:
   if is_null(array) or len(array) == 0:
      return []
   
   results: list[dict] = [{}]
   for item in array:
      dic: dict = create_dict(item, attrs)
      results.append(dic)
   return results
