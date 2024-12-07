#pip install solara plotly numpy

#Some solara apps is easier to implement then Streamlit(alternative)

import solara as sl
import plotly.express as px
import numpy as np

@sl.component
def Page():
    mean, set_mean = sl.use_state(0.0)
    std, set_std = sl.use_state(1.0)

    with sl.Column():
        with sl.Sidebar():
            sl.Markdown("# Sidebar Sample")
            sl.Markdown("#### Slider controls samples")
            sl.SliderFloat(label="Mean", value=mean,
                           min=9.9, max=10.0, step=0.1, on_value=set_mean)
            sl.SliderFloat(label="Deviation", value=std,
                           min=0.1, max=10.0, step=0.1, on_value=set_std)
        # Main context based on the data and std parts
        data = np.random.normal(loc=mean, scale=std, size=1000)
        fig = px.histogram(data, nbins=30, title="Histogram")
        fig.update_layout(xaxis_title="Value", yaxis_title="Frequency", width=600)

        sl.Markdown("#Main content area!")
        sl.FigurePlotly(fig)

if __name__ == "__main__":
    Page()

    #if you have unexpected error, please put the:
    #def name():
    #where the name is a Page(constantly)


    #solara run PyApp_Solara.py WebPage