# Confident Wrong Noisy

## ex_00026_5adf37a95542995ec70e8f97

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
- Workspace noise score: `1.8848363497294485`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
The 2011–12 VCU Rams men's basketball team, led by third year head coach Shaka Smart, represented Virginia Commonwealth University which was founded in what year?
```
Prediction:
```text
1834. The Virginia Commonwealth University was founded in 183
```
Aliases:
```text
['1838']
```
Judge reason:
```text
The accepted answer is 1838, but the model answer states 1834, which is historically incorrect. Virginia Commonwealth University was indeed founded in 1838, not 1834.
```
Late workspace top-1 trajectory:
```text
  L27:办学 | L28:办学 | L29:Virginia | L30:Virginia | L31:民国
  L32: ______ | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.088: ['民国', 'Virginia', ' Virginia', '.”', '？”']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.002: ['1', '\n', '\ufeff\n', '8', ' ']
```


## ex_01644_5a773d8955429966f1a36cc4

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999250173568726`
- Workspace noise score: `1.7096542604267597`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What is the first year that the second largest university in Alabama fielded a football team?
```
Prediction:
```text
1912. The second largest university in Alabama is the University of Alabama
```
Aliases:
```text
['1892']
```
Judge reason:
```text
The accepted answer is 1892, but the model answer is 1912. The model answer is clearly a different year, and the statement about the University of Alabama being the second largest in Alabama is factually incorrect. The University of Alabama is the largest, and the second largest is the University of Alabama at Birmingham (UAB), which did not field a football team in 1912.
```
Late workspace top-1 trajectory:
```text
  L27: Alabama | L28:办学 | L29: Alabama | L30: Alabama | L31:民国
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L28 entropy=3.169: ['办学', ' NCAA', ' campus', 'University', ' Alabama']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.029: ['1', '2', '8', '9', ' year']
```


## ex_05448_5adfb992554299603e418391

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9998839497566223`
- Workspace noise score: `1.9847240913659334`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What year was the inventor of Rejuvelac born?
```
Prediction:
```text
1842. The inventor of Rejuvelac, which is a
```
Aliases:
```text
['1909']
```
Judge reason:
```text
The accepted answer is 1909, which is the correct birth year of the inventor of Rejuvelac. The model answer of 1842 is clearly different and incorrect.
```
Late workspace top-1 trajectory:
```text
  L27: born | L28: born | L29:法国 | L30: French | L31: born
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.495: [' born', ' Born', ' Nicolas', ' Georges', ' Jacques']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.026: ['1', '8', '2', '7', ' The']
```


## ex_05266_5ae531695542990ba0bbb1fb

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9997982978820801`
- Workspace noise score: `2.0233756050467493`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
In what year was the coach who led the 2007 South Carolina Gamecocks football team in his third season as USC head coach born?
```
Prediction:
```text
1953. The coach was Steve Spurrier, who was born
```
Aliases:
```text
['1945']
```
Judge reason:
```text
The accepted answer is 1945, but the model answer is 1953. Steve Spurrier was born in 1945, not 1953, making the model answer factually incorrect.
```
Late workspace top-1 trajectory:
```text
  L27: born | L28: born | L29: born | L30: born | L31: September
  L32: December | L33: September | L34:1
```
Noisiest late layer top tokens:
```text
L30 entropy=2.707: [' born', ' December', ' October', ' September', ' August']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.081: ['1', ' September', ' December', ' October', ' November']
```


## ex_01761_5ade27e05542997c77aded7d

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9997288584709167`
- Workspace noise score: `1.96431981366768`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
When was the friends song was released which is taken from the fourth studio album of canadian singer and song writer Justin Bieber?
```
Prediction:
```text
2010
```
Aliases:
```text
['August 17, 2017']
```
Judge reason:
```text
The model answer '2010' is clearly incorrect as it does not match the accepted answer 'August 17, 2017', which is the release date of the song from Justin Bieber's fourth studio album.
```
Late workspace top-1 trajectory:
```text
  L27:专辑 | L28:专辑 | L29: October | L30: October | L31: October
  L32:2 | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L27 entropy=2.654: ['专辑', ' Release', 'Release', '演唱', '发布']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '1', '3', '4', '7']
