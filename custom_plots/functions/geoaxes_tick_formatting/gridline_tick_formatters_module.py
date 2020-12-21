# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:09:27 2019

@author: lealp
"""

import matplotlib.pyplot as plt
from matplotlib import ticker
from formatters import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import cartopy.crs as ccrs

_DEGREE_SYMBOL = u'\u00B0'


def set_gridline_tick_axis_positions(gridliner , 
                                     gridline_tick_axis_positions
                                     ):
	 
	 gridliner.top_labels  = gridline_tick_axis_positions['top_labels']
	 gridliner.bottom_labels  = gridline_tick_axis_positions['bottom_labels']
	 
	 gridliner.right_labels  = gridline_tick_axis_positions['right_labels']
	 gridliner.left_labels = gridline_tick_axis_positions['left_labels']
	 
	 return gridliner
	 
 

def set_number_of_ticks_in_Gridliner(gridliner, nbins, locator='xlocator'):
    locator = getattr(gridliner, locator)
    
    locator = ticker.MaxNLocator(nbins)
    
    return gridliner




def change_gridline_tick_formating(gridliner, gridline_tick_formating='{0:.2f}', axis='yaxis', 
                                   decimal_separator=',', geographical_symbol=_DEGREE_SYMBOL):  
	 
    def custom_tick_func_formatter(x, y):
        ticklabel = '{0}'.format(gridline_tick_formating).format(x) 
        
        return ticklabel.replace('.', decimal_separator) + geographical_symbol
	 
    if axis.lower() == 'both':
 
        gridliner.xformatter = ticker.FuncFormatter(lambda x, y : custom_tick_func_formatter(x, y))
        gridliner.yformatter = ticker.FuncFormatter(lambda x, y : custom_tick_func_formatter(x, y))
			 
    else:
        if axis.lower().startswith('x'):
            gridliner.xformatter = ticker.FuncFormatter(lambda x, y : custom_tick_func_formatter(x, y))
        else:
            gridliner.yformatter = ticker.FuncFormatter(lambda x, y : custom_tick_func_formatter(x, y))
	
	
    return gridliner


def format_gridline_major_ticklabels(gl, gridline_tick_formating, decimal_separator='.', 
                                     geographical_symbol=_DEGREE_SYMBOL):
    
    
    # Instanciating the Formater for the gridline
    
    longitude_tick_formating = gridline_tick_formating['longitude_tick_formating']
    
    west_hemisphere_str = longitude_tick_formating.get('west_hemisphere_str', 'W')  
    east_hemisphere_str = longitude_tick_formating.get('east_hemisphere_str', 'E')  
    degree_symbol = longitude_tick_formating.get('degree_symbol', '°')
    
    
    lon_formatter = LONGITUDE_FORMATTER(degree_symbol=degree_symbol,
                                       west_hemisphere_str=west_hemisphere_str,
                                       east_hemisphere_str=east_hemisphere_str)
    
    
           
    latitude_tick_formating = gridline_tick_formating['latitude_tick_formating']
    
    north_hemisphere_str = latitude_tick_formating.get('north_hemisphere_str', 'N')  
    south_hemisphere_str = latitude_tick_formating.get('south_hemisphere_str', 'S')  
    degree_symbol = latitude_tick_formating.get('degree_symbol', '°')
    	 
    
    lat_formatter = LATITUDE_FORMATTER(degree_symbol=degree_symbol,
                                      north_hemisphere_str=north_hemisphere_str,
                                      south_hemisphere_str=south_hemisphere_str)
    
   
    #############################
    
    
    
    change_gridline_tick_formating(gl,  
                                   gridline_tick_formating=longitude_tick_formating.get('number_format', '{0:.2f}'), 
                                   axis='x', 
                                   decimal_separator=decimal_separator,
                                   geographical_symbol=geographical_symbol)
    
    change_gridline_tick_formating(gl,  
                                   gridline_tick_formating=latitude_tick_formating.get('number_format', '{0:.2f}'), 
                                   axis='y', 
                                   decimal_separator=decimal_separator,
                                   geographical_symbol=geographical_symbol)
                                   
    
    # setting the gridline Formatter
    
        # The xformatter does no work for subplots at the moment.
        # Wait to see what happens in : https://stackoverflow.com/questions/65298032/how-can-one-set-cartopys-gridline-label-styles-major-xticks-and-minor-xticks
    
    gl.xformatter = lon_formatter
    gl.yformatter = lat_formatter
    
    return gl
    
    
    
    
def add_custom_gridline(geo_axes, 
                    
                        gridline_attr=dict(draw_labels=True,
                                       linewidth=1, 
                                    color='black', 
                                    alpha=0.35, 
                                    linestyle='--',
                                    x_inline=False, y_inline=False),
                                       
                        n_coordinate_ticks={'x_number':3,  'y_number':3},
                        
                        ticklabel_padding={'xpadding':5,  'ypadding':3},
                    
                        gridline_tick_formating=dict(latitude_tick_formating={'number_format':'{0:.2f}', # com duas casas decimais
                                                              'degree_symbol':'°', # u'\u00B0'
                                                              'north_hemisphere_str': 'N',
                                                              'south_hemisphere_str': 'S'} ,
                                                       

                        longitude_tick_formating={'number_format':'{0:.2f}', # com duas casas decimais
                                                  'degree_symbol':'°', # u'\u00B0'
                                                  # ONLY APPLICABLE TO LONGITUDE DATA
                                                  'west_hemisphere_str': 'O',
                                                  'east_hemisphere_str': 'L'}) ,
                      
						gridline_xlabel_style = {'color': 'k', 
                                                 'xpadding':10,
                                                 'weight': 'normal', 
                                                 'rotation':90,
                                                 'size':12,
                                                 'ha':'right'},
                 
                        gridline_ylabel_style = {'color': 'k', 
                                                 'ypadding':10,
                                                 'weight': 'normal', 
                                                 'rotation':0,
                                                 'size':12,
                                                 'ha':'left'},  
							
    
						gridline_tick_axis_positions={'top_labels':False,
												 'left_labels':True,
												 'right_labels':False,
												 'bottom_labels':True}		,
                                
                        decimal_separator='.',										   
                        geographical_symbol='°'
                        ):

    """
        Function description:
			This inserts custom gridlines into a given axes.
			
			parameters:
				
				draw_labels(bool): whether to draw the labels in the gridline or not
					Default = True
				
				gridline_attr (dict): sets the linewidth, the linecolor, the alpha of the linecolor, linestyle

				n_coordinate_ticks (dict): sets the number of lines in the gridlines x coordinate (longitude) and y coordinate (latitude)
				
					Default = {'x_number':3,  'y_number':3}
		
				gridline_tick_formating (dict): contains parameters for setting the lines of the gridlines. 
				
					latitude_tick_formating: dictionary containing parameters for defining the ticklines of the y axis of the given axes:
						
						'number_format' (string or matplotlib formatter function based): sets the format of the coordinate number in the gridlines ticklabels
						
						'degree_symbol' (string): sets the symbol of the coordinates
							Default = '°'
						
						
						'north_hemisphere_str' (string): the string to be used for the north hemisphere.
							Default = 'N' 
						
						'south_hemisphere_str' (string): the string to be used for the south hemisphere
							Default = 'S' for south hemisphere
					
					
					longitude_tick_formating: the same thing as latitude_tick_formating for longitude data, except that it is relative to the xaxis of the given axes.
					
						
					gridline_xlabel_style (dict): sets xlabel style of the griline of the given axes. It accepts all parameters that ax.gridlines().xlabel_style accepts.
					
					gridline_ylabel_style (dict): sets xlabel style of the griline of the given axes. It accepts all parameters that ax.gridlines().ylabel_style accepts.
					
					gridline_tick_axis_positions: allows further customization of the ticklabels. It sets which axis the labels should be drawn in a given axes.

    """
 
    
    gl = geo_axes.gridlines(crs=ccrs.PlateCarree(), **gridline_attr) # axes projection here too
    
    # Setting which position are to be placed the coordinate - ticklabels
    
    gl = set_gridline_tick_axis_positions(gl , 
                                     gridline_tick_axis_positions
                                     )		
    
    
    
    
    # setting the gridline Formatter
    
        # There are some problems in the gridline Formatter
        # Wait to see what happens in : https://stackoverflow.com/questions/65298032/how-can-one-set-cartopys-gridline-label-styles-major-xticks-and-minor-xticks
    
        # The solution seems to be in respect to the order of settings of the 
        # gridliner
    gl.xlabel_style = gridline_xlabel_style
    
    gl.ylabel_style = gridline_ylabel_style
    
    
    # Setting ticklabels formatters
    
    
    gl = format_gridline_major_ticklabels(gl, gridline_tick_formating, 
                                     decimal_separator=decimal_separator, 
                                     geographical_symbol=geographical_symbol)
    
    # Setting number of ticks in the gridlines
    
    gl = set_number_of_ticks_in_Gridliner(gridliner=gl, 
                                          nbins=n_coordinate_ticks.get('y_number', 3), 
                                          locator='ylocator')
    
    
    gl = set_number_of_ticks_in_Gridliner(gridliner=gl, 
                                          nbins=n_coordinate_ticks.get('x_number', 3), 
                                          locator='xlocator')
    
    
    
    # Fixing padding for gridline ticklabels
    
    gl.xpadding = ticklabel_padding.get('xpadding', 10)
    gl.ypadding = ticklabel_padding.get('ypadding', 10)
                    
    
    
    return gl
        
        
     
    
    

if '__main__' ==__name__:
        
    
    
    from fancy_spatial_geometries_plot.custom_plots import get_standard_gdf
    
    SHP = get_standard_gdf()
    
    SHP['CD_GEOCMU'] = SHP['CD_GEOCMU'].apply(int)
    
    
    projection = ccrs.PlateCarree() # projection.proj4_init
    
    Transform = ccrs.Geodetic(globe=ccrs.Globe(ellipse='GRS80'))
    
    
    
    fig, ax = plt.subplots(1, subplot_kw={'projection':projection})
    
    
    SHP.plot(ax=ax, transform=Transform)
    
    Grider = ax.gridlines(draw_labels=True)
    
   
    
    change_gridline_tick_formating(Grider,  axis='both')
    
    
    
    set_gridline_tick_axis_positions(Grider, 
                                     {'top_labels':False,
												 'left_labels':True,
												 'right_labels':False,
												 'bottom_labels':True}	)
    
   
    
    fig.subplots_adjust()
    
    fig.show()
    
    
    
    ##################################################################################################################
    
    ##################################################################################################################
    
    ##################################################################################################################
    
    ##################################################################################################################
    
    fig, axes = plt.subplots(3,3, subplot_kw={'projection':projection},
                             sharex=True, sharey=True)
    
    axes = axes.ravel()
    
    for ax in axes:
        SHP.plot(ax=ax)
        
        
        
        gl = add_custom_gridline(ax, 
                                
                                gridline_attr=dict(draw_labels=True,
                                                   linewidth=1, 
                                                   color='black', 
                                                   alpha=0.35, 
                                                   linestyle='--',
                                                   x_inline=False, 
                                                   dms=True,
                                                   y_inline=False),
                                                   
                                n_coordinate_ticks={'x_number':3,  'y_number':3},
                                
                                gridline_tick_formating=dict(latitude_tick_formating={'number_format':'{0:.1f}', # com duas casas decimais
                                                                          'degree_symbol':'°', # u'\u00B0'
                                                                          'north_hemisphere_str': 'N',
                                                                          'south_hemisphere_str': 'S'} ,
                                                                   
            
                                                            longitude_tick_formating={'number_format':'{0:.2f}', # com duas casas decimais
                                                                           'degree_symbol':'°', # u'\u00B0'
                                                                           'dateline_direction_label':True, # ONLY APPLICABLE TO LONGITUDE DATA
                                                                           'west_hemisphere_str': 'O',
                                                                           'east_hemisphere_str': 'L'}
                                                                           
                                                            ) ,
                                
                                gridline_xlabel_style = {'color': 'k', 
                                                         #'weight': 'bold', 
                                                         'rotation':45,
                                                         'size':8,
                                                         'ha':'right'},
                             
                                gridline_ylabel_style = {'color': 'k', 
                                                       #'weight': 'bold', 
                                                       'rotation':0,
                                                       'ha':'right',
                                                       'size':8},  
        							
        							ticklabel_padding = dict(xpadding=5, ypadding=3),
                
                                
        							gridline_tick_axis_positions={'top_labels':False,
    												 'left_labels':True,
    												 'right_labels':False,
    												 'bottom_labels':True}									   
                                
                                )

            
    
    fig.subplots_adjust(top=0.962,
                        bottom=0.193,
                        left=0.025,
                        right=0.975,
                        hspace=0.2,
                        wspace=0.2)
    
    fig.show()