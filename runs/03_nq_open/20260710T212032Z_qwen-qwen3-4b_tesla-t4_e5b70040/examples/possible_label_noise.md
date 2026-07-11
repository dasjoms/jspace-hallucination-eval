# Possible Label Noise

## ex_00102_nq-open-102

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9921842217445374`
- Workspace noise score: `1.5889692164957523`
- Quadrant: ``

Question:
```text
who has the most catches in nfl history
```
Prediction:
```text
1,381 catches. (Jerry Rice
```
Aliases:
```text
['Jerry Rice']
```
Late workspace top-1 trajectory:
```text
  L27:总数 | L28:总数 | L29: receptions | L30: receptions | L31: receptions
  L32: catches | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=3.345: [' catches', ' receptions', 'catch', '1', '8']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.060: ['1', '9', '2', '7', '8']
```


## ex_01003_nq-open-1003

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9996181130409241`
- Workspace noise score: `1.441405833605677`
- Quadrant: ``

Question:
```text
when was the last amendment to the constitution passed
```
Prediction:
```text
1992. The 27th Amendment was ratified in 1
```
Aliases:
```text
['May 5, 1992']
```
Judge reason:
```text
The model answer correctly identifies 1992 as the year the 27th Amendment was ratified, which is semantically equivalent to the accepted answer 'May 5, 1992' for the last amendment passed.
```
Late workspace top-1 trajectory:
```text
  L27:宪法 | L28:宪法 | L29:宪法 | L30:修正 | L31: December
  L32: December | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.783: ['1', '修订', ' December', ' Amend', ' ratified']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.006: ['1', '2', ' ratified', '修正', '修订']
```


## ex_00419_nq-open-419

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9986634254455566`
- Workspace noise score: `1.313373503088951`
- Quadrant: ``

Question:
```text
when was harry potter and the philosophers stone published
```
Prediction:
```text
1997. The first Harry Potter book was published on June 2
```
Aliases:
```text
['in 1997', '1997']
```
Late workspace top-1 trajectory:
```text
  L27: Rowling | L28:出版 | L29: Rowling | L30: Hogwarts | L31:1
  L32:1 | L33: November | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.894: [' November', '  \n', ' June', '1', ' July']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.068: ['1', '2', '6', ' June', ' November']
```


## ex_02771_nq-open-2771

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9840013980865479`
- Workspace noise score: `2.1649234533309936`
- Quadrant: ``

Question:
```text
where did the christmas tree at rockefeller center come from
```
Prediction:
```text
1883. The tree was brought from the home of the German immigrant
```
Aliases:
```text
['State College, PA']
```
Judge reason:
```text
The accepted answer 'State College, PA' refers to the origin of the tree's location, while the model answer provides a year and a reason for the tree's origin (from a German immigrant's home). The model answer is partially correct but does not fully align with the accepted answer, leading to ambiguity.
```
Late workspace top-1 trajectory:
```text
  L27:Tree | L28:Tree | L29:传统 | L30: Copenhagen | L31: Germany
  L32: Germany | L33: Germany | L34:1
```
Noisiest late layer top tokens:
```text
L27 entropy=3.237: ['Tree', '树枝', '森林', '装饰', 'TreeNode']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.367: ['1', ' Germany', '2', '4', ' German']
```


## ex_00130_nq-open-130

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9966822862625122`
- Workspace noise score: `2.340066301822662`
- Quadrant: ``

Question:
```text
what percentage of sunlight is captured by plants to convert it into food energy
```
Prediction:
```text
1-6% of sunlight is captured by plants to convert it into food energy
```
Aliases:
```text
['45%', '3 to 6%']
```
Judge reason:
```text
The model answer '1-6% of sunlight is captured by plants to convert it into food energy' is a range that overlaps with the accepted answers '45%' and '3 to 6%'. However, '45%' is not within the range provided by the model answer, and there is ambiguity in the accepted answers due to the presence of both '45%' and '3 to 6%'. The model answer is partially correct but not clearly equivalent to the accepted answers.
```
Late workspace top-1 trajectory:
```text
  L27:太阳能 | L28:效率 | L29:]% | L30:]% | L31:]%
  L32:ranges | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=3.284: ['1', '大约', '0', ' Less', 'ranges']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.635: ['1', '3', '0', '2', ' Less']
