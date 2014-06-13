#!/usr/bin/env python 
import sys
import argparse
import os, os.path
import glob
from src import mgmg2ogp,fgdc2ogp,logger

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("workspace",help="indicate the path where the metadata to be converted is contained")
    parser.add_argument("output_path",help="indicate the path where the output should be sent")
    parser.add_argument("metadata_type",help="Metadata standard used for input XMLs. Acceptable values are FGDC or MGMG", choices=['MGMG','FGDC'])
    parser.add_argument("--et", type=int,help="acceptable level of error which decides for any given XML file whether it will be included in the final output folder," +
                                              " or the error folder. Default value of 5000. Lower value means less tolerance (0 means any missing or incorrect OGP field" +
                                              " will cause the file to be moved to error folder)")
    args = parser.parse_args()
   
    ws = args.workspace
    output = args.output_path

    if not os.path.isabs(ws):
        ws = os.path.abspath(os.path.relpath(ws,os.getcwd()))

    if not os.path.isabs(output):
        output = os.path.abspath(os.path.relpath(output,os.getcwd()))
    
    md = args.metadata_type
    et = args.et

    if et == None:
        et = 5000    

    if os.path.exists(output) == False:
        try:
            os.mkdir(output)
        except OSError:
            print "There's a problem with the output path: %s. Are you sure you entered it correctly?" % (output)

    if os.path.exists(ws) == False:
        print "Workspace %s does not seem to exist. Are you sure you entered it correctly?" % (ws)

    elif os.path.exists(ws) == True:
        files = glob.glob(os.path.join(self.ws,'*[!aux].xml'))

        d = datetime.today()
        log_name = "OGP_MD_LOG_" + d.strftime("%y%m%d%M%S") + ".txt"
        sys.stdout = logger.Logger(self.output_path, log_name)

        for i in files:
            tree = et.ElementTree()
            root = tree.parse(i)

            if md.lower() == "mgmg":
                doc = mgmg2ogp.MGMGDocument(root)

            elif md.lower() == "fgdc":
                doc = mgmg2ogp.FGDCDocument(root)

            elif md.lower() == "arcgis":
                doc = mgmg2ogp.ArcGISDocument(root)


        """
        if md.lower() == "mgmg":
            mgmg2ogp.MGMG(ws,output, et)   
        elif md.lower() == "fgdc":
            fgdc2ogp.FGDC(ws,output, et)
        else:
            print "Unsupported metadata type entered. Currently supported values are FGDC or MGMG"
        """

if __name__ == "__main__":
    sys.exit(main())
