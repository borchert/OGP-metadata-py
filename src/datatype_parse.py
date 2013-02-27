"""
Helper functions for parsing data type
"""
    
def dataTypeParseFGDC(root):
    try:
        if root.findtext("*//geoform").lower() == "scanned paper map":
            return "Paper Map"
        elif root.findtext("*//direct").lower() == "raster":
            return "Raster"
        elif (root.findtext("*//direct").lower() == "g-polygon" or root.findtext("*//direct").lower() == "polygon" or root.findtext("*//direct").lower() == "chain"):
            return "Polygon"
    except AttributeError as e:
        print "Can't determine data type, setting to UNKNOWN for now"
        return "UKNOWN"

def dataTypeParseMGMG(root):

    # There does not seem to be a separate listing for paper maps in the MN
    # standards. Instead the detailed abstract seems to have replaced original
    # form type fields...

    try:
        if root.findtext("*//direct").lower() == "raster":
            return "Raster"
        elif root.findtext("*//direct").lower() =="vector":       
            if "area" in root.findtext("*//mgmg3obj").lower() or "polygon" in root.findtext("*//mgmg3obj").lower() or "region" in root.findtext("*//mgmg3obj").lower() or "TIN" in root.findtext("*//mgmg3obj").lower():
                return "Polygon"
            elif "line" in root.findtext("*//mgmg3obj").lower() or "network" in root.findtext("*//mgmg3obj").lower() or "route-section" in root.findtext("*//mgmg3obj").lower():
                return "Line"
            elif "node" in root.findtext("*//mgmg3obj").lower() or "point" in root.findtext("*//mgmg3obj").lower():
                return "Point"
            
    except AttributeError as e:
        print "Can't determine data type, setting to Undefined for now"
        return "Undefined"
