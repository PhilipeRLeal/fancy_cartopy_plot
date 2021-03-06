
from .north_arrow import add_north_arrow_to_fig

from .scale_bar import fancy_scalebar, scale_bar_class
import numpy as np



def add_north_arrow_with_fancy_scale_bar(ax, 
                                         scalebar_properties = dict(location=(1.1, 0.1), 
                                                 length=200,
                                                   
                                                 metres_per_unit=1000, 
                                                 unit_name='km',
                                                 tol=0.01, 
                                                 angle=0,
                                                 dy = 0.05,
                                                 max_stripes=5,
                                                 ytick_label_margins = 0.25,
                                                 fontsize= 8,
                                                 font_weight='bold',
                                                 rotation = 45,
                                                 zorder=999,
                                                 paddings = {'xmin':0.3,
                                                             'xmax':0.3,
                                                             'ymin':0.3,
                                                             'ymax':0.3},
                                    
                                                 bbox_kwargs = {'facecolor':'w',
                                                                'edgecolor':'k',
                                                                'alpha':0.7}
                                                                
                                                                ),
                                                 arrow_properties = dict(
                                                    xmean=0.85,
                                                    y0=0.05,
                                                    y1=0.085, 
                                                    arrow_xshift=0.1,
                                                    arrow_yshift=0.1)
                                            
                                            ):
                                            
                                            
    # Adding north arrow:
    xmean = arrow_properties['xmean'] + arrow_properties['arrow_xshift']
    
    y0 = arrow_properties['y0'] + arrow_properties['arrow_yshift']
    
    y1 = arrow_properties['y1'] + arrow_properties['arrow_yshift']
    
    
    add_north_arrow_to_fig(fig=ax.get_figure(), 
                           x_tail=xmean,
                           y_tail=y0,
                           x_head=xmean,
                           y_head=y1)
                           
    # Fancy scalebar:
    
    fancy_scalebar(ax=ax, **scalebar_properties)
    
    




def add_north_arrow_with_old_scale_bar(ax, 
                                            distance=300, 
                                            units='km',
                                            x0=0.85,
                                            y0=0.05,
                                            x1=0.85,
                                            y1=0.085, 
                                            arrow_xshift=0.1,
                                            arrow_yshift=0.1):
    
    box = scale_bar_class.get_scalebar_with_rounded_kilometer_distance_based(ax=ax, 
   
                                                                            distance_in_km=distance, 
                                                                            length_unit=units,
                                                                            rounding_value_for_xsize=0,
                                                                            pad=0.5,sep=2, borderpad=5, 
                                                                            background_facecolor=(1,1,1,0.5),
                                                                            background_edgecolor ='black',
                                                                            background_facealpha=1,
                                                                            x0=x0,
                                                                             y0=y0,
                                                                             x1=x1,
                                                                             y1=y1)
    
    xmean = np.mean([x0, x1]) + arrow_xshift
    
    y0 += arrow_yshift
    
    y1 += arrow_yshift
    
    add_north_arrow_to_fig(fig=ax.get_figure(), 
                           x_tail=xmean,
                            y_tail=y0,
                            x_head=xmean,
                            y_head=y1)
    
    
    