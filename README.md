# Multi-dimensional data viewer
**ndview** is a lightweight multi-dimensional array viewer for jupyter/jupyterlab.

## Install
### Set up environment
Jupyterlab with ipympl:
- `conda create -n jupyterlab_env -c conda-forge python=3 jupyterlab ipympl nb_conda_kernels nodejs=13`
- `conda activate jupyterlab_env`
- [on Windows, you may have to apply the [shutil.py patch](https://github.com/jupyterlab/jupyter-renderers/issues/127#issuecomment-646571193)]
- `jupyter labextension install @jupyter-widgets/jupyterlab-manager`
- `jupyter lab` ...

Work environment: 
- `conda create -n work_env -c conda-forge python=3 ipympl numpy ipywidgets`

### Install ndview
Development:
- Clone this repository. Navigate to the directory containing `setup.py`.
- `conda activate work_env`
- `pip install -e .`

Alternative:
- `conda activate work_env`
- `pip install -e git+https://github.com/danionella/ndview.git`


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
