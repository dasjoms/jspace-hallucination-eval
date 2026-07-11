# Confident Wrong Noisy

## ex_03216_bb-6266

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999998807907104`
- Workspace noise score: `1.6638818308361807`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
In 2015 Japan lowered its voting age from what to what?
```
Prediction:
```text
18 to 16. The answer is 18 to 1
```
Aliases:
```text
['20 to 18', '20 to 18', '20 to 18', '', '']
```
Judge reason:
```text
The model answer '18 to 16. The answer is 18 to 1' is clearly incorrect. The accepted answers indicate that Japan lowered its voting age from 20 to 18 in 2015, not from 18 to 16 or 18 to 1.
```
Late workspace top-1 trajectory:
```text
  L27:投票 | L28:年龄 | L29:投票 | L30:年龄 | L31:投票
  L32:十七 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.948: ['十七', '十八', ' seventeen', '十六', '十七条']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.001: ['1', '2', ' Teen', '¹', ' teen']
```


## ex_03221_bb-6314

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999809265136719`
- Workspace noise score: `1.768061751127243`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Name Adele's record-breaking 2015 album?
```
Prediction:
```text
21. The album "21" by Adele was released in
```
Aliases:
```text
['25', '25', 'twenty-five', '25', 'twenty five', '', '']
```
Judge reason:
```text
The model answer refers to '21', which is Adele's 2011 album, not her 2015 record-breaking album '25'.
```
Late workspace top-1 trajectory:
```text
  L27:专辑 | L28:专辑 | L29:专辑 | L30:伦敦 | L31:专辑
  L32:二十 | L33: twenty | L34:2
```
Noisiest late layer top tokens:
```text
L31 entropy=3.497: ['专辑', '最强', '(**', '诚实', 'Album']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.022: ['2', '3', '1', '\n', ' twenty']
```


## ex_07025_sfq-22127

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.999980628490448`
- Workspace noise score: `1.5979355454444886`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
In which decade of the 17th Century was the new model army created?
```
Prediction:
```text
1640s. The New Model Army was created in 16
```
Aliases:
```text
["40's", '40’s', '40-49', '40s', "40's", '40s', '40 49', '40 s', '', '']
```
Judge reason:
```text
The model answer '1640s' refers to the 1640s decade, which is part of the 17th century. However, the accepted answers are '40's', '40s', etc., which refer to the 1940s, not the 1640s. The question asks for the decade of the 17th century, and '1640s' is not semantically equivalent to the accepted answers, which are aliases for the 1940s.
```
Late workspace top-1 trajectory:
```text
  L27:英格兰 | L28:革命 | L29: Revolutionary | L30: sevent | L31:**

  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.334: ['**\n', ' sevent', ' Crom', ' Cavaliers', 'Mid']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.097: ['1', '6', ' late', ' The', ' Charles']
```


## ex_01084_qb-4163

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999717473983765`
- Workspace noise score: `1.6394716903567315`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What is the second event of a men’s decathlon?
```
Prediction:
```text
100-meter dash. The second event in a men's decathlon is
```
Aliases:
```text
['Long jump', 'Longjumper', 'Running long jump', 'Farthest jumper', 'Long jumping', 'Long-jumping', 'Long jumper', 'Broad jump', 'Long-jumper', 'Longjump', 'Long jump', 'Long jump (sport)', 'Long Jump', 'farthest jumper', 'long jump sport', 'long jumping', 'long jump', 'long jumper', 'longjumper', 'longjump', 'broad jump', 'running long jump', '', '']
```
Judge reason:
```text
The model answer '100-meter dash' is not semantically equivalent to the accepted answers, which all refer to 'Long jump' as the second event in a men's decathlon. The 100-meter dash is the first event, not the second.
```
Late workspace top-1 trajectory:
```text
  L27:athlon | L28: Athletics | L29:跑 | L30: Athletics | L31:跳跃
  L32: Shot | L33: Shot | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=3.084: [' Shot', ' jav', '1', ' Hundred', 'Shot']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.026: ['1', '2', ' Shot', '4', 'shot']
```


