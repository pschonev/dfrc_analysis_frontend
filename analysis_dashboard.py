# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "polars==1.25.2",
# ]
# ///

import marimo

__generated_with = "0.11.20"
app = marimo.App(
    width="medium",
    app_title="Double Fischer Random Chess Analysis",
    layout_file="layouts/analysis_dashboard.grid.json",
)


@app.cell
def _():
    import marimo as mo
    import polars as pl

    FEN_TEMPLATE = "https://lichess.org/analysis/{black}/pppppppp/8/8/8/8/PPPPPPPP/{white}_w_KQkq_-_0_1?color=white"
    return FEN_TEMPLATE, mo, pl


@app.cell
def _(mo, pl):
    df = pl.read_parquet("analysis_data/data/analysis_results.parquet")
    table = mo.ui.table(df, selection="single")
    table
    return df, table


@app.cell
def _(FEN_TEMPLATE, table):
    fen_white = table.value["white"][0]
    fen_black = table.value["black"][0]
    dfrc_id = table.value["dfrc_id"][0]
    fen = FEN_TEMPLATE.format(black=fen_black, white=fen_white.upper())
    return dfrc_id, fen, fen_black, fen_white


@app.cell
def _(dfrc_id, fen, mo):
    mo.md(f"[lichess]({fen}) for position {dfrc_id}")
    return


@app.cell
def _(fen, mo):
    mo.Html(f'<iframe src="{fen}" style="width: 400px; aspect-ratio: 10/11;" allowtransparency="true" frameborder="0"></iframe>')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
