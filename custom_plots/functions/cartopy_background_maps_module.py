
import cartopy.feature as cfeature



Coastline = cfeature.NaturalEarthFeature(
        category='physical',
        name='Coastline',
        scale='10m',
        facecolor='none')

states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')

def add_background(ax, **kwargs):
    old_bounds = ax.get_extent()
    
    ax.add_feature(states_provinces, zorder=-1, **kwargs)
    ax.add_feature(Coastline, zorder=-1, **kwargs)
    ax.set_extent(old_bounds)