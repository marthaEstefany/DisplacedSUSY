#!/usr/bin/env python

#intLumi = 112800 # full RunII
intLumi =   59700 # 2018
energy = '13'
#channel = 'emu'
channel = None # set to None for multi-channel plots

process = 'staus'
masses = [str(m) for m in range(200, 401, 100)]
lifetimes = [str(b*10**e) for e in range(-1, 2) for b in range(1, 10)] + [str(100)]

# description of all the plots to be made
plotDefinitions = [
    {
        # this will be the name of the canvas in the output root file
        'title' : 'standard_staus',

        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        'yAxisType' : 'lifetime',

        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#tau}} [GeV]',
        'yAxisLabel' : 'c#tau [cm]',

        #define all the curves to include on this canvas
        'th2fs' : [
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'th2fsToInclude' : ['obs'],
            },
        ],
        'graphs' : [
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'graphsToInclude' : ['exp', 'oneSigma', 'obs'],
                'colorScheme' : 'susy_pag',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_mass_staus',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'mass',
        # xmin, xmax, label
        'xAxisLabel' : 'm_{#tilde{#tau}} [GeV]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'lifetime' : '0.1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'yellow',
                'legendEntry' : '0.01 cm',
            },
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'lifetime' : '1',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'purple',
                'legendEntry' : '0.1 cm',
            },
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'lifetime' : '10',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '1 cm',
            },
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'lifetime' : '100',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '10 cm',
            },
        ],
    },
    {
        # this will be the name of the canvas in the output root file
        'title' : 'limits_vs_lifetime_staus',
        # current options are 'mass' and 'lifetime'
        'xAxisType' : 'lifetime',
        # xmin, xmax, label
        'xAxisLabel' : 'c#tau [cm]',

        'showTheory' : True,
        'showTheoryError' : True,

        #define all the curves to include on this canvas
        'graphs' : [
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'mass' : '200',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'blue',
                'legendEntry' : '200 GeV',
            },
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'mass' : '300',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'red',
                'legendEntry' : '300 GeV',
            },
            {
                'source' : 'combined_staus_2018_unblinded_19May2021',
                'mass' : '400',
                'graphsToInclude' : ['exp'],
                'colorScheme' : 'green',
                'legendEntry' : '400 GeV',
            },
        ],
    },
]
