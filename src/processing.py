from typing import Iterable, Any

def filter_by_state(dict_list: Iterable[list[dict[Any, Any]]], state: Any='CANCELED')-> list[list[dict[Any, Any]]]:
    """функция для выведения данных по значению"""
    executed_list = []
    for i in dict_list:
        if i['state'] == state:
            executed_list.append(i)
    return executed_list

