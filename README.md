# Landsat Quality Assessment (QA) ArcGIS Toolbox
Quality Assessment (QA) information is a helpful resource for evaluating the overall usefulness of a Landsat pixel. Each pixel in the QA band contains an integer value that represents bit-packed combinations of surface, atmospheric, and sensor conditions that can affect the individual pixel quality. QA bands are delivered with [Landsat Collection 1 Level-1](https://landsat.usgs.gov/landsat-collections) and [Landsat Level-2 and Level-3 Science](https://landsat.usgs.gov/landsat-science-data-products) data products. 

The Landsat QA ArcGIS Toolbox contains functionality to classify and/or extract bit-packed values from QA bands, which enhance the applications of interpretation, mapping and applying QA values to Landsat data products.

Note: The [Landsat Quality Assessment (QA) Tools](https://landsat.usgs.gov/landsat-qa-tools) also contain the functionality of extracting bit-packed values to individual bands, but only for Level-1 QA information.

Follow the instructions below to download and install the tools. Information on the QA bands and how the tools operate on each band is also provided. The limitations of the tools are noted in the caveats section.

**Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.**


## Version 1.3 Release Notes
Release Date: July 2018

See git tag [1.3](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/tree/1.3)

### Changes
* Modified lookup_dict.py to contain only bit-wise interpretations.
    * Value-wise interpretations can still be viewed in tags [1.0](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/tree/1.0), [1.1](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/tree/1.1), and/or the [Landsat Surface Reflectance QA](https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment) web page.
* Modified qa_decode.py to use bit-wise interpretations. 
* Modified qa_decode.py and qa_decode_tool.py to optionally exclude labels coded as "low", with the exception of "low radiometric saturation" in BQA.
    * Updated Landsat_QA_ArcGIS_Tools.DecodeQA.pyt.xml (documentation for "low" removal option.)
* Addition of *Extract QA Bands* tool.
    * Added extract_bands.py and extract_bands_tool.py to allow users to make individual bands from bit-packed layers.
    * Added Landsat_QA_ArcGIS_Tools.ExtractBands.pyt.xml (documentation for new tool.)
    * Updated Landsat_QA_ArcGIS_Tools.pyt to add new tool to interface.
* Updated README to reflect changes, which includes updates to graphics.     


## Download
The Landsat QA ArcGIS Toolbox can be downloaded [here](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/archive/master.zip).


## Installation
The Landsat QA ArcGIS Toolbox can be installed using the following steps:

1. Extract the contents of the .zip file,
2. Open ArcMap or ArcCatalog,
3. Open ArcToolbox, right-click on the top-level "ArcToolbox" folder, and select "Add Toolbox...", and
4. Select "Landsat_QA_ArcGIS_Toolbox.pyt" from the directory extracted in Step 1.


## Compatible Products
The Landsat QA ArcGIS Toolbox is compatible with all Landsat Level-1 and Science Product QA bands. Below is a brief description of each band’s properties:

| Band | Source | Product | Tool Support | Product Page |
| --- | --- | --- | --- | --- |
| BQA         | Level-1      | Level-1 Proudct | [Decode QA](#tool-decode-qa), [Extract QA Bands](#tool-extract-qa-bands) | https://landsat.usgs.gov/collectionqualityband |
| pixel_qa    | Science Products | TOA, SI, SR             | [Decode QA](#tool-decode-qa), [Extract QA Bands](#tool-extract-qa-bands) | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |
| radsat_qa   | Science Products | TOA, SI, SR             | [Decode QA](#tool-decode-qa), [Extract QA Bands](#tool-extract-qa-bands) | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |
| sr_cloud_qa | Science Products | Landsat 4-7 SR (LEDAPS) | [Decode QA](#tool-decode-qa), [Extract QA Bands](#tool-extract-qa-bands) | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |
| sr_aerosol  | Science Products | Landsat 8 SR (LaSRC)    | [Decode QA](#tool-decode-qa), [Extract QA Bands](#tool-extract-qa-bands) | https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment |

*BQA Level-1 Quality Assessment Band File, LaSRC Landsat Surface Reflectance Code, LEDAPS Landsat Ecosystem Disturbance Adaptive Processing System, SI Spectral Indices, SR Surface Reflectance, TOA Top of Atmosphere Reflectance*


## Tool: Decode QA
The “Decode QA” tool performs the following steps:

1. Builds an attribute table containing all unique values in the QA band, 
2. Writes a description (“Descr”) column in the attribute table,
3. Assigns a description of each bit value in the table,
4. (ArcMap only) loads the band into Table of Contents in the active data frame, and
5. Optionally removes "low" labels, with the exception of "low radiometric saturation" for BQA. In all other QA tests, "low" denotes the least probable outcome of a test, therefore it may be undesirable for visualization purposes.

An example of the graphical user interface is provided below.

<img src="assets/decode_qa.png" width="500">

*Example of the Decode QA graphical user interface.*

The result is a raster band displayed with each QA bit value as a unique value, assigned random colors. A graphical representation is provided below.

<img src="assets/graphic_small.png" width="400">

*Graphical representation of a bit packed pixel_qa raster before (left) and after (right) the Decode QA tool is run.*

### Tool-specific caveats
* If an attribute table already exists for the target raster, it will be overwritten by the Decode QA tool.
* In the BQA band, if all non-saturation labels are set to "low", and the "Remove low labels" option is checked, then the final label is set as "Clear", even though BQA does not explicitly have a "clear" bit. Please see the [Landsat Collection 1 Level-1 Quality Assessment Band](https://landsat.usgs.gov/collectionqualityband) web page for details.

## Tool: Extract QA Bands
The "Extract QA Bands" tool performs the following steps:
1. Finds all unique values in the QA band,
2. Extracts classes individually, as defined by user input,
3. Writes each class to a new image file, and
4. Optionally combines all selected classes into a single file.

An example of the graphical user interface is provided below.

<img src="assets/extract_qa.png" width="500">

*Example of the Extract QA Bands graphical user interface.*

The result is a raster band (or multiple bands) assigned a `1` if the QA class is true, and a `0` if the QA class is false. If the `combine` option is selected, the raster band is assigned a `1` if any QA class is true, and a `0` if all QA classes are false. A graphical representation is provided below.

<img src="assets/graphic_extract.png" width="400">

*Graphical representation of a bit-packed pixel_qa raster before (left) and after (right) the Extract QA Bands tool is run.*

### Tool-specific caveats
* N/A

## Caveats
* The toolbox was designed using ArcGIS version 10.4.1 and Python version 2.7.10. The functionality of the toolbox cannot be guaranteed for previous software versions, and cross-compatibility of newer and future ArcGIS and Python releases are subject to vendor discretion. 
* Input data must be in GeoTIFF (.tif), binary (.img), or other single-band raster format supported by ArcGIS.
* Input data must be stored in integer format; any float, double, or complex data types are not supported.
* Any band with values outside of the supported range will not process. If you encounter this issue and believe it to be an error inherent to the tool, please [submit an issue in Github](https://github.com/USGS-EROS/landsat-qa-arcgis-toolbox/issues) or contact [USGS User Services](https://landsat.usgs.gov/contact). 
* If using non-standard (i.e., modified) file naming conventions, the tool may not correctly identify your band type, which may result in incorrect output products. Ensure the `sensor` and `band` categories are set accordingly.

## Notes
* The QA decoding is performed using a lookup table with descriptions of each bit-packed value. This table is located in [lookup_dict.py](./Scripts/lookup_dict.py). The values are also described in the [Surface Reflectance QA](https://landsat.usgs.gov/landsat-surface-reflectance-quality-assessment) web page.

## Contributions
If you wish to contribute feature requests, ideas, source code, or have a question regarding tool use, please submit them through this Github repository or [USGS User Services](https://landsat.usgs.gov/contact).

## Citation
Please use the following citation when referencing this software:

`U.S. Geological Survey, 2017. Landsat Quality Assessment ArcGIS Toolbox. U.S. Geological Survey software release. doi:10.5066/F7JM284N.`
