# Nygen_Interview
Implementation of Parashar's workflow

## Workflow (as described by Parashar)
1. Run basic [scIV](https://scvi-tools.org/) on any data from [CellXGene](https://cellxgene.cziscience.com/datasets)
2. Run [CyteType](https://github.com/NygenAnalytics/CyteType) on the clusters

## Pipeline Graph

```
Import CellXGene data ─────────┐
↓                              │
Convert to AnnData data object │
↓                              ╵
Filter data               scvi-tools       
↓                              ╷
Train model on dataset         │ 
↓                              │
Cluster data ──────────────────┘
↓
Annotate clusters ──────── CyteType
↓
Plot
```

