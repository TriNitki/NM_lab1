from utils import Bounds, Input
import numpy as np

def get_input() -> Input:
    method_num = int(input("Введите номер метода: "))
    func = input("Введите исследуемую функцию: ").strip()
    left_bound = float(input("Введите левую границу: "))
    right_bound = float(input("Введите парвую границу: "))
    accuracy = float(input("Введите точность решения: "))
    
    bounds = Bounds(left_bound, right_bound)
    user_input = Input(method_num, func, bounds, accuracy)
    
    return user_input

def function_parser(func: str, x: float) -> str:
    # Логарифмы, cos, sin, exp,pi
    
    if _have_unparsed(func):
        if "log(" in func:
            find_index = func.find("log(")
            inner_func_start_index = find_index + len("log(")
            inner_func_end_index = _find_bracket_end(func, find_index)
            
            inner_func = func[inner_func_start_index:inner_func_end_index]
            
            full_inner_func = func[find_index:inner_func_end_index + 1]
            
            parsed_inner_func = function_parser(inner_func, x)
            
            temp_result = np.log10(eval(parsed_inner_func))
            func = func.replace(full_inner_func, str(temp_result), 1)
    
    if _have_unparsed(func):
        func = function_parser(func, x)
    
    return func


def _find_bracket_end(func: str, func_index) -> int:
    open_amount = 0
    close_amount = 0
    for i in range(func_index, len(func)):
        if func[i] == "(":
            open_amount += 1
        elif func[i] == ")":
            close_amount += 1
        
        if open_amount != 0 and open_amount == close_amount:
            return i
    
    return -1
        

# def _bracket_funcs(func, func_name, x):
#     pass


# Проверяет есть ли в функции отпарсилась или нет
def _have_unparsed(func: str) -> bool:
    if "log(" in func:
        return True
    
    if "cos(" in func:
        return True
    
    if "sin(" in func:
        return True
    
    if "pi" in func:
        return True
    
    if "exp" in func:
        return True
    
    return False