T-reX publication revision

Author: S.C. McDowall

Date: 2024-09-22

Revision requirements checklist

☒ response to reviewers comments

separate document “Response to reviewers”

Point by point, with changes or rebuttals

☐ Updated manuscript source files (latex and vector graphics)

☐ Updated graphical abstract (just cosmetic changes)

Response to reviewers

Dear reviewers, editor,

We would like to thank you for the time and attention that you have contributed to the review of our T-reX manuscript, and we are especially grateful for the extensive and constructive commentary. We have addressed each of your comments in the following text, and have made the necessary changes to the manuscript. We hope that you find the revised manuscript to be satisfactory.

1. Reviewer One

“I think that this manuscript needs to be ameliorated.”

Summary

More detail for case study requested, also sensitivity/uncertainty analysis

Comment 1: system boundary

Comment 2: input-output data

Comment 3: material footprint data (more discussion, and ‘overall material footprint’)

Comment 4: sensitivity analysis or uncertainty analysis

Author responses

As the reviewer points out, the case study could, indeed, benefit from more detail. Additional explanation has been added to the main text (XX) and further data added to the supplementary information (sections X, Y). Furthermore, the complete datasets are publicly available on Github and Zenodo. It is important to note, however, that the case study was included only to demonstrate some potential use cases of T-reX and not to provide a comprehensive waste and material footprint analysis of the Li-ion battery market. The case study is not intended to be intensive or exhaustive and the results are not intended to be used for decision-making purposes. The authors have updated the text to make this more explicit to the reader (in the methodology, results and discussion sections)

Comment 1.1 - Case study system boundary

“The system boundary of the case study should define, and it can be shown more clearly by adding diagrams.”

Response 1.1 - Case study system boundary

A figure could be added to the supplementary information to illustrate the system boundary of the case study. However, given the limitations on space, the authors believe that it would not add any perteniant information. The system boundary is very simple, as defined in the text (methodology section X.X lines Y-Z) as that of the Li-ion battery markets exactly as modelled in ecoinvent version 3.9.1. Essentially, a single market activity for each battery, to serve as a basic example.

Comment 1.2 - Input-output data

“No input-output table provided for the case studies. Please provide this inventory data in the manuscript.”

Response 1.2 - Input-output data

As described in the methodology section (line X-Y), the inventory data is taken directly from the respective activities in the ecoinvent database (version 3.9.1). The input-output data used in the case study is as given by the ecoinvent database without amendment.

Comment 1.3 - Material footprint data

“Result and Discussion section; this study was present some part of material footprint. I recommend further discussions and interpretation the result. In addition, it is necessary to present the overall material footprint of battery.”

Response 1.3 - Material footprint data

The authors have added to the discussion section (line X-Y) to make this context more clear to the reader. As detailled in the lines X-Y and Y-Z of the methodology section, lines X-Y of the results section, and lines X-Y of the discussion section, the material footprint results calculated by T-reX are aggregations of the exchanges in the model system that are targeted by the user’s search criteria (in this case, a default selection of XX materials and their flows as presented by the ecoinvent database). The authors believe that it would be incorrect to present the reader with a ‘total material footprint’ based on the sum of the material footprints of the individual materials, as the LCA models only represent certain aspects of the system. A ‘total material footprint’ without respect for the nature of the material is meaningless, and indeed, one of the strengths of T-reX is to allow the user to pinpoint the materials of interest to them.

Comment 1.4 - Sensitivity analysis and uncertainty analysis

“Authors should also perform the sensitivity analysis or uncertainty analysis.”

Response 1.4 - Sensitivity analysis and uncertainty analysis

Indeed, this is something that could be done, and would be and interesting extension to the study. However, given that the data for the batteries in this case study is taken directly from the ecoinvent activities and offered as a rudimentary example of the programme’s utility, the authors believe that a sensitivity or uncertainty analysis on the case study results is not necessary or relevant. The authors believe that the presentation of this could be distracting from the message of the paper. For clarity, however, the authors have added to the discussion on the limitations of the case study results (line X-Y) to make this more apparent to the reader.

## Reviewer Two

“The manuscript is well-written and presents a clear argument. I had a few minor suggestions.”

2.0 Summary

* Expand comparison with existing methods

* Simplify some of the language

* Expand on the future developments and applications of T-reX

* Resolution of graphical abstract

Author responses

