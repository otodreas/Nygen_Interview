# Nygen_Interview
Implementation of Parashar's workflow

## Instructions

1. Run basic [scIV](https://scvi-tools.org/) on any data from [CellXGene](https://cellxgene.cziscience.com/datasets)
2. Run [CyteType](https://github.com/NygenAnalytics/CyteType) on the clusters

## Workflow

### Overview

The general workflow is

```
download data -> import, feature selection, model training -> clustering -> CyteType
```

### Programs

The `py` scripts in `./scripts` are intended to be run as is, without arguments (filepaths are hard-coded, so `.h5ad` input data needs to match).

```
Tool        Script              Pipeline step
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
CellXGene   train_scvi.py       Raw data
                                ↓
scanpy                          Feature selection
                                ↓
scvi-tools                      scVI (reduce expression profiles to 10D)
                                ↓
scanpy      cluster.py          Neighbor graph
                                ↓
scanpy                          Leiden Clustering (based on neighbor graph)
                                ↓
scanpy                          Get marker genes (top genes that define clusters)
                                ↓
CyteType    cytetype_predict.py Predict cell types etc.
```

### Inspecting results

`./scripts/CTViz.ipynb` contains plots showing
- scVI model training diagnostics
- UMAP projections of neighbor graph, with annotated clusters
    - Author annotations
    - CyteType annotations

Note that during clustering, I used the default number of clusters. Had I had more time I would have also generated results with different numbers of clusters, but for now I left it as the default. It was interesting to see that even though the number of clusters are different in the two UMAP plots, there is still a lot of agreement between the plots.

The CyteType report web page is linked in `./cytetype_report.txt`

## Data

See `./docs/papers/Data_paper_Gongetal2025.pdf`. It studies immune ageing. The specific data used in this pipeline was the monocytes and dendritic cells, which together form a vague cluster in the full dataset when the expression profiles are vizualised with UMAP. They do not show much DE between age groups, unlike T-cells.
