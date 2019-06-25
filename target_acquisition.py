import math
import sys
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
from astropy.io import fits

plotly.offline.init_notebook_mode(connected=True)

fits_file = fits.open(sys.argv[1])
file_name = sys.argv[1].split('.')[0]

def roundup_to_hundred(a,b):
    """rounds up the max of a and b to the nearest hundred"""
    return math.ceil( (max(a,b)) / 100) * 100

def rounddown_to_hundred(a,b):
    """rounds down the min of a and b to the nearest hundred"""
    return math.floor( (min(a,b)) / 100) * 100

upper_range_xaxis = roundup_to_hundred(fits_file[0].header['ACQCENTX'],fits_file[0].header['ACQPREFX']) + 100
lower_range_xaxis = rounddown_to_hundred(fits_file[0].header['ACQCENTX'],fits_file[0].header['ACQPREFX']) - 100
upper_range_xaxis = min(upper_range_xaxis, 1000)
lower_range_xaxis = max(lower_range_xaxis, 0)

upper_range_yaxis = roundup_to_hundred(fits_file[0].header['ACQCENTY'],fits_file[0].header['ACQPREFY']) + 100
lower_range_yaxis = rounddown_to_hundred(fits_file[0].header['ACQCENTY'],fits_file[0].header['ACQPREFY']) - 100
upper_range_yaxis = min(upper_range_yaxis, 1000)
lower_range_yaxis = max(lower_range_yaxis, 0)

range_xaxis = [lower_range_xaxis, upper_range_xaxis]
range_yaxis = [lower_range_yaxis, upper_range_yaxis]


title = "APERTURE: " + fits_file[0].header['APERTURE'] + ', ' + "OPTICAL ELEMENT: " + fits_file[0].header['OPT_ELEM'] + '<br>' + "ACQSLEWX (arcsec): " + (str)(fits_file[0].header['ACQSLEWX']) + ", ACQSLEWY (arcsec): " + (str)(fits_file[0].header['ACQSLEWY'])

data_acqcent = fits_file[1].data
data_acqpref = fits_file[4].data

trace_acqcent = go.Heatmap(
        z = data_acqcent,
        colorscale = 'Viridis',
    )

trace_acqpref = go.Heatmap(
        z = data_acqpref,
        colorscale = 'Viridis',
    )

fig = tools.make_subplots(rows=1, cols=2, subplot_titles=('ACQCENT', 'ACQPREF'))

fig.append_trace(trace_acqcent, 1, 1)
fig.append_trace(trace_acqpref, 1, 2)

fig['layout'].update(height=500, width=1000, title=title, titlefont = dict(size = 16))

fig['layout']['xaxis1'].update(title='AD', range=range_xaxis)
fig['layout']['yaxis1'].update(title='XD', range=range_yaxis, scaleanchor="x1", scaleratio=1)

fig['layout']['xaxis2'].update(title='AD', range=range_xaxis)
fig['layout']['yaxis2'].update(title='XD', range=range_yaxis, scaleanchor="x2", scaleratio=1)

#plotly.offline.iplot(fig, filename=file_name)
plotly.io.write_html(fig, file_name+'.html', include_plotlyjs=True)