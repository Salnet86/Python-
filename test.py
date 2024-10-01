x = ['abbiamo superato 10' if t > 10 else f'valore e {t}' for t in range(11)]
z = [t if t < 10 else f'valore superiore io 9 e {t}' for t in range(11)]


#print(x)

print(z)


[expression for item in iterable if condition]

even_numbers = [x for x in range(20) if x % 2 == 0]
squares = [(x, x**2) for x in range(5)]
nested_list = [[1, 2], [3, 4], [5]]
flat_list = [item for sublist in nested_list for item in sublist]
uppercase_words = [word.upper() for word in ['hello', 'world']]
words = [word for line in ['hello world', 'python is great'] for word in line.split()]
