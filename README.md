# Multi-dimensional data viewer
**ndview** is a small multi-dimensional array viewer for jupyter/jupyterlab.

## Install
### Set up environment
Jupyterlab with ipympl:
- `conda create -n jupyterlab_env -c conda-forge python=3 jupyterlab ipympl nb_conda_kernels`

Work environment: 
- `conda create -n work_env -c conda-forge python=3 ipympl numpy ipywidgets` (make sure that the ipympl version is the same as in your jupyterlab environment)

### Install ndview
- `conda install -c danionella ndview`

Or, for development and the latest version:
- Clone this repository. Navigate to the directory containing `setup.py`.
- `pip install -e .`

## Example

```
import numpy as np
from ndview import ndv
%matplotlib widget

data = np.random.rand(500,200,10,5)

ndv(data)
```

## See also
- [napari](https://github.com/napari/napari)
