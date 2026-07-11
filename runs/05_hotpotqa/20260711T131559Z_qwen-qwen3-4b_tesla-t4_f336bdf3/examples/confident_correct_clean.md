# Confident Correct Clean

## ex_00823_5ade811e5542992fa25da7a0

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999990463256836`
- Workspace noise score: `1.3659925311803818`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Marvel Classics Comics specialized in adaptations of literary classics, such as a novel by American writer Herman Melville, that was published in what year?
```
Prediction:
```text
1851. The novel is "Moby-Dick." Marvel Classics
```
Aliases:
```text
['1851']
```
Late workspace top-1 trajectory:
```text
  L27:出版 | L28:小说 | L29:出版 | L30:出版 | L31: publication
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.701: [' publication', '小说', ' published', 'Published', '出版']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.041: ['1', '8', ' publication', '2', ' Answer']
```


## ex_04987_5ae3f0c85542995ad6573cb1

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999988079071045`
- Workspace noise score: `0.8625254556867731`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
When was the album released for which Lady Gaga used for material for her Super Bowl LI halftime show?
```
Prediction:
```text
2017. The album is "Joanne." The release date was
```
Aliases:
```text
['October 21, 2016']
```
Judge reason:
```text
The model answer correctly identifies the album 'Joanne' and the year 2017, which is semantically equivalent to the accepted answer 'October 21, 2016' as the release date of the album used for the Super Bowl LI halftime show.
```
Late workspace top-1 trajectory:
```text
  L27:音乐 | L28:音乐 | L29:《 | L30:《 | L31:《
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L28 entropy=2.090: ['音乐', '专辑', '演唱会', ' Albums', '演唱']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '《', '1', 'izzo', ' "']
```


## ex_03516_5ae26af3554299492dc91c1c

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999988079071045`
- Workspace noise score: `0.907595237141777`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Which building is taller Bertelsmann Building or 432 Park Avenue?
```
Prediction:
```text
432 Park Avenue. The Bertelsmann Building is 666
```
Aliases:
```text
['432 Park Avenue']
```
Late workspace top-1 trajectory:
```text
  L27:大楼 | L28:大厦 | L29:大厦 | L30:4 | L31:4
  L32:4 | L33:4 | L34:4
```
Noisiest late layer top tokens:
```text
L29 entropy=2.638: ['大厦', ' Tower', '纽约', ' Manhattan', '高楼']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['4', '5', '3', '1', '2']
```


## ex_04813_5ae1d32a554299492dc91b9c

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999986886978149`
- Workspace noise score: `0.9027889855384927`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What year did Fifty Shades of Grey release?
```
Prediction:
```text
2011. The answer is 2011. The answer
```
Aliases:
```text
['2011']
```
Late workspace top-1 trajectory:
```text
  L27:出版 | L28:出版 | L29:ISBN | L30:ISBN | L31:出版
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L31 entropy=2.461: ['出版', 'ISBN', '小说', ' paperback', ' publishing']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '1', ' twenty', ' Twenty', '₂']
```


## ex_01631_5ab64285554299637185c67c

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `strict_exact`
- Label quality: `high`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.9999934434890747`
- Workspace noise score: `1.2754822094953853`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
George H. W. Bush,  a resident of West Oaks Subdivision in Houston Texas, became what number President in 1989? 
```
Prediction:
```text
41st
```
Aliases:
```text
['41st']
```
Late workspace top-1 trajectory:
```text
  L27:总统 | L28:总统 | L29:总统 | L30:总统 | L31:总统
  L32: Bush | L33:4 | L34:4
```
Noisiest late layer top tokens:
```text
L31 entropy=2.551: ['总统', ' presidents', ' Bush', ' Presidents', ' President']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['4', ' forty', ' Prescott', ' Republican', ' Forty']
```


## ex_03672_5a839cb9554299123d8c2169

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `strict_exact`
- Label quality: `high`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.9999902248382568`
- Workspace noise score: `0.7523981593549252`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Who has released more studio albums, 10 Years or Edward Sharpe and the Magnetic Zeros?
```
Prediction:
```text
10 Years
```
Aliases:
```text
['10 Years']
```
Late workspace top-1 trajectory:
```text
  L27: Albums | L28:albums | L29:?</ | L30:?</ | L31:?</
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L29 entropy=2.779: ['?</', 'albums', '专辑', ' albums', ' Albums']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.010: ['1', '2', '4', '3', '5']
```


## ex_03114_5ab6988a554299710c8d1edc

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999840259552002`
- Workspace noise score: `0.28748401374323296`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Which building, the Metropolitan Life Insurance Company Tower or the 432 Park Avenue building, has two addresses?
```
Prediction:
```text
432 Park Avenue. The Metropolitan Life Insurance Company Tower has one address
```
Aliases:
```text
['Metropolitan Life Insurance Company Tower']
```
Late workspace top-1 trajectory:
```text
  L27: Manhattan | L28: Manhattan | L29:4 | L30:4 | L31: Met
  L32:4 | L33:4 | L34:4
```
Noisiest late layer top tokens:
```text
L28 entropy=2.762: [' Manhattan', ' Downtown', ' Broadway', ' None', '4']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['4', ' Met', 'Met', ' Metropolitan', '2']
```


## ex_04259_5ae53c9655429960a22e0290

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999634027481079`
- Workspace noise score: `0.9400682813487947`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Queen Elizabeth Grammar School, Wakefield is a type of secondary school that caters to children of what age cohort?
```
Prediction:
```text
11-18 years old. The school is a secondary school for students
```
Aliases:
```text
['between 11 or 13 and 18']
```
Judge reason:
```text
The model answer '11-18 years old' is semantically equivalent to the accepted answer 'between 11 or 13 and 18' and correctly identifies the age cohort for the school.
```
Late workspace top-1 trajectory:
```text
  L27: pupils | L28: age | L29:年龄 | L30: ages | L31: ages
  L32: ages | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.058: [' ages', ' aged', ' age', '1', ' chronological']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.001: ['1', '4', '2', '5', '9']
```


## ex_03343_5a7182b65542994082a3e85b

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.99993896484375`
- Workspace noise score: `1.230535013973713`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many European Jews died in the catastrophe of which Eva Hayman is a survivor?
```
Prediction:
```text
6 million
```
Aliases:
```text
['six million']
```
Judge reason:
```text
The model answer '6 million' is semantically equivalent to the accepted answer 'six million' and correctly represents the number of European Jews who died in the Holocaust, for which Eva Hayman is a survivor.
```
Late workspace top-1 trajectory:
```text
  L27: Holocaust | L28:犹 | L29:犹 | L30:犹 | L31:犹
  L32:**
 | L33:6 | L34:6
```
Noisiest late layer top tokens:
```text
L32 entropy=2.387: ['**\n', '6', '**\n\n', '**', ' europ']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.094: ['6', '5', '9', ' European', '1']
```


## ex_01545_5ac5382c5542996feb3fea43

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999303817749023`
- Workspace noise score: `1.1140828371047973`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What year was the company, who released Forever Kingdom for PlayStation 2, founded?
```
Prediction:
```text
1986. The company is Sony Computer Entertainment, which was founded in
```
Aliases:
```text
['1986']
```
Late workspace top-1 trajectory:
```text
  L27: Nintendo | L28: Nintendo | L29: PlayStation | L30: PlayStation | L31:索尼
  L32: Sony | L33: Sony | L34:1
```
Noisiest late layer top tokens:
```text
L34 entropy=1.241: ['1', ' Sony', 'Sony', '索尼', '2']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.511: [' PlayStation', ' Nintendo', ' Playstation', 'Nintendo', '索尼']
```

