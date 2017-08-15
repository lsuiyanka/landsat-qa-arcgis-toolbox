"""
This software has been approved for release by the U.S. Geological Survey
(USGS). Although the software has been subjected to rigorous review, the USGS
reserves the right to update the software as needed pursuant to further
analysis and review. No warranty, expressed or implied, is made by the USGS or
the U.S. Government as to the functionality of the software and related
material nor shall the fact of release constitute any such warranty.
Furthermore, the software is released on condition that neither the USGS nor
the U.S. Government shall be held liable for any damages resulting from its
authorized or unauthorized use.

Author:         Steve Foga
Affiliation:    SGT Inc., contractor to USGS EROS Center
Contact:        steven.foga.ctr@usgs.gov
Created:        15 May 2017
Version:        1.2

Changelog
1.0     15 May 2017     Original development with Python 2.7.10 and
                        ArcGIS 10.4.1.
1.1     09 Aug 2017     Update to handle any L8 pixel_qa terrain occlusion.
1.2     21 Aug 2017     Added ability to unpack bits to individual files.
"""
import sys
import os
import arcpy
import lookup_dict


def build_attr_table(raster_in, sensor, band):
    """
    Build attribute table for thematic raster using pre-defined dictionary.

    :param raster_in: <str> Path to target raster.
    :param sensor: <str> Sensor type.
    :param band: <str> Band type.
    :return:
    """
    # read lookup dictionary
    qa_values = lookup_dict.qa_values

    # check to ensure raster is not floating/double/complex
    vt = int(str(arcpy.GetRasterProperties_management(raster_in, "VALUETYPE")))
    if vt >= 9:
        arcpy.AddError("ERROR: Data type of input raster must be integer.")
        sys.exit()

    # build attribute table
    arcpy.BuildRasterAttributeTable_management(raster_in, "Overwrite")

    # add description field to table
    arcpy.AddField_management(raster_in, "Descr", "TEXT", "", "", 120)
    fields = ("Value", "Descr")

    # re-map input sensor name to qa_values sensor name
    if sensor == 'Landsat 4-5, 7':
        sens = 'L47'
    elif sensor == 'Landsat 8':
        sens = 'L8'
    else:
        arcpy.AddError("ERROR: Incorrect sensor provided. Input: {0}; "
                       "Potential options: Landsat 4-5, 7 | Landsat 8"
                       .format(sensor))

    # assign values to attribute table
    with arcpy.da.UpdateCursor(raster_in, fields) as cursor:
        for row in cursor:
            try:
                if band == "radsat_qa":  # radsat_qa is sensor-agnostic
                    row[1] = qa_values[band][row[0]]
                elif sens == 'L8' and band == "pixel_qa" \
                        and row[0] >= 1024:  # L8 terrain occlusion
                    row[1] = 'Terrain occlusion'
                else:
                    row[1] = qa_values[band][sens][row[0]]

                cursor.updateRow(row)

            except KeyError:
                arcpy.AddError("ERROR: Band value {0} in file {1} does not "
                               "have a corresponding key value for {2} band."
                               .format(row[0], raster_in, band))

    # if running in ArcMap, refresh display in current mxd
    try:
        mxd = arcpy.mapping.MapDocument("CURRENT")
    except RuntimeError:
        pass
    else:
        # get current (active) data frame
        df = mxd.activeDataFrame

        # find source layer (if it exists)
        try:
            source_lyr = arcpy.mapping.ListLayers(mxd,
                                                  raster_in.split(os.sep)[-1],
                                                  df)[0]
        except IndexError:
            pass

        # create target layer
        raster_fname, ext = os.path.splitext(raster_in.split(os.sep)[-1])
        result = arcpy.MakeRasterLayer_management(raster_in,
                                                  raster_fname + ext)
        layer = result.getOutput(0)

        # add new layer
        arcpy.mapping.AddLayer(df, layer, "AUTO_ARRANGE")

        # remove old layer (if it exists)
        try:
            arcpy.mapping.RemoveLayer(df, source_lyr)
        except (UnboundLocalError, NameError):
            pass

        arcpy.RefreshTOC()
