import streamlit as st
from functions import ExperienceFunctions as ef
from functions import ConvertMeasures as cm
import math as mt

st.title('Calculadora De Hidráulica') 

options = st.selectbox('Selecione o tipo de operação que deseja', ['Selecione uma opção','Resolver a Equação Nikuradse', 'Criar o Grafico da Experiência de Nikuradse'])

match options:
    case 'Resolver a Equação Nikuradse':
        
        D, e, v, J, result = None, None, None, None, None

        ef.Show_latex_exmpression(r"V = -2\sqrt{2gDJ}.log((\varepsilon/3,71.D) + (2,51.\nu/D\sqrt{2gDJ}))")


        st.markdown('### Agora insira os valores das variáveis da equação')
        st.warning('Atenção!! Tenha certeza que todas as medidas estão no sistema internacional de unidades (SI)')
        
        col1, col2 = st.columns(2)

        option_negative = col1.checkbox('Tenho medidas a converter')
        option_positive = col2.checkbox('Minhas medidas já estão nas unidades corretas')
        

        if option_negative:
            type_measure = st.selectbox('Selecione para qual a unidade de medida deseja converter',
                                        ['Selecione uma opção',
                                         'Milímetros -> Metros',
                                         'Centímetros -> Metros',
                                         'Kilômetros -> Metros'])
            
            match type_measure:
                case 'Milímetros -> Metros':
                    D = st.number_input('Digite o valor do seu diâmetro')
                    e = st.number_input('Digite o valor da sua rugosidade')

                    # Converting measures
                    D = cm.milimeter_to_meter(value=D)
                    e = cm.milimeter_to_meter(value=e)

                case 'Centímetros -> Metros':
                    
                    D = st.number_input('Digite o valor do seu diâmetro')
                    e = st.number_input('Digite o valor da sua rugosidade')

                    # Converting measures
                    D = cm.centimeter_to_meter(value=D)
                    e = cm.centimeter_to_meter(value=e)
                case 'Kilômetros -> Metros':
                    D = st.number_input('Digite o valor do seu diâmetro')
                    e = st.number_input('Digite o valor da sua rugosidade')

                    # Converting measures
                    D = cm.kilometer_to_meter(value=D)
                    e = cm.kilometer_to_meter(value=e)  
                case 'Selecione uma opção':
                    pass 

        if option_positive:
            J = st.number_input('Digite o valor do seu J')
            D = st.number_input('Digite o valor do seu diâmetro')
            e = st.number_input('Digite o valor da sua rugosidade')
            v = st.number_input('Digite o valor da sua viscosidade cinemática')
        
        if D and e is not None:
            # For case when i converted measures
            if J is None:
                J = st.number_input('Digite o valor do seu J (Já está na base 10^-3)')
                J=float(J*10**-3)
            if v is None:
                v = st.number_input('Digite o valor da sua viscosidade cinemática (Já está na base 10^-6)')
                v = float(v*10**-6)
            if st.button('Calcular'):
                result = ef.Nikuradse(D=D,J=J,v=v,e=e)                
                result_show = st.success(f'{result} m/s')
                if result is not None:
                    if st.button('Limpar resultado'):
                        result_show.empty()
                
    case 'Selecione uma opção':
        pass

    case 'Criar o Grafico da Experiência de Nikuradse':
        st.info('Ainda em Desenvolvimento...')