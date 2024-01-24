WasteFootprint: A Python tool in the Brightway2 framework to categorise and quantify waste flows in LCA 

Elizabeth Lanphear1, Stewart Charles McDowall1, Stefano Cucurachi1, and Carlos Felipe Blanco1 

1 Institute of Environmental Sciences (CML), Leiden University, P.O. Box 9518, 2300 RA Leiden, The Netherlands.  

E-mail contact: e.y.lanphear@cml.leidenuniv.nl 

 
As the European Union and other governmental bodies strive to transition toward a circular economy — a concept focused on the prevention of waste and the reuse of resources — appropriate tools to identify and quantify waste flows through supply chains are of critical importance (EC, 2020). Life Cycle Assessment (LCA) is a crucial tool for this, given its capacity to pinpoint hotspots of environmental impact throughout the life cycle of products and services, those where the implementation of circular principles could be most effective. 

In this study, we present a Python-based tool that enables the aggregation of mass and volume for all waste exchanges, and the creation of flexible categories to differentiate between waste types and End-of-Life (EOL) handling using (in this case) the Ecoinvent 3.9 cutoff database.  

This tool provides a method for the calculation of waste footprint impact category results, differentiated by the type of waste handling. Furthermore, the tool facilitates rapid investigation and identification of waste hotspots, enabled by standard contribution analysis and Sankey diagram visualization tools. The authors consider this a crucial step in addressing the deficit of Life Cycle Assessment (LCA) methods that consider waste flows in the evaluation of a product or process’ circular economy potential.  

First, we identified all Ecoinvent technosphere exchanges that produce waste. We then further classified the waste into non-mutually exclusive categories such as its destination (i.e. dumped, incinerated, etc.), hazardousness, and form (solid vs. liquid). After cloning the technosphere exchanges as biosphere exchanges, we aggregated and quantified them, by waste category, into matching impact categories in the Life Cycle Impact Assessment.  

In our simplified test case of six battery types, we were able to identify ‘waste hotspots’ and distinguish the major sources of contribution to waste generation on a process-level. One conspicuous result from the case study (and potential direction for further work) is that many waste flows are tied to processes lacking a clear EOL pathway. Further development of this tool could involve developing an algorithm using identifiers of each background waste process to predict where these uncategorised wastes land in their EOL management. 

 

 

LINK TO FOLDER CONTAINING SUPPORTING FIGURES: 

LL_ISIE_Submission_WasteFootprintTool 

REFERENCES: 

European Commission (EC). (2020). Circular economy action plan: for a cleaner and more 

Competitive Europe. https://eur-lex.europa.eu/legal-content/EN/TXT/?	qid=1583933814386&uri=COM:2020:98:FIN  

 

FOEN (ed.). (2021). Swiss Eco-Factors 2021 according to the Ecological Scarcity Method. Methodological fundamentals and their application in Switzerland. Federal Office for the Environment, Bern. Environmental studies. https://www.bafu.admin.ch/bafu/en/home/topics/economy-consumption/economy-and-consumption-publications/publications-economy-and-consumption/eco-factors-switzerland.html 

Laurenti, R., Demirer Demir, D., & Finnveden, G. (2023). Analyzing the relationship between product waste footprints and environmental damage – A life cycle analysis of 1,400+ products. Science of The Total Environment, 859, 160405. https://doi.org/10.1016/J.SCITOTENV.2022.160405 

Moreno Ruiz, E., et al. (2020). Documentation of changes implemented in ecoinvent database v3. 7 

& v3. 7.1. ecoinvent Association. 

 https://ecoinvent.org/wp-content/uploads/2022/10/ChangeReportv3.9.pdf 

 

Mutel, C. (2017). Brightway: an open source framework for life cycle assessment. Journal of Open 

Source Software, 2(12), 236. DOI: 10.21105/joss.00236 

 

Mutel, C. (2017). Wurst documentation.  

https://buildmedia.readthedocs.org/media/pdf/wurst/stable/wurst.pdf  

 

Reinhard, J. et al. (2019). Contribution-based prioritization of LCI database improvements: the most 	Important unit processes in ecoinvent. Int J Life Cycle Assess. 24, pg. 1778–1792. 

 

 

 