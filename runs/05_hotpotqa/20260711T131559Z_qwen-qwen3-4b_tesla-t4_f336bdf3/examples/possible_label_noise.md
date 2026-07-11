# Possible Label Noise

## ex_05238_5ae143ed55429920d5234360

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9999034404754639`
- Workspace noise score: `1.2567686262540518`
- Quadrant: ``

Question:
```text
In what year was the university where Sergei Aleksandrovich Tokarev was a professor founded?
```
Prediction:
```text
1724. The university is Saint Petersburg State University. Wait, but
```
Aliases:
```text
['1755']
```
Judge reason:
```text
The accepted answer is 1755, but the model answer is 1724. The model also provides a possible alias (Saint Petersburg State University), which may be incorrect or outdated. The founding year of Saint Petersburg State University is generally considered to be 1724, but the accepted answer of 1755 may refer to a different institution or a different historical context. This creates ambiguity due to potential historical disputes or changes in institutional naming.
```
Late workspace top-1 trajectory:
```text
  L27:莫斯科 | L28:莫斯科 | L29:莫斯科 | L30:俄罗斯 | L31:莫斯科
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.367: ['莫斯科', '康熙', '俄罗斯', ' Moscow', '清朝']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.006: ['1', '7', '8', '2', '9']
```


## ex_00839_5ae80919554299540e5a56f6

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.7200888991355896`
- Workspace noise score: `1.7971977025270462`
- Quadrant: ``

Question:
```text
Isabella Kelly was born at a ruined castle characterized as one of the most isolated fortifications in Britain by who?
```
Prediction:
```text
19th-century historian and archaeologist, John Morris
```
Aliases:
```text
['The Changing Scottish Landscape']
```
Judge reason:
```text
The accepted answer refers to a publication or work title, while the model answer refers to a person. The question asks for the source that characterized the castle, but the model answer provides a person rather than the work or publication. This makes the answer partially correct but not clearly equivalent.
```
Late workspace top-1 trajectory:
```text
  L27: historian | L28: historian | L29: historian | L30: historian | L31: historian
  L32: William | L33: William | L34: William
```
Noisiest late layer top tokens:
```text
L34 entropy=3.108: [' William', ' Robert', ' John', ' Sir', ' Henry']
```
Cleanest late layer top tokens:
```text
L30 entropy=0.224: [' historian', ' historians', ' History', ' Histor', '历史']
```


## ex_05543_5ae361605542994393b9e69b

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.6483321189880371`
- Workspace noise score: `0.503917145729065`
- Quadrant: ``

Question:
```text
The facility where Robert Croft worked as a navy instructor was also known as?
```
Prediction:
```text
19th Naval Training Center. The facility where Robert Croft worked as a
```
Aliases:
```text
['"Home of the Submarine Force"']
```
Judge reason:
```text
The model answer refers to "19th Naval Training Center" which is a specific name for the facility, but the accepted answer is a descriptive alias "Home of the Submarine Force". While the two may refer to the same facility, the model answer is not semantically equivalent to the accepted answer and lacks completeness.
```
Late workspace top-1 trajectory:
```text
  L27: Navy | L28: Navy | L29: Navy | L30: Naval | L31: Naval
  L32: Naval | L33: Naval | L34: Naval
```
Noisiest late layer top tokens:
```text
L28 entropy=1.210: [' Navy', '训练', ' Naval', ' Training', 'Training']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.296: [' Naval', ' Navy', ' Marine', ' Sea', ' naval']
```


## ex_01805_5adf3e835542993a75d26442

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.5206868052482605`
- Workspace noise score: `0.47551279664039614`
- Quadrant: ``

Question:
```text
Which comic series involves characters such as Nick Fury and Baron von Strucker?
```
Prediction:
```text
1960s Marvel comics
```
Aliases:
```text
['Marvel']
```
Late workspace top-1 trajectory:
```text
  L27:漫画 | L28:漫画 | L29: Marvel | L30: Marvel | L31: Marvel
  L32: Marvel | L33: Marvel | L34: Marvel
```
Noisiest late layer top tokens:
```text
L27 entropy=1.524: ['漫画', ' Comics', ' Marvel', ' comics', 'Comic']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.187: [' Marvel', ' Avengers', ' Spider', ' Wolverine', 'Marvel']
```


## ex_06630_5ab916e155429919ba4e23a4

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.5220816135406494`
- Workspace noise score: `1.6389736771583556`
- Quadrant: ``

Question:
```text
12 Years a Slave starred what British actor born 10 July 1977)
```
Prediction:
```text
12 Years a Slave starred Chiwetel Ejiofor
```
Aliases:
```text
['Chiwetel Ejiofor']
```
Late workspace top-1 trajectory:
```text
  L27:演员 | L28:演员 | L29:演员 | L30:演员 | L31: actor
  L32:played | L33:played | L34: actor