## ex_00359_qz-1429

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999152421951294`
- Workspace noise score: `1.9070621252059936`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What is the final event in a decathlon?
```
Prediction:
```text
110m Hurdles. Wait, no. The decathlon has
```
Aliases:
```text
['1500 metres', '1500 metres', '1500 distance', 'one thousand, five hundred  distance', '1500 metres', 'one thousand five hundred distance', '1500 distance', '', '']
```
Judge reason:
```text
The model answer '110m Hurdles' is not the final event in a decathlon. The final event in a decathlon is the 1500 metres, which is explicitly listed in the accepted answers/aliases.
```
Late workspace top-1 trajectory:
```text
  L27:athlon | L28:athlon | L29:马拉松 | L30: Athletics | L31:马拉松
  L32:Long | L33: jav | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.896: [' jav', ' walk', 'shot', '马拉松', ' Walk']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.371: ['1', '2', '4', '5', 'shot']
```


## ex_02600_wh-3689

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9998236298561096`
- Workspace noise score: `2.2117398738861085`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Which movie won the Oscar for Best Film at the 2013 Academy Award ceremony ?
```
Prediction:
```text
12 Years a Slave
```
Aliases:
```text
['ARGO', 'Argo (Film)', 'Argo (disambiguation)', 'Argo (film)', 'Argo Film', 'ARGO', 'argo film', 'argo', 'argo disambiguation', '', '']
```
Judge reason:
```text
The model answer '12 Years a Slave' is not semantically equivalent to the accepted answers, which all refer to 'Argo' as the film that won the Oscar for Best Film at the 2013 Academy Award ceremony. '12 Years a Slave' won the Oscar for Best Picture in 2013, but for a different category and not as the Best Film.
```
Late workspace top-1 trajectory:
```text
  L27:电影 | L28:电影 | L29:《 | L30:《 | L31:《
  L32:《 | L33: Lincoln | L34: Ar
```
Noisiest late layer top tokens:
```text
L32 entropy=2.849: ['《', ' Gravity', '，《', 'Gravity', '新常态']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.056: ['《', '，《', '电影', '导演', ' Winner']
```


## ex_05820_sfq-8111

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.999481737613678`
- Workspace noise score: `1.5864402025938034`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
During which conflict was the battle of Agincourt fought?
```
Prediction:
```text
1016. Wait, no, that's not right. The Battle
```
Aliases:
```text
['Hundred Years War', '100 Years War', '100 years war', "100 Years' War", "Hundred Years' War", "Hundred years' war", 'Hundred year war', 'English Occupation of France', 'One Hundred Years War', 'HYW', 'Hundred Years War', 'Hundred Years Wars', '1oo years war', 'Hundred Years’ War', '100 Year War', "One Hundred Years' War", "The Hundred Years' War", 'Hundred Years war', "116 Years' War", '116 year war', "Houndred Year's War", "100 Year's War", 'HUndred Years War', 'Hundred years war', "Hundred Years' war", 'The Hundred Year War', 'Hundred Year War', "Hundred Sixteen Years' War", 'The Hundred Years War', '116 years war', "The Hundred Year's War", '116 Years War', "Hundred Year's War", 'one hundred years war', 'hundred years wars', '1oo years war', 'hyw', '100 year s war', '116 year war', '100 years war', '100 year war', 'hundred year war', 'hundred sixteen years war', 'hundred years war', 'english occupation of france', 'houndred year s war', 'hundred year s war', '116 years war', '', '']
```
Judge reason:
```text
The model answer '1016' is incorrect as the Battle of Agincourt was fought during the Hundred Years' War, not in the year 1016. The accepted answers all refer to the conflict, not a specific year.
```
Late workspace top-1 trajectory:
```text
  L27:战争 | L28:战争 | L29:法国 | L30:英格兰 | L31:战
  L32: Hundred | L33: Hundred | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.657: ['战', '百年', 'Battle', ' Wars', ' Battle']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.178: ['1', ' English', ' Hundred', ' Battle', ' French']
```


