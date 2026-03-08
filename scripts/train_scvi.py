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
    / "breastcancer_scatlas.h5ad",
    backup_url=(
        "https://datasets.cellxgene.cziscience.com/7cdea341-ca7a-40fd-8192-b8ecb2d7b91e.h5ad"
    ),
)

# Filter cells with few genes
sc.pp.filter_cells(adata, min_genes=500)

# Filter genes that appear in few cells
sc.pp.filter_genes(adata, min_cells=60)

# Save raw counts to `counts` layer in anndata object
adata.layers["counts"] = adata.X#.astype(np.int32)

# Normalize cells to 10,000 counts
sc.pp.normalize_total(adata, target_sum=1e4)

# Change to log scale
sc.pp.log1p(adata)

# Save raw data
adata.raw = adata

# Perform feature selection
sc.pp.highly_variable_genes(
    adata,
    n_top_genes=1500,
    subset=True,
    layer="counts",
    flavor="seurat_v3",
    batch_key="batch",
)

# Setup anndata object for model fitting
scvi.model.SCVI.setup_anndata(
    adata, layer="counts", categorical_covariate_keys=["donor_id", "assay"]
)

#### TRAIN MODEL ####
# Instantiate model
model = scvi.model.SCVI(adata)

# Train model
model.train(train_size=0.8, check_val_every_n_epoch=1)

#### SAVE DATA AND MODEL ####

# Save filtered anndata object as new .h5ad file
adata.write_h5ad(
    Path(__file__).resolve().parent.parent / "data" / "breastcancer_scatlas_filter.h5ad"
)

# Save model
model.save(Path(__file__).resolve().parent.parent / "models" / "scvi2", overwrite=True)
