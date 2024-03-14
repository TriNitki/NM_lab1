from utils import Bounds, Result, f, g

def dyhotomy(func: str, bounds: Bounds, eps: float) -> Result:
    bound_l = bounds.l
    bound_r = bounds.r
    root = None
    while abs(f(func, bound_r)-f(func, bound_l)) > eps:
        mid = (bound_l+bound_r) / 2
        if f(func, mid) == 0 or abs(f(func, mid)) < eps:
            break
        elif f(func, bound_l)*f(func, mid) < 0:
            bound_r = mid
        else:
            bound_l = mid

    root = mid

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

def iteration(func: str, bounds: Bounds, eps: float, max_attempts: int = 10) -> Result:
    x0 = bounds.l
    attempt = 0
    
    while True:
        attempt += 1
        x1 = g(func, x0)

        if max_attempts <= attempt:
            root = g(func, bounds.l)
            break
        
        if abs(x1 - x0) <= eps:
            root = x1
            break
        
        x0 = x1
    
    print(f"root = {root}")
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result

def golden(func: str, bounds: Bounds, eps: float) -> Result:
    import math
    
    a = bounds.l
    b = bounds.r
    
    j = (math.sqrt(5) + 1) / 2
    
    while True:
        d = a + (b - a) / j
        c = a + (b - a) / j**2
        
        if (f(func, a) * f(func, d) <= 0):
            b = d
        else:
            a = c
        
        if abs((b - a) / 2) <= eps:
            root = c
            break
    
    
    
    func_value = f(func, root)
    result = Result(root, func_value, func_value)
    return result