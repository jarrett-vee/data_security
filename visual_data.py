# counts number of values per state and plots. No real reason besides data visualization.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

state_counts = df["state"].value_counts()

state_counts.plot(kind="bar", figsize=(12, 6), color="c")
plt.xlabel("State")
plt.ylabel("Number of Emails")
plt.title("Number of Emails per State")
plt.grid(axis="y")

plt.tight_layout()
plt.show()
