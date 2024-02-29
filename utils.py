from func_parser import function_parser
from sympy import diff, symbols, cos, sin, log  # noqa: F401

class Bounds:
    def __init__(self, left_bound: float, right_bound: float) -> None:
        self.l = left_bound
        self.r = right_bound

class Input:
    def __init__(self, method_num: int, func: str, bounds: Bounds, eps: float) -> None:
        self.method_num = method_num
        self.func = func
        self.bounds = bounds
        self.eps = eps

class Result:
    def __init__(self, result_value: float, func_value: float, eps: float) -> None:
        self.result_value = result_value
        self.func_value = func_value
        self.eps = eps
    
    def __str__(self) -> str:
        return f"{'Решение уравнения:':40}{self.result_value:.7f}\n" + \
            f"{'Значение функции в найденной точке x:':40}{self.func_value:.7f}\n" + \
            f"{'Погрешность полученного решения:':40}{self.eps:.6f}%"

def get_input() -> Input:
    method_num = int(input("Введите номер метода: "))
    func = input("Введите исследуемую функцию: ").strip()
    left_bound = float(input("Введите левую границу: "))
    right_bound = float(input("Введите парвую границу: "))
    accuracy = float(input("Введите точность решения: "))
    
    bounds = Bounds(left_bound, right_bound)
    user_input = Input(method_num, func, bounds, accuracy)
    
    return user_input    

def f(func, x_value):
    return eval(function_parser(func, x_value))

def d(func, x_value):
    x = symbols('x')
    dir_func = str(diff(eval(func), x))
    return eval(function_parser(dir_func, x_value))