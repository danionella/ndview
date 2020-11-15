import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import Layout

def ndv(data, figsize=None, YX = [-2,-1], vox_sz=None, clim=None, **kwargs):
    
    dims = data.shape
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    
    plt.show()
    if not clim: clim = [min(0, data.min()), data.max()]
    im = []
    sliders = []
    
    def rbCallback(event=None):
        if rbX.value == rbY.value:
            if event['owner'] == rbX: rbY.value = event['old']
            elif event['owner'] == rbY: rbX.value = event['old']
        ax.clear()
        refreshimage();
        sliderCallback();
        ax.set_xlabel(f'axis {rbX.value}')
        ax.set_ylabel(f'axis {rbY.value}')
        #plt.ylabel('axis')

    def sliderCallback(event=None):
        im.set_data(getslice())
        ax.figure.canvas.draw_idle()

    def getslice():
        subs = [sliders[i].value for i in range(len(sliders))];
        subs[rbY.value] = slice(None);
        subs[rbX.value] = slice(None);
        out = data[tuple(subs)]
        if rbX.value < rbY.value: out = out.T
        return out

    def refreshimage():
        nonlocal im
        aspect = vox_sz[rbX.value]/vox_sz[rbY.value] if vox_sz else 'auto'
        im = ax.imshow(getslice(), interpolation='nearest', aspect=aspect, vmin=clim_slider.value[0], vmax=clim_slider.value[1], **kwargs)
        plt.colorbar(im)
        
    def clim_sliderCallback(event):
        im.set_clim(clim_slider.value)

    for i in range(len(dims)):
        slider = widgets.IntSlider(value=0,min=0,max=dims[i]-1,description=f'[{dims[i]}]',layout=Layout(width='500px', height='17px'))
        slider.observe(sliderCallback, names='value')
        sliders.append(slider)
    rbY = widgets.RadioButtons(options=[i for i in range(len(dims))],layout={'width':'40px'},value=(len(dims)+YX[0])%len(dims))
    rbX = widgets.RadioButtons(options=[i for i in range(len(dims))],layout={'width':'40px'},value=(len(dims)+YX[1])%len(dims))
    rbY.observe(rbCallback, names='value')
    rbX.observe(rbCallback, names='value')
    clim_slider = widgets.FloatRangeSlider(value=clim,min=0,max=data.max(),step=1/1000,description='clim:',readout_format='.3', layout=Layout(width='500px', height='30px'))
    clim_slider.observe(clim_sliderCallback, names='value')
    hb = widgets.HBox([widgets.VBox([widgets.Label('Y'), rbY]), widgets.VBox([widgets.Label('X'), rbX]), widgets.VBox([clim_slider, widgets.VBox(sliders)])])
    display(hb)
    
    rbCallback()
    plt.tight_layout()
    