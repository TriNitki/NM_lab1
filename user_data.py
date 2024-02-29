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
            inner_func_end_index = inner_func_start_index + func[inner_func_start_index:].find(")")
            
            inner_func = func[inner_func_start_index:inner_func_end_index]
            
            inner_bracket_amount = inner_func.count("(")
            inner_func += ")" * inner_bracket_amount
            
            full_inner_func = func[find_index:inner_func_end_index + inner_bracket_amount + 1]
            
            parsed_inner_func = function_parser(inner_func, x)
            
            temp_result = np.log(eval(parsed_inner_func))
            func = func.replace(full_inner_func, str(temp_result), 1)
            
    return func

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