import sqlite3 as sq


class Backend:
    def conectadb(self):
        self.conn = sq.connect("hospital.db")
        self.cursor = self.conn.cursor()

    def desconectdb(self):
        self.cursor.close()
        self.cursor.close()

    def criartabelas(self):
        try:
            self.conectadb()
            self.conn.execute("PRAGMA foreign_keys=on")

            # Criação da tabela do hospital
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS hospital( 
                                cnpj VARCHAR(13) PRIMARY KEY UNIQUE,
                                nome VARCHAR(20) NOT NULL,
                                rua VARCHAR(50) NOT NULL,
                                bairro VARCHAR(20) NOT NULL,
                                cidade VARCHAR(20) NOT NULL,
                                cep VARCHAR(8) NOT NULL,
                                telefone VARCHAR(10) NOT NULL)"""
            )

            # Criação da tabela do medico
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS medico(
                                crm VARCHAR(10) PRIMARY KEY UNIQUE,
                                cpf VARCHAR(11) NOT NULL,
                                nome VARCHAR(50) NOT NULL,
                                rua VARCHAR(50) NOT NULL,
                                bairro VARCHAR(20) NOT NULL,
                                cidade VARCHAR(20) NOT NULL,
                                cep VARCHAR(8) NOT NULL)"""
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
                                documento VARCHAR(10) NOT NULL,
                                especialidade_desc VARCHAR(50) NOT NULL,
                                crm_medico REFERENCES medico(crm))"""
            )

            # Criação da tabela telefone
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS telefone(
                                cod_num INTEGER(4) PRIMARY KEY UNIQUE,
                                documento VARCHAR(10) NOT NULL,
                                telefone VARCHAR(10) NOT NULL,
                                crm_medico REFERENCES medico(crm))"""
            )

            # Criação da tabela enfermeira
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS enfermeira(
                                coren VARCHAR(10) PRIMARY KEY UNIQUE,
                                cpf INTEGER(11) NOT NULL,
                                nome VARVHAR(50) NOT NULL,
                                rua VARCHAR(50) NOT NULL,
                                bairro VARCHAR(20) NOT NULL,
                                cidade VARCHAR(20) NOT NULL,
                                cep VARCHAR(8) NOT NULL)"""
            )

            # Criação da tabela paciente
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS paciente(
                                cpf INTEGER(11) NOT NULL,
                                nome VARVHAR(50) NOT NULL,
                                rua VARCHAR(50) NOT NULL,
                                bairro VARCHAR(20) NOT NULL,
                                cidade VARCHAR(20) NOT NULL,
                                cep VARCHAR(8) NOT NULL)"""
            )

            self.conn.commit()
            print("\033[1;36m\nTabelas criadas com sucesso!\033[m")

        except ConnectionError as e:
            print("Erro no banco", e)

        finally:
            self.desconectdb()

    def inserthospital(self):
        print("\033[1;36m-=\033[m" * 15)
        print(f'\033[1;36m{"CADASTRO DE HOSPITAL":>22}\033[m')
        print("\033[1;36m-=\033[m" * 15)

        cnpj = int(input("CNPJ do Hospital: "))
        nome = input("Nome do Hospital: ")
        print("*Endereço*")
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = int(input("CEP: "))
        telefone = int(input("Telefone: "))

        try:
            self.conectadb()

            self.cursor.execute(
                """INSERT INTO hospital (cnpj, nome, rua, bairro, cidade, cep, telefone) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    cnpj,
                    nome,
                    rua,
                    bairro,
                    cidade,
                    cep,
                    telefone,
                ),
            )

            self.conn.commit()

            print("\033[1;36m\nHospital criado com sucesso!\033[m")

        except sq.Error as e:
            print("Erro!", e)

        finally:
            self.desconectdb()


class menufront(Backend):
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
                    case 4:
                        self.acao = 4
                        print("\nSaindo... Até logo!")
                if self.acao > 4 or self.acao < 1:
                    print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")

            except ValueError:
                print("\033[1;31m\nOops...Ação inválida. Tente novamente!\n\033[m")


if __name__ == "__main__":
    app = menufront()
