# Listing and links to CZIMEA data and metadata

- [Cross-CZO sample processing workflow diagram (pdf)](https://drive.google.com/open?id=0B9NLnOiN5c1RUXIzbGNYVTNWMG8)
- [Mayorga et al, Cross-Site Soil and Microbial Ecology Cyberinfrastructure for the CZIMEA EarthCube Project (pdf).](https://github.com/BiG-CZ/CZIMEA/blob/master/EMayorga_ECAHM2017_Poster.pdf) Poster presented at the [CUAHSI Conference on Hydroinformatics in Tuscaloosa, AL, July 2017.](https://www.cuahsi.org/community/cuahsi-science-meetings/)
- Also relevant: data collected by the CZO's at the same sites

## Sampling planning and geospatial data
- MODIS-derived mean monthly time series of Enhanced Vegetation Index (EVI), to identify the timing of peak greenness. [Here's an example](https://github.com/BiG-CZ/CZIMEA/blob/master/MonthlyMeanMODIS_EVI_SouthernSierraCZOsite.png)
- Environmental characterization for the site, based on spatial datasets. For now, see [these notes](#4) about this effort. These will be loaded into the CZIMEA ODM2 Admin system listed below

## Site/stample metadata, environmental data and non-omics biological data
- CZIMEA ODM2 Admin
  - Development version, https://dev-odm2admin.cuahsi.org/CZIMEA/ User permission is required for full access. A subset of functionality is publicly accessible read-only via the map interface at http://dev-odm2admin.cuahsi.org/CZIMEA/mapdata.html 
  - Live version (coming)
- Sample metadata ([SESAR](http://www.geosamples.org/) & IGSN). Examples
  - Southern Sierra CZO: San Joaquin Experimental Reserve (SJER) Core, IGSN IERRR00AS: https://data.geosamples.org/sample/igsn/IERRR00AS
  - CZO0050 Individual Sample from the above Core, IGSN IERRR00GV: https://data.geosamples.org/sample/igsn/IERRR00GV
  - List of all CZO sites (not just CZIMEA CZO sites): https://app.geosamples.org/cruise_search.php?group_id=255  "This group includes all CZO samples registered with object type `Site`. This might help with your sample registration so that you can also include a parent sample for the CZO site. You'll need to do some filtering to find the site that you wish to associate with your samples - it might be easiest to do `Items per page > All`, then `Control F` to find the site (and IGSN) that you're looking for."
- Sampling and analytical methods. Some are available as documents online. A better approach could be explored using systems like https://www.protocols.io
- Soil physical properties: field capacity, gravimetric water, texture
- C & N concentrations, isotopes, pH
- Biological: microbial mass

## Omics data
- MG-RAST CZIMEA data: http://www.mg-rast.org/linkin.cgi?project=mgp80869 ("merged, quality filtered, and unassembled shotgun sequences are available")
- Other data deposited at IMG and Figshare, as described in a CZIMEA manuscript being submitted for publication
