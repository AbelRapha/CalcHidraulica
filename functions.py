import streamlit as st
#import matplotlib.pyplot as plt
import math as mt

class ExperienceFunctions:

    def Show_latex_exmpression(latex_expression) -> str:
        st.latex(latex_expression)
    
    def Nikuradse(D , J , e , v ) -> float:

        equation_solve = -2*mt.sqrt(2*9.81*D*J) * mt.log((e/3.71*D)+(2.51*v)/(D*mt.sqrt(2*9.81*D*J)))

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


        