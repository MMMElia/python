a = input("Введите число в основании ")
n = input("Введите число в степени ")

def recur(base, st, fix):
    if int(st) > 1:
        base = int(base) * int(fix)
        st = int(st) - 1
        return recur(base, st, fix)
    else:
        return base
    
print(recur(a, n, a))