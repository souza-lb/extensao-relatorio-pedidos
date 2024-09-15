#!/usr/bin/env bash

# Este script shell visa a organização
# do ambiente de desenvolvimento Jupyter.
# Ele cria um ambiente virtal para uso e organiza
# os notebooks em pastas.
# Este script também instala e habilita o tema escuro.

# Configuração Jupyter Notebook.
if [ ! -d "$HOME/Jupyter/ambientes/padrao" ]; then
    mkdir -p "$HOME/Jupyter/notebooks/padrao"
    virtualenv "$HOME/Jupyter/ambientes/padrao"
    source "$HOME/Jupyter/ambientes/padrao/bin/activate"
    pip install --upgrade pip
    pip install ipykernel jupyterthemes==0.20.0
    python3 -m ipykernel install --user --name=padrao
    jt -t onedork -T -N -kl
    deactivate
    echo "[ INFO - jupyter ok - $(date) ]"
fi
