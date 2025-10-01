# facet grid
import seaborn as sns
import matplotlib.pyplot as plt

# Penguins dataset
penguins = sns.load_dataset("penguins")

# FacetGrid
g = sns.FacetGrid(penguins, col="sex", row="species")
g.map(sns.scatterplot, "bill_length_mm", "bill_depth_mm")

plt.show()
