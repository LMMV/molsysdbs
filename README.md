# molsysdbs

molsysdbs is a small Python library to download protein-related data from
public databases such as the Protein Data Bank (PDB) and UniProt.

## Quick start

```python
from molsysdbs import download_mmcif, download_uniprot_json

download_mmcif("1CRN", out_dir="data")
download_uniprot_json("P69905", out_dir="data")
```

## Development

- Tests: `pytest`
- Docs: `sphinx-build -b html docs docs/_build`

### Conda environment (developers)

```bash
conda env create -f environment.yml
conda activate molsysdbs
pip install -e .
```
