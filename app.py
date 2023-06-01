import sqlite3 as sq
import entities


# Implementação e criação do banco de dados
class Database:
    def conectadb(self):
        self.conn = sq.connect("hospital.db")
        self.cursor = self.conn.cursor()

    def desconectdb(self):
        self.cursor.close()
        self.conn.close()

    def criartabelas(self):
        try:
            self.conectadb()
            self.conn.execute("PRAGMA foreign_keys=on")

            # Criação da tabela do hospital
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS hospital( 
                                cnpj TEXT(13) PRIMARY KEY UNIQUE,
                                nome TEXT(20) NOT NULL,
                                rua TEXT(50) NOT NULL,
                                bairro TEXT(20) NOT NULL,
                                cidade TEXT(20) NOT NULL,
                                cep TEXT(8) NOT NULL,
                                telefone INTEGER(10) NOT NULL)"""
            )

            # Criação da tabela do medico
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS medico(
                                crm TEXT(10) PRIMARY KEY UNIQUE,
                                cpf TEXT(11) NOT NULL,
                                nome TEXT(50) NOT NULL,
                                rua TEXT(50) NOT NULL,
                                bairro TEXT(20) NOT NULL,
                                cidade TEXT(20) NOT NULL,
                                cep INTEGER(8) NOT NULL)"""
            )

            # Criação da tabela auxiliar hospital x medico
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS hosp_med(
                                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                id_cnpj REFERENCES hospital(cnpj),
                                id_crm REFERENCES medico(crm))"""
            )

            # Criação da tabela auxiliar hospital x enfermeira
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS hosp_enfer(
                                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                id_cnpj REFERENCES hospital(cnpj),
                                id_coren REFERENCES enfermeira(coren))"""
            )

            # Criação da tabela auxiliar medico x paciente
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS med_pac(
                                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
                                id_crm REFERENCES medico(crm),
                                id_cpf REFERENCES paciente(cpf))"""
            )

            # Criação da tabela auxiliar medico x enfermeira
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS med_enf(
                                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
                                id_crm REFERENCES medico(crm),
                                id_coren REFERENCES enfermeira(coren))"""
            )

            # Criação da tabela especialidade
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS especialidade(
                                cod_esp INTEGER(4) PRIMARY KEY UNIQUE,
                                documento TEXT(10) NOT NULL,
                                especialidade_desc TEXT(50) NOT NULL,
                                crm_medico REFERENCES medico(crm))"""
            )

            # Criação da tabela telefone
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS telefone(
                                cod_num INTEGER(4) PRIMARY KEY UNIQUE,
                                documento TEXT(10) NOT NULL,
                                telefone INTEGER(10) NOT NULL,
                                crm_medico REFERENCES medico(crm))"""
            )

            # Criação da tabela enfermeira
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS enfermeira(
                                coren TEXT(10) PRIMARY KEY UNIQUE,
                                cpf TEXT(11) NOT NULL,
                                nome TEXT(50) NOT NULL,
                                rua TEXT(50) NOT NULL,
                                bairro TEXT(20) NOT NULL,
                                cidade TEXT(20) NOT NULL,
                                cep INTEGER(8) NOT NULL)"""
            )

            # Criação da tabela paciente
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS paciente(
                                cpf TEXT(11) NOT NULL,
                                rg TEXT(10) NOT NULL,
                                nome TEXT(50) NOT NULL,
                                rua TEXT(50) NOT NULL,
                                bairro TEXT(20) NOT NULL,
                                cidade TEXT(20) NOT NULL,
                                cep TEXT(8) NOT NULL)"""
            )

            self.conn.commit()
            print("\033[1;36m\nTabelas criadas com sucesso!\033[m")

        except ConnectionError as e:
            print("Erro no banco", e)

        finally:
            self.desconectdb()


