#!/usr/bin/env python3

#### CONFIGURE ####
# Import libraries
from pathlib import Path
import scanpy as sc
import scvi
import torch

# Set seed and torch settings
scvi.settings.seed = 0
torch.set_float32_matmul_precision("high")

#### PREPARE DATA ####
# Load data
adata = sc.read(
    filename=Path(__file__).resolve().parent.parent
    / "data"
    / "monocyte_dendritic.h5ad",
    backup_url=(
        "https://datasets.cellxgene.cziscience.com/c2068d3f-87e7-4a0e-9795-4dae11bcb9ac.h5ad"
    ),
)

# Save raw counts to `counts` layer in anndata object
adata.layers["counts"] = adata.raw.X.copy()

# Filter genes that appear in few cells
sc.pp.filter_genes(adata, min_counts=10)

# Normalize cells to 10,000 counts
sc.pp.normalize_total(adata, target_sum=1e4)

# Change to log scale
sc.pp.log1p(adata)

# Perform feature selection
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=1500,
    subset=True,
    layer="counts",
    flavor="seurat_v3",
    batch_key="batch_id",
)

# Setup anndata object for model fitting
scvi.model.SCVI.setup_anndata(
    adata,
    layer="counts",
    categorical_covariate_keys=["well_id"],
    continuous_covariate_keys=["pct_counts_mito"]
)

#### TRAIN MODEL ####
# Instantiate model
model = scvi.model.SCVI(adata)

# Train model
model.train(train_size=0.8, check_val_every_n_epoch=1)

#### SAVE DATA AND MODEL ####

# Save filtered anndata object as new .h5ad file
adata.write_h5ad(
    Path(__file__).resolve().parent.parent
    / "data"
    / "monocyte_dendritic_filter.h5ad"
)

# Save model
model.save(
    Path(__file__).resolve().parent.parent / "models" / "scvi3", overwrite=True
)
