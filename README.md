# Multi-dimensional data viewer
**ndview** is a small multi-dimensional array viewer for jupyter/jupyterlab.

## Install
### Set up environment
Jupyterlab with ipympl:
- `conda create -n jupyterlab_env -c conda-forge python=3 jupyterlab ipympl nb_conda_kernels nodejs=13`
- `conda activate jupyterlab_env`
- [on Windows, you may have to apply the [shutil.py patch](https://github.com/jupyterlab/jupyter-renderers/issues/127#issuecomment-646571193) to install jupyterlab extensions]
- `jupyter labextension install @jupyter-widgets/jupyterlab-manager`

Work environment: 
- `conda create -n work_env -c conda-forge python=3 ipympl numpy ipywidgets` (make sure that the ipympl version is the same as in your jupyterlab environment)

### Install ndview
- `conda install -c danionella ndview`

Or, for development and the latest version:
- Clone this repository. Navigate to the directory containing `setup.py`.
- `pip install -e .`

### Proxy settings
If you are on linux and use a university/company proxy:
```
export http_proxy="http://proxy.charite.de:8080"
export https_proxy="http://proxy.charite.de:8080"
export HTTP_PROXY="http://proxy.charite.de:8080"
export HTTPS_PROXY="http://proxy.charite.de:8080"
conda config --set proxy_servers.http http://proxy.charite.de:8080 
conda config --set proxy_servers.https http://proxy.charite.de:8080

git config --global http.proxy http://proxy.charite.de:8080
git config --global https.proxy http://proxy.charite.de:8080
pip config set global.proxy http://proxy.charite.de:8080

//After installing nodejs:
npm config set http-proxy http://proxy.charite.de:8080
npm config set https-proxy http://proxy.charite.de:8080
```

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
