# T-reX publication revision --- Response to reviewers

Author: S.C. McDowall

Date: 2024-11-27

-----------

Dear reviewers, editor,

We would like to thank you for the time and attention that you have contributed to the review of our T-reX manuscript. We are especially grateful for the extensive and constructive commentary. We have addressed each of your comments in the following text, and have made the necessary changes to the manuscript. We hope that you find the revised manuscript to be satisfactory.

---

## 1.  Reviewer One

*“I think that this manuscript needs to be ameliorated.”*

### Summary of review

 - More detail for case study requested, also sensitivity/uncertainty analysis

        - Comment 1.1: system boundary
        - Comment 1.2: input-output data
        - Comment 1.3: material footprint data (more discussion, and ‘overall material footprint’)
        - Comment 1.4: sensitivity analysis or uncertainty analysis

### Author responses

#### General response
As the reviewer points out, the case study could, indeed, benefit from more detail. Additional explanation has been added to the main text and there is detailled discussion in the supplementary information (especially appendices 3 and 4). Furthermore, the complete datasets are publicly available on Github and Zenodo. The case study was included only to demonstrate some potential use cases of T-reX and not to provide a comprehensive waste and material footprint analysis of the Li-ion battery market. This is detailled in the abstract, as well as subsection 2.2 of the methods and 3.2 of the results. The case study is not intended to be intensive or exhaustive and the results are not intended to be used for decision-making purposes. The authors intent is for the focus of the paper to be on the T-reX program itself.

#### Specific responses

##### Reviewer comment 1.1 - Case study system boundary

"*The system boundary of the case study should define, and it can be shown more clearly by adding diagrams.*"

##### Author response 1.1 - Case study system boundary

A figure could be added to the supplementary information to illustrate the system boundary of the case study. However, given the limitations on space, and that the authors feel it would not add any perteniant information. The system boundary is very simple, as defined in the text (methodology section 2.2). That is, exactly the inventory of the Li-ion battery markets as modelled in ecoinvent version 3.9.1. Essentially, a single market activity for each battery, to serve as a basic example.

##### Reviewer comment 1.2 - Input-output data

"*No input-output table provided for the case studies. Please provide this inventory data in the manuscript.”*

##### Author response 1.2 - Input-output data

