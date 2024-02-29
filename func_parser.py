import numpy as np

def function_parser(func: str, x: float) -> str:
    if _have_unparsed(func):
        if "log(" in func:
            func = _bracket_func_parser(func, x, np.log10, "log(")
        if "cos(" in func:
            func = _bracket_func_parser(func, x, np.cos, "cos(")
        if "sin(" in func:
            func = _bracket_func_parser(func, x, np.sin, "sin(")
    
    if _have_unparsed(func):
        func = function_parser(func, x)
    elif "x" in func:
        func = func.replace("x", str(x))
    
    return func


def _find_bracket_end(func: str, func_index: int) -> int:
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
        

def _bracket_func_parser(func, x, parsing_type, parsing_type_name):
    # Находим границы мат. фуекции
    find_index = func.find(parsing_type_name)
    inner_func_start_index = find_index + len(parsing_type_name)
    inner_func_end_index = _find_bracket_end(func, find_index)
    
    # Находим внутреннюю и полную функции
    inner_func = func[inner_func_start_index:inner_func_end_index]
    full_inner_func = func[find_index:inner_func_end_index + 1]
    
    # Парсим функцию
    parsed_inner_func = function_parser(inner_func, x)
    
    # Добавляем x
    parsed_inner_func = parsed_inner_func.replace("x", str(x))
    
    # Получаем значение мат. функции и этим значием заменяем ее в строке
    temp_result = parsing_type(eval(parsed_inner_func))
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