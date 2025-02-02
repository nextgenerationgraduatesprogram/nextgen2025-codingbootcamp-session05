import sys
import h5py
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

sys.path.append(str(Path(".").absolute()))

if __name__ == "__main__":
    # generate a sin wave
    f = 2.5 # Hz
    sps = 30.0
    T = 10
    t = np.linspace(0, T, int(sps*T))
    y = np.sin(2 * np.pi * f * t)

    # root
    root = Path("./data/files")
    root.mkdir(exist_ok=True, parents=True)

    # binary
    with open(root.joinpath("wave.bin"), "wb") as f:
        for idx in range(y.shape[0]):
            f.write(y[idx])

    # text
    with open(root.joinpath("wave.txt"), "w") as f:
        for idx in range(y.shape[0]):
            f.write(f"{y[idx]}\n")

    # h5py
    with h5py.File(root.joinpath("wave.HDF5"), "w") as f:
        f.create_dataset("y", data=y)

    # image
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(t,y)
    fig.savefig(root.joinpath("wave.png"))
    