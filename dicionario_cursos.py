# IMPLEMENTAR AS SEGUINTES FUNÇÕES:
    # Listar os cursos cadastrados - retornar o número de cadastros
    # Dado um código de curso, retornar o nome do curso e duração em anos
    # Dado o nome de um curso, retornar o código do curso e duração em anos
    # Dado um código de curso, retornar um vetor com o nome de todas das disciplinas cadastradas para este curso
    # Dado o nome de um curso, retornar um vetor com o nome de todas das disciplinas cadastradas para este curso
    # Dado um código de curso, retornar a carga horária total de todas das disciplinas cadastradas para este curso
    # Dado o nome de um curso, retornar a carga horária total de todas das disciplinas cadastradas para este curso
    # Dado o nome de uma disciplina, consultar os cursos que a oferecem - retornar em um vetor
    # Dado o código de um curso, retornar um vetor contendo o código, o nome e a carga horária das disciplinas

DScurso=[ 
          {"CODIGO":"123456","NOME":"SISTEMAS DE INFORMACAO","DURACAO":4},
          {"CODIGO":"456789","NOME":"ENGENHARIA DE SOFTWARE","DURACAO":5},
          {"CODIGO":"987123","NOME":"CIENCIA DE DADOS","DURACAO":4},
          {"CODIGO":"567123","NOME":"NEGOCIOS DIGITAIS","DURACAO":4},
          {"CODIGO":"789432","NOME":"CIENCIA DA COMPUTACAO","DURACAO":5},
       ]

DSdisciplinas=[
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9031","DISCIPLINA":"ALGORITMOS E LÓGICA DE PROGRAMACAO I","HORASAULAS":120},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"3317","DISCIPLINA":"MINERACAO DE DADOS I","HORASAULAS":80},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"1418","DISCIPLINA":"MINERACAO DE DADOS II","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9032","DISCIPLINA":"ALGORITMOS E LÓGICA DE PROGRAMACAO II","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9033","DISCIPLINA":"ALGORITMOS E LÓGICA DE PROGRAMACAO III","HORASAULAS":120},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"4219","DISCIPLINA":"MINERACAO DE DADOS II","HORASAULAS":80},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"1034","DISCIPLINA":"PROJETO INTEGRADOR I","HORASAULAS":40},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6518","DISCIPLINA":"MODELAGEM DE NEGOCIOS DIGITAIS I","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6618","DISCIPLINA":"MODELAGEM DE NEGOCIOS DIGITAIS II","HORASAULAS":120},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9047","DISCIPLINA":"BANCO DE DADOS: APLICACAO","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6303","DISCIPLINA":"PROGRAMACAO WEB","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6342","DISCIPLINA":"BANCO DE DADOS I","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9059","DISCIPLINA":"BANCO DE DADOS: SEGURANCA","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9058","DISCIPLINA":"BANCO DE DADOS: CRIPTOGRAFICA","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9162","DISCIPLINA":"PROJETO INTEGRADOR I","HORASAULAS":120},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9264","DISCIPLINA":"PROJETO INTEGRADOR II","HORASAULAS":120},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9071","DISCIPLINA":"MINERACAO DE DADOS I","HORASAULAS":80},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"2923","DISCIPLINA":"PROJETO INTEGRADOR II","HORASAULAS":40},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"0301","DISCIPLINA":"ALGORITMOS COM PYTHON I","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9279","DISCIPLINA":"MINERACAO DE DADOS II","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6437","DISCIPLINA":"BANCO DE DADOS II","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6419","DISCIPLINA":"METODOLOGIAS ÁGEIS","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9372","DISCIPLINA":"ESTATISTICA I","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9384","DISCIPLINA":"ESTATISTICA II","HORASAULAS":40},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9392","DISCIPLINA":"INTELIGENCIA ARTIFICIAL I","HORASAULAS":160},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"1302","DISCIPLINA":"ALGORITMOS COM PYTHON  II","HORASAULAS":80},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"2303","DISCIPLINA":"ALGORITMOS COM PYTHON  III","HORASAULAS":80},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9032","DISCIPLINA":"BANCO DE DADOS: CONCEITOS","HORASAULAS":80},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"8302","DISCIPLINA":"ESTATISTICA I","HORASAULAS":40},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"3304","DISCIPLINA":"ESTATISTICA II","HORASAULAS":40},
        {"CODIGOCURSO":"789432","CODIGODISCIPLINA":"9384","DISCIPLINA":"INTELIGENCIA ARTIFICIAL II","HORASAULAS":160},     
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"0001","DISCIPLINA":"ALGORITMOS I","HORASAULAS":80},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"1002","DISCIPLINA":"ALGORITMOS II","HORASAULAS":80},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"2003","DISCIPLINA":"ALGORITMOS III","HORASAULAS":80},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"1042","DISCIPLINA":"BANCO DE DADOS I","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6177","DISCIPLINA":"PROJETO INTEGRADOR I","HORASAULAS":60},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"1302","DISCIPLINA":"PROJETO INTEGRADOR I","HORASAULAS":40},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"2304","DISCIPLINA":"PROJETO INTEGRADOR II","HORASAULAS":40},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6287","DISCIPLINA":"PROJETO INTEGRADOR II","HORASAULAS":120},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"2037","DISCIPLINA":"BANCO DE DADOS II","HORASAULAS":80},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"3019","DISCIPLINA":"BANCO DE DADOS III","HORASAULAS":80},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"4018","DISCIPLINA":"BANCO DE DADOS IV","HORASAULAS":80},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"1342","DISCIPLINA":"BANCO DE DADOS I","HORASAULAS":80},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"2338","DISCIPLINA":"BANCO DE DADOS II","HORASAULAS":80},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"1102","DISCIPLINA":"PROJETO INTEGRADOR I","HORASAULAS":40},
        {"CODIGOCURSO":"123456","CODIGODISCIPLINA":"2204","DISCIPLINA":"PROJETO INTEGRADOR II","HORASAULAS":40},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"0007","DISCIPLINA":"ALGORITMOS E LÓGICA I","HORASAULAS":80},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"1008","DISCIPLINA":"ALGORITMOS E LÓGICA  II","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6201","DISCIPLINA":"ALGORITMOS COM JAVA I","HORASAULAS":80},
        {"CODIGOCURSO":"567123","CODIGODISCIPLINA":"6202","DISCIPLINA":"ALGORITMOS COM JAVA II","HORASAULAS":80},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"2009","DISCIPLINA":"ALGORITMOS E LÓGICA  III","HORASAULAS":80},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"1020","DISCIPLINA":"BANCO DE DADOS: CONCEITOS","HORASAULAS":80},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"2015","DISCIPLINA":"BANCO DE DADOS: APLICACAO","HORASAULAS":80},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"6302","DISCIPLINA":"INTELIGENCIA ARTIFICIAL I","HORASAULAS":120},
        {"CODIGOCURSO":"987123","CODIGODISCIPLINA":"7304","DISCIPLINA":"INTELIGENCIA ARTIFICIAL II","HORASAULAS":120},
        {"CODIGOCURSO":"456789","CODIGODISCIPLINA":"3011","DISCIPLINA":"MINERACAO DE DADOS I","HORASAULAS":80},
        
        ]

