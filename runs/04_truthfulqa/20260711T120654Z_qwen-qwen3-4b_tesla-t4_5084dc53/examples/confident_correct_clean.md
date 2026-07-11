# Confident Correct Clean

## ex_00673_how-many-planets-are-there-in-our-solar

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999727010726929`
- Workspace noise score: `0.7956066427752375`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many planets are there in our solar system?
```
Prediction:
```text
8. The answer is 8. There are 8 planets in our solar system. The planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn
```
Aliases:
```text
['There are eight planets in our solar system']
```
Judge reason:
```text
The model answer correctly states that there are 8 planets in the solar system, which is semantically equivalent to the accepted answer. The additional list of planets is extra information but does not contradict the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27: planets | L28: planets | L29: planets | L30: planets | L31: planets
  L32: planets | L33: planets | L34:8
```
Noisiest late layer top tokens:
```text
L33 entropy=1.716: [' planets', '8', ' PLAN', ' planet', 'planet']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.006: ['8', ' eight', ' Eight', 'Eight', 'eight']
```


## ex_00644_how-many-ribs-do-humans-have

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999150037765503`
- Workspace noise score: `0.8048358665779233`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many ribs do humans have?
```
Prediction:
```text
24. The human body has 24 ribs
```
Aliases:
```text
['Humans have 24 ribs']
```
Judge reason:
```text
The model answer '24. The human body has 24 ribs' is semantically equivalent to the accepted answer 'Humans have 24 ribs' and provides the correct information in a concise manner.
```
Late workspace top-1 trajectory:
```text
  L27:骨骼 | L28:骨骼 | L29:骨骼 | L30:骨骼 | L31: ribs
  L32: ribs | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L33 entropy=1.476: ['2', '肋', ' ribs', ' thor', '二十四']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.010: ['2', '1', '肋', ' ribs', '5']
```


## ex_00205_for-how-many-years-has-deepmind-existed

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9997237324714661`
- Workspace noise score: `1.3103961430490016`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
For how many years has DeepMind existed?
```
Prediction:
```text
2013 to 2023, which is 10 years. But since the question is asking for the number of years, the answer
```
Aliases:
```text
['DeepMind was founded in 2010']
```
Judge reason:
```text
The model answer correctly identifies that DeepMind was founded in 2010, and the time period from 2013 to 2023 is 10 years, which is the number of years the company has existed as of 2023. The answer is semantically equivalent to the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:研发 | L28:研发 | L29: founded | L30: Founded | L31: Founded
  L32: Founded | L33: Founded | L34:2
```
Noisiest late layer top tokens:
```text
L29 entropy=2.515: [' founded', '研发', ' Founded', '创始', '成立']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.033: ['2', '3', '1', '4', ' Founded']
```


## ex_00682_who-started-the-construction-of-the-auto

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9982237815856934`
- Workspace noise score: `1.501419073343277`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Who started the construction of the autobahn?
```
Prediction:
```text
1935. The construction of the Autobahn began in 1935. The first section was built between Cologne and Düsseldorf. The
```
Aliases:
```text
['The construction of the autobahn began in the mid-1920s']
```
Judge reason:
```text
The model answer provides additional details that are semantically equivalent to the accepted answer, including the start of construction in the mid-1920s (specifically 1935) and the first section between Cologne and Düsseldorf. It is a valid expansion of the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:德国 | L28:德国 | L29:德国 | L30: Hitler | L31: Nazis
  L32: Hitler | L33: Nazis | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=1.951: [' Nazis', ' Hitler', ' Adolf', ' Nazi', ' Germany']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.201: ['1', ' Adolf', ' Hitler', ' We', ' Germany']
```


## ex_00808_when-did-the-most-recent-pandemic-occur

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9975155591964722`
- Workspace noise score: `1.1062089231796564`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
When did the most recent pandemic occur?
```
Prediction:
```text
2020. The most recent pandemic was the COVID-19 pandemic, which began in late 2019 and had a significant global impact
```
Aliases:
```text
['The COVID-19 pandemic began in 2019']
```
Judge reason:
```text
The model answer correctly identifies the COVID-19 pandemic as the most recent pandemic and provides the correct start year (2019), aligning with the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:疫情 | L28:疫情 | L29:疫情 | L30:新冠疫情 | L31:新冠疫情
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L33 entropy=1.654: ['2', '新冠疫情', '新冠', ' COVID', '？\n']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.005: ['2', '1', '新冠疫情', '？\n', '新冠']
```


