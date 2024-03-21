import streamlit as st
import math as mt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    
    def Nikuradse_experience():
        pass
        # fig = make_subplots(rows=2, cols=2,
        #                     specs=[[{"secondary_y": True}, {"secondary_y": True}],
        #                         [{"secondary_y": True}, {"secondary_y": True}]])

        # # Top left
        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis data"),
        #     row=1, col=1, secondary_y=False)

        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis2 data"),
        #     row=1, col=1, secondary_y=True,
        # )

        # # Top right
        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis3 data"),
        #     row=1, col=2, secondary_y=False,
        # )

        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis4 data"),
        #     row=1, col=2, secondary_y=True,
        # )

        # # Bottom left
        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis5 data"),
        #     row=2, col=1, secondary_y=False,
        # )

        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis6 data"),
        #     row=2, col=1, secondary_y=True,
        # )

        # # Bottom right
        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis7 data"),
        #     row=2, col=2, secondary_y=False,
        # )

        # fig.add_trace(
        #     go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis8 data"),
        #     row=2, col=2, secondary_y=True,
        # )

        # st.plotly(fig)

class ConvertMeasures:

    
    def milimeter_to_meter(value):
        return value*0.001
    
    def centimeter_to_meter(value):
        return value*0.01
    
    def kilometer_to_meter(self,value):
        return value*1000


        