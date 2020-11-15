# Multi-dimensional data viewer
**ndview** is a lightweight multi-dimensional array viewer for jupyter/jupyterlab.

## Install
### Set up environment
- ...

### Install ndview
Development:
- Clone this repository. Navigate to the directory containing `setup.py`.
- `pip install -e .`

Alternative:
- `pip install -e git+https://github.com/danionella/ndview.git`


## Example

```import numpy as np
from ndview import ndv
%matplotlib widget

data = np.random.rand(500,200,10,5)

ndv(data)
```

## See also
- [napari](https://github.com/napari/napari)
