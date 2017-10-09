# Notes on General Soils Datasets for possible integration by BiGCZ and use in CZIMEA analysis

These notes may be more appropriate in some other BiGCZ repository rather than CZIMEA, but this is a good place to start.

A general warning / caution about many soil data compilations: **soil profile location (lat-lon) are not always highly accurate, or even present at all.** eg, in a review of the WoSIS paper, it was stated that "In the current version of WoSIS, about 20% of the soil profiles do not have a quantitative georeference, i.e. numeric geographic coordinates". The ISCN documentation makes similar warnings, while highlighting the value of data that has many consistent parameters at one profile/horizon even though it doesn't have good (or any) lat-lon locations.

## Data for the US

### CZOData
- As available primarily from CZOCentral WOF
- Data structure is highly variable, but this is a resource that must be assessed. Luquillo CZO would be a great place to start.

### NEON

### LTER

### SSURGO, G-SURGO (?), and other federal agency datasets
- See ModelMyWatershed efforts. Anthony can fill in details on this.
- [USA National Cooperative Soil Survey Soil Characterization database](http://ncsslabdatamart.sc.egov.usda.gov/)
- [USA National Soil Information System](http://soils.usda.gov/technical/nasis/)

### Dylan Beaudette (USDA-NRCS)
- Anything Dylan is doing! https://twitter.com/DylanBeaudette, https://github.com/dylanbeaudette, https://casoilresource.lawr.ucdavis.edu/people/dylan-e-beaudette/
- He even studies the "Sierra Foothill Region of California" and lives in that area, so may be of direct interest to Emma and the Southern Sierra CZO

### others, specially for soil properties
- eg, this older reference: *Kern, J. 1995, Geographic patterns of soil water-holding capacity in the contiguous United States. Soil Science Society of America Journal 59, 1126-1133*. Can then look up recent studies that cite it in building newer, better, broader US datasets


## Global data

### [ISCN: International Soil Carbon Network](http://iscn.fluxdata.org)
- In coordination with BiGCZ goals, it'd be good to try to ingest/map some data from ICSN into ODM2. That'd benefit both CZIMEA and BiGCZ in multiple ways.
- Jennifer (Jen) Harden <82soiljen@gmail.com> is the new lead; Deb Agarwal <DAAgarwal@lbl.gov> is or was a technical data lead. Margaret Torn (no longer the lead) also mentioned Chris Swanston <cswanston@fs.fed.us> as being involved
- "Now in its 3rd generation (12/2015), the ISCN database includes data for over 430,000 individual soil layers from over 71,000 profiles worldwide."
- Somewhat related FLUXNET Data Management paper from Deb (who co-led the development of the FLUXNET database): Agarwal, D. A., Humphrey, M., Beekwilder, N. F., Jackson, K. R., Goode, M. M. and van Ingen, C. (2010), A data-centered collaboration portal to support global carbon-flux analysis. Concurrency Computat.: Pract. Exper., 22(17): 2323–2334. [doi:10.1002/cpe.1600](http://dx.doi.org/10.1002/cpe.1600)
- [ICSN meeting that happened just before AGU 2016](http://iscn.fluxdata.org/2016/10/20/agenda-posted-pre-agu-iscn-hands-meeting/)

### [WoSIS: World Soil Information Service](http://www.isric.org/explore/wosis)
- Recent paper (2017-1): *WoSIS: providing standardised soil profile data for the world, Earth Syst. Sci. Data, [doi:10.5194/essd-9-1-2017](https://doi.org/10.5194/essd-9-1-2017)*
- Has [working GeoServer instance](http://data.isric.org/geoserver/), with OGC (WMS, WFS, etc) access to all the data! I've already tested it successfully with QGIS.

### [SoilGrids](http://www.isric.org/explore/soilgrids)
- This looks like a fantastic resource
- **SoilGrids1km** and now (Feb. 2017) **SoilGrids250m**
  - **SoilGrids250m:**
    - https://github.com/ISRICWorldSoil/SoilGrids250m
    - Hengl T, Mendes de Jesus J, Heuvelink GBM, Ruiperez Gonzalez M, Kilibarda M, Blagotić A, et al. (2017) SoilGrids250m: Global gridded soil information based on machine learning. PLoS ONE 12(2): e0169748. [doi:10.1371/journal.pone.0169748](http://dx.doi.org/10.1371/journal.pone.0169748)
  - **SoilGrids1km:** Hengl T, de Jesus JM, MacMillan RA, Batjes NH, Heuvelink GBM, Ribeiro E, et al. (2014) SoilGrids1km — Global Soil Information Based on Automated Mapping. PLoS ONE 9(8): e105992. [doi:10.1371/journal.pone.0105992](http://dx.doi.org/10.1371/journal.pone.0105992)
- All data are [downloadable as geotiffs](ftp://soilgrids:soilgrids@ftp.soilgrids.org/data/recent/). Also available via [GeoServer application](http://webservices.isric.org/geoserver), and "For accessing SoilGrids at point locations please refer to http://rest.soilgrids.org documentation"
- Very nice [interactive map application](https://www.soilgrids.org)

### [GSIF: Global Soil Information Facilities](http://gsif.isric.org)
- Not a dataset, but a set of software tools in R, plus the collaborators involved. It's described as the "ISRIC Cyberinfrastructure" for global soils work. See the GSIF section in the SoilsGrids1km paper
- Looks like it's mainly the group that's developing WoSIS and SoilsGrids1km, but also have links to [Dylan Beaudette (USDA-NRCS)](https://twitter.com/DylanBeaudette)?!
- Are running a ["Spring school: 15 – 19 May 2017."](http://www.isric.org/utilise/capacity-building/springschool/gsif) Looks great!

### [WISE30sec](http://www.isric.org/data/isric-wise-derived-soil-property-estimates-30-30-arcsec-global-grid-wise30sec)
- Batjes, N.H. 2016. Harmonized soil property values for broad-scale modelling (WISE30sec) with estimates of global soil carbon stocks. Geoderma 269:61-68, [doi:10.1016/j.geoderma.2016.01.034](http://dx.doi.org/10.1016/j.geoderma.2016.01.034). PDF available [here](https://www.researchgate.net/publication/292605384_Harmonized_soil_property_values_for_broad-scale_modelling_WISE30sec_with_estimates_of_global_soil_carbon_stocks).
- How is this related to *SoilsGrids1km* (above)? Both are from ISRIC, same group.

### [GlobalSoilMap](http://www.globalsoilmap.net/)
- Quite ambitious. *But,* web site looks highly dated and stale, hence I'm suspicious about its current status ...
- Publications:
  - See their [Publications page](http://www.globalsoilmap.net/biblio) (through 2014, and even that is incomplete)
  - Published a book: [Arrouays et al, 2014, GlobalSoilMap: Basis of the global spatial soil information system](http://www.globalsoilmap.net/content/globalsoilmap-basis-global-spatial-soil-information-system)
  - Motivator? Sanchez et al, 2009, Digital Soil Map of the World, [doi:10.1126/science.1175084](http://dx.doi.org/10.1126/science.1175084)
  - Arrouays, D., Grundy, M. G., Hartemink, A. E., Hempel, J. W., Heuvelink, G. B. M., Hong, S. Y., Lagacherie, P., Lelyk, G.,
McBratney, A. B., McKenzie, N. J., Mendonca-Santos, M. d. L., Minasny, B., Montanarella, L., Odeh, I. O. A.,
Sanchez, P. A., Thompson, J. A., Zhang, G.-L., and Donald, L. S., 2014, GlobalSoilMap: Toward a Fine-Resolution Global
Grid of Soil Properties, Advances in Agronomy, Volume 125, 93-134, [doi:10.1016/B978-0-12-800137-0.00003-0](http://dx.doi.org/10.1016/B978-0-12-800137-0.00003-0)

### Terrestrial Radiocarbon Database
- Only reference and information I have is this: Trumbore, S., M. Torn, L. Smith. 2011. Constructing a Database of Terrestrial Radiocarbon Measurements. Terrestrial Radiocarbon Database Workshop, Berkeley, California, 20–22 July 2011. Eos 92(43):376, 25 October 2011, [doi:10.1029/2011EO430006](http://dx.doi.org/10.1029/2011EO430006)
- Probably linked to the ICSN project? Has some of the same people and groups.
- Don't know its current status. Margaret Torn was listed as the contact person in Eos article
