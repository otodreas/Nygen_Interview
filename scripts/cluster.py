#!/usr/bin/env python3

#### CONFIGURE ####
# Import libraries
from pathlib import Path
import scanpy as sc
import scvi

# Set seed
scvi.settings.seed = 0

#### LOAD DATA ####
# Load anndata
adata = sc.read(
    filename=Path(__file__).parent.parent
    / "data"
    / "monocyte_dendritic_filter.h5ad"
)

# Load fitted scVI model
model = scvi.model.SCVI.load(
    Path(__file__).parent.parent / "models" / "scvi3", adata=adata
)

#### CLUSTER ####
# Generate neighbor graph
sc.pp.neighbors(adata, use_rep="X_scVI")

# Save UMAP coordinates
sc.tl.umap(adata, min_dist=0.3)

# Cluster cells
sc.tl.leiden(adata, key_added="leiden_scVI", resolution=0.5)

# Calculate marker genes for each cluster
sc.tl.rank_genes_groups(adata, groupby="clusters", key_added="rank_genes_clusters", method="wilcoxon")

#### SAVE NEW ANNDATA OBJECT ####
# Save
adata.write_h5ad(
    Path(__file__).resolve().parent.parent
    / "data"
    / "monocyte_dendritic_cluster.h5ad"
)
