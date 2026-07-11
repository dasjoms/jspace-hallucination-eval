# Confident Wrong Noisy

## ex_02007_nq-open-2007

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999979734420776`
- Workspace noise score: `1.9896332502365113`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when was the mission san antonio de valero built
```
Prediction:
```text
1687. The mission was founded on June 28
```
Aliases:
```text
['the 18th century', '1718']
```
Judge reason:
```text
The model answer of 1687 is incorrect as the accepted answers state the mission was built in the 18th century (specifically 1718). The model answer provides an incorrect date.
```
Late workspace top-1 trajectory:
```text
  L27:墨西哥 | L28:西班牙 | L29:西班牙 | L30:西班牙 | L31:公元
  L32:七月 | L33: June | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.280: ['公元', '七月', ' Musk', '明', ' Jul']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.828: ['1', ' June', '6', ' Jun', 'June']
```


## ex_03458_nq-open-3458

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999977350234985`
- Workspace noise score: `1.943131662835367`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when was the death penalty reinstated in oregon
```
Prediction:
```text
1978. The death penalty was reinstated in Oregon in 1
```
Aliases:
```text
['1984']
```
Judge reason:
```text
The accepted answer is 1984, but the model answer states 1978, which is clearly a different year and thus incorrect.
```
Late workspace top-1 trajectory:
```text
  L27: Oregon | L28: Oregon | L29: Oregon | L30:Oregon | L31:)((
  L32: December | L33:--> | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=3.612: [' December', '…..', 'December', '‥', '---']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '₁', '2', 'orte', 'oose']
```


## ex_01545_nq-open-1545

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999884366989136`
- Workspace noise score: `1.676313051005127`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when was the drinking age set to 21
```
Prediction:
```text
1984. The drinking age was set to 21 in the
```
Aliases:
```text
['By mid-1988']
```
Judge reason:
```text
The accepted answer indicates 'By mid-1988,' which implies the drinking age was set to 21 in 1988. The model answer of 1984 is historically incorrect as the drinking age was not set to 21 until 1986 in the United States, with full implementation by 1988.
```
Late workspace top-1 trajectory:
```text
  L27:酒精 | L28: legalization | L29:啤酒 | L30:])** | L31:December
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.450: ['December', '__;', ' December', 'AMI', '_Date']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', ' ', ' Essay', 'Answer']
```


## ex_00605_nq-open-605

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.999988317489624`
- Workspace noise score: `1.598079610350726`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when does isle of dogs come out in us
```
Prediction:
```text
2018.07.21. The movie "Isle
```
Aliases:
```text
['April 13, 2018', 'March 23, 2018', 'March\xa023,\xa02018']
```
Judge reason:
```text
The model answer provides a date (July 21, 2018) which is not listed in the accepted answers/aliases. The correct release date of 'Isle of Dogs' in the US was March 23, 2018, not July 21, 2018.
```
Late workspace top-1 trajectory:
```text
  L27:上映 | L28:上映 | L29:上映 | L30:April | L31: April
  L32:2 | L33: May | L34:2
```
Noisiest late layer top tokens:
```text
L30 entropy=2.317: ['April', ' April', ' June', '上映', 'July']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '₂', ' July', '1', ' May']
```


## ex_01177_nq-open-1177

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999769926071167`
- Workspace noise score: `1.9369226817041636`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when did sussex split into east and west
```
Prediction:
```text
1072. The Domesday Book of 1086
```
Aliases:
```text
['1832', '1889']
```
Judge reason:
```text
The model answer refers to 1072 and the Domesday Book, which is unrelated to Sussex splitting into East and West. The accepted answers of 1832 and 1889 refer to the historical division of the county of Sussex into East and West Sussex, which is a well-established fact.
```
Late workspace top-1 trajectory:
```text
  L27:英格兰 | L28:英格兰 | L29: medieval | L30: medieval | L31: medieval
  L32:1 | L33: medieval | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=3.279: [' medieval', ' Angle', ' Created', '1', ' Vikings']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.016: ['1', '5', '9', ' until', '2']
```


