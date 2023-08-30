from patterns import *
from math import sqrt
from re import findall

def get_number(eq: str, pattern):
    eq_part = findall(pattern, eq)[0]
    eq_part = eq_part.replace('^2', '')
    numbers = findall(NUMBERS, eq_part)
    if numbers:
        number = int(numbers[0])
    else:
        number = 1
    if '-' in eq_part:
        number *= -1
    return number

def get_data_eq(eq: str):
    val_name = findall(VAL_RE, eq)[0]
    a = get_number(eq, A_RE)
    b = get_number(eq, B_RE)
    c = get_number(eq, C_RE)
    return val_name, a, b, c 

def normalize_x(x: float):
    s1, s2 = str(x).split('.')
    for i in s2:
        if i == '0':
            s2 = s2[:-1]
        else:
            break
    if s2 == '':
        return s1
    return s1 + ',' + s2
            
def get_decision(eq: str):
    val_name, a, b, c = get_data_eq(eq.replace('−', '-'))
    d1 = b ** 2 
    d2 = - 4 * a * c
    d = d1 + d2
    z = ''
    if d2 > 0:
        z = '+' 
    result_strings = [
        f'D={d1}{z}{d2}={d}'
    ] 
    if d < 0:
        result_strings[0] += '; D<0 - нет корней'
    else:
        d = int(sqrt(d))
        result_strings.append(
            f'{val_name}_1=({-b}-{d})/{2 * a}={normalize_x((-b - d)/(2 * a))}'
        )
        if d != 0:
            result_strings[1] +=  f'; {val_name}_2=({-b}+{d})/{2 * a}={normalize_x((-b + d)/(2 * a))}'
    return result_strings