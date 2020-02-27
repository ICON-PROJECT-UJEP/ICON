from sigpipes.sigcontainer import SigContainer
from sigpipes.plotting import Plot
import matplotlib.pyplot as plt

sig = SigContainer.from_csv("pnp.csv", dir="", header=False, fs=250)
plt.show(sig | Plot())