## ex_03085_nq-open-3085

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999737739562988`
- Workspace noise score: `2.334090495109558`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when does the turn of the screw take place
```
Prediction:
```text
1894. The story was published in 1894
```
Aliases:
```text
['1898']
```
Judge reason:
```text
The accepted answer is "1898", but the model answer states "1894", which is incorrect. The story "The Turn of the Screw" was published in 1894, but the events of the story are set in 1898.
```
Late workspace top-1 trajectory:
```text
  L27:别墅 | L28:别墅 | L29:少爷 | L30:童年 | L31: gover
  L32:ghost | L33:ghost | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.237: [' gover', '.child', '孩子', ' children', '儿童']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.587: ['1', '2', '3', '4', '6']
```


## ex_00370_nq-open-370

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999526143074036`
- Workspace noise score: `1.6221418442204594`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when was the biltmore house opened to the public
```
Prediction:
```text
1895. The Biltmore House was opened to the public on
```
Aliases:
```text
['March 1930']
```
Judge reason:
```text
The model answer states 1895, which is incorrect. The accepted answer is March 1930, indicating the correct date the Biltmore House was opened to the public.
```
Late workspace top-1 trajectory:
```text
  L27:游客 | L28:游客 | L29:游客 | L30:游客 | L31:开放
  L32:1 | L33: August | L34:1
```
Noisiest late layer top tokens:
```text
L30 entropy=2.977: ['游客', '开放', ' Opens', ' opened', ' visitors']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.013: ['1', '8', ' August', '2', ' ']
```


## ex_03531_nq-open-3531

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `low`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (low)
- First content token prob: `0.9998672604560852`
- Workspace noise score: `1.7417740846285596`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when did god save the queen became the national anthem
```
Prediction:
```text
1959. The song "God Save the Queen" became the national
```
Aliases:
```text
['in the 1780s and 1790s', 'After the Battle of Culloden']
```
Judge reason:
```text
{"verdict":"incorrect","confidence":"high","reason":"The model answer '1959' is incorrect as 'God Save the Queen' has been the national anthem of the United Kingdom since the 18th century, long before 1959. The accepted answers 'in the 1780s and 1790s' and 'After the Battle of Culloden' are historically accurate, while 1959 refers to a different context (e.g., the song's use in the UK Armed Forces)."}}
```
Late workspace top-1 trajectory:
```text
  L27:英格兰 | L28:英国 | L29:英国 | L30:英国 | L31: January
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.538: [' January', ' July', ' June', '这首歌', '英格兰']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', '7', ' July', '3']
```


## ex_01045_nq-open-1045

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.999862551689148`
- Workspace noise score: `1.7626453407108784`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when was the first driver's license required
```
Prediction:
```text
1899. The first driver's license was issued in 18
```
Aliases:
```text
['1888', '1 January 1904']
```
Judge reason:
```text
The model answer '1899. The first driver's license was issued in 18' is clearly incorrect as it contradicts the accepted answers '1888' and '1 January 1904'. The accepted answers indicate that the first driver's license was required in 1888, not 1899.
```
Late workspace top-1 trajectory:
```text
  L27:发明 | L28:驾照 | L29:驾照 | L30: bicycle | L31:plate
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.587: ['plate', '民国', '伦', ' Stockholm', ' Licensed']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.027: ['1', '8', '2', ' August', ' The']
```


## ex_00317_nq-open-317

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.99974524974823`
- Workspace noise score: `1.6170946140831801`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
when does madea's family funeral come out
```
Prediction:
```text
2009.06.12. (June 12
```
Aliases:
```text
['2018']
```
Judge reason:
```text
The accepted answer is '2018', which indicates the release year of 'Madea's Family Funeral'. The model answer '2009.06.12' refers to a different film, 'Madea's Family Reunion', which was released on June 12, 2009. The dates are clearly different entities.
```
Late workspace top-1 trajectory:
```text
  L27:November | L28:上映 | L29: December | L30: December | L31: December
  L32: December | L33: November | L34:2
```
Noisiest late layer top tokens:
```text
L27 entropy=2.693: ['November', 'December', ' December', ' November', ' April']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', ' December', ' February', '1', ' November']
```

