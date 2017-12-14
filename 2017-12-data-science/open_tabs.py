import webbrowser

tabs = ['https://www.anaconda.com/what-is-anaconda/',
        'http://www.numpy.org/',
        'http://www.sympy.org/en/index.html',
        'https://docs.scipy.org/doc/scipy/reference/',
        'http://scikit-learn.org/stable/',
        'https://pandas.pydata.org/',
        'https://matplotlib.org/',
        'https://seaborn.pydata.org/',
        'http://bokeh.pydata.org/en/latest/',
        'http://holoviews.org/',
        'https://plot.ly/python/',]

for tab in tabs:
    webbrowser.open(url=tab, new=2)