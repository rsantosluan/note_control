import streamlit as st
import pandas    as pd
from cad_geral import cadastros as cad


# Menu de navegação entre as páginas
with st.sidebar: 
    op_cad = st.selectbox("Cadastros:",
                                    ["---","Cadastro de Cargos", "Cadastro de Funcionários", "Cadastrar Equipamentos"]
            )
    
    
# Paginação  
if op_cad == '---':  
    st.info( 'Aqui vai nosso Dashboard!!!' )
elif op_cad == "Cadastro de Cargos":
    cad.cadastrar_cargo()
elif op_cad == "Cadastro de Funcionários":
    cad.cadastrar_funcionario()
else:
    st.warning( 'Em construção', icon="⚠️" )
