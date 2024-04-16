nome = "MaXsUel"

print(nome)
print(nome.upper())
print(nome.lower())
print(nome.title())
print(nome.capitalize())
print(nome.center(20, '='))
print('_'.join(nome))
print(nome.ljust(30), end='.\n')
print(nome.rjust(30), end='.\n')

print('---'*30)
curso = '    python    '

print(curso + '.')
print(curso.strip() + '.')
print(curso.lstrip() + '.')
print(curso.rstrip() + '.')