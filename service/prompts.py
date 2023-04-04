from string import Template

INIT_ANALYSIS_TPL = Template('''Summarize this text into less than 5 most important premises with the credibility of each premise in [strong, moderate, weak], and the conclusion. Assess if the argument is sound and valid, and provide less than 5 urls that is related to the topic. Do not make up the urls. Output with json in the following format: 
 {"succeed": true,
  "premises" : [{"id": int, "text": str, "credibility": int}], 
  "conclusion": str, "assessment": str, 
  "related_resources": [{"title": str, "url": str}]}
The json objects need to be parsable and no "," following the last item.
Return {"not_applicable_reason": str} if the text is not suitable for analysis:  
$selected_text''')

ELABORATE_PROMISE_TPL = "Elaborate premise id {premise_id}."
ELABORATE_PROMISE_CREDI_TPL = "Elaborate the credibility of premise id {premise_id}."
ELABORATE_CONCLUSION =  "Elaborate on the conclusion."
ELABORATE_ASSESSMENT = "How did you make the assessment?"