Comment 2.1 - To expand on the comparison with existing methods

“To clearly communicate the novelty of this work, the author may consider emphasizing explicit Comparison with Existing Methods. Although section 3 has comparisons, it’s hard to tell the differences between T-rex with the existing LCIA methods (i.e CO2 emissions/waste). Providing a detailed comparison of T-reX with existing LCA and LCIA methods will be helpful to justify the novelty.”

Response 2.1 - To expand on the comparison with existing methods

As the reviewer correctly points out, there are many simalarities between the footprints calculated by T-reX, and that of some exiting LCIA methods. Indeed, the choice of the term 'pseudo-LCIA' is derived from this. The main difference lies in directness of T-reX aggregations, with comparison to the abstracted methods such as Crustal Scarcity Potential, for example. The authors have expanded the comparison with existing methods by adding more specific details in the relevant sections. In the introduction, this is subsection 1.1 (starting at line 73 on to 1.1.1 and 1.1.2). In the methodology, this is 2.1.2, starting at line 244). In the results section, this is subsection 3.2.5 and 3.2.6. In the discussion, this is first two paragraphs (lines 389 - 411)

Comment 2.2 - To simplify some of the language

“There are sections where the language can be simplified for better clarity without losing technical precision. For example, the abstract succinctly summarizes the study. However, consider adding a sentence on the main findings from the case study to give a complete overview. The phrase ”frantic pursuit of sustainability objectives” in the introduction could be toned down to “dedicated pursuit of sustainability objectives” for a more neutral tone”

Response 2.2 - To simplify some of the language

The authors have restructured the abstract to include reference to the case study results (line X). Additionally, the language in the text has been amended to improve clarity and purvey a more neutral tone, particularly the first sentence of the abstract and the first paragraph of the introduction.

Comment 2.3 - To expand on the future developments and applications of T-reX

”A discussion on potential future developments and applications of T-reX will be helpful”

Response 2.3 - To expand on the future developments and applications of T-reX

The authors have expanded the discussion on potential future developments and applications of T-reX in the discussion section (lines X-Y [second paragraph]). The authors hope that this will provide the reader with a better understanding of the potential of T-reX, as well as its limitations and their relation to some of the challenges in our field, most notably, the need for more comprehensive and reliable data on which to build our models.

Comment 2.4 - Resolution of graphical abstract

“the graphical of abstract (low resolution figure) is hard to read.”

Response 2.4 - Resolution of graphical abstract

The publication portal rendered the resolution of the graphical abstract in this way. It was an oversight from the authors not to correct this. The graphical abstract in is available in its full glory and in various formats on the T-reX documentation website and in the Github repositories. The authors will ensure that the graphical abstract is presented in the final publication as a vector graphic, or in a high resolution raster format.

## Reviewer Three

“I think that the paper presents an interesting and novel method to assess waste generation and consumption of material in systems, but some aspects need a more extensive explanation.”

3.0 Summary

Clarification on the difference between T-reX and LCI

Clarification on the terminology ‘pseudo-LCIA’

Clarification on the single score calculation of T-reX

### Major comments

Comment 3.1.1 - Clarification on the difference between T-reX and LCI

“Lines 105-106: I can understand the difference between the T-reX method and the results that one can derive from the LCI analysis (i.e. the list of elementary flows associated with the system under analysis) in the case of waste, because, as you said, T-reX considers also waste flows that are treated, but what about material flows? Why should T-reX results be different from those that one can obtain by the LCI analysis? This point remains unclear to me even after reading the entire paper.”

Response 3.1.1 - Clarification on the difference between T-reX and LCI

This is an important point. In some cases the sum of the elementary flows will, indeed, match quite closely with the result of the T-reX method. This is especially so when there is a more simple and direct flow from the biosphere extraction to consumption (such as in the black coal example in Fig. 6). Where the LCA models have co-production or recovery of materials, i.e. creation of supply flows inside the technosphere from the consumption of another material, then these will be included in the T-reX footprint score as negative demands. These are distinct from emissions as all exchanges occur within the technosphere. The authors attempt to explain this in the manuscript’s methodology sub-section ‘2.1.1 Functionality and purpose’ (specifically lines 247-260) and in the results subsection ‘3.2.5. Comparison with ‘similar’ LCIA methods’ (specifically lines 374-385).

