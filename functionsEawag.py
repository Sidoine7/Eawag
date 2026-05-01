def get_swiss_coords(ds):
    """
    get x and y from CTD dataset
    
    E : ds=dataset of CTD
    R : x and y, coords
    """
    
    
    return ds.attrs['xsc'], ds.attrs['ysc']