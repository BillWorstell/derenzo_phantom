import numpy as np
import matplotlib.pyplot as plt

def plot_phantom():
    # Placeholder for the actual plotting logic
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1.0
    x1 = r * np.cos(theta)
    y1 = r * np.sin(theta)

    fig, ax = plt.subplots(1)
    ax.plot(x1, y1)
    ax.set_aspect(1)
    plt.grid(linestyle='--')
    plt.show()

if __name__ == "__main__":
    plot_phantom()
