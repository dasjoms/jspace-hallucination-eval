# Confident Wrong Clean Blindspots

## ex_00538_nq-open-538

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999997615814209`
- Workspace noise score: `1.458288522141811`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when did they start assigning social security numbers at birth
```
Prediction:
```text
1936. The Social Security Act was signed into law in 1
```
Aliases:
```text
['1990']
```
Judge reason:
```text
The model answer refers to 1936, which is when the Social Security Act was signed into law, not when social security numbers started being assigned at birth. The accepted answer of 1990 is correct for the specific question about when they started assigning social security numbers at birth.
```
Late workspace top-1 trajectory:
```text
  L27:年开始 | L28:年开始 | L29: January | L30: January | L31:World
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.405: ['World', '1', ' World', ' January', '二战']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' January', '2', '9', '二战']
```


## ex_00532_nq-open-532

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999996423721313`
- Workspace noise score: `0.6782379247204517`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when was the reaper invented by cyrus mccormick
```
Prediction:
```text
1831. The Reaper was invented by Cyrus McCormick in 1
```
Aliases:
```text
['1837', '1834']
```
Judge reason:
```text
The model answer '1831' is not semantically equivalent to the accepted answers '1837' or '1834'. The correct year for the invention of the Reaper by Cyrus McCormick is either 1837 or 1834, making the model answer clearly incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:发明 | L28:发明 | L29:发明 | L30: invention | L31: invention
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=1.834: [' invention', '发明', '1', ' patent', ' Patent']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '8', '2', ' The', '\ufeff\n']
```


## ex_03197_nq-open-3197

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999995231628418`
- Workspace noise score: `1.1806548380271522`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when did the book thief movie come out
```
Prediction:
```text
2012. The book thief movie was released in 201
```
Aliases:
```text
['November 27, 2013', '2013', 'November\xa027,\xa02013']
```
Judge reason:
```text
The model answer states the movie was released in 2012, but the accepted answers clearly state it was released on November 27, 2013. The model answer is factually incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:电影 | L28:电影 | L29:电影 | L30:Release | L31: April
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L30 entropy=2.538: ['Release', '-release', 'February', ' April', ' January']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '₂', '1', '２', '²']
```


## ex_01215_nq-open-1215

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999993443489075`
- Workspace noise score: `1.2904509961605073`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when was the letter j introduced to the alphabet
```
Prediction:
```text
1716. The letter J was introduced to the English alphabet in
```
Aliases:
```text
['in Middle High German', '1524']
```
Judge reason:
```text
The accepted answers indicate the letter J was introduced in Middle High German in 1524, but the model answer states 1716, which is a different year and not semantically equivalent to the accepted answers.
```
Late workspace top-1 trajectory:
```text
  L27:字母 | L28:公元前 | L29:公元前 | L30:公元前 | L31:公元前
  L32:公元 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.769: ['1', ' Letter', ' Letters', 'Letter', '公元前']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.043: ['公元前', '公元', '罗马', ' Roman', '字母']
```