# Listar os cursos cadastrados - retornar o número de cadastros

for curso in DScurso:
    print(curso)
    
num_curso = len(DScurso)
print(f"Cursos cadastrados:{num_curso}")

# Dado um código de curso, retornar o nome do curso e duração em anos

def local_curso(local):
    for curso in DScurso:
        if curso['CODIGO'] == local:
            return curso['NOME'], curso['DURACAO']
    return "Curso não encontrado", None

codigo_curso=input("Digite o codigo do curso:")
nome_curso, duracao_curso = local_curso(codigo_curso)
print("Nome do curso:", nome_curso)
print("Duração do curso:", duracao_curso, "anos")

# Dado o nome de um curso, retornar o código do curso e duração em anos

def local_nome(course_name):
    for curso in DScurso:
        if curso['NOME'] == course_name:
            return curso['CODIGO'], curso['DURACAO']
    return "Curso não encontrado", None

nome_curso=input("Digite o nome do curso:")
codigo_curso, duracao_curso = local_nome(nome_curso)
print("Código do curso:", codigo_curso)
print("Duração do curso:", duracao_curso, "anos")

# Dado um código de curso, retornar um vetor com o nome de todas das disciplinas cadastradas para este curso
def diciplinas(course_code):
    nome_diciplina = []
    for disciplina in DSdisciplinas:
        if disciplina['CODIGOCURSO'] == course_code:
            diciplinas.append(disciplina['DISCIPLINA'])
    return diciplinas

codigo_curso=input("Digite o codigo do curso:")
disciplinas_do_curso = diciplinas(codigo_curso)
print("Disciplinas do curso:", disciplinas_do_curso)

# Dado o nome de um curso, retornar um vetor com o nome de todas das disciplinas cadastradas para este curso

def get_course_code(course_name):
    for curso in DScurso:
        if curso['NOME'] == course_name:
            return curso['CODIGO']
    return None

def diciplinas_curso(course_name):
    course_code = get_course_code(course_name)
    if course_code is None:
        return None
    else:
        return diciplinas_curso(course_code)

nome_curso=input("Digite o nome do curso:")
disciplinas_do_curso = diciplinas_curso(nome_curso)
print("Disciplinas do curso:", disciplinas_do_curso)

# Dado um código de curso, retornar a carga horária total de todas das disciplinas cadastradas para este curso

def horas(course_code):
    total_horas = 0
    for disciplina in DSdisciplinas:
        if disciplina['CODIGOCURSO'] == course_code:
            total_horas += disciplina['HORASAULAS']
    return total_horas

codigo_curso=input("Digite o codigo do curso:")
carga_horaria_total = horas(codigo_curso)
print("Carga horária total do curso:", carga_horaria_total)

# Dado o nome de um curso, retornar a carga horária total de todas das disciplinas cadastradas para este curso
def horas_nome(course_name):
    total_hours = 0
    course_code = None
    for curso in DScurso:
        if curso['NOME'] == course_name:
            course_code = curso['CODIGO']
            break
    if course_code:
        for disciplina in DSdisciplinas:
            if disciplina['CODIGOCURSO'] == course_code:
                total_hours += disciplina['HORASAULAS']
    return total_hours

# Testando a função
nome_curso=input("Digite o nome do curso:")
carga_horaria_total = horas_nome(nome_curso)
print("Carga horária total do curso:", carga_horaria_total)

# Dado o nome de uma disciplina, consultar os cursos que a oferecem - retornar em um vetor

def cursos_diciplina(disciplina_nome):
    courses = []
    course_codes = []
    for disciplina in DSdisciplinas:
        if disciplina['DISCIPLINA'] == disciplina_nome:
            course_codes.append(disciplina['CODIGOCURSO'])
    for curso in DScurso:
        if curso['CODIGO'] in course_codes:
            courses.append(curso['NOME'])
    return courses

nome_disciplina = input("Digite o nome da disciplinas:")
cursos = cursos_diciplina(nome_disciplina)
print("Cursos que oferecem a disciplina:", cursos)
