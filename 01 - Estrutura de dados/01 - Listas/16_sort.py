# sort - ordena lista
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)
linguagens.sort()  # ['c', 'csharp', 'java', 'js', 'python']
print(linguagens)

print()

linguagens = ["python", "js", "c", "java", "csharp"]
# pega a lista ordenada e coloca de tras para frente / ['python', 'js', 'java', 'csharp', 'c']
linguagens.sort(reverse=True)
print(linguagens)

print()

# ordenando por tamanho da palavra - ordem crescente
linguagens = ["python", "js", "c", "java", "csharp"]
# ['c', 'js', 'java', 'python', 'csharp']
linguagens.sort(key=lambda x: len(x))
print(linguagens)

print()

linguagens = ["python", "js", "c", "java", "csharp"]
# ['python', 'csharp', 'java', 'js', 'c']
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)
