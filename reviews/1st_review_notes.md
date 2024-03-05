# Revision after first internal review (V1)

Date: 2023-03-05
  
Reviewers:

* SC: Stefano Cucurachi
* CB: Carlos Felipe Rocha Blanco
* LL: Elizabeth Lanphear

## Actions

* [x] changed "WasteAndMaterialFootprint to "T-reX" in manuscript
* [ ] changed "WasteAndMaterialFootprint to "T-reX" in code, documentation, github, etc.
* [ ] re-run the program with the new name
* [ ] re-run the analysis with the new name
* [x] revised the highlights/spotlight points
* [x] revised the abstract
* [ ] added a graphical abstract
* [ ] add a list of abbreviations
* [x] revised the introduction
* [ ] separate the introduction into two sections: background and  short introduction
* [ ] define 'waste/material footprint' in the introduction
* [ ] maybe move the text about Laurenti's method to somewhere earlier
* [ ] move CSI to later in the intro/background ~122 in V1
* [x] revised the methods
* [x] move code detail to supplementary information
* [ ] revised the results
* [ ] revised the discussion
* [ ] revised the conclusion
* [ ] revised the methods flowchart
* [ ] created a sankey diagram for the first results
* [ ]

## Replies to comments from

* list numbering refers to the line number in V1 of the manuscript
* Bold text generally denotes something that needs to be discussed further

### Highlights and Spotlight

* 2 - agree. but there is a word limit
* 6 - ditto
* 9 - changed 'flexible' to 'customisable'

### Abstract

* 21 - changed 'WasteAndMaterialFootprint' to 'T-reX'
* 23 - Sorry Liz for my bad spelling! (I had already changed it after we spoke, this is an older version)
* 26 - Good suggestion, Liz. I've changed the first line of the abstract.
* 31 - ditto.
* 35 - '...quantifies and compares demands and potential environmental impacts, aiding sustainable decision-making' changed to 'T-reX quantifies and compares inventory demands and, thus, potential environmental burdens, aiding sustainable decision-making.'

### Introduction

* 48 - **LL 'Would also be good for the background section' - I don't understand what you mean. Can you clarify?**
* 51 - **TODO** Add a definition of 'waste/material footprint' in the introduction
* 70 - **SC: 'LCIA focuses on the characterization of waste impacts, I'd think. Waste generation does not equate environmental impacts. Be more specific.' - Let's talk about this paragraph again**
* 73 - **The units are from the methods referenced in the previous sentence. We can restructure the paragraph to make it more clear**
* 74 - **SC: 'Why are we back to LCA? Why here? Shift all LCA and LCA/waste content to the same place.' - I thought it was all about LCA**
* 74 - **CB: 'Also keep in mind impacts are also calculated at midpiont. But I think this may not needed at all. Just say once that aggregation into CFs makes finding the waste and material footprints difficult, I think you already did this at the end of 1.1.' - Okay. I'll recheck the paragraph**
* 89 - **SC 'The focus here is on demand and volumes, not impacts. CSI is a midpoint impact assessment method. I don't think our is. We do not characterize impacts.' - I don't mean to say that we do. I'll rephrase the sentence**
* 92 - SC & CB: 'Separate the introduction into two sections: background and short introduction' - okay. I'll do that
* 93 - SC & CB: 'move Laurenti's method to somewhere earlier' - Okay, probably a good idea
* 94 - LL: "MaWaF tool (said like Borat)" - You'll have to demonstrate that for us, Liz. :D
* 95 - LL: 'Can probably remove this' - True.
* 96 - **SC: 'tool or method or package' - the T-reX is a tool with an underlying method? But it is also a python package...**

### Methods

* 164 - ditto
* Table 1 - CB: 'Do we need this?' - Maybe... maybe not... You asked me last meeting if there were any other software papers in this journal my inexaustive search only found Franco's Pycirk paper [(LINK)](https://doi.org/10.1016/j.resconrec.2019.104508). They don't have such a table. I took the inspiration for this table from Bernhard's ActivityBrowser paper, which was published in *SoftwareImpacts* [(LINK)](http://dx.doi.org/10.1016/j.simpa.2019.100012).
* 179 - SC and CB: 'shift code to supplementary' - okay, underway.
