#IMPORT SQLITE3 MODULES
import sqlite3
from sqlite3 import Error
from time import sleep


class CrudDatabase:
    
    def __init__(self):
        self.DATABASE_PATH = ""
        self.conn = None
        self.c = None
    
    #CRIANDO CONEXÃO COM O BANCO DE DADOS
    def criando_conexao(self):   
        self.DATABASE_PATH = "database" + '\\' + 'Cozinha_PDG.db'
        
        try:
            self.conn = sqlite3.connect(self.DATABASE_PATH)
            self.conn.execute("PRAGMA foreing_key = ON")
            return self.conn
        
        except Error as e:
            print(e)
            
        self.conn.close() #ENCERRANDO CONEXÃO
    
    #******************CRUD**********************    
    
    #CRIAR TABELAS
    def create(self): #                            C
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.c = self.conn.cursor()
        
        #CRIANDO TABELA "ESTADO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS ESTADO (
		    Uf CHAR(2) NOT NULL PRIMARY KEY,
            Nome_estado VARCHAR(50) NOT NULL);
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela ESTADO ") 
        
        #CRIANDO TABELA "MUNICIPIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS MUNICIPIO (
            Id_Municipio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Codigo INTEGER NOT NULL,
            Nome_municipio VARCHAR(255) NOT NULL,
		    Uf CHAR(2) NOT NULL,
            FOREIGN KEY (Uf) REFERENCES ESTADO(Uf));
            
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela MUNICIPIO ") 
        
        #CRIANDO TABELA "TIPO_USUARIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS TIPO_USUARIO (
            SIGLA_USUARIO CHAR(3) NOT NULL PRIMARY KEY,
            DESCRICAO_USUARIO VARCHAR(15) NOT NULL);
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela TIPO_USUARIO ")

            #CRIANDO TABELA "CONTATO_USUARIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS CONTATO_USUARIO (
            ID_CONTATO_USUARIO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            TELEFONE INT(11));
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela CONTATO_USUARIO ")
           
        #CRIANDO TABELA "ENDERECO_USUARIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS ENDERECO_USUARIO (
		    ID_ENDERECO_USUARIO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ESTADO_USUARIO VARCHAR(50),
            CIDADE_USUARIO VARCHAR(255),
            RUA_USUARIO VARCHAR(255),
            BAIRRO_USUARIO VARCHAR(255));
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela ENDERECO_USUARIO ")   
           
        #CRIANDO TABELA "ACESSO_USUARIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS ACESSO_USUARIO (
		    ID_ACESSO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            EMAIL_USUARIO VARCHAR(255),
            SENHA_USUARIO VARCHAR(15) NOT NULL);
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela ACESSO_USUARIO ")
           
        #CRIANDO TABELA "PERMISSAO_USUARIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS PERMISSAO_USUARIO (
		    ID_PERMISSAO_USUARIO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ACESSAR CHAR(2) NOT NULL,
            CRIAR CHAR(2) NOT NULL,
            LER CHAR(2) NOT NULL,
            ATUALIZAR CHAR(2) NOT NULL,
            DELETAR CHAR(2) NOT NULL);
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela PERMISSAO_USUARIO ")
           
            #CRIANDO TABELA "USUARIO"
        try: 
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS USUARIO (
            ID_USUARIO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            NOME_USUARIO VARCHAR(20) NOT NULL,
            SOBRENOME_USUARIO VARCHAR(255) NOT NULL,
            IMAGEM_USUARIO VARCAHR(255) NOT NULL, 
            SIGLA_USUARIO CHAR(3) NOT NULL,
            ID_CONTATO_USUARIO INTEGER,
            ID_ENDERECO_USUARIO INTEGER,
            ID_ACESSO INTEGER NOT NULL,
            ID_PERMISSAO_USUARIO INTEGER,
            FOREIGN KEY (SIGLA_USUARIO) REFERENCES TIPO_USUARIO(SIGLA_USUARIO)
            FOREIGN KEY (ID_CONTATO_USUARIO) REFERENCES CONTATO_USUARIO(ID_CONTATO_USUARIO)
            FOREIGN KEY (ID_ENDERECO_USUARIO) REFERENCES ENDERECO_USUARIO(ID_ENDERECO_USUARIO)
            FOREIGN KEY (ID_ACESSO) REFERENCES ACESSO_USUARIO(ID_ACESSO)
            FOREIGN KEY (ID_PERMISSAO_USUARIO) REFERENCES PERMISSAO_USUARIO(ID_PERMISSAO_USUARIO));
            """)
        except Error as e:
            print(f"ERRO {e} na Tabela USUARIO ")
    
        
        self.conn.close() #ENCERRANDO CONEXÃO
        

    #VERIFICAR SE O DADO PASSADO ESTÁ PRESENTE NA TABELA PASSADA
    def verificar_insercao(self, coluna, w_coluna, tabela, dado):
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.c = self.conn.cursor()
        
        self.conn.cursor()
        self.c.execute(f"SELECT {coluna} FROM {tabela} WHERE {w_coluna} = {dado};")
        resultado = self.c.fetchall()
        return resultado
    
    #PROCUARAR INSERÇÕES DE ACORDO COM OS DADOS PASSADOS 
    def procurar(self, select, coluna, tabela, dado):
        self.conn = sqlite3.connect("database" + '\\' + 'Cozinha_PDG.db')
        self.c = self.conn.cursor()
        self.conn.cursor()
        
        if (tabela == 'ESTADO'):
            self.c.execute(f"SELECT {select} FROM ESTADO;")
            resultado = self.c.fetchall()
            return resultado
        
        elif (tabela == 'MUNICIPIO'):
            self.c.execute(f"SELECT {select} FROM MUNICIPIO WHERE {coluna} LIKE {dado};")
            resultado = self.c.fetchall()
            return resultado
        
        elif (tabela == 'TIPO_USUARIO'):
            self.c.execute(f"SELECT {select} FROM TIPO_USUARIO WHERE {coluna} = {dado};")
            resultado = self.c.fetchall()
            return resultado

        elif tabela == 'USUARIO':
            self.c.execute(f"SELECT NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO FROM USUARIO WHERE {coluna} = {dado};")
            resultado = self.c.fetchall()
            return resultado

        elif tabela == 'USUARIO-ID':
            self.c.execute(f"SELECT U.ID_USUARIO, U.NOME_USUARIO, U.SOBRENOME_USUARIO, A.EMAIL_USUARIO, C.TELEFONE, E.ESTADO_USUARIO, E.CIDADE_USUARIO, E.RUA_USUARIO, E.BAIRRO_USUARIO, T.DESCRICAO_USUARIO, P.ACESSAR, P.CRIAR, P.LER, P.ATUALIZAR, P.DELETAR FROM USUARIO U INNER JOIN ACESSO_USUARIO A ON U.ID_ACESSO =  A.ID_ACESSO INNER JOIN CONTATO_USUARIO C ON U.ID_CONTATO_USUARIO =  C.ID_CONTATO_USUARIO INNER JOIN ENDERECO_USUARIO E ON U.ID_ENDERECO_USUARIO =  E.ID_ENDERECO_USUARIO INNER JOIN TIPO_USUARIO T ON U.SIGLA_USUARIO =  T.SIGLA_USUARIO INNER JOIN PERMISSAO_USUARIO P ON U.ID_PERMISSAO_USUARIO =  P.ID_PERMISSAO_USUARIO WHERE ID_USUARIO = {dado};")
            resultado = self.c.fetchall()
            return resultado

        elif tabela == 'USUARIO-ALL':
            self.c.execute(f"SELECT U.ID_USUARIO, U.NOME_USUARIO, U.SOBRENOME_USUARIO, U.IMAGEM_USUARIO, A.EMAIL_USUARIO, C.TELEFONE, E.ESTADO_USUARIO, E.CIDADE_USUARIO, E.RUA_USUARIO, E.BAIRRO_USUARIO, T.DESCRICAO_USUARIO, P.ACESSAR, P.CRIAR, P.LER, P.ATUALIZAR, P.DELETAR FROM USUARIO U INNER JOIN ACESSO_USUARIO A ON U.ID_ACESSO =  A.ID_ACESSO INNER JOIN CONTATO_USUARIO C ON U.ID_CONTATO_USUARIO =  C.ID_CONTATO_USUARIO INNER JOIN ENDERECO_USUARIO E ON U.ID_ENDERECO_USUARIO =  E.ID_ENDERECO_USUARIO INNER JOIN TIPO_USUARIO T ON U.SIGLA_USUARIO =  T.SIGLA_USUARIO INNER JOIN PERMISSAO_USUARIO P ON U.ID_PERMISSAO_USUARIO =  P.ID_PERMISSAO_USUARIO WHERE U.NOME_USUARIO LIKE '%{dado}%' ORDER BY U.NOME_USUARIO ASC;")
            resultado = self.c.fetchall()
            return resultado
    
        self.conn.close() #ENCERRANDO CONEXÃO    
    
    #INSERIR DADOS NAS TABELAS    
    def inserir(self, tabela, ID, dados):
        self.DATABASE_PATH = "database" + '\\' + 'Cozinha_PDG.db'
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.c = self.conn.cursor()
        self.conn.cursor()
        
        if tabela == 'CONTATO_USUARIO':
            try:    
                self.c.execute(f"INSERT INTO CONTATO_USUARIO (TELEFONE) VALUES ('{dados[4][0]}');")
                self.c.execute(F"SELECT MAX(ID_CONTATO_USUARIO) FROM CONTATO_USUARIO;") 
                resultado = self.c.fetchall()  
                self.conn.commit()      
                return resultado
            except Error as e:
                print(f"ERRO {e} na hora de inserir na tabela CONTATO_USUARIO")

        elif tabela == 'ENDERECO_USUARIO':
            try:    
                self.c.execute(f"INSERT INTO ENDERECO_USUARIO (ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES ('{dados[5][0]}', '{dados[6][0]}', '{dados[8][0]}', '{dados[7][0]}');")
                self.c.execute("SELECT MAX(ID_ENDERECO_USUARIO) FROM ENDERECO_USUARIO;")   
                resultado = self.c.fetchall()  
                self.conn.commit()   
                return resultado   
            except Error as e:
                print(f"ERRO {e} na hora de inserir na tabela ENDERECO_USUARIO")

        elif tabela == "ACESSO_USUARIO":
            try:    
                self.c.execute(f"INSERT INTO ACESSO_USUARIO (EMAIL_USUARIO, SENHA_USUARIO) VALUES ('{dados[3][0]}', '123');")
                self.c.execute("SELECT MAX(ID_ACESSO) FROM ACESSO_USUARIO;")   
                resultado = self.c.fetchall()  
                self.conn.commit()
                return resultado      
            except Error as e:
                print(f"ERRO {e} na hora de inserir na tabela ACESSO_USUARIO")

        elif tabela == "PERMISSAO_USUARIO":
            try:    
                self.c.execute(f"INSERT INTO PERMISSAO_USUARIO (ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES ('OK', 'OK', 'OK', 'OK', 'OK');")
                self.c.execute("SELECT MAX(ID_PERMISSAO_USUARIO) FROM PERMISSAO_USUARIO;")   
                resultado = self.c.fetchall()  
                self.conn.commit()
                return resultado      
            except Error as e:
                print(f"ERRO {e} na hora de inserir na tabela PERMISSAO_USUARIO")


        elif (tabela == 'USUARIO'):
            try:    
                self.c.execute(f"INSERT INTO USUARIO (NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES ('{dados[0]}', '{dados[1]}', '{dados[2]}', '{dados[3]}', '{dados[4]}', '{dados[5]}', '{dados[6]}', '{dados[7]}');")
                self.c.execute("SELECT ID_USUARIO FROM USUARIO;")   
                self.conn.commit()      
            except Error as e:
                print(f"ERRO {e} na hora de inserir na tabela USUARIO")
                        
        self.conn.close() #ENCERRANDO CONEXÃO
   
    def data(self):
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.c = self.conn.cursor()
        self.conn.cursor()
        try:
            self.c.execute("SELECT GETDATE ( );") 
            resultado = self.c.fetchall()
            self.conn.commit()   
        except Error as e:
                print(f"ERRO {e} na hora de obter a data")
               
        self.conn.close() #ENCERRANDO CONEXÃO        
        return resultado

 #CRIANDO AS INSERÇÕES INICIAIS DO BANCO DE DADOS
    def insercoes_iniciais(self):
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.c = self.conn.cursor()
        
        #INSERINDO EM "Estado"
        try: 
            self.c.executescript("""
            Insert into Estado (Uf, Nome_estado) values ('AC', 'Acre');
            Insert into Estado (Uf, Nome_estado) values ('AL', 'Alagoas');
            Insert into Estado (Uf, Nome_estado) values ('AP', 'Amapá');
            Insert into Estado (Uf, Nome_estado) values ('AM', 'Amazonas');
            Insert into Estado (Uf, Nome_estado) values ('BA', 'Bahia');
            Insert into Estado (Uf, Nome_estado) values ('CE', 'Ceará');
            Insert into Estado (Uf, Nome_estado) values ('DF', 'Distrito Federal');
            Insert into Estado (Uf, Nome_estado) values ('ES', 'Espírito Santo');
            Insert into Estado (Uf, Nome_estado) values ('GO', 'Goiás');
            Insert into Estado (Uf, Nome_estado) values ('MA', 'Maranhão');
            Insert into Estado (Uf, Nome_estado) values ('MT', 'Mato Grosso');
            Insert into Estado (Uf, Nome_estado) values ('MS', 'Mato Grosso do Sul');
            Insert into Estado (Uf, Nome_estado) values ('MG', 'Minas Gerais');
            Insert into Estado (Uf, Nome_estado) values ('PA', 'Pará');
            Insert into Estado (Uf, Nome_estado) values ('PB', 'Paraíba');
            Insert into Estado (Uf, Nome_estado) values ('PR', 'Paraná');
            Insert into Estado (Uf, Nome_estado) values ('PE', 'Pernambuco');
            Insert into Estado (Uf, Nome_estado) values ('PI', 'Piauí');
            Insert into Estado (Uf, Nome_estado) values ('RJ', 'Rio de Janeiro');
            Insert into Estado (Uf, Nome_estado) values ('RN', 'Rio Grande do Norte');
            Insert into Estado (Uf, Nome_estado) values ('RS', 'Rio Grande do Sul');
            Insert into Estado (Uf, Nome_estado) values ('RO', 'Rondônia');
            Insert into Estado (Uf, Nome_estado) values ('RR', 'Roraima');
            Insert into Estado (Uf, Nome_estado) values ('SC', 'Santa Catarina');
            Insert into Estado (Uf, Nome_estado) values ('SP', 'São Paulo');
            Insert into Estado (Uf, Nome_estado) values ('SE', 'Sergipe');
            Insert into Estado (Uf, Nome_estado) values ('TO', 'Tocantins');
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela ESTADO")

        #INSERINDO EM "Municipio"    
        try: 
            self.c.executescript("""
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1101500','Seringueiras', 'RO');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1101559','Teixeirópolis', 'RO');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1101609','Theobroma', 'RO');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1101708','Urupá', 'RO');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1101757','Vale do Anari', 'RO');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1101807','Vale do Paraíso', 'RO');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200013','Acrelândia', 'AC');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200054','Assis Brasil', 'AC');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200104','Brasiléia', 'AC');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200138','Bujari', 'AC');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200179','Capixaba', 'AC');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200203','Cruzeiro do Sul', 'AC');
            Insert into Municipio (Codigo, Nome_municipio, Uf) values ('1200252','Epitaciolândia', 'AC');
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela MUNICIPIO")
            
        #INSERINDO EM "TIPO_USUARIO"     
        try: 
            self.c.executescript("""
            INSERT INTO TIPO_USUARIO (SIGLA_USUARIO,  DESCRICAO_USUARIO) VALUES ('ADM', 'Administrador');
            INSERT INTO TIPO_USUARIO (SIGLA_USUARIO,  DESCRICAO_USUARIO) VALUES ('COZ', 'Cozinheiro');
            INSERT INTO TIPO_USUARIO (SIGLA_USUARIO,  DESCRICAO_USUARIO) VALUES ('EST', 'Estoquista');
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela TIPO_USUARIO")

        #INSERINDO EM "CONTATO_USUARIO"    
        try: 
            self.c.executescript("""
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (1, 11111111111);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (2, 11222222222);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (3, 11333333333);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (4, 11444444444);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (5, 11555555555);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (6, 11666666666);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (7, 11777777777);
            INSERT INTO CONTATO_USUARIO (ID_CONTATO_USUARIO, TELEFONE) VALUES (8, 11888888888);
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela CONTATO_USUARIO")

        #INSERINDO EM "ENDERECO_USUARIO"    
        try: 
            self.c.executescript("""
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (1, 'Rondônia', 'Seringueiras', 'Rua José Lopes', 'Bairro Jardim Beira Mar');
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (2, 'Rondônia', 'Teixeirópolis', 'Rua Germano Vítor dos Santos ', 'Bairro Sé Bela Vista');   
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (3, 'Rondônia', 'Theobroma', 'Rua Glucínio', 'Bairro Bom Retiro');   
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (4, 'Rondônia', 'Urupá', 'Praça Antônio Pereira Martins', 'Bairro Cambuci');   
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (5, 'Acre', 'Acrelândia', 'Rua Nelson Ferreira', 'Bairro Consolação');
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (6, 'Acre', 'Assis Brasil', 'Rua Clodomiro Pinheiro', 'Bairro Liberdade');   
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (7, 'Acre', 'Brasiléia', 'Rua Emí­lio Retrosi', 'Bairro Santa Cecília');   
            INSERT INTO ENDERECO_USUARIO (ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO) VALUES (8, 'Acre', 'Bujari', 'Rua Comendador Assad Abdalla', 'Bairro Sé');                
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela ENDERECO_USUARIO")

        #INSERINDO EM "ACESSO_USUARIO"    
        try: 
            self.c.executescript("""
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (1, 'luis@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (2, 'fred@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (3, 'fernando@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (4, 'luciano@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (5, 'amadeus@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (6, 'taina@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (7, 'mateus@gmail.com', '123');
            INSERT INTO ACESSO_USUARIO (ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO) VALUES (8, 'bruna@gmail.com', '123');
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela ACESSO_USUARIO")

        #INSERINDO EM "PERMISSAO_USUARIO"    
        try: 
            self.c.executescript("""
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (1, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (2, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (3, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (4, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (5, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (6, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (7, 'OK', 'OK', 'OK', 'OK', 'OK');
            INSERT INTO PERMISSAO_USUARIO (ID_PERMISSAO_USUARIO, ACESSAR, CRIAR, LER, ATUALIZAR, DELETAR) VALUES (8, 'OK', 'OK', 'OK', 'OK', 'OK');
            """)
            self.conn.commit()
            
        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela PERMISSAO_USUARIO")

        #INSERINDO EM "USUARIO"
        try:
            self.c.executescript("""
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (1, 'Luis', 'Guilherme', 'gui/images/users/default_user.png', 'ADM', 1, 1, 1, 1);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (2, 'Frederico', 'Rufino', 'gui/images/users/default_user.png', 'EST', 2, 2, 2, 2);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (3, 'Fernando', 'Papini', 'gui/images/users/default_user.png', 'COZ', 3, 3, 3, 3);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (4, 'Luciano', 'Filadelfo', 'gui/images/users/default_user.png', 'ADM', 4, 4, 4, 4);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (5, 'Amadeus', 'Pantoja', 'gui/images/users/default_user.png', 'ADM', 5, 5, 5, 5);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (6, 'Tainá', 'Valentim', 'gui/images/users/default_user.png', 'COZ', 6, 6, 6, 6);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (7, 'Mateus', 'Borges', 'gui/images/users/default_user.png', 'EST', 7, 7, 7, 7);
            INSERT INTO USUARIO (ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO, ID_CONTATO_USUARIO, ID_ENDERECO_USUARIO, ID_ACESSO, ID_PERMISSAO_USUARIO) VALUES (8, 'Bruna', 'Leme', 'gui/images/users/default_user.png', 'EST', 8, 8, 8, 8);
            """)
            self.conn.commit()

        except Error as e:
            print(f"ERRO {e} na hora de inserir na tabela USUARIO")
        
        self.conn.close() #ENCERRANDO CONEXÃO 

    def vizualizar(self):
        self.conn = sqlite3.connect(self.DATABASE_PATH)
        self.c = self.conn.cursor()
        
        '''#MUNICIPIO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT Nome_municipio, Uf FROM MUNICIPIO;")
            resultado = self.c.fetchall()
            print("{:<10} {:<0}".format("Nome", "UF"))
            for item in range(len(resultado)):
                print("{:<10} {:<0}".format(resultado[item][0], resultado[item][1]))
            
            self.conn.commit()   
            
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela MUNICIPIO")
        '''
           
        '''#ESTADO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT Uf, Nome_estado FROM ESTADO;")
            resultado = self.c.fetchall()
            print("{:<10} {:<0}".format("UF", "Nome"))
            for item in range(len(resultado)):
                print("{:<10} {:<0}".format(resultado[item][0], resultado[item][1]))
            
            self.conn.commit()   
            
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela ESTADO")'''
                      
        '''#TIPO_USUARIO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT SIGLA_USUARIO, DESCRICAO_USUARIO FROM TIPO_USUARIO;")
            resultado = self.c.fetchall()
            print("{:<10} {:<0}".format("Sigla", "Descrição"))
            for item in range(len(resultado)):
                print("{:<10} {:<0}".format(resultado[item][0], resultado[item][1]))
            
            self.conn.commit()   
            
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela TIPO_USUARIO")'''
        
        '''#CONTATO_USUARIO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT ID_CONTATO_USUARIO, TELEFONE FROM CONTATO_USUARIO;")
            resultado = self.c.fetchall()
            print("{:<10} {:<0}".format("ID", "TELEFONE"))
            for item in range(len(resultado)):
                print("{:<10} {:<0}".format(resultado[item][0],  resultado[item][1]))
            
            self.conn.commit()   
            
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela CONTATO_USUARIO")'''
         
        '''#ENDERECO_USUARIO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT ID_ENDERECO_USUARIO, ESTADO_USUARIO, CIDADE_USUARIO, RUA_USUARIO, BAIRRO_USUARIO FROM ENDERECO_USUARIO;")
            resultado = self.c.fetchall()
            print("{:<5} {:<5} {:<5} {:<5} {:<0}".format("ID", "EST", "MUN", "RUA", "BAI"))
            for item in range(len(resultado)):
                print("{:<5} {:<5} {:<5} {:<5} {:<0}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4]))
            self.conn.commit()   
    
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela ENDERECO_USUARIO")
         '''

        '''#ACESSO_USUARIO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT ID_ACESSO, EMAIL_USUARIO, SENHA_USUARIO FROM ACESSO_USUARIO;")
            resultado = self.c.fetchall()
            print("{:<10} {:<10} {:<0}".format("ID", "EMAIL", "SENHA"))
            for item in range(len(resultado)):
                print("{:<10} {:<10} {:<0}".format(resultado[item][0],  resultado[item][1], resultado[item][2]))
            
            self.conn.commit()   
            
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela ACESSO_USUARIO")'''
         
        '''#USUARIO
        try:
            self.conn.cursor()
            self.c.execute(f"SELECT ID_USUARIO, NOME_USUARIO, SOBRENOME_USUARIO, IMAGEM_USUARIO, SIGLA_USUARIO FROM USUARIO;")
            resultado = self.c.fetchall()
            print("{:<10} {:<15} {:<15} {:<15} {:<0}".format("ID", "NOME", "SOBRENOME", "IMG", "SIGLA"))
            for item in range(len(resultado)):
                print("{:<10} {:<15} {:<15} {:<15} {:<0}".format(resultado[item][0],  resultado[item][1], resultado[item][2],  resultado[item][3],  resultado[item][4]))
            
            self.conn.commit()   
            
        except Error as e:
            print(f"ERRO {e} na hora de mostrar dados da tabela USUARIO")'''     
        #str = ''
        #teste = CrudDatabase.procurar(self,'*', 'NOME_USUARIO', 'USUARIO-ALL', str)
        #print(teste)

        self.conn.close()
        
    
        
        
  

