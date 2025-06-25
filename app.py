import numpy as np
import seaborn as sns
from palmerpenguins import load_penguins
import matplotlib.pyplot as plt
from shiny.express import ui, input, render

#Loading Penguins Dataset
penguins = load_penguins()

# Set page title
ui.page_opts(title="Interactive Histogram", fillable=True)

# Create a slider in the sidebar
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

# Create histogram output for random data

@render.plot(alt="Histogram using the selected number of bins")
def plot_histogram():
    # Generate random data
    data = np.random.randn(1000)
    plt.hist(data, bins=input.selected_number_of_bins(), density=True, color ="steelblue", edgecolor = "black")
    plt.title("Random Data Histogram")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.grid(True)

#Create Scatter plot for Penguins Dataset

@render.plot(alt="Scatterplot of Penguin Flipper Length vs Body Mass")
def penguin_scatter():
    sns.scatterplot(
        data=penguins,
        x="flipper_length_mm",
        y="body_mass_g",
        hue="sex",
        style="species"
    )
    plt.title("Penguin Flipper Length vs Body Mass")
    plt.xlabel("Flipper Length (mm)")
    plt.ylabel("Body Mass (g)")
    plt.grid(True)


