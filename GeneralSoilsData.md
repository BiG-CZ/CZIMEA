# Notes on General Soils Datasets for possible integration by BiGCZ and use in CZIMEA analysis

These notes may be more appropriate in some other BiGCZ repository rather than CZIMEA, but this is a good place to start.

## Data for the US

### CZOData
- As available primarily from CZOCentral WOF
- Data structure is highly variable, but this is a resource that must be assessed. Luquillo CZO would be a great place to start.

### NEON

### LTER

### SSURGO, G-SURGO (?)
- See ModelMyWatershed efforts

### others, specially for soil properties
- eg, this older reference: *Kern, J. 1995, Geographic patterns of soil water-holding capacity in the contiguous United States. Soil Science Society of America Journal 59, 1126-1133*. Can then look up recent studies that cite it in building newer, better, broader US datasets


## Global data

### [ISCN: International Soil Carbon Network, ICSN](http://iscn.fluxdata.org)
- In coordination with BiGCZ goals, it'd be good to try to ingest/map some data from ICSN into ODM2. That'd benefit both CZIMEA and BiGCZ in multiple ways.
- Jennifer (Jen) Harden <82soiljen@gmail.com> is the new lead; Deb Agarwal <DAAgarwal@lbl.gov> is or was a technical data lead. Margaret Torn (no longer the lead) also mentioned Chris Swanston <cswanston@fs.fed.us> as being involved
- "Now in its 3rd generation (12/2015), the ISCN database includes data for over 430,000 individual soil layers from over 71,000 profiles worldwide."
- Somewhat related FLUXNET Data Management paper from Deb (who co-led the development of the FLUXNET database): Agarwal, D. A., Humphrey, M., Beekwilder, N. F., Jackson, K. R., Goode, M. M. and van Ingen, C. (2010), A data-centered collaboration portal to support global carbon-flux analysis. Concurrency Computat.: Pract. Exper., 22(17): 2323–2334. [doi:10.1002/cpe.1600](http://dx.doi.org/10.1002/cpe.1600)
- **ASAP:** Suggest to Anthony and Emma if they can and would like to attend this [pre-AGU ICSN meeting, Sun 12/11](http://iscn.fluxdata.org/2016/10/20/agenda-posted-pre-agu-iscn-hands-meeting/)

### [WoSIS: World Soil Information Service](http://www.isric.org/data/wosis)
- [Recent/initial paper (2016-10), WoSIS: Serving standardised soil profile data for the world](http://www.earth-syst-sci-data-discuss.net/essd-2016-34/), doi:10.5194/essd-2016-34, Manuscript under review for journal Earth Syst. Sci. Data
- Has [working GeoServer instance](http://wfs.isric.org/geoserver/), with OGC (WMS, WFS, etc) access to all the data! I've already tested it successfully with QGIS.

### [WISE30sec](http://www.isric.org/data/isric-wise-derived-soil-property-estimates-30-30-arcsec-global-grid-wise30sec)
- Batjes, N.H. 2016. Harmonized soil property values for broad-scale modelling (WISE30sec) with estimates of global soil carbon stocks. Geoderma 269:61-68, [doi:10.1016/j.geoderma.2016.01.034](http://dx.doi.org/10.1016/j.geoderma.2016.01.034). PDF available [here](https://www.researchgate.net/publication/292605384_Harmonized_soil_property_values_for_broad-scale_modelling_WISE30sec_with_estimates_of_global_soil_carbon_stocks).

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