db = Database()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
#  Implementação do menu e chamada de métodos das entidades
class menufront:
    def __init__(self):
        super().__init__()
        self.program()

    def menu(self):
        print("\n")
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"MENU INICIAL":>22}\033[m')
        print("\033[1;36m-=\033[m" * 15)
        print("\n1 - Criar tabelas")
        print("")
        print("Hospital")
        print("2 - Criar hospital")
        print("2.1 - Excluir hospital")
        print("2.2 - Alterar hospital")
        print("")
        print("Médicos")
        print("3 - Criar médico(a)")
        print("3.1 - Deletar médico(a)")
        print("3.2 - Alterar médico(a)")
        print("")
        print("Enfermeira")
        print("4 - Criar enfermeira(o)")
        print("4.1 - Deletar enfermeira(o)")
        print("4.2 - Alterar enfermeira(o)")
        print("")
        print("Paciente")
        print("5 - Criar paciente")
        print("5.1 - Deletar paciente")
        print("5.2 - Alterar paciente")
        print("")
        print("7 - Sair")

    def program(self):
        print("\033[1;36m\nSEJA BEM VINDO...\033[m")

        self.acao = 0

        while self.acao != 7:
            try:
                self.menu()
                self.acao = float(input("\nInsira a ação desejada: "))
                match self.acao:
                    case 1:
                        db.criartabelas()
                    case 2:
                        self.insert_hospital()
                    case 2.1:
                        self.delete_hospital()
                    case 2.2:
                        self.update_hospital()
                    case 3:
                        self.insert_medico()
                    case 3.1:
                        self.delete_medico()
                    case 3.2:
                        self.update_medico()
                    case 4:
                        self.insert_enfermeira()
                    case 4.1:
                        self.delete_enfermeira()
                    case 4.2:
                        self.update_enfermeira()
                    case 5:
                        self.insert_paciente()
                    case 5.1:
                        self.delete_paciente()
                    case 5.2:
                        self.update_paciente()
                    case 7:
                        self.acao = 7
                        print("\nSaindo... Até logo!")
                if self.acao > 7 or self.acao < 1:
                    print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")

            except ValueError:
                print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")

    # Instanciando métodos da entidade Médico
    def insert_medico(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE MÉDICO(A)":>15}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        crm = input("CRM: ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")

        medico = entities.Medico(crm, cpf, nome, rua, bairro, cidade, cep)

        medico.inserir_medico()

    def delete_medico(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO MEDICO":>26}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        crm = input("\nInsira o CRM do médico(a): ")

        medico = entities.Medico(crm, None, None, None, None, None, None)

        medico.buscar_medico()

        check = input("\nDeseja confirmar a exclusão? ")

        if check in "SssimSim":
            medico.deletar_medico()
        else:
            self.program()

    def update_medico(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"ALTERAR CADASTRO MEDICO":>27}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        print("*Insira as novas informações*")
        crm = input("CRM: ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        medico = entities.Medico(crm, cpf, nome, rua, bairro, cidade, cep)

        medico.alterar_medico()

    # Instanciando métodos da entidade Hospital
    def insert_hospital(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE HOSPITAL":>20}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cnpj = input("CNPJ: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))
        telefone = int(input("Telefone: "))

        hosp = entities.Hospital(cnpj, nome, rua, bairro, cidade, cep, telefone)

        hosp.inserir_hospital()

    def delete_hospital(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO HOSPITAL":>26}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cnpj = input("\nInsira o CNPJ do hospital: ")

        hosp = entities.Hospital(cnpj, None, None, None, None, None, None)

        hosp.buscar_hospital()

        check = input("\nDeseja confirmar a exclusão? ")

        if check in "SssimSim":
            hosp.deletar_hospital()
        else:
            self.program()

    def update_hospital(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"ALTERAR CADASTRO HOSPITAL":>27}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        print("*Insira as novas informações*")
        cnpj = input("CNPJ: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))
        tel = int(input("Telefone: "))

        hosp = entities.Hospital(cnpj, nome, rua, bairro, cidade, cep, tel)

        hosp.alterar_hospital()

    # Instanciando métodos da entidade Enfermeira
    def insert_enfermeira(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE ENFERMEIRA":>26}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        coren = input("COREN: ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")

        enf = entities.Enfermeira(coren, cpf, nome, rua, bairro, cidade, cep)

        enf.inserir_enfermeira()

    def delete_enfermeira(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO ENFERMEIRA":>29}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        coren = input("\nInsira o COREN da enfermeira(o): ")

        enf = entities.Enfermeira(coren, None, None, None, None, None, None)

        enf.buscar_enfermeira()

        check = input("\nDeseja confirmar a exclusão? ")

        if check in "SssimSim":
            enf.deletar_enfermeira()
        else:
            self.program()

    def update_enfermeira(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"ALTERAR CADASTRO ENFERMEIRA":>29}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        print("*Insira as novas informações*")
        coren = input("COREN: ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        enf = entities.Enfermeira(coren, cpf, nome, rua, bairro, cidade, cep)

        enf.alterar_enfermeira()

    # Instanciando métodos da entidade Paciente
    def insert_paciente(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE PACIENTE":>25}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cpf = input("CPF: ")
        rg = input("RG: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")

        pac = entities.Paciente(cpf, rg, nome, rua, bairro, cidade, cep)

        pac.inserir_paciente()

    def delete_paciente(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO PACIENTE":>28}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cpf = input("\nInsira o CPF do paciente: ")

        pac = entities.Paciente(cpf, None, None, None, None, None, None, None)

        pac.buscar_paciente()

        check = input("\nDeseja confirmar a exclusão? ")

        if check in "SssimSim":
            pac.deletar_paciente()
        else:
            self.program()

    def update_paciente(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"ALTERAR CADASTRO PACIENTE":>28}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        print("*Insira as novas informações*")
        cpf = input("CPF: ")
        rg = input("RG: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        pac = entities.Paciente(cpf, rg, nome, rua, bairro, cidade, cep)

        pac.alterar_paciente()


if __name__ == "__main__":
    app = menufront()