```
Noisiest late layer top tokens:
```text
L33 entropy=2.605: ['played', ' Actor', ' actor', ' actors', '演员']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.615: ['演员', '(actor', '非洲', '饰演', 'Actor']
```


## ex_07121_5a713b325542994082a3e6b5

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `strict_exact`
- Label quality: `high`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.5805788040161133`
- Workspace noise score: `0.7387014180421829`
- Quadrant: ``

Question:
```text
What was the capital of India when the Taj Mahal was commissioned?
```
Prediction:
```text
Agra
```
Aliases:
```text
['Agra']
```
Late workspace top-1 trajectory:
```text
  L27: Delhi | L28: Delhi | L29: Delhi | L30: Delhi | L31: Delhi
  L32: Delhi | L33: A | L34: A
```
Noisiest late layer top tokens:
```text
L33 entropy=2.486: [' A', '\tA', '*A', ' |\n\n', ' Aur']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.017: [' Delhi', ' Hyderabad', ' Mumbai', '印度', ' Bangalore']
```


## ex_02276_5a7a77425542995eb53be83e

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.41117554903030396`
- Workspace noise score: `2.0747334003448485`
- Quadrant: ``

Question:
```text
Who has released more solo albums, Nick Carter or Brady Seals?
```
Prediction:
```text
1. Nick Carter. 2. Brady Seals. 3. Nick
```
Aliases:
```text
['Brady Seals']
```
Late workspace top-1 trajectory:
```text
  L27:数量 | L28:?</ | L29:?</ | L30:?</ | L31:?</
  L32:1 | L33: Nick | L34: Nick
```
Noisiest late layer top tokens:
```text
L30 entropy=2.704: ['?</', '(None', ':</', '艺人', 'none']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.673: [' Nick', 'Nick', ' nick', '3', '_nick']
```


## ex_01273_5a7153d05542994082a3e7dc

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `strict_exact`
- Label quality: `high`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.7761611938476562`
- Workspace noise score: `0.7701452165842056`
- Quadrant: ``

Question:
```text
Which Istanbul mosque is unique for retaining a Baroque style of architecture, the Bayezid II Mosque or the Nusretiye Mosque?
```
Prediction:
```text
Nusretiye Mosque
```
Aliases:
```text
['Nusretiye Mosque']
```
Late workspace top-1 trajectory:
```text
  L27:	None | L28:?</ | L29:	N | L30: N | L31: N
  L32: N | L33: N | L34: N
```
Noisiest late layer top tokens:
```text
L27 entropy=2.270: ['\tNone', 'None', '?</', '答案', '?\r\n']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.109: [' N', ' Answer', '\tN', ' Bay', 'N']
```


## ex_06254_5a72688c5542997f827839b2

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.8595290780067444`
- Workspace noise score: `0.3057260259985924`
- Quadrant: ``

Question:
```text
The Atik Valide Mosque and Valens Aqueduct are found in what country?
```
Prediction:
```text
Turkey. The Atik Valide Mosque and Valens Aqueduct are located in
```
Aliases:
```text
['Turkey']
```
Late workspace top-1 trajectory:
```text
  L27:土耳其 | L28:土耳其 | L29:土耳其 | L30: Turkey | L31: Turkey
  L32: Turkey | L33: Turkey | L34: Turkey
```
Noisiest late layer top tokens:
```text
L27 entropy=0.962: ['土耳其', 'Turkey', ' Romania', ' Bulgaria', ' Turkey']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.079: [' Turkey', 'Turkey', '土耳其', ' Romania', ' Türkiye']
```


## ex_02940_5a7796e05542992a6e59df0f

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.8776551485061646`
- Workspace noise score: `0.8469390511512757`
- Quadrant: ``

Question:
```text
What country is the theme park served by the Huis Ten Bosch train service themed on?
```
Prediction:
```text
19th century Netherlands. The country is the Netherlands. The answer is the
```
Aliases:
```text
['Netherlands']
```
Late workspace top-1 trajectory:
```text
  L27: Netherlands | L28: Netherlands | L29:荷兰 | L30:荷兰 | L31:荷兰
  L32:荷兰 | L33:荷兰 | L34:荷兰
```
Noisiest late layer top tokens:
```text
L28 entropy=2.423: [' Netherlands', ' Italy', 'Italy', '荷兰', 'Germany']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.533: ['荷兰', ' Netherlands', ' Dutch', ' Holland', ' Belgium']
```

