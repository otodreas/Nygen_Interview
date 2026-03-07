#!/usr/bin/env python3

# Import libraries
from pathlib import Path
import anndata
import numpy as np
import scanpy as sc
import scvi
import torch

# Set seed
scvi.settings.seed = 0

# Load data
adata = sc.read(
    filename=Path.cwd() / "data" / "breastcancer_scatlas.h5ad",
    backup_url=(
        "https://datasets.cellxgene.cziscience.com/7cdea341-ca7a-40fd-8192-b8ecb2d7b91e.h5ad"
    )
)

# Filter cells with few genes
sc.pp.filter_cells(adata, min_genes=200)

# Filter genes that appear in few cells
sc.pp.filter_genes(adata, min_cells=3)