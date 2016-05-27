import scipy.ndimage as mm
from . import binary_morphology as bm

def dilation(f, b=bm.create_structure_element_cross()):
    return mm.grey_dilation(f,structure=b)

def erosion(f, b=bm.create_structure_element_cross()):
    return mm.grey_erosion(f,structure=b)

def closing(f, b=bm.create_structure_element_cross()):
    return mm.grey_closing(f, structure=b)

def opening(f, b=bm.create_structure_element_cross()):
    return mm.grey_opening(f, structure=b)



