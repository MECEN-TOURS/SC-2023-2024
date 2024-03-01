#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Exemple d'utilisation de typer
"""

from typer import Typer  # type: ignore

app = Typer()


@app.command()
def hello(nom: str):
    print(f"Bonjour {nom}")


@app.command()
def goodbye(nom: str):
    print(f"Au revoir {nom}")


if __name__ == "__main__":
    app()
