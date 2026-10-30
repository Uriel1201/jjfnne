import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 3: Central Limit Theorem
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    rng = np.random.default_rng(42)
    return mo, norm, np, plt, rng


@app.cell
def _(np, rng):
    def exponential(size):
        return rng.exponential(size=size) - 1

    def uniform(size):
        return rng.uniform(-np.sqrt(3), np.sqrt(3), size=size)

    return exponential, uniform


@app.cell
def _(exponential, n, norm, np, plt, uniform):
    N = 100_000
    nn = n.value

    y_exp = exponential((N, nn)).sum(axis=1) / np.sqrt(nn)
    y_uni = uniform((N, nn)).sum(axis=1) / np.sqrt(nn)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    z = np.linspace(-5, 5, 500)

    ax[0].hist(y_exp, bins=100, density=True, alpha=0.6)
    ax[0].plot(z, norm.pdf(z), "k-", lw=2)
    ax[0].set_title("Shifted exponential")

    ax[1].hist(y_uni, bins=100, density=True, alpha=0.6)
    ax[1].plot(z, norm.pdf(z), "k-", lw=2)
    ax[1].set_title("Uniform")

    for a in ax:
        a.set_xlim(-5, 5)
        a.set_ylim(0, 0.5)
        a.set_xlabel(r"$y = \frac{1}{\sqrt{n}}\sum_i x_i$")
        a.set_ylabel("density")

    fig.suptitle(f"n = {nn}")
    plt.tight_layout()

    fig
    return


@app.cell(hide_code=True)
def _(mo):
    n = mo.ui.slider(
        start=1,
        stop=100,
        step=1,
        value=1,
        label="n",
        show_value=True
    )

    n
    return (n,)


if __name__ == "__main__":
    app.run()
