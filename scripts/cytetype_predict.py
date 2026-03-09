#!/usr/bin/env python3

#### CONFIGURE ####
# Import libraries
from pathlib import Path
import scanpy as sc
from cytetype import CyteType

#### LOAD DATA ####
# Load anndata
adata = sc.read(
    filename=Path(__file__).parent.parent
    / "data"
    / "monocyte_dendritic_cluster.h5ad"
)
#### CYTETYPE ####
# Run CyteType and plot predicted cell type UMAP
group_key = "clusters"
annotator = CyteType(
    adata,
    group_key=group_key,
    rank_key="rank_genes_" + group_key,
    n_top_genes=100
)

adata = annotator.run(
    study_context="Human PBMC from healthy donors 25-90. Study on the efficacy of influenza vaccines."
)

#### SAVE NEW ANNDATA OBJECT ####
# Save
adata.write_h5ad(
    Path(__file__).resolve().parent.parent
    / "data"
    / "monocyte_dendritic_cytetype.h5ad"
)