```


## ex_02298_nq-open-2298

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9999755620956421`
- Workspace noise score: `0.6056847096000638`
- Quadrant: ``

Question:
```text
when did colour tv come out in uk
```
Prediction:
```text
1969. The BBC began broadcasting in colour in 196
```
Aliases:
```text
['July 1, 1967', '1967/1969/1976', '1967']
```
Judge reason:
```text
The model answer '1969. The BBC began broadcasting in colour in 196' is partially correct but incomplete. The accepted answers include '1967', '1967/1969/1976', and 'July 1, 1967', indicating that colour TV in the UK had a multi-year rollout. The model answer focuses on 1969, which is one of the aliases, but the answer is incomplete and lacks the full context of the multi-year introduction.
```
Late workspace top-1 trajectory:
```text
  L27:BBC | L28:电视 | L29: BBC | L30: BBC | L31:1
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=1.510: ['1', ' November', ' January', ' October', '\u200b']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', '3', '9', '5']
```


## ex_00814_nq-open-814

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.3653838634490967`
- Workspace noise score: `1.91219220161438`
- Quadrant: ``

Question:
```text
what color is the cue ball in pool
```
Prediction:
```text
1. White. 2. Yellow. 3. Red. 4
```
Aliases:
```text
['white']
```
Late workspace top-1 trajectory:
```text
  L27:颜色 | L28:球 | L29:白色 | L30:白色 | L31:黄色
  L32: yellow | L33: yellow | L34: yellow
```
Noisiest late layer top tokens:
```text
L34 entropy=2.686: [' yellow', ' ivory', ' cushion', 'ellow', ' white']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.334: ['颜色', '的颜色', '白色', '-colored', '球']
```


## ex_01839_nq-open-1839

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.7889927625656128`
- Workspace noise score: `2.6442456245422363`
- Quadrant: ``

Question:
```text
premier league players to score 5 goals in one game
```
Prediction:
```text
1. Alan Shearer (2002-03) 2
```
Aliases:
```text
['Alan Shearer', 'Andy Cole', 'Jermain Defoe', 'Sergio Agüero', 'Dimitar Berbatov']
```
Late workspace top-1 trajectory:
```text
  L27:进球 | L28:进球 | L29:英超 | L30:进球 | L31:⚽
  L32: Arsenal | L33: Arsenal | L34:1
```
Noisiest late layer top tokens:
```text
L30 entropy=3.158: ['进球', '英超', '阿森纳', ' Jamie', '⚽']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.710: ['英超', '进球', '球员', '曼联', ' Tottenham']
```


## ex_03315_nq-open-3315

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.957690417766571`
- Workspace noise score: `1.4644770741462707`
- Quadrant: ``

Question:
```text
what are the five compulsory prayers in islam
```
Prediction:
```text
5 daily prayers: Fajr, Dhuhr, Asr, Mag
```
Aliases:
```text
['Asr', 'Maghrib', 'Isha', 'Zuhr', 'Fajr']
```
Late workspace top-1 trajectory:
```text
  L27: prayers | L28:伊斯兰 | L29: prayers | L30: prayers | L31: prayers
  L32: Salah | L33: prayers | L34:5
```
Noisiest late layer top tokens:
```text
L33 entropy=2.353: [' prayers', ' pray', ' prayer', ' Salah', 'صلاة']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.626: ['5', ' Salah', ' pray', '1', ' prayers']
```


## ex_02859_nq-open-2859

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `strict_exact`
- Label quality: `high`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.4251828193664551`
- Workspace noise score: `1.7442262887954711`
- Quadrant: ``

Question:
```text
the vast interior rural area of australia is known as the
```
Prediction:
```text
Outback
```
Aliases:
```text
['The Outback', 'Outback']
```
Late workspace top-1 trajectory:
```text
  L27:内陆 | L28:内陆 | L29:Australia | L30: Australian | L31: Australia
  L32:Australia | L33: Out | L34: Out
```
Noisiest late layer top tokens:
```text
L27 entropy=2.085: ['内陆', 'Australia', '草原', ' wilderness', ' Australia']
```
Cleanest late layer top tokens:
```text
L29 entropy=1.658: ['Australia', ' Australian', ' Australia', '澳洲', 'Australian']
```

