# Cadastro de Skills e Tecnologias para o seu portfólio

skillsList = []

while True:
    skill = input("Inclua uma skill ou tecle (s) para sair: ")
    if not skill:
        skill = input("Inclua uma skill ou tecle (s) para sair: ")
    elif skill == 's':
        break
    else:
        skillsList.append(skill)

print()
print("Skills cadastradas para o seu portfólio: ")
print()
for skills in skillsList:
    print(skills)

