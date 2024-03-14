from utils import Bounds, Result, f, g

def dyhotomy(func: str, bounds: Bounds, eps: float) -> Result:
    bound_l = bounds.l
    bound_r = bounds.r
    root = None
    while abs(f(func, bound_r)-f(func, bound_l)) > eps:
        mid = (bound_l+bound_r) / 2
        if f(func, mid) == 0 or abs(f(func, mid)) < eps:
            root = mid
            break
        elif f(func, bound_l)*f(func, mid) < 0:
            bound_r = mid
        else:
            bound_l = mid

    func_value = f(func, root)

    result = Result(root, func_value, func_value)
    return result

def chord(func: str, bounds: Bounds, eps: float) -> Result:
    bound_l = bounds.l
    bound_r = bounds.r
    while True:
        assert f(func, bound_l) != f(func, bound_r), "Деление на 0"
        
        x0 = (bound_l-(bound_r-bound_l)*f(func, bound_l) / 
            (f(func, bound_r) - f(func, bound_l)))
        
        bound_l, bound_r = bound_r, x0
        
        if abs(f(func, x0)) <= eps:
            root = x0
            break
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result

def newton(func: str, bounds: Bounds, eps: float) -> Result:  
    bound_l = bounds.l  
    while True:
        assert g(func, bound_l) != 0.0, "Деление на 0"
        
        x0 = bound_l-f(func, bound_l)/g(func, bound_l)
        bound_l = x0
        
        if abs(f(func, x0)) <= eps:
            root = x0
            break
        
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result

def combined(func: str, bounds: Bounds, eps: float) -> Result:
    bound_l = bounds.l
    bound_r = bounds.r
    while True:
        c = (bound_l-(bound_r-bound_l)*f(func, bound_l) / 
            (f(func, bound_r) - f(func, bound_l)))

        if f(func, bound_l)*g(func, bound_l) > 0:
            bound_l = bound_l-f(func, bound_l)/g(func, bound_l)
            bound_r = c
        elif f(func, bound_r)*g(func, bound_r) > 0:
            bound_l = c
            bound_r = bound_l-f(func, bound_l)/g(func, bound_l)
        
        if abs(f(func, c)) <= eps:
            root = c
            break
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result

def iteration(func: str, bounds: Bounds, eps: float) -> Result:
    x0 = bounds.l
    
    while True:
        x1 = g(func, x0)

        if abs(x1 - x0) <= eps:
            root = x1
            break
        
        x0 = x1
    
    print(f"root = {root}")
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result

def golden(func: str, bounds: Bounds, eps: float) -> Result:
    bound_l = bounds.l
    bound_r = bounds.r
    while True:
        x1 = bound_r - (bound_r-bound_l) / 1.618
        x2 = bound_l + (bound_r-bound_l) / 1.618
        y1 = f(func, x1)
        y2 = f(func, x2)
        
        if y1 >= y2:
            bound_l = x1
        else:
            bound_r = x2

        if abs(bound_r-bound_l) < eps:
            root = (bound_l+bound_r) / 2
            break
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result