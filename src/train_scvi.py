#!/usr/bin/env python3

import os
from pathlib import Path
import anndata
import numpy as np
import scanpy as sc
import scvi
import torch

scvi.settings.seed = 0
model_dir = os.path.join(os.getcwd(), "data", "model")

adata = sc.read(
    filename=Path.cwd() / "data" / "raw" / "breastcancer_scatlas.h5ad",
    backup_url=(
        "https://datasets.cellxgene.cziscience.com/7cdea341-ca7a-40fd-8192-b8ecb2d7b91e.h5ad"
    )
)