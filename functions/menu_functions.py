
import sys
import time
import os
import database.db_crud



class MenuFunctions():
    def __init__(self, acesso):
        self.acesso = acesso
    
        self.database = database.db_crud.CrudDatabase
     
    def search(self, table, data):
        if table == 'ESTADO':
            result = self.database.procurar(self, 'Nome_estado, Uf', 'Nome_estado', 'ESTADO', "")
            return result

        elif table == 'MUNICIPIO':
            result = self.database.procurar(self, 'Nome_municipio', 'Uf', 'MUNICIPIO', ('\''+data+'\''))
            return result
        
        elif table == 'USUARIO':
            result = self.database.procurar(self, 'NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO', 'ID_USUARIO', 'USUARIO', self.acesso[1])
            return result

        elif table == 'USUARIO-ALL':
            result = self.database.procurar(self, '*', 'NOME_USUARIO', 'USUARIO-ALL', data)
            return result
        
    def insert(self, table, data):
        if table == "USUARIO":
            id_contato = self.database.inserir(self, "CONTATO_USUARIO", id, data)
            id_endereco = self.database.inserir(self, "ENDERECO_USUARIO", id, data)
            id_acesso = self.database.inserir(self, "ACESSO_USUARIO", id, data)
            id_permissao = self.database.inserir(self, "PERMISSAO_USUARIO", id, "")
            imagem_url =  'gui/images/users/default_user.png'
            sigla = self.database.procurar(self,"SIGLA_USUARIO", "DESCRICAO_USUARIO", "TIPO_USUARIO", ('\''+data[9]+'\''))

            user = (data[0][0], data[1][0], imagem_url, sigla[0][0], id_contato[0][0], id_endereco[0][0], id_acesso[0][0], id_permissao[0][0])

            self.database.inserir(self, "USUARIO", self.acesso[1], user)
     



