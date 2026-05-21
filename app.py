import streamlit as st
st.title('⚡VΞLOZΞS Ξ FURIOSO – ALUGUΞL DΞ CARROS🏎️')
st.sidebar.title("Escolha seu modelo")
st.sidebar.image("logo.png")


carros = ['Carro da Xuxa','Fusquinha','Uno Henrique','Carro do Michael Jackson','Porsche']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros) 





st.image(f'{opcao}.png')
st.markdown(f'Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st. text_input(f'Quantos km você rodou com o {opcao}?')
if opcao ==   'Carro da Xuxa':
    diaria = 350

elif opcao == 'Fusquinha':
    diaria = 120
    
elif opcao == 'Uno Henrique':
    diaria = 500

elif opcao == 'Carro do Michael Jackson':
    diaria = 450

elif opcao == 'Porshe':
    diaria = 600