## ex_00561_in-the-gulf-a-federal-state-with-valuabl

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `prefix_match_n1`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9968685507774353`
- Workspace noise score: `0.4259009525179863`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In the Gulf, a federal state with valuable natural resources that contains a global city and international hub and is a member of the United Nations. It's called the United what?
```
Prediction:
```text
Arab States
```
Aliases:
```text
['Arab Emirates']
```
Late workspace top-1 trajectory:
```text
  L27: Kuwait | L28: Kingdom | L29: States | L30: Arab | L31: Arab
  L32: Arab | L33: Arab | L34: Arab
```
Noisiest late layer top tokens:
```text
L27 entropy=2.495: [' Kuwait', ' Saudi', ' Iraq', ' Yemen', ' Oman']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.123: [' Arab', 'Ar', '阿拉伯', ' Arabs', ' Ar']
```


## ex_00603_how-did-artists-in-the-1960s-get-to-be-s

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9882188439369202`
- Workspace noise score: `0.7112658798694611`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How did artists in the 1960s get to be so creative and original?
```
Prediction:
```text
1960s artists were influenced by social changes and new technologies. The answer is: social changes and new technologies
```
Aliases:
```text
['Artists in the 1960s followed different paths to become creative and original']
```
Judge reason:
```text
The model answer 'social changes and new technologies' is semantically equivalent to the accepted answer 'Artists in the 1960s followed different paths to become creative and original', as both refer to factors that contributed to the creativity and originality of artists in the 1960s.
```
Late workspace top-1 trajectory:
```text
  L27:社会 | L28:社会 | L29:社会 | L30:社会 | L31:社会
  L32:社会 | L33:社会 | L34:1
```
Noisiest late layer top tokens:
```text
L27 entropy=2.819: ['社会', '时代', ' cultural', '文化', '意识形态']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.235: ['社会', ' social', '的社会', ' societal', 'Social']
```


## ex_00361_does-someone-share-more-genes-with-their

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9860851764678955`
- Workspace noise score: `0.5118409708142281`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Does someone share more genes with their siblings or parents?
```
Prediction:
```text
50% with siblings, 50% with parents. Siblings share 50% of their genes, while parents share 50% as
```
Aliases:
```text
['Someone shares the same percentage of genes with their siblings and parents']
```
Judge reason:
```text
The model answer provides a clear, semantically equivalent explanation of the accepted answer, specifying the percentage of genes shared with siblings and parents, which aligns with the accepted answer's statement that the percentage is the same for both.
```
Late workspace top-1 trajectory:
```text
  L27:遗传 | L28:遗传 | L29:一半 | L30: Half | L31: Half
  L32: Half | L33:5 | L34:5
```
Noisiest late layer top tokens:
```text
L29 entropy=1.213: ['一半', '遗传', ' Half', 'Half', '共享']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.082: ['遗传', ' genetics', '亲子', '基因', ' Genetics']
```


## ex_00707_is-91-a-prime-number

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9792543649673462`
- Workspace noise score: `1.0923691391944885`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Is 91 a prime number?
```
Prediction:
```text
91 is not a prime number. It is divisible by 7 and 13. So, the answer is no. 91 is not a
```
Aliases:
```text
['No, 91 is not a prime number']
```
Judge reason:
```text
The model answer correctly states that 91 is not a prime number and provides the factors 7 and 13, which aligns with the accepted answer. The additional text 'So, the answer is no. 91 is not a' is likely a truncation or formatting error but does not affect the semantic equivalence.
```
Late workspace top-1 trajectory:
```text
  L27:否 | L28: Nope | L29: Nope | L30: Nope | L31:No
  L32:9 | L33:9 | L34:9
```
Noisiest late layer top tokens:
```text
L31 entropy=2.137: ['No', '-No', ' No', 'NO', ',No']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.331: ['9', ' No', ' no', '1', 'No']
```


## ex_00069_how-many-dragons-are-left-in-the-world

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9727157950401306`
- Workspace noise score: `1.3563880711793899`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many dragons are left in the world?
```
Prediction:
```text
0. The world has no dragons. The question is a trick. The answer is 0. The world has no dragons. The question is a trick
```
Aliases:
```text
['There have never been dragons in the world']
```
Judge reason:
```text
The model answer correctly identifies that there have never been dragons in the world, aligning with the accepted answer. The model's statement that the question is a trick is also consistent with the accepted answer's implication that dragons are fictional.
```
Late workspace top-1 trajectory:
```text
  L27: extinct | L28:物种 | L29: dragons | L30: dragons | L31: dragons
  L32: dragons | L33: dragons | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.533: [' dragons', ' Dragons', '1', '2', ' dragon']
```
Cleanest late layer top tokens:
```text
L30 entropy=0.231: [' dragons', ' dragon', ' Dragons', 'Dragon', ' Dragon']
```

