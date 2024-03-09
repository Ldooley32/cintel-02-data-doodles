import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # provides the Palmer Peguin dataset

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

penguins_df.describe()

ui.page_opts(title="Mrs. Doodles Penguins ", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(penguins_df, y="body_mass_g", color="sex",
                            title="Body Mass", 
                            color_discrete_map={"male":"skyblue", "female":"pink"} )
 
    @render_plotly
    def plot2():
        return px.histogram(penguins_df, y="bill_length_mm", color="sex",
                            title="Bill Length",
                            color_discrete_map={"male":"skyblue", "female":"pink"} )

   