One significant difference, and a highlight of the method of the T-reX program is how it makes it easy to identify "hotspots" and perform contribution analysis. Furthermore, the strength of T-reX is to make these calculations simple and easily repeatable (in the way that the databases are manipulated, and the footprints calculated as if they were LCIA methods). The relevant sections have been refined with the aim of more clearly communicating these differences.

Comment 3.1.2 - Clarification/replacement of the terminology ‘pseudo-LCIA’

“Line 213: I think that T-reX is a method to perform the interpretation of the LCI results, it does not evaluate impacts; as it is correctly reported in lines 409-410, T-reX method calculates waste and material inventory footprints, so the terminology”pseudo-LCIA” is in my opinion misleading (even if there is the “pseudo”) and it should be replaced with e.g. “LCI interpretation” method.”

Response 3.1.2 - Clarification/replacement of the terminology ‘pseudo-LCIA’

Following from the response to the previous comment, the authors agree that the distinction between LCI and LCIA is critical and the text has been refined so as to make this more explicit (lines X,Y in the methodology, and lines X-Y in the discussion). The choice of the term ‘pseudo-LCIA method’ derives from the fact that the T-reX methods are integrated into the code in the same way as LCIA methods. This structure allows for a more user-friendly calculation of these LCI results, being customisable and easy to implement in existing frameworks. The authors have rephrased the relevant sections of the text to make this distinction more clear to the reader (lines X-Y, X-Y).

Comment 3.1.3 - Clarification on the single score calculation of T-reX

“Line 300: please say how the single score is calculated for T-reX evaluation. Results section: as in a standard LCA, the results should be reported before starting with their interpretation, so please consider adding here for the analysed systems some of the results in absolute terms. This will really help the reader to understand the type of output that can be achieved with T-reX method.”

Response 3.1.3 - Clarification on the single score calculation of T-reX

As the reviewer correctly points out, the phrase "single score" is not clear, and could mislead the reader. T-reX gives a "single score" only in the sense of calculating an aggregate of the particular waste or material streams associated with the production of a given functional unit (in the case study, one kg. of various batteries). The language in subsection 2.2.1 ‘LCA calculations’ was amended to more explicitly convey this point, and further, to better explain the results presented in the case study (lines X-Y). The phrase “single score”, was replaced with “???” which the authors believe conveys a more specific and appropriate description of the waste and material inventory results (line X).

### Minor comments

Comment: “In general, when you refer to the SM section 6, please indicate also the sub-section.”

Responese: This has been corrected in the revised manuscript (line X).

Comment: “In general, try to avoid putting words in ’’ and use this only when it is strictly necessary (e.g. line 433: why did you write ‘circular economy’ and not simply circular economy?)”

Response: This has been corrected in several places in the revised manuscript.

“Line 128: what do you mean with ”generic waste processing models”? e.g. models that do not take into consideration the type of waste? Usually, databases include different treatment processes for the different types of waste, so please explain what you mean.”

This sentence has been rephrased in the revised manuscript (line X).

“Line 227:”the waste categories include incineration, recycling”: do you mean “the waste categories include waste sent to incineration, recycling”?“

Yes, that was the intended meaning. This has been corrected in the revised manuscript (line X).

“Lines 230-231:”a characterisation factor of -1 is applied to the waste footprint methods”: what do you mean? Usually, a CF is given to a flow.”

This sentence has been removed. Being somewhat technical, it has not a general relevence, and could be confusing, perhaps. The previous phrasing stems from the way that methods are constructed in the brightway code, where the characterisation factor is embedded in the method as a parameter. This is then applied to the relevant flow in the LCIA, as you correctly point out. The -1 corrects the perspective to be that of waste produced and not on the treatment services (as in “Waste is not a service”, Guinee 2021).

“Line 231: please explain the acronym CCS”

Yes. Thank you for pointing out the oversight. The expanded form of CCS has been moved to the first mention of carbon capture and storage in the text and the acronym has been added to the list of abbreviations.

“Table 4 of the SM: there is sand but not gravel: why?”

There is no reason that gravel could not be included, the user of T-reX can decide on the material and waste streams of interest to them. The list of materials included in the default configuration of T-reX is based on the list of critical raw materials and then expanded to include other materials commonly deemed strategic or important. Some were added solely based on the interest of the authors (thus, sand and not gravel). The list is not supposed to be exhaustive or comprehensive and can be expanded or condensed by the user at their will. Instructions for configuration are included in the documentation of the software in its Github repository. 