As described in the methodology section (subsection 2.2), the inventory data is taken directly from the respective activities in the ecoinvent database (version 3.9.1). The input-output data used in the case study is directly that given by the ecoinvent database, without amendment. Full details are provided in the supplementary information of this manuscript (appendix 3 and 6) and complete data is available in the [Github](https://github.com/Stew-McD/T-reX_Publication) and [Zenodo](https://zenodo.org/records/10925359) repositories.

##### Reviewer comment 1.3 - Material footprint data

*“Result and Discussion section; this study was present some part of material footprint. I recommend further discussions and interpretation the result. In addition, it is necessary to present the overall material footprint of battery.”*

##### Author Response 1.3 - Material footprint data

As is mentioned throughout the manuscript, the material footprint results calculated by T-reX are aggregations of the exchanges in the model system that are targeted by the user’s search criteria (in this case, a default selection of 59 materials and their flows as presented by the ecoinvent database and listed in appendix 3, sub section 2 and 3). The authors believe that it would be misleading to present the reader with a ‘total material footprint’ based on the sum of the material footprints of the individual materials, as the LCA models only represent certain aspects of the system. A ‘total material footprint’ without respect for the nature of the material is meaningless, and indeed, one of the strengths of T-reX is to allow the user to pinpoint the materials of interest to them.

##### Reviewer comment 1.4 - Sensitivity analysis and uncertainty analysis

*“Authors should also perform the sensitivity analysis or uncertainty analysis.”*

#### Author response 1.4 - Sensitivity analysis and uncertainty analysis

Indeed, this is something that also could be done, and may yet make and interesting extension for the next study. However, given that the data for the batteries in this case study is taken directly from the ecoinvent activities and offered as a rudimentary example of the programme’s utility, the authors believe that a sensitivity or uncertainty analysis on the case study results is not called for. The authors believe that the presentation of this could be distracting from the message of the paper. For clarity, however, the authors have added further to the discussion on the limitations of the case study results (paragraphs 4-6 and subsection 4) to make this more apparent to the reader.

-------

## Reviewer Two

*“The manuscript is well-written and presents a clear argument. I had a few minor suggestions.”*

### 2. Reviewer Two

#### Summary of this review

        - Expand comparison with existing methods
        - Simplify some of the language
        - Expand on the future developments and applications of T-reX
        - Include higher resolution version of graphical abstract

#### Specific responses

##### Reviewer comment 2.1 - To expand on the comparison with existing methods

*“To clearly communicate the novelty of this work, the author may consider emphasizing explicit Comparison with Existing Methods. Although section 3 has comparisons, it’s hard to tell the differences between T-rex with the existing LCIA methods (i.e CO2 emissions/waste). Providing a detailed comparison of T-reX with existing LCA and LCIA methods will be helpful to justify the novelty.”*

##### Author response 2.1 - To expand on the comparison with existing methods

As the reviewer correctly points out, there are many simalarities between the inventory footprints calculated by T-reX, and that of some exiting LCIA methods. Indeed, the choice of the term 'pseudo-LCIA' is derived from this, because the calculation strategy is very similar to LCIA methods in general. Apart from the added functionality of T-reX, one main difference lies in directness of T-reX aggregations, with comparison to the abstracted methods such as Crustal Scarcity Potential, for example. The authors have expanded the comparison with existing methods by adding more specific details in the relevant sections. In the introduction, this is subsection 1.1 (paragraphs 3-5) and 1.2.1 (paragraph 3). In the methodology, this is 2.1.2, paragraphs 6-7 and section 3.3.2 paragraph 3. In the results section, this is subsection 3.2.5 and 3.2.6. In the discussion, this is first two paragraphs (lines 389 - 411). Additionally, appendix 3, section 3.3.2, paragraph 3 and 4 cover this in more detail and some of this material has been brought forward to the methods section for more prominance (subsection 2.1.2 paragraph 7-8).

##### Reviewer comment 2.2 - To simplify some of the language

*"There are sections where the language can be simplified for better clarity without losing technical precision. For example, the abstract succinctly summarizes the study. However, consider adding a sentence on the main findings from the case study to give a complete overview. The phrase ”frantic pursuit of sustainability objectives” in the introduction could be toned down to “dedicated pursuit of sustainability objectives” for a more neutral tone”*

#####  Author response 2.2 - To simplify some of the language

The authors have restructured the abstract to include more reference to the case study (paragraph 3). Additionally, the language in the text has been amended to improve clarity and purvey a more neutral tone, particularly the first sentence of the abstract and the first paragraph of the introduction.

##### Reviewer comment 2.3 - To expand on the future developments and applications of T-reX

*”A discussion on potential future developments and applications of T-reX will be helpful”*

##### Author response 2.3 - To expand on the future developments and applications of T-reX. 

The authors have expanded the discussion on potential future developments and applications of T-reX in the discussion section (paragraphs 4 and 5). The authors hope that this will provide the reader with a better understanding of the potential of T-reX, as well as its limitations and their relation to some of the challenges in our field, most notably, the need for more comprehensive and reliable data on which to build our models.


##### Reviewer comment 2.4 -  The graphical of abstract

*'low resolution figure is hard to read'*

##### Author response 2.4 -  The graphical of abstract

The publication portal rendered the resolution of the graphical abstract in this way. It was an unfortunate oversight from the authors not to correct this in the initial submission. The graphical abstract in is now also available in various formats and resolutions in the portal submission as well in the online material that is available with the software.


## 3. Reviewer Three

*“I think that the paper presents an interesting and novel method to assess waste generation and consumption of material in systems, but some aspects need a more extensive explanation.”*

### Review summary

    * Clarification on the difference between T-reX and LCI
    * Clarification on the terminology ‘pseudo-LCIA’
    * Clarification on the single score calculation of T-reX

### Major comments

#### Reviewer comment 3.1 - Clarification on the difference between T-reX and LCI
            
*“Lines 105-106: I can understand the difference between the T-reX method and the results that one can derive from the LCI analysis (i.e. the list of elementary flows associated with the system under analysis) in the case of waste, because, as you said, T-reX considers also waste flows that are treated, but what about material flows? Why should T-reX results be different from those that one can obtain by the LCI analysis? This point remains unclear to me even after reading the entire paper.”*

#### Author response 3.1 - Clarification on the difference between T-reX and LCI

One significant difference, and a highlight of the method of the T-reX program is how it makes it easy to identify "hotspots" and perform contribution analysis. Furthermore, the strength of T-reX is to make these calculations simple and easily repeatable (in the way that the databases are manipulated, and the footprints calculated as if they were LCIA methods). The as described in the response to reviewer two, the relevant sections have been refined with the aim of more clearly communicating these differences.

#### Reviewer comment 3.2 - Clarification/replacement of the terminology ‘pseudo-LCIA’

*“Line 213: I think that T-reX is a method to perform the interpretation of the LCI results, it does not evaluate impacts; as it is correctly reported in lines 409-410, T-reX method calculates waste and material inventory footprints, so the terminology”pseudo-LCIA” is in my opinion misleading (even if there is the “pseudo”) and it should be replaced with e.g. “LCI interpretation” method.”*

#### Author response 3.2 - Clarification/replacement of the terminology ‘pseudo-LCIA’

Following from the response to the previous comment, the authors agree that the distinction between LCI and LCIA is critical and the text has been refined so as to make this more explicit. The choice of the term ‘pseudo-LCIA method’ derives from the fact that the T-reX methods are integrated into the code in the same way as LCIA methods. This structure allows for a more user-friendly calculation of these LCI results, being customisable and easy to implement in existing frameworks. The authors have rephrased the relevant sections of the text to make this distinction more clear to the reader.

### Reviewer comment 3.1.3 - Clarification on the single score calculation of T-reX

*“Line 300: please say how the single score is calculated for T-reX evaluation. Results section: as in a standard LCA, the results should be reported before starting with their interpretation, so please consider adding here for the analysed systems some of the results in absolute terms. This will really help the reader to understand the type of output that can be achieved with T-reX method.”*

#### Response 3.1.3 - Clarification on the single score calculation of T-reX

As the reviewer correctly points out, the phrase "single score" is not clear, and could mislead the reader. T-reX gives a "single score" only in the sense of calculating an aggregate of the particular waste or material streams associated with the production of a given functional unit (in the case study, one kg. of various batteries). The language in subsection 2.2.1 ‘LCA calculations’ was amended to more explicitly convey this point, and further, to better explain the results presented in the case study (lines X-Y). The phrase “single score”, was replaced with total summation which the authors believe conveys a more specific and appropriate description of the waste and material inventory results. The sentence now reads *"For each combination of activity, method, and database, a total summation was calculated along with details of the top contributing processes."*

### Minor comments

##### Reviewer comment: 
“In general, when you refer to the SM section 6, please indicate also the sub-section.”

##### Author response: 
This has been corrected in the revised manuscript

##### Reviewer comment: 
“In general, try to avoid putting words in ’’ and use this only when it is strictly necessary (e.g. line 433: why did you write ‘circular economy’ and not simply circular economy?)”

##### Author response: 
This has been corrected in several places in the revised manuscript.

##### Reviewer comment:
“Line 128: what do you mean with ”generic waste processing models”? e.g. models that do not take into consideration the type of waste? Usually, databases include different treatment processes for the different types of waste, so please explain what you mean.”

##### Author response:
This sentence has been rephrased in the revised manuscript (line X).

##### Reviewer comment:
“Line 227:”the waste categories include incineration, recycling”: do you mean “the waste categories include waste sent to incineration, recycling”?“

##### Author response: 
Yes, that was the intended meaning. This has been corrected in the revised manuscript (line X).

##### Reviewer comment:
“Lines 230-231:”a characterisation factor of -1 is applied to the waste footprint methods”: what do you mean? Usually, a CF is given to a flow.”

##### Author response: 
This sentence has been removed. Being somewhat technical, it has not a general relevence, and could be confusing, perhaps. The previous phrasing stems from the way that methods are constructed in the brightway code, where the characterisation factor is embedded in the method as a parameter. This is then applied to the relevant flow in the LCIA, as you correctly point out. The -1 corrects the perspective to be that of waste produced and not on the treatment services (as in “Waste is not a service”, Guinee 2021).

##### Reviewer comment: 
“Line 231: please explain the acronym CCS”

##### Author response:
Yes. Thank you for pointing out the oversight. The expanded form of CCS has been moved to the first mention of carbon capture and storage in the text and the acronym has been added to the list of abbreviations.

##### Reviewer comment:
“Table 4 of the SM: there is sand but not gravel: why?”

##### Author response:
There is no reason that gravel could not be included, the user of T-reX can decide on the material and waste streams of interest to them. The list of materials included in the default configuration of T-reX is based on the list of critical raw materials and then expanded to include other materials commonly deemed strategic or important. Some were added solely based on the interest of the authors (thus, sand and not gravel). The list is not supposed to be exhaustive or comprehensive and can be expanded or condensed by the user at their will. Instructions for configuration are included in the documentation of the software in its Github repository. 

##### Reviewer comment:
“Li ne 247: which are the methods are you referring to?”

##### Author response:
This paragraph has been changed to make a more specific reference to the existing LCA methods (such as the Crustal Scarcity Indicator) that are described initially in the introduction (lines X-Y). The textual connection was lost due to restructuring.

##### Reviewer comment:
“Lines 251-253: T-reX does not calculate impacts, so what do you mean with ”including non-direct impacts on the market such as co-production of other materials”?“

##### Author response:        
The word “impacts” has been replaced with “effects” to avoid confusion (line X).

##### Reviewer comment:
“Lines 255-257: are you referring to the cases where the mining of one material is done together with the extraction of another material? Please say more explicitly the situations are you referring to.”

##### Reviewer comment:
“Lines 258-260: where exactly can the reader see this aspect in sub-section 3.2?”

##### Author response:
This paragraph has been revised to improve clarity and specificity (lines X-Y). As the reviewer suggests, co-production is one example of such a situation. It was previously intended to include a more detailed exploration of this through the example of nickle metal production, however, due to space constraints, this data will not be in the main section of the manuscript, but will be in the supplementary material.  


##### Reviewer comment:
“Line 260 and line 382: ”substitution”: substitution of what?“

##### Author response:
This has been clarified in the text to be more explicit. The term “substitution” here refers to the subtraction of co-products from the system in question (those which are not the functional unit) using the standard LCA methodology.
    
##### Reviewer comment:
“Lines 289 and 290: LT stays for what?”

##### Author response:
“LT” stands for “long term”. The abbreviation has been replaced by the complete word in the lines X and Y.

##### Reviewer comment:
“Line 303-305: this sentence is not clear to me. Please consider rephrasing it.”

##### Author response:
Indeed, the reference to the graph traversal algorithm used in brightway was not clearly explained here. The text has been revised to improve on the description of the calculation methodology (lines X-Y).
    
##### Reviewer comment:
“Lines 322 and 332: the title includes both waste and material but then nothing is said about the material inventory footprint in the sub-section.”
##### Author response:
Yes, only one example was given to illustrate this type of result as the method and the form is identical for both waste and material inventory footprints. This has been made explicit in the text (lines X-Y). The caption now reads ¨Sankey visualisation of flow inventory footprints"

##### Reviewer comment:
“Figure 2: if I consider arrows that enter the cobalt production box, I have 12% + 20% that is more than 22% (cobalt box): why?”

##### Author response:
The Sankey diagram shown in Figure 2 is a greatly abridged and simplified version of that produced by using T-reX with the ActivityBrowser software. The full Sankey diagram is far too large and complex to print. Examples of these diagrams are included in theie full form in the supplementary information (section XX)

##### Reviewer comment:
“Figure 2 caption: here you say that the diagram shows the total solid waste footprint but at the top of the diagram I see the box ”treatment of inert waste, landfill”, so I do not understand how to read the diagram.”

##### Author response:
Figure 2 and its caption have been amended to portray a clearer depiction of the result that the authors are trying to present here. As in the response to the previous comment, the complexity of these flows make it challenging to contain them in a printable figure.

##### Reviewer comment:
“Line 343: what do you mean with ”carbon dioxide waste”? Is it not better to call it “waste from CCS”?“

##### Author response:
As suggested, the text has been revised to replace “carbon dioxide waste” with “carbon dioxide waste from CCS” (lines X,Y,Z).

##### Reviewer comment:
“Figure 3b: CCS instead of CSS?”

##### Author response:
Yes, this typographical error has been corrected in the revised manuscript.

##### Reviewer comment:
“Line 370: I think that ”T-reX Coal (black) demand method” should be replaced with “Coal (black) demand of T-reX method”. The same consideration is valid for the EDIP method (EDIP is the method, “coal no LT” is one of the results of the method).”

##### Author response:
This phrasing has been amended as suggested by the reviewer (lines X, Y, Fig X, Y)

##### Reviewer comment:
“Lines 373 and 374: natural gas is given as example of fossil fuel related methods and zinc for metal demand methods, but natural gas and zinc are just elementary flows and not methods. So please use the correct terminology.”

##### Author response:
The terminology has been corrected (lines X, Y, Z).

##### Reviewer comment:        
“Lines 422-423: how can a waste represent a loss of resources or an environmental risk? Please explain it better, maybe adding some examples.”

##### Author response:
The message here about the importance of knowing the specific nature and context of what is described as a waste flow in the LCA databases is of fundamental importance in the interpretation of the results obtained from T-reX. This paragraph has been revised to better explain this point (lines X-Y).

##### Reviewer comment:
“Lines 436-437: I didn’t understand the second part of this sentence. Please consider rephrasing it.”

##### Author response:
This sentence has been rephrased in the revised manuscript make the database manipulation process more clear to the reader.

##### Reviewer comment:
“Line 443: it does not seem to me that T-reX ”examines their connections so supply chain risks and potential environmental damage”: T-reX gives simply an overview of waste generated and materials consumed.”

##### Author response: 
Agreed. It was intended to convey that T-reX can aid the user in this examination by facilitating the generation of specific inventories. This sentence has been revised to better reflect this (lines X-Y)
