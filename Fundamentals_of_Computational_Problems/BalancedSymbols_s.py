# simple version - SA

lista = []
string = input()
for x in string:
    if x == '{' or x =='[' or x== '(':
        lista.append(x)
    
    else:
        if len (lista) > 0 and x == ')' and lista[-1] == '(':
            lista.pop(-1)
        elif len(lista) > 0 and x == ']' and lista[-1] == '[':
            lista.pop(-1)
        elif len(lista) > 0 and x == '}' and lista[-1] == '{':
            lista.pop(-1)
        elif x == ')' or x == ']' or x == '}':
            lista.append(x)
            break
    print(lista)
if len(lista) == 0:
    print("string bem formada")
else:
    print("string mal formada")