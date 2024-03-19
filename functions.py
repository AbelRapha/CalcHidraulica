import streamlit as st
#import matplotlib.pyplot as plt
import math as mt

class ExperienceFunctions:

    def Show_latex_exmpression(latex_expression) -> str:
        st.latex(latex_expression)
    
    def Nikuradse(D , J , e , v ) -> float:

        raiz = mt.sqrt(2*9.81*D*J)

        part1_log = e/(3.71*D)
        part2_log = 2.51*v/(D*raiz)
        log = mt.log(part1_log + part2_log)

        equation_solve = -2*raiz * log

        return equation_solve
    
    def Nikuradse_experience(e,D,f, Re) -> float:
        # Pass a range of values of functions
        pass

class ConvertMeasures:

    
    def milimeter_to_meter(value):
        return value*0.001
    
    def centimeter_to_meter(value):
        return value*0.01
    
    def kilometer_to_meter(self,value):
        return value*1000


        