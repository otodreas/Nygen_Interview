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
↓                              │
Filter data                    ╵
↓                         scvi-tools                              
Train model on dataset         ╷
↓                              │
Save trained model as `.pt`    │ 
↓                              │
Cluster data ──────────────────┘
↓
Annotate clusters ──────── CyteType
↓
Plot
```

## Requirements
The python version used can be found in `.python-version`, and the required packages can be installed into a viritual environment with `pip install -r requirements.txt`.

`requirements.txt` only includes `ipykernel`, not `jupyter`, meaning that an IDE with a Jupyter plugin is required. If the user does not have access to one, they will need to run `pip install jupyter`.

## Notes
`adata.obs` is the **observation dataframe** with various data.