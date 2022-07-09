pacientes  = []
procedimento = 0
codigo_paciente = 0

class Paciente:
    def __init__(self, codigo, nome, cpf, vacina, data, n_lote):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.vacina = vacina
        self.data = data
        self.n_lote = n_lote

def imprime_instrucoes():
    print("[1] Para cadastrar novo paciente;")
    print("[2] Para listar aplicações;")
    print("[3] Para buscar por CPF;")
    print("[4] Para sair.")

def cadastrar_paciente():
        nome_paciente = input("Informe o nome do paciente: ")
        cpf_paciente = input("Informe o CPF do paciente: ")
        vacina_paciente = input("Informe a vacina aplicada no paciente: ")
        data_aplicacao = input("Informe a data de aplicação da vacina: ")
        lote_vacina = input("Informe o número do lote da vacina: ")
        paciente = Paciente(codigo_paciente, nome_paciente, cpf_paciente, vacina_paciente, data_aplicacao, lote_vacina)
        pacientes.append(paciente)

def listar_aplicacoes():
    for n in pacientes:
        print("\nCódigo:", n.codigo)
        print("Nome:", n.nome)
        print("CPF:", n.cpf)
        print("Vacina aplciada:", n.vacina)
        print("Data de aplicação:", n.data)
        print("Número do lote da vacina:", n.n_lote)
        print("=====================================\n")
    
def buscar_cpf():
    cont = 0
    cpf_informado = input("Informe o CPF: ")
            
    for x in pacientes:
        if(cpf_informado == x.cpf):
            print("\nCódigo:", x.codigo)
            print("Nome:", x.nome)
            print("CPF:", x.cpf)
            print("Vacina aplciada:", x.vacina)
            print("Data de aplicação:", x.data)
            print("Número do lote da vacina:", x.n_lote)
            print("=====================================\n")
            cont += 1
        else:
            False
            
    if(cont == 0):
        print("Não há pacientes cadastrados com esse CPF!")

while procedimento != 4:

    imprime_instrucoes()
    procedimento = int(input("Informe qual o procedimento: "))

    if(procedimento > 4 or procedimento < 0):
        print("Comando inválido!!")
    
    if(procedimento == 1):
        cadastrar_paciente()
        codigo_paciente += 1

    if(len(pacientes) > 0):
        if(procedimento == 2):
            listar_aplicacoes()
            
        if(procedimento == 3):
            buscar_cpf()

    else:
        print("Não há pacientes cadastrados!!")        
