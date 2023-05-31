import sqlite3 as sq


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


# Cadastro de entidades
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

            print(f"\033[1;36m\nMédico {self.nome}, inserido com sucesso!\033[m")

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
            print(
                f"\033[1;36m\nDados do médico(a) de CRM: {self.crm} foi excluído com sucesso!\033[m"
            )

        except Exception as e:
            print("\033[1;31m\nErro ao deletar medico:\033[m", str(e))

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

            print(f"\033[1;36m\nMédico {self.nome}, alterado com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("\033[1;31m\nErro ao alterar medico:\033[m", e)

        finally:
            db.desconectdb()


class Hospital:
    def __init__(self, cnpj, nome, rua, bairro, cidade, cep, telefone):
        self.cnpj = cnpj
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.telefone = telefone

    def inserir_hospital(self):
        query = "INSERT INTO hospital (cnpj, nome, rua, bairro, cidade, cep, telefone) VALUES (?, ?, ?, ?, ?, ?, ?)"
        parametros = (
            self.cnpj,
            self.nome,
            self.rua,
            self.bairro,
            self.cidade,
            self.cep,
            self.telefone,
        )
        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nHospital {self.nome}, inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir hospital:", e)

        finally:
            db.desconectdb()

    def deletar_hospital(self):
        query = "DELETE FROM hospital WHERE cnpj = (?)"
        parametros = (self.cnpj,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)
            print(
                f"\033[1;36m\nDados do Hospital {self.nome}, foram excluídos com sucesso!\033[m"
            )
            db.conn.commit()
        except Exception as e:
            print("Erro ao deletar hospital:", str(e))

    def buscar_hospital(self):
        query = "SELECT cnpj, nome FROM hospital WHERE cnpj = (?)"
        parametros = (self.cnpj,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                cnpj_sl = row[0]
                nome_sl = row[1]
            print(f"\nCNPJ: {cnpj_sl}")
            print(f"Nome: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar hospital:", e)

        finally:
            db.desconectdb()

    def alterar_hospital(self):
        query = "UPDATE hospital SET cnpj = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ?, telefone = ? WHERE cnpj = (?)"
        parametros = (
            self.cnpj,
            self.nome,
            self.rua,
            self.bairro,
            self.cidade,
            self.cep,
            self.telefone,
        )

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nHospital {self.nome}, alterado com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("\033[1;31m\nErro ao alterar hospital:\033[m", e)

        finally:
            db.desconectdb()


class Enfermeira:
    def __init__(self, coren, cpf, nome, rua, bairro, cidade, cep):
        self.coren = coren
        self.cpf = cpf
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def inserir_enfermeira(self):
        query = "INSERT INTO enfermeira (coren, cpf, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?, ?)"
        parametros = (
            self.coren,
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

            print(f"\033[1;36mEnfermeira(o) {self.nome}, inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir hospital:", e)

        finally:
            db.desconectdb()

    def deletar_enfermeira(self):
        query = "DELETE FROM enfermeira WHERE coren = (?)"
        parametros = (self.coren,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)
            print(
                f"\033[1;36m\nDados da enfermeira(o) {self.nome}, foram excluídos com sucesso!\033[m"
            )
            db.conn.commit()
        except Exception as e:
            print("Erro ao deletar enfermeira:", str(e))

    def buscar_enfermeira(self):
        query = "SELECT coren, nome FROM enfermeira WHERE coren = (?)"
        parametros = (self.coren,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                coren_sl = row[0]
                nome_sl = row[1]
            print(f"\nCOREN: {coren_sl}")
            print(f"Nome: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar enfermeira:", e)

        finally:
            db.desconectdb()

    def alterar_enfermeira(self):
        query = "UPDATE enfermeira SET coren = ?, cpf = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE coren = (?)"
        parametros = (
            self.coren,
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

            print(f"\033[1;36m\nEnfermeira(o) {self.nome}, alterada com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("\033[1;31m\nErro ao alterar enfermeira:\033[m", e)

        finally:
            db.desconectdb()


class Paciente:
    def __init__(self, cpf, nome, rua, bairro, cidade, cep):
        self.cpf = cpf
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def inserir_paciente(self):
        query = "INSERT INTO paciente (cpf, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?)"
        parametros = (
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

            print(f"\033[1;36m\nPaciente {self.nome}, inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir paciente:", e)

        finally:
            db.desconectdb()

    def deletar_paciente(self):
        query = "DELETE FROM paciente WHERE cpf = (?)"
        parametros = (self.cpf,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)
            print(
                f"\033[1;36m\nDados do paciente {self.nome}, foram excluídos com sucesso!\033[m"
            )
            db.conn.commit()
        except Exception as e:
            print("Erro ao deletar paciente:", str(e))

    def buscar_paciente(self):
        query = "SELECT cpf, nome FROM paciente WHERE cpf = (?)"
        parametros = (self.coren,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                cpf_sl = row[0]
                nome_sl = row[1]
            print(f"\nCOREN: {cpf_sl}")
            print(f"Nome: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar paciente:", e)

        finally:
            db.desconectdb()

    def alterar_paciente(self):
        query = "UPDATE paciente SET cpf = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE cpf = (?)"
        parametros = (
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

            print(f"\033[1;36m\nPaciente {self.nome}, alterado com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("\033[1;31m\nErro ao alterar paciente:\033[m", e)

        finally:
            db.desconectdb()


# Implementação do menu e chamada de métodos das entidades
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

        medico = Medico(crm, cpf, nome, rua, bairro, cidade, cep)

        medico.inserir_medico()

    def delete_medico(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO MEDICO":>26}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        crm = input("\nInsira o CRM do médico(a): ")

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
        crm = input("CRM: ")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        medico = Medico(crm, cpf, nome, rua, bairro, cidade, cep)

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

        hosp = Hospital(cnpj, nome, rua, bairro, cidade, cep, telefone)

        hosp.inserir_hospital()

    def delete_hospital(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO HOSPITAL":>26}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cnpj = input("\nInsira o CNPJ do hospital: ")

        hosp = Hospital(cnpj, None, None, None, None, None, None)

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

        hosp = Hospital(cnpj, nome, rua, bairro, cidade, cep, tel)

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

        enf = Enfermeira(coren, cpf, nome, rua, bairro, cidade, cep)

        enf.inserir_enfermeira()

    def delete_enfermeira(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO ENFERMEIRA":>29}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        coren = input("\nInsira o COREN da enfermeira(o): ")

        enf = Enfermeira(coren, None, None, None, None, None, None)

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

        enf = Enfermeira(coren, cpf, nome, rua, bairro, cidade, cep)

        enf.alterar_enfermeira()

    # Instanciando métodos da entidade Paciente
    def insert_paciente(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE PACIENTE":>25}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cpf = input("CPF: ")
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")

        pac = Paciente(cpf, nome, rua, bairro, cidade, cep)

        pac.inserir_paciente()

    def delete_paciente(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"EXCLUIR CADASTRO PACIENTE":>28}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cpf = input("\nInsira o CPF do paciente: ")

        pac = Paciente(cpf, None, None, None, None, None, None)

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
        nome = input("Nome: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))

        pac = Paciente(cpf, nome, rua, bairro, cidade, cep)

        pac.alterar_paciente()


if __name__ == "__main__":
    app = menufront()
