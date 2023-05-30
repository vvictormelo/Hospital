import sqlite3 as sq


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
                                cnpj INTEGER(13) PRIMARY KEY UNIQUE,
                                nome TEXT(20) NOT NULL,
                                rua TEXT(50) NOT NULL,
                                bairro TEXT(20) NOT NULL,
                                cidade TEXT(20) NOT NULL,
                                cep INTEGER(8) NOT NULL,
                                telefone INTEGER(10) NOT NULL)"""
            )

            # Criação da tabela do medico
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS medico(
                                crm INTEGER(10) PRIMARY KEY UNIQUE,
                                cpf INTEGER(11) NOT NULL,
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
                                coren INTEGER(10) PRIMARY KEY UNIQUE,
                                cpf INTEGER(11) NOT NULL,
                                nome TEXT(50) NOT NULL,
                                rua TEXT(50) NOT NULL,
                                bairro TEXT(20) NOT NULL,
                                cidade TEXT(20) NOT NULL,
                                cep INTEGER(8) NOT NULL)"""
            )

            # Criação da tabela paciente
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS paciente(
                                cpf INTEGER(11) NOT NULL,
                                nome INTEGER(50) NOT NULL,
                                rua INTEGER(50) NOT NULL,
                                bairro INTEGER(20) NOT NULL,
                                cidade INTEGER(20) NOT NULL,
                                cep TEXT(8) NOT NULL)"""
            )

            self.conn.commit()
            print("\033[1;36m\nTabelas criadas com sucesso!\033[m")

        except ConnectionError as e:
            print("Erro no banco", e)

        finally:
            self.desconectdb()


db = Database()


class Medico:
    def __init__(self, crm, cpf, nome, rua, bairro, cidade, cep):
        super().__init__
        self.crm = crm
        self.cpf = cpf
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def inserir_medico(self):
        query = "INSERT INTO medico (crm, cpf, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?, ?)"
        parametros = (
            self.crm,
            self.cpf,
            self.nome,
            self.rua,
            self.bairro,
            self.cidade,
            self.cep,
        )
        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(
                f"\033[1;36m-=\033[m\nMédico {self.nome}, inserido com sucesso!\033[m"
            )

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir medico:", e)

        finally:
            db.desconectdb()

    def deletar_medico(self):
        query = "DELETE FROM medico WHERE crm = (?)"
        parametros = (self.crm,)

        try:
            db.executar_query(query, parametros)
            print(f"Dados do médico(a) de CRM: {self.crm} foi excluído com sucesso!")

        except Exception as e:
            print("Erro ao deletar medico:", str(e))

    def buscar_medico(self):
        query = "SELECT crm, nome FROM medico WHERE crm = (?)"
        parametros = (self.crm,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                crm_sl = row[0]
                nome_sl = row[1]
            print(f"\nCRM: {crm_sl}")
            print(f"Nome: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar medico(a):", e)

        finally:
            db.desconectdb()

    def alterar_medico(self):
        query = "UPDATE medico SET crm = ?, cpf = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE crm = (?)"
        parametros = (
            self.crm,
            self.cpf,
            self.nome,
            self.rua,
            self.bairro,
            self.cidade,
            self.cep,
        )

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(
                f"\033[1;36m-=\033[m\nMédico {self.nome}, alterado com sucesso!\033[m"
            )

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir medico:", e)

        finally:
            db.desconectdb()


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
        print("2 - Criar hospital")
        print("3 - Criar médico(a)")
        print("3.1 - Deletar médico(a)")
        print("3.2 - Alterar médico(a)")
        print("4 - Sair")

    def program(self):
        print("\033[1;36m\nSEJA BEM VINDO...\033[m")

        self.acao = 0

        while self.acao != 4:
            try:
                self.menu()
                self.acao = float(input("\nInsira a ação desejada: "))
                match self.acao:
                    case 1:
                        self.criartabelas()
                    case 2:
                        self.inserthospital()
                    case 3:
                        self.insert_medico()
                    case 3.1:
                        self.delete_medico()
                    case 3.2:
                        self.update_medico()
                    case 4:
                        self.acao = 4
                        print("\nSaindo... Até logo!")
                if self.acao > 4 or self.acao < 1:
                    print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")

            except ValueError:
                print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")

    def insert_medico(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE MÉDICO(A)":>15}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        crm = int(input("CRM: "))
        cpf = int(input("CPF: "))
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        medico = Medico(crm, cpf, nome, rua, bairro, cidade, cep)

        medico.inserir_medico()

    def delete_medico(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO MEDICO":>26}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        crm = int(input("\nInsira o CRM do médico(a): "))

        medico = Medico(crm, None, None, None, None, None, None)

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
        crm = int(input("CRM: "))
        cpf = int(input("CPF: "))
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        medico = Medico(crm, cpf, nome, rua, bairro, cidade, cep)

        medico.alterar_medico()


if __name__ == "__main__":
    app = menufront()
