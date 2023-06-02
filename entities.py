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
            db.cursor.execute(query, parametros)
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

    def listar_medicos(self):
        query = "SELECT crm, nome FROM medico ORDER BY nome"

        try:
            db.conectadb()
            db.cursor.execute(query)

            for medico in db.cursor.fetchall():
                crm, nome = medico
                print(f"""CRM: {crm} / Nome: {nome}""")

        except Exception as e:
            print("Erro ao buscar medicos:", e)

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

            print(f"\033[1;36m\n{self.nome}, inserido com sucesso!\033[m")

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

    def listar_hospitais(self):
        query = "SELECT cnpj , nome FROM hospital ORDER BY nome"

        try:
            db.conectadb()
            db.cursor.execute(query)

            for hospital in db.cursor.fetchall():
                cnpj, nome = hospital
                print(f"""CNPJ: {cnpj} / Nome: {nome}""")

        except Exception as e:
            print("Erro ao buscar hospitais:", e)

        finally:
            db.desconectdb()


class HospMed:
    def __init__(self, cnpj, crm):
        self.cnpj = cnpj
        self.crm = crm

    def vinc_hospital_medicos(self):
        query = "INSERT INTO hosp_med (cnpj, crm) VALUES (?, ?)"
        parametros = (
            self.cnpj,
            self.crm,
        )
        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nVínculo inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir vínculo:", e)

        finally:
            db.desconectdb()


class HospEnf:
    def __init__(self, cnpj, coren):
        self.cnpj = cnpj
        self.coren = coren

    def vinc_hospital_medicos(self):
        query = "INSERT INTO hosp_enfer (cnpj, coren) VALUES (?, ?)"
        parametros = (
            self.cnpj,
            self.coren,
        )
        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nVínculo inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir vínculo:", e)

        finally:
            db.desconectdb()


class MedPac:
    def __init__(self, crm, cpf):
        self.crm = crm
        self.cpf = cpf

    def vinc_medicos_paciente(self):
        query = "INSERT INTO med_pac (crm, cpf) VALUES (?, ?)"
        parametros = (
            self.crm,
            self.cpf,
        )
        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nVínculo inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir vínculo:", e)

        finally:
            db.desconectdb()


class MedEnf:
    def __init__(self, crm, coren):
        self.crm = crm
        self.coren = coren

    def vinc_medicos_enfermeiros(self):
        query = "INSERT INTO med_enf (crm, coren) VALUES (?, ?)"
        parametros = (
            self.crm,
            self.coren,
        )
        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nVínculo inserido com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("Erro ao inserir vínculo:", e)

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

            print(f"\033[1;36m\nEnfermeira(o) {self.nome}, inserido com sucesso!\033[m")

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

    def listar_enfermeiros(self):
        query = "SELECT coren , nome FROM enfermeira ORDER BY nome"

        try:
            db.conectadb()
            db.cursor.execute(query)

            for hospital in db.cursor.fetchall():
                coren, nome = hospital
                print(f"""COREN: {coren} / Nome: {nome}""")

        except Exception as e:
            print("Erro ao buscar enfermeiros:", e)

        finally:
            db.desconectdb()


class Paciente:
    def __init__(self, cpf, rg, nome, rua, bairro, cidade, cep):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def inserir_paciente(self):
        query = "INSERT INTO paciente (cpf, rg, nome, rua, bairro, cidade, cep) VALUES (?, ?, ?, ?, ?, ?, ?)"
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

    def listar_pacientes(self):
        query = "SELECT cpf , nome FROM paciente ORDER BY nome"

        try:
            db.conectadb()
            db.cursor.execute(query)

            for paciente in db.cursor.fetchall():
                cpf, nome = paciente
                print(f"""CPF: {cpf} / Nome: {nome}""")

        except Exception as e:
            print("Erro ao buscar paciente:", e)

        finally:
            db.desconectdb()


class Especialidade:
    def __init__(self, documento, especi):
        self.documento = documento
        self.especi = especi

    def inserir_especialidade(self):
        query = "INSERT INTO especialidade (documento, especi_desc) VALUES (?, ?)"
        parametros = (
            self.documento,
            self.especi,
        )

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(
                f"\033[1;36m\nEspecialidade {self.especi}, inserido com sucesso!\033[m"
            )

            db.conn.commit()

        except Exception as e:
            print("Erro ao inserir especialidade:", e)

        finally:
            db.desconectdb()

    def deletar_especialidade(self):
        query = "DELETE FROM especialidade WHERE cod = (?)"
        parametros = (self.cod,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)
            print(
                f"\033[1;36m\nDados da especialidade, foram excluídos com sucesso!\033[m"
            )
            db.conn.commit()
        except Exception as e:
            print("Erro ao deletar especialidade:", str(e))

    def buscar_especialidade(self):
        query = "SELECT cod, especi_desc FROM especialidade WHERE cod = (?)"
        parametros = (self.cod,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                cod_sl = row[0]
                nome_sl = row[1]
            print(f"\nCódigo: {cod_sl}")
            print(f"Especialidade: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar especialidade:", e)

        finally:
            db.desconectdb()

    def alterar_especialidade(self):
        query = "UPDATE especialidade SET cod = ?, documento = ?, especi_desc = ? WHERE cod = (?)"
        parametros = (
            self.cod,
            self.documento,
            self.especi,
        )

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(
                f"\033[1;36m\nEspecialidade {self.especi}, alterado com sucesso!\033[m"
            )

            db.conn.commit()
        except Exception as e:
            print("\033[1;31m\nErro ao alterar especialidade:\033[m", e)

        finally:
            db.desconectdb()


class Telefone:
    def __init__(self, documento, tele):
        self.documento = documento
        self.tele = tele

    def inserir_telefone(self):
        query = "INSERT INTO telefone (documento, tel) VALUES ( ?, ?)"
        parametros = (
            self.documento,
            self.tele,
        )

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nTelefone inserido com sucesso!\033[m")

            db.conn.commit()

        except Exception as e:
            print("Erro ao inserir telefone:", e)

        finally:
            db.desconectdb()

    def deletar_telefone(self):
        query = "DELETE FROM telefone WHERE cod = (?)"
        parametros = (self.cod,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)
            print(f"\033[1;36m\nDados do telefone, foram excluídos com sucesso!\033[m")
            db.conn.commit()
        except Exception as e:
            print("Erro ao deletar telefone:", str(e))

    def buscar_telefone(self):
        query = "SELECT cod, telFROM telefone WHERE cod = (?)"
        parametros = (self.cod,)

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            for row in db.cursor.fetchall():
                cod_sl = row[0]
                nome_sl = row[1]
            print(f"\nCódigo: {cod_sl}")
            print(f"Telefone: {nome_sl}")

        except Exception as e:
            print("Erro ao buscar telefone:", e)

        finally:
            db.desconectdb()

    def alterar_telefone(self):
        query = (
            "UPDATE especialidade SET cod = ?, documento = ?, tel = ? WHERE cod = (?)"
        )
        parametros = (
            self.cod,
            self.documento,
            self.tele,
        )

        try:
            db.conectadb()
            db.cursor.execute(query, parametros)

            print(f"\033[1;36m\nTelefone {self.tele}, alterado com sucesso!\033[m")

            db.conn.commit()
        except Exception as e:
            print("\033[1;31m\nErro ao alterar telefone:\033[m", e)

        finally:
            db.desconectdb()
