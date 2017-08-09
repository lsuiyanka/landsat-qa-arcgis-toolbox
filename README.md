# Landsat Quality Assessment (QA) ArcGIS Toolbox
Quality Assessment (QA) bands are a helpful resource for evaluating the overall usefulness of a Landsat pixel. Each pixel in the QA band contains an integer value that represents bit packed combinations of surface, atmospheric, and sensor conditions that can affect the individual pixel quality. QA bands are currently provided with Collection 1 based products, including Landsat [Level-1 Standard Data Products](https://landsat.usgs.gov/landsat-level-1-standard-data-products) and [Higher Level Science Data Products](https://landsat.usgs.gov/landsat-higher-level-science-data-products). 

The Landsat QA ArcGIS Toolbox provides functionality to classify bit packed values for Level-1 and Higher-Level QA bands, which enhance the applications of interpretation, mapping and applying QA values to Landsat data products.  Another set of tools is the [Landsat Quality Assessment (QA) Tools](https://landsat.usgs.gov/landsat-qa-tools), which provides the functionality of extracting bit packed values to individual bands.  

The instructions below detail how to download and install the tools, as well as information on the QA bands and how the tools operate on each band. The limitations of the tools are provided in the caveats section.

**Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.**


## Version 1.1 Release Notes
Release Date: August 2017

See git tag [1.1]

### Changes
* Update to qa_decode.py to handle all terrain occlusion bits in L8 pixel_qa band.


## Download
The Landsat QA ArcGIS Toolbox can be downloaded from [here](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/archive/master.zip).


## Installation
The Landsat QA ArcGIS Toolbox can be installed using the following steps:

1. Extract the contents of the .zip file,
2. Open ArcMap or ArcCatalog,
3. Open ArcToolbox, right-click on the top-level "ArcToolbox" folder, and select "Add Toolbox...", and
4. Select "Landsat_QA_ArcGIS_Toolbox.pyt" from the directory extracted in Step 1.


## Compatible Products
The Landsat QA ArcGIS Toolbox is compatible with all Landsat Level-1 and Higher-Level QA bands. Below is a brief description of each band’s properties:

| Band | Source | Product | Product Page |
| --- | --- | --- | --- |
| BQA         | Level-1      | Standard Level-1 Proudct | https://landsat.usgs.gov/collectionqualityband |
| pixel_qa    | Higher-Level | TOA, SI, SR             | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |
| radsat_qa   | Higher-Level | TOA, SI, SR             | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |
| sr_cloud_qa | Higher-Level | Landsat 4-7 SR (LEDAPS) | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |
| sr_aerosol  | Higher-Level | Landsat 8 SR (LaSRC)    | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |

*BQA Level-1 Quality Assurance Band File, LaSRC Landsat Surface Reflectance Code, LEDAPS Landsat Ecosystem Disturbance Adapative Processing System, SI Spectral Indices, SR Surface Reflectance, TOA Top of Atmosphere Reflectance*


## Tool: Decode QA
Currently, the only tool in the toolbox is the “Decode QA” tool, which performs the following steps:

1. Builds an attribute table containing all unique values in the QA band, 
2. Writes a description (“Descr”) column in the attribute table,
3. Assigns a description of each bit value in the table, and
4. (ArcMap only) loads the band into Table of Contents in the active data frame.

An example of the graphical user interface is provided below.

<img src="assets/decode_qa.png" width="500">

*Example of the Decode QA graphical user interface.*

The result is a raster band displayed with each QA bit value as a unique value, assigned random colors. A graphical representation is provided below.

<img src="assets/graphic_small.png" width="400">

*Graphical representation of a bit packed pixel_qa raster before (left) and after (right) the Decode QA tool is run.*

## Caveats
* The toolbox was designed using ArcGIS version 10.4.1 and Python version 2.7.10. The functionality of the toolbox cannot be guaranteed for previous software versions, and cross-compatibility of newer and future ArcGIS and Python releases are subject to vendor discretion. 
*	Input data must be in GeoTIFF (.tif), binary (.img), or other single-band raster format supported by ArcGIS.
*	Input data must be stored in integer format; any float, double, or complex data types are not supported.
*	Any band with values outside of the supported range will not process. If you encounter this issue and believe it to be an error inherent to the tool, please [submit an issue in Github](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/issues) or contact [USGS User Services](https://landsat.usgs.gov/contact). 
*	If using non-standard (i.e., modified) file naming conventions, the tool may not correctly identify your band type, which may result in incorrect output products. Ensure the `sensor` and `band` categories are set accordingly.
*	If an attribute table already exists for the target raster, it will be overwritten by the Decode QA tool.


## Notes
* The QA decoding is performed using a lookup table of descriptions that correspond with each bit-packed value. This table is located in lookup_dict.py (in the Scripts folder.) The values are also described in the [Surface Reflectance QA web page](https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment).

## Contributions
If you wish to contribute feature requests, ideas, source code, or have a question regarding tool use, please submit them through this Github repository or [USGS User Services](https://landsat.usgs.gov/contact).

## Citation
Please use the following citation when referencing this software:

`U.S. Geological Survey, 2017. Landsat Quality Assurance ArcGIS Toolbox. U.S. Geological Survey software release. doi:10.5066/F7JM284N.`
