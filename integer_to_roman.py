I=1
II=2
III=3
IV=4
V=5
VI=6
VII=7
VIII=8  
IX=9
X=10
L=50
C=100
D=500
M=1000
CM=900
CD=400  
XC=90
XL=40

def int_to_roman(num):
    val = [
        M, CM, D, CD,
        C, XC, L, XL,
        X, IX, V, IV,
        I
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

print(int_to_roman(1994))
print(int_to_roman(2025))
