# Revision after second internal review (V2)

Date: 2023-03-15


Reviewers:

* SC: Stefano Cucurachi
* CB: Carlos Felipe Blanco
* LL: Elizabeth Lanphear
* PJ: Pierre Jouannais
* DB: Deborah Bozzato
* KM: Katrina McDowall

## Topics for discussion


### Phrasing

2. Nomenclature 1: Tool, method, package....  *Tool is now embedded as T(ool)-reX, it seems, but it is all three, I think*
3. Nomenclature 2: "pseudo LCIA", "pseudo biosphere"
4. Nomenclature 3: "demand footprint" vs "inventory footprint" etc.

### Introduction

5. How to split up the the introduction into "background and short introduction" (I think I managed that now, we'll see)

### Methods

6. Mathematical basis? 
7. New flowchart. Is it everything you were dreaming of CB?

### Results

8. Premise problem
9. Sankey diagram. Look through Activity Browser, talk about which to choose.

### Discussion


### Supplementary Information

11. Anything else to include?


## Actions taken or planned by SM since V2 review

### General

* [x] changed "WasteAndMaterialFootprint to "T-reX" in manuscript
* [x] changed "WasteAndMaterialFootprint to "T-reX" in code, documentation, github, etc.
* [x] re-run the program with the new name
* [x] re-run the analysis with the new name
* [x] revised the highlights/spotlight points
* [x] revised the abstract
* [ ] make graphical abstract
* [x] add a list of abbreviations

### Introduction

* [ ] add more about Laurenti's method
* [x] revised the introduction
* [x] separate the introduction into two sections: background and short introduction
* [x] define 'waste/material footprint' in the introduction
* [x] move the text about Laurenti's method to somewhere earlier
* [x] move CSI to later in the intro/background ~122 in V1
* [x] add mention of limitations of current approaches in the introduction (regarding the future)
* [x] add explicit mention of EDIP in the intro

### Methods

* [ ] added section of mathematical basis
* [ ] remove word "explode" or explain it better
* [x] revised the methods
* [x] move code detail to supplementary information
* [x] generalised the methods section (more simple)
* [x] revised the methods flowchart (simple workflow)

### Results

* [ ] find problem with premise
* [x] revised the results
* [x] included a sankey from ActivityBrowser
* [ ] coded a better sankey diagram
* [ ] recalculated everything with the new name (will take some days - but same results)

### Discussion

* [x] revised the discussion

### Conclusion

* [x] revised the conclusion

### Supplementary Information

* [x] revised the supplementary information
* [x] compiled the supplementary information pdf
* [ ] final check to see if all correct and complete


## Comments from reviewers

### PJ: General comments

My general comment is that you should highlight more:

- why it is important to assess the flows of waste in themselves, and the flows of materials in themselves (why
not only at the interface Technosphere-biosphere ?) 
- What can this pseudo-LCIA metric be used for? What
does it indicate? I have commented in some paragraphs where you could better highlight this.
- **And above all:**
- why is T-rex better than Laurenti et al (and other approaches)? Because it’s all integrated into a software ? Because the methodology behind is more valid?
- In addition, I think it would really benefit from a little diagram showing a simplified product system and the way
your LCIA pseudo method would calculate the different results. 
- I have attached the type of diagram I had in
mind (done in 27 sec). 
- You could also use it to show how you deal with potential double accountings, for
instance how do you deal with market vs production activities? This would help to really clarify what the metric you assess is and what it can be used for.

#### PJ: suggested diagram

![alt text](PJ_DB/PJ_suggested_diagram.jpg)


## Replies to comments from reviewers

* list numbering refers to the line number in V2 of the manuscript
* Bold text generally denotes something that needs to be discussed further

### Highlights and Spotlight

### Abstract

### Introduction

### Methods

### Results

### Discussion

### Credit statement



## **The following is from the V1 revision**

## Topics for discussion 

1. Everyone okay with the new name "T-reX"? Grrr (or whatever) No one knows what sound they made. In any case it will require a small explanation. Great for a graphical abstract and a funny logo.
2. It would need to be the full name " Tool-reX" in git and pip, of course t-rex is already taken

### Phrasing 
2. Nomenclature 1: Tool, method, package....  *Tool is now embedded as T(ool)-reX, it seems, but it is all three, I think*
3. Nomenclature 2: "pseudo LCIA", "pseudo biosphere"
4. Nomenclature 3: "demand footprint" vs "inventory footprint" etc.

### Introduction
5. How to split up the the introduction into "background and short introduction" (I think I managed that now, we'll see)

### Methods

6. Mathematical basis? I am not convinced that it would add much to interest anyone. But
7. New flowchart. Is it everything you were dreaming of CB?
8. Removal of the 'codey' stuff to SI

### Results

9. Sankey diagram. Look through Activity Browser, talk about which to choose. Then I can make it pretty and write the few sentences about it. Probably I can't write code to batch process all of the results (without disappearing for a few weeks). Also, we have a limit on the number of total figures, so some need to be cut. 

### Discussion

10. "Limitations" - SC wants to hide the flaws :P

### Supplementary Information

11. Anything else to include?



## Actions taken or planned by SM since V1 review

### General

* [x] changed "WasteAndMaterialFootprint to "T-reX" in manuscript
* [x] changed "WasteAndMaterialFootprint to "T-reX" in code, documentation, github, etc. (I've contacted LL to ask her opinion)
* [x] re-run the program with the new name
* [x] re-run the analysis with the new name
* [x] revised the highlights/spotlight points
* [x] revised the abstract
* [x] added a graphical abstract (lol, I'll make a better one if you don't like this one)
* [x] add a list of abbreviations

### Introduction

* [x] revised the introduction
* [x] separate the introduction into two sections: background and short introduction
* [x] define 'waste/material footprint' in the introduction
* [x] maybe move the text about Laurenti's method to somewhere earlier
* [x] move CSI to later in the intro/background ~122 in V1
* [x] add mention of limitations of current approaches in the introduction (regarding the future)
* [x] add explicit mention of EDIP in the intro


### Methods

* [x] revised the methods
* [x] move code detail to supplementary information
* [x] generalised the methods section (more simple)
* [ ] added section of mathematical basis (does this add anything?)
* [x] revised the methods flowchart (simple workflow)

### Results

* [x] revised the results
* [x] included a sankey from ActivityBrowser
* [ ] coded a better sankey diagram
* [ ] recalculated everything with the new name (will take some days - but same results)

### Discussion

* [x] revised the discussion

### Conclusion

* [x] revised the conclusion

### Supplementary Information

* [x] revised the supplementary information
* [x] compiled the supplementary information pdf
* [ ] final check to see if all correct and complete

## Replies to comments from reviewers

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
* 76 - **SC removed "1.2 Material Demand in LCA" - SCM: why remove this and not "Waste in LCA"?**
* 89 - **SC 'The focus here is on demand and volumes, not impacts. CSI is a midpoint impact assessment method. I don't think our is. We do not characterize impacts.' - I don't mean to say that we do. I'll rephrase the sentence**
* 92 - SC & CB: 'Separate the introduction into two sections: background and short introduction' - okay. I'll do that
* 93 - SC & CB: 'move Laurenti's method to somewhere earlier' - Okay, probably a good idea
* 94 - LL: "MaWaF tool (said like Borat)" - You'll have to demonstrate that for us, Liz. :D
* 95 - LL: 'Can probably remove this' - True.
* 96 - **SC: 'tool or method or package' - the T-reX is a tool with an underlying method? But it is also a python package...**

### Methods

* 164 - ditto
* Table 1 - CB: 'Do we need this?' - Maybe... maybe not... You asked me last meeting if there were any other software papers in this journal my inexaustive search only found Franco's Pycirk paper [(LINK)](https://doi.org/10.1016/j.resconrec.2019.104508). They don't have such a table. I took the inspiration for this table from Bernhard's ActivityBrowser paper, which was published in *SoftwareImpacts* [(LINK)](http://dx.doi.org/10.1016/j.simpa.2019.100012).
* 179 - SC and CB: 'shift code to supplementary' - okay, done.
* 180-203 - corrected.
* 205 - SC: 'This should also be mentioned in the introduction. We don't talk about the lack of future in the limitations of current approaches.' SCM: Has been added to the intro
* 318 - CB: 'This awesome functionality needs to be in the Intro, maybe even in the abstract! Making a strong case as to why the forward-looking analysis is useful.' - SCM: ditto


### Results

* 336 - CB: (re: code output in SI) 'Why??? This is the juice! Bring it to the front (and send all that codey Python stuff to the SI instead!)' - SCM: as we discussed in the last meeting, the product of the tool is the manipulated database and the output referred to here is just the print statements from the code. I added some clarification to the text.
* 374 - CB: "Give us a Sankey pleaaaaseeeee" - SCM: Síííííííí. For now, please be satisfied with the ActivityBrowser export, I don't want to get distracted from writing the text at the moment. I'll write the code to make the Sankey diagram while you are considering V2 of the manuscript. As with the other figures, once finalised, I'll go over them again and maximise readibility by tinkering with a vector graphics editor.
* 385 - SC: "do we have a comparison to CSP for a CRM in any of the systems considered in the case study?" - SCM "For EDIP there are a few (Al, Cu, Co, Ni, Zi) . Seen in 'similar_methods.pdf'. We can choose one. But from CSP, the calculation was at the endpoint level, giving units of SiO2 eq. See figure in 'CSP-endpoint.png' and the screenshot of the methods in Activity Browser 'CSP-method_in_AB.png'. Inpenetrable, unentwineable, and uninterpretable, this CSP... 
* 391 - SC "These are really the methods we care about." - SCM: what do you mean? Should I separate or stress it more?

### Discussion

* 422 - SC: "Our contribution improves on the state-of-the-art by..." - SCM: I guess you meant that I start the next paragraph with this. Done. 
* 427 -**SC removed "One main limitation is..." ** SCM: 'hmmmmm...'**
* 430 - **SC: "Additional work on the impact assessment and characterization of waste flows is needed to couple the results of the waste footprint to a suitable impact assessment method." SCM: Additional is an understatement :D**

### Credit statement

* SCM: Everyone okay with it as is? Should we submit with both versions? or only the graphical?
* by the way, the inspiration comes from this ["Nature Index" article from 2021](https://www.nature.com/nature-index/news/researchers-embracing-visual-tools-contribution-matrix-give-fair-credit-authors-scientific-papers), the Latex code I adapted was written by "Dan O'Shea (@djoshea) 2022". I found it [here on Overleaf](https://www.overleaf.com/latex/examples/author-contribution-matrix-heatmap-graphic/fpvnqvjjkcwy). The licence is CCBY-4, so I should maybe reference him, but all I have to go on is a very common Irish name, maybe I can track him down.
* 
