import streamlit as st
import pandas as pd
from BD.CRUD import bd

class cadastros:

    # Página de cadastro de cargos
    def cadastrar_cargo():
        ### Definição do diretório
        diretorio = './BD/note_control.db'
        op = st.radio('Selecione', ['Consultar', 'Cadastrar', 'Excluir', 'Atualizar'], horizontal = True)

        ### Consulta de cargos
        if op == 'Consultar':
            st.header("Consulta de Cargos")
            consulta_cargo = st.text_input("Cargo a ser consultado:")

            if consulta_cargo == '':
                dados = bd.busca_dados(diretorio, 'Cargos', '*')
                dados_tratados = pd.DataFrame( dados[2], columns = ['Id', 'Descrição', 'Nível Acesso'] )
                st.dataframe( dados_tratados, hide_index=  True )
            else:
                dados = bd.busca_dados( diretorio, 'Cargos', '*', 'descricao', [consulta_cargo] )
                dados = pd.DataFrame( dados[2], columns = ['Id', 'Descrição', 'Nível Acesso'] )
                st.dataframe( dados, hide_index=  True )


        ### Cadastro de Cargos
        elif op == 'Cadastrar':
            st.header("Cadastro de Cargos")
            novo_cargo = st.text_input("Novo Cargo:")
            n_aceso    = st.selectbox( 'Nível de acesso', (1,2,3,4,5) )
            if st.button("Adicionar Cargo"):
                #SELECT pra buscar todas as informações contidas na tabela Cargos
                ### 'SELECT descricao, n_acesso FROM Cargos WHERE descricao = ? AND n_acesso = ?', (novo_cargo, n_acesso)
                erro_con, erro_exec, dados  = bd.busca_dados( 
                    diretorio,'Cargos','id',['descricao', 'n_aceso'],[novo_cargo, n_aceso]

                                             )

                ##Tratamento das mensagens de erro
                #Erro de Conexão
                if erro_con != False:
                    st.error( f'Erro na conexão (Busca). {erro_con}', icon = '🚨' )
                elif erro_exec != False:
                    st.error( f'Erro execução (Busca). {erro_exec}', icon = '🚨' )
                else:
                    if dados == None:
                        erro_con, erro_exec = bd.insere_dados(
                            './BD/note_control.db', 'Cargos', 'descricao, n_aceso',[novo_cargo, n_aceso], '?,?'
                        )
                        if erro_con != True:
                            st.error( f'Erro na conexão. {erro_con}', icon = '🚨' )
                        elif erro_exec != True:
                            st.error( f'Erro execução. {erro_exec}', icon = '🚨' )
                        else:
                            st.success( 'Dados inseridos com sucesso!!!', icon = '🤖')
                    else:
                        st.error( 'Dado já existente no Banco', icon = '🚨' )        



            ## Se Nome do cargo & Nível de acesso já estiverem cadastrados, temos que retornar uma mensagem de erro para o usuário

            #Aqui, vamos criar a Query e adicionar os valores no banco

            return None

    # Página de cadastro de funcionários
    def cadastrar_funcionario():
        st.header("Cadastro de Funcionários")
        nome = st.text_input("Nome:")
        cargo = st.selectbox("Cargo:",['Cargo1', 'Cargo2'])
        if st.button("Adicionar Funcionário"):
           #Aqui, vamos criar a Query e adicionar os valores no banco
            return None    