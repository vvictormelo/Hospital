from app import db


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
    def __init__(self, rg, cpf, nome, rua, bairro, cidade, cep):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def inserir_paciente(self):
        query = "INSERT INTO paciente (cpf, rg, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?)"
        parametros = (
            self.cpf,
            self.rg,
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
        parametros = (self.cpf,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                cpf_sl = row[0]
                nome_sl = row[1]
            print(f"\nCPF: {cpf_sl}")
            print(f"Nome: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar paciente:", e)

        finally:
            db.desconectdb()

    def alterar_paciente(self):
        query = "UPDATE paciente SET cpf = ?, rg = ?, nome = ?, rua = ?, bairro = ?, cidade = ?, cep = ? WHERE cpf = (?)"
        parametros = (
            self.cpf,
            self.rg,
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
