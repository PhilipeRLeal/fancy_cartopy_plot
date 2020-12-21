
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

import matplotlib


from .functions import (custom_colorbars, north_arrow, scale_bar, North_arrow_plus_scale_bar_standard_adder,
                        add_zebra, add_custom_gridline, add_background)

#custom_cbar = colorbars.custom_colorbars


def make_cbars(ax, vmin, vmax, colorbar_ax_yticks_format='%.0f'):
    
    cbar = custom_colorbars.add_colorbar_for_axes(axes=ax, vmax=vmax, vmin=vmin, colorbar_ax_yticks_format=colorbar_ax_yticks_format)
    
    return cbar


def make_fig(nrows=2,ncols=2):
    
    Projection = ccrs.PlateCarree()
    
    fig, ax = plt.subplots(nrows,ncols, sharex=True, sharey=True, subplot_kw={'projection':Projection}, figsize=(12,6.5))
    
    return fig, ax

    


def add_gridlines(ax,
                  
                  decimal_separator='.',
                  
                  gridline_tick_formating=dict(latitude_tick_formating={'number_format':'.1f', # com duas casas decimais
                                                                      'degree_symbol':'°', # u'\u00B0'
                                                                      'north_hemisphere_str': 'N',
                                                                      'south_hemisphere_str': 'S'} ,
                                                               
        
                                                      longitude_tick_formating={'number_format':'.1f', # com duas casas decimais
                                                                       'degree_symbol':'°', # u'\u00B0'
                                                                       'dateline_direction_label':True, # ONLY APPLICABLE TO LONGITUDE DATA
                                                                       'west_hemisphere_str': 'W',
                                                                       'east_hemisphere_str': 'E'}
                                                                       
                                                        ) ,
                                           
                  n_coordinate_ticks={'x_number':4,  'y_number':3},                      
                                                                                
                  gridline_xlabel_style={'color': 'black', 'rotation': 90, 'fontsize': 7},
                  
                  gridline_ylabel_style={'color': 'black', 'rotation': 0, 'fontsize': 7},
                  
                  gridline_attr=dict(draw_labels=True,
                                               linewidth=1, 
                                            color='black', 
                                            alpha=0.35, 
                                            linestyle='--'),
                                     
                  gridline_tick_axis_positions={'xlabels_top':False,
    												 'ylabels_left':True,
    												 'ylabels_right':False,
    												 'xlabels_bottom':True},
                  
                  zebra_gridlines={'add':True,
                                   'pad':2}
                  
                  ):
    
    
    gridline = add_custom_gridline(ax,
                                   gridline_attr= gridline_attr,
                                   n_coordinate_ticks=n_coordinate_ticks,
                                   gridline_tick_axis_positions=gridline_tick_axis_positions,
                                   gridline_tick_formating=gridline_tick_formating,
                                   gridline_xlabel_style= gridline_xlabel_style,
                                   gridline_ylabel_style=gridline_ylabel_style)
    
    if zebra_gridlines['add']:
        add_zebra(gridline, pad=zebra_gridlines['pad'])                      

    return gridline
 



    