# Nygen_Interview
Implementation of Parashar's workflow

## Workflow (as described by Parashar)
1. Run basic [scIV](https://scvi-tools.org/) on any data from [CellXGene](https://cellxgene.cziscience.com/datasets)
2. Run [CyteType](https://github.com/NygenAnalytics/CyteType) on the clusters

## Pipeline Graph

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

## Data

See `./docs/papers/Data_paper_Gongetal2025.pdf`. It studies immune ageing. The specific data used in this pipeline was the monocytes and dendritic cells, which together form a vague cluster in the full dataset when the expression profiles are vizualised with UMAP. They do not show much DE between age groups, unlike T-cells.