“Line 247: which are the methods are you referring to?”

This paragraph has been changed to make a more specific reference to the existing LCA methods (such as the Crustal Scarcity Indicator) that are described initially in the introduction (lines X-Y). The textual connection was lost due to restructuring.

“Lines 251-253: T-reX does not calculate impacts, so what do you mean with”including non-direct impacts on the market such as co-production of other materials”?“

The word “impacts” has been replaced with “effects” to avoid confusion (line X).

“Lines 255-257: are you referring to the cases where the mining of one material is done together with the extraction of another material? Please say more explicitly the situations are you referring to.”

As you suggest, this is one example of such a situation. This paragraph has been revised to improve clarity and specificity (lines X-Y).

“Lines 258-260: where exactly can the reader see this aspect in sub-section 3.2?”

XXX - THIS IS BECAUSE WE LEFT OUT THE NICKLE EXAMPLE - XXX ooooops

“Line 260 and line 382:”substitution”: substitution of what?“

The term “substitution” here refers to the subtraction of co-products from the system in question (those which are not the functional unit) using the standard methodology prescribed by ISO XXXXX

“Lines 289 and 290: LT stays for what?”

“LT” stands for “long term”. The abbreviation has been replaced by the complete word in the lines X and Y.

“Line 303-305: this sentence is not clear to me. Please consider rephrasing it.”

Indeed, the reference to the graph traversal algorithm used in brightway was not clearly explained here. The text has been revised to improve on the description of the calculation methodology (lines X-Y).

“Lines 322 and 332: the title includes both waste and material but then nothing is said about the material inventory footprint in the sub-section.”

Yes, only one example was given to illustrate this type of result as the method and the form is identical for both waste and material inventory footprints. This has been made explicit in the text (lines X-Y).

“Figure 2: if I consider arrows that enter the cobalt production box, I have 12% + 20% that is more than 22% (cobalt box): why?”

The Sankey diagram shown in Figure 2 is a greatly abridged and simplified version of that produced by using T-reX with the ActivityBrowser software. The full Sankey diagram is far too large and complex to print. Examples of these diagrams are included in there full form in the supplementary information (section XX)

“Figure 2 caption: here you say that the diagram shows the total solid waste footprint but at the top of the diagram I see the box”treatment of inert waste, landfill”, so I do not understand how to read the diagram.”

Figure 2 and its caption have been amended to portray a clearer depiction of the result that the authors are trying to present here. As in the response to the previous comment, the complexity of these flows make it challenging to contain them in a printable figure.

“Line 343: what do you mean with”carbon dioxide waste”? Is it not better to call it “waste from CCS”?“

As suggested, the text has been revised to replace “carbon dioxide waste” with “waste from CCS” (lines X,Y,Z)

“Figure 3b: CCS instead of CSS?”

Yes, this typographical error has been corrected in the revised manuscript.

“Line 370: I think that”T-reX Coal (black) demand method” should be replaced with “Coal (black) demand of T-reX method”. The same consideration is valid for the EDIP method (EDIP is the method, “coal no LT” is one of the results of the method).”

This phrasing has been amended as suggested by the reviewer (lines X, Y, Fig X, Y)

“Lines 373 and 374: natural gas is given as example of fossil fuel related methods and zinc for metal demand methods, but natural gas and zinc are just elementary flows and not methods. So please use the correct terminology.”

The terminology has been corrected (lines X, Y, Z)

“Lines 422-423: how can a waste represent a loss of resources or an environmental risk? Please explain it better, maybe adding some examples.”

The message here about the importance of knowing the specific nature and context of what is described as a waste flow in the LCA databases is of fundamental importance in the interpretation of the results obtained from T-reX. This paragraph has been revised to better explain this point (lines X-Y).

“Lines 436-437: I didn’t understand the second part of this sentence. Please consider rephrasing it.”

This sentence has been rephrased in the revised manuscript make the database manipulation process more clear to the reader.

“Line 443: it does not seem to me that T-reX”examines their connections so supply chain risks and potential environmental damage”: T-reX gives simply an overview of waste generated and materials consumed.”

Agreed. It was intended to convey that T-reX can aid the user in this examination by facilitating the generation of specific inventories. This sentence has been revised to better reflect this (lines X-Y)