## ex_00560_nq-open-560

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999993443489075`
- Workspace noise score: `1.2507187742565293`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when were birth certificates first issued in the united states
```
Prediction:
```text
1870. The first birth certificates in the United States were issued in
```
Aliases:
```text
['1902', '1900', 'From 1900 to 1946']
```
Judge reason:
```text
The model answer of 1870 is incorrect. The accepted answers include 1900, 1902, and a range from 1900 to 1946, which are all consistent with historical records indicating that birth certificates were first issued in the United States in 1900 or 1902. 1870 is not a correct answer for this question.
```
Late workspace top-1 trajectory:
```text
  L27: Pennsylvania | L28: Pennsylvania | L29: Massachusetts | L30: Massachusetts | L31: Massachusetts
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.788: [' Massachusetts', '(state', ' state', ' states', '状态']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' All', ' July', ' ```\n', '普法']
```


## ex_00335_nq-open-335

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999992847442627`
- Workspace noise score: `1.1969665091950445`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when was the first nuclear power plant opened
```
Prediction:
```text
1951. The first nuclear power plant was opened in 19
```
Aliases:
```text
['December 20, 1951', 'June 27, 1954', 'On June 27, 1954', 'the USSR', 'December 2, 1942']
```
Judge reason:
```text
The model answer is clearly incorrect as it refers to 1951, which is not the correct year for the first nuclear power plant. The accepted answers specify December 20, 1951, which is the correct date for the first nuclear power plant (Obninsk, USSR). The model answer is also incomplete and does not match the accepted aliases.
```
Late workspace top-1 trajectory:
```text
  L27:核电 | L28:核电 | L29:核 | L30:苏联 | L31: reactors
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.797: [' reactors', '电站', ' reactor', ' React', '_dec']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', '0', ' October', 'October']
```


## ex_01766_nq-open-1766

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999992847442627`
- Workspace noise score: `0.7301318951154826`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when was the japanese videogame company nintendo founded
```
Prediction:
```text
1949. The company was founded by Fusajiro Yamajiri
```
Aliases:
```text
['23 September 1889']
```
Judge reason:
```text
The accepted answer states the foundation date as 23 September 1889, which refers to the founding of Nintendo's parent company, Matsuzaka & Company. The model answer states 1949, which is the date when Nintendo Co., Ltd. was founded as a separate entity. These are distinct events and entities, making the model answer incorrect.
```
Late workspace top-1 trajectory:
```text
  L27: Nintendo | L28: Nintendo | L29: Nintendo | L30: Nintendo | L31: December
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.078: [' December', 'January', ' Nintendo', 'December', 'November']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '8', ' December', ' November', ' January']
```


## ex_01295_nq-open-1295

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999985694885254`
- Workspace noise score: `1.3100606970052469`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when was last time bayern munich won champions league
```
Prediction:
```text
2022. The last time Bayern Munich won the Champions League was in
```
Aliases:
```text
['2012–13', '2013', '2000–01']
```
Judge reason:
```text
The model answer '2022' is incorrect because Bayern Munich did not win the Champions League in 2022. The accepted answers are '2012–13', '2013', and '2000–01', which are all correct and historically accurate.
```
Late workspace top-1 trajectory:
```text
  L27: Winners | L28: Bundesliga | L29: Bundesliga | L30: Munich | L31:?</
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L31 entropy=2.594: ['?</', '*</', '()</', ';</', '**:']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '1', ' ```', '3', '₂']
```


## ex_00632_nq-open-632

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999985694885254`
- Workspace noise score: `0.8338179381215014`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
when was the first dark tower book published
```
Prediction:
```text
1987. The first Dark Tower book, "The Dark Tower
```
Aliases:
```text
['1982', '1998']
```
Judge reason:
```text
The accepted answers are '1982' and '1998', but the model answer is '1987', which is not listed as an accepted answer or alias. The first Dark Tower book, 'The Dark Tower', was actually published in 1982.
```
Late workspace top-1 trajectory:
```text
  L27:小说 | L28:小说 | L29:小说 | L30:小说 | L31: October
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.186: [' October', ' November', '小说', 'October', ' December']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', ' November', 'October', ' October']
```


## ex_01919_nq-open-1919

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999974966049194`
- Workspace noise score: `0.5612596961638701`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
where was the last world cup held and who won
```
Prediction:
```text
2022 in Qatar, Argentina. (2022 World Cup
```
Aliases:
```text
['Germany', 'hosted by Brazil', 'won by Germany', 'Estádio do Maracanã']
```
Judge reason:
```text
The model answer refers to the 2022 World Cup in Qatar, which is not the 'last' World Cup. The accepted answers refer to the 2014 World Cup in Brazil, which was the most recent before the 2022 tournament. Additionally, the model answer states that Argentina won, which is incorrect as Germany won the 2014 World Cup.
```
Late workspace top-1 trajectory:
```text
  L27:世界杯 | L28: Argentina | L29: Argentina | L30: Brazil | L31: Brazil
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L29 entropy=1.854: [' Argentina', '阿根廷', ' FIFA', 'Argentina', ' Brazil']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', ' Brazil', ' Russia', '２', ' Chile']
```

