import sqlite3 as sq
from sqlite3 import Error

class bd:
    def insere_dados( diretorio,n_tabela,campos, dados, args ):
        '''
        diretorio = Caminho do banco de dados \n
        n_tabela  = Nome da tabela onde os dados vão ser inseridos \n
        campos    = Quais campos receberão as informações \n
        dados     = Os dados a serem inseridos na tabela \n
        args      = Quantos caracteres coringas serão usados
        '''

        #Mensagem de verificação de estado de conexão
        ec = True
        #Mensagem de verificação de execução
        exec = True

        #Tratamento de erro da conexão
        try:
            conn   = sq.connect( diretorio )
            cursor = conn.cursor()
        except Error as e:
            ec = e
        finally:
            if conn:
                #Tratamento de erro da execução
                try:
                    cursor.execute( 
                        f"INSERT INTO {n_tabela}({campos}) VALUES ({args})", dados                        
                    )
                except Error as e:
                    exec = e  
                finally:
                    conn.commit()
                    conn.close()

        return ec, exec            

    def busca_dados( diretorio,n_tabela,retorno, campo =  None, args = None ):
        '''
        diretorio = Caminho do banco |
        n_tabela  = Nome tabela para retornar os dados |
        retorno   = Campos a serem retornados |
        campo     = Lista de campos a serem comparados |
        args      = Lista de valores a serem comparados com os campos |
        '''
        #Mensagem de verificação de estado de conexão
        ec = False
        #Mensagem de verificação de execução
        exec = False
        #Variável para receber retorno do SELECT
        dados = None

        #Tratamento de erro da conexão
        try:
            conn   = sq.connect( diretorio )
            cursor = conn.cursor()
        except Error as e:
            ec = e
        finally:
            if conn:
                #Tratamento de erro da execução
                try:
                    if args == None:
                        cursor.execute( 
                            f"SELECT {retorno} FROM {n_tabela}"
                        ) 
                        dados = cursor.fetchall()

                    elif len(args) > 1:
                        cursor.execute( 
                            f"SELECT {retorno} FROM {n_tabela} WHERE {campo[0]} = '{args[0]}' AND {campo[1]} = '{args[1]}' "
                        )           
                        dados = cursor.fetchone()

                    else:    
                        cursor.execute( 
                            f"SELECT {retorno} FROM {n_tabela} WHERE {campo} LIKE '{args[0]}%'"
                        )
                        dados = cursor.fetchall()

                except Error as e:
                    exec = e  
                finally:
                    conn.close()  

        return ec, exec, dados