```


## ex_04618_5a76bbe85542993735360191

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9996209144592285`
- Workspace noise score: `1.8432508707046509`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Which American spy thriller TV series, which was developed by Howard Gordon and Alex Gansa, had a fourth season episode titled "Krieg Nicht Lieb?"
```
Prediction:
```text
24
```
Aliases:
```text
['Homeland']
```
Judge reason:
```text
The model answer '24' refers to a different American spy thriller TV series developed by Howard Gordon and Alex Gansa. '24' is a separate show from 'Homeland', and the episode title 'Krieg Nicht Lieb' is not associated with '24'.
```
Late workspace top-1 trajectory:
```text
  L27:电视剧 | L28: FBI | L29:电视剧 | L30:谍 | L31: Homeland
  L32: Homeland | L33:《 | L34: Homeland
```
Noisiest late layer top tokens:
```text
L28 entropy=2.727: [' FBI', '电视剧', '_DC', '杀手', '白宫']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.840: ['电视剧', '剧中', '电视', '该剧', '犯罪']
```


## ex_00802_5abe2b0155429976d4830a83

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9995214939117432`
- Workspace noise score: `1.6722887948155403`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Max Hoffmann along with Hindenburg and Ludendorff, masterminded the devastating defeat of the Russian armies in a battle fought when ?
```
Prediction:
```text
1916. The Battle of the Somme
```
Aliases:
```text
['26–30 August 1914']
```
Judge reason:
```text
The model answer refers to the Battle of the Somme in 1916, which was a major battle during World War I, but it was not the battle where Max Hoffmann, Hindenburg, and Ludendorff masterminded the defeat of the Russian armies. The accepted answer refers to the Battle of the Frontiers (26–30 August 1914), which was the initial phase of World War I and involved the defeat of the Russian armies.
```
Late workspace top-1 trajectory:
```text
  L27:战争 | L28:俄军 | L29:俄国 | L30:俄国 | L31:战
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.113: ['战', '秋季', '春季', '冬天', ' Winter']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.010: ['1', ' World', ' Battle', ' the', ' The']
```


## ex_03392_5adfd30c55429906c02daa53

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9994000792503357`
- Workspace noise score: `1.9302139461040497`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What movie studio produced The Benchwarmers, which starred Rob Schneider and Napoleon Dynamites lead actor, Jon Heder?
```
Prediction:
```text
20th Century Fox. The Benchwarmers was produced by 20
```
Aliases:
```text
['Revolution Studios']
```
Judge reason:
```text
The accepted answer is "Revolution Studios", which is the correct studio that produced "The Benchwarmers." The model answer "20th Century Fox" is incorrect as it did not produce the film. Additionally, the model answer is incomplete and contains a partial statement that does not align with the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27: Pixar | L28: Pixar | L29: Pixar | L30: Pixar | L31: Pixar
  L32: Paramount | L33: Paramount | L34: Paramount
```
Noisiest late layer top tokens:
```text
L33 entropy=2.546: [' Paramount', ' Universal', 'Universal', ' Columbia', ' Legendary']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.233: [' Pixar', ' Films', '迪士尼', '电影', ' Disney']
```


## ex_01814_5a81a84e5542990a1d231e4e

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9993797540664673`
- Workspace noise score: `1.5971332054585219`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What year was the Argentine singer and actor who both directed and starred in El Tio Disparate born?
```
Prediction:
```text
1947. The Argentine singer and actor who directed and starred in
```
Aliases:
```text
['1942']
```
Judge reason:
```text
The model answer provides an incorrect year (1947) for the birth year of the Argentine singer and actor who directed and starred in 'El Tio Disparate.' The accepted answer is 1942, which is correct based on general knowledge.
```
Late workspace top-1 trajectory:
```text
  L27: born | L28: born | L29: born | L30: born | L31: born
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.559: ['1', ' September', ' October', ' November', ' August']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.024: ['1', '2', '9', ' October', '4']
```


## ex_06246_5ae157ed5542990adbacf75d

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9992762207984924`
- Workspace noise score: `2.4639221627265213`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
When was the English writer and screenwriter,died who was creator and writer of "Are You Being Served?" with David Croft?
```
Prediction:
```text
1995
```
Aliases:
```text
['23 December 2014']
```
Judge reason:
```text
The model answer '1995' is incorrect as it refers to the year of the show's creation, not the death date of the writer. The accepted answer '23 December 2014' is the correct death date of the writer, which is semantically equivalent to the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:编剧 | L28:BBC | L29: Nigel | L30:BBC | L31: Nigel
  L32: Julian | L33: Ronnie | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=3.334: [' Julian', '1', ' Tony', ' Nigel', ' Alan']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.020: ['1', '2', ' Roy', '7', ' Tony']
```