## ex_08117_odql-6918

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9993055462837219`
- Workspace noise score: `1.6439981818199159`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
For which film did Tatum O'Neal receive the Best Supporting Actress 'Oscar'?
```
Prediction:
```text
1975's "A Christmas Story" (1983
```
Aliases:
```text
["'PAPER MOON'", 'A Paper Moon', "It's Only a Paper Moon", "It's Only A Paper Moon", 'It’s Only a Paper Moon', "It's only a paper moon", "'PAPER MOON'", "It's Only a Paper Moon (song)", "It's Only A Paper Moon (song)", 'paper moon', 'it s only paper moon song', 'it s only paper moon', '', '']
```
Judge reason:
```text
The model answer refers to 'A Christmas Story' (1983), but Tatum O'Neal received the Best Supporting Actress Oscar for 'Paper Moon' (1973), not 'A Christmas Story'. The accepted answers all point to 'Paper Moon' as the correct film.
```
Late workspace top-1 trajectory:
```text
  L27:电影 | L28:电影 | L29:《 | L30:《 | L31:)**
  L32:**) | L33:*( | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=3.176: ['**)', ' **', '**', '*(', '*A']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.057: ['《', ' Stranger', '，《', 'Neighbors', 'Dirty']
```


## ex_07532_tb-1935

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9991233944892883`
- Workspace noise score: `2.467831975221634`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Dr. Benjamin Rush gave what expeditionary group mercury laced laxatives which proved to be excellent tracers by which archaeologists have now been able to track their actual route?
```
Prediction:
```text
1768–1769 expedition of the French
```
Aliases:
```text
['Lewis and Clark expedition', 'Lewis and clark', 'The Lewis and Clark Expedition', 'Lewis and Clark Expedition', 'Clark Expedition', 'John Robertson (U.S. Soldier)', "Lewis and Clark's Corps of Discovery", 'The corps of discovery', 'The Corps of Discovery', 'Lewis and Clark expedition', 'Corps of Discovery Expedition', 'Dates to lewis and clarks voyage', 'Lewis & Clark Expedition', "Lewis and Clark's Expedition", 'Silas Goodrich', 'Lewis and Clark', 'Lewis and Clark expedition in 1803', 'Louis and Clark Expidition', 'Lewis & Clark', 'Louis and Clark Expedition', 'John Robertson (U.S. soldier)', 'Hugh McNeal', 'Lewis&Clark', 'louis and clark expidition', 'louis and clark expedition', 'lewis and clark', 'john robertson u s soldier', 'lewis and clark expedition', 'corps of discovery', 'lewis clark expedition', 'dates to lewis and clarks voyage', 'lewis clark', 'corps of discovery expedition', 'lewis and clark s expedition', 'silas goodrich', 'hugh mcneal', 'clark expedition', 'lewis and clark s corps of discovery', 'lewis and clark expedition in 1803', '', '']
```
Judge reason:
```text
The model answer refers to the 1768–1769 expedition of the French, which is not the Lewis and Clark expedition. The accepted answers all refer to the Lewis and Clark Expedition (1803), not a French expedition in the 1760s. The model answer is clearly a different entity and fact.
```
Late workspace top-1 trajectory:
```text
  L27:探险 | L28:探险 | L29:探险 | L30:Colon | L31:Colon
  L32: colonies | L33:Explorer | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=3.612: ['Explorer', ' colonies', ' settlers', '*******\n', ' Franklin']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.232: ['探险', ' settlers', ' travelers', 'Trail', ' Expedition']
```


## ex_02175_dpql-5360

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9986509680747986`
- Workspace noise score: `1.906351900100708`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Which king’s beloved son William was drowned in the tragedy of the White Ship?
```
Prediction:
```text
1066. The answer is the year of the event, not the
```
Aliases:
```text
['Henry I', 'Enrique I', 'Henry the 1st', 'Enrico I', 'Henry I', 'Henry the First', 'Hendrik I', 'Henry the first', 'Henry 1', 'Henry I (disambiguation)', 'King Henry I', 'Henri I', 'enrico i', 'hendrik i', 'henry first', 'henry i disambiguation', 'henri i', 'henry i', 'henry 1', 'enrique i', 'henry 1st', 'king henry i', '', '']
```
Judge reason:
```text
The model answer refers to the year 1066, which is the year of the Norman Conquest, not the king whose son was drowned in the White Ship tragedy. The correct answer is King Henry I.
```
Late workspace top-1 trajectory:
```text
  L27:英格兰 | L28:英格兰 | L29:唐朝 | L30:Norm | L31:Edward
  L32: William | L33: William | L34:1
```
Noisiest late layer top tokens:
```text
L30 entropy=2.940: ['Norm', 'William', 'Henry', '北宋', 'Edward']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.526: ['英格兰', '唐代', '唐朝', '爱尔兰', '国王']
```

