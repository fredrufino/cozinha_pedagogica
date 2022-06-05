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