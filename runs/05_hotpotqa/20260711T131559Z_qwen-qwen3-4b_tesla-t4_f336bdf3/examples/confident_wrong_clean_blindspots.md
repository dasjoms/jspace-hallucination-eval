# Confident Wrong Clean Blindspots

## ex_07188_5a9080275542995651fb5175

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
- Workspace noise score: `1.1006383535452187`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What year was the Leeds football club, which Arthur Hydes played, formed? 
```
Prediction:
```text
1871. The Leeds football club was formed in 187
```
Aliases:
```text
['1919']
```
Judge reason:
```text
The accepted answer is 1919, which refers to the formation of Leeds United Football Club. The model answer of 1871 refers to the formation of Leeds Football Club, which is a different entity and not the same as the club associated with Arthur Hydes.
```
Late workspace top-1 trajectory:
```text
  L27: Leeds | L28: Leeds | L29: rugby | L30: Leeds | L31: founded
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.111: [' founded', ' rugby', '\ufeff\n', '俱乐部', '\ufeff']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.005: ['1', '8', '2', '\ufeff\n', ' late']
```


## ex_04811_5a75e16055429976ec32bc6a

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
- Workspace noise score: `1.243482568114996`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Miller County is named after a governor who was born in which year ?
```
Prediction:
```text
1808
```
Aliases:
```text
['1776']
```
Judge reason:
```text
The accepted answer is 1776, which is the birth year of the governor after whom Miller County is named. The model answer of 1808 is incorrect and does not match the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:出生 | L28: born | L29: born | L30: born | L31: birth
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.433: [' birth', ' born', '生于', '出生', 'born']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.024: ['1', '8', ' Miller', '7', '2']
```


## ex_02882_5ab480715542991751b4d798

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
- Workspace noise score: `1.158031053635932`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In which year was this historic diner in Albany, New York built, which also was a filming location for major portions of Ironweed?
```
Prediction:
```text
1937. The diner was built in 1937 and
```
Aliases:
```text
['1941']
```
Judge reason:
```text
The accepted answer is 1941, and the model answer states 1937, which is a different year. The model answer is clearly incorrect based on the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:餐厅 | L28:民国 | L29:始建于 | L30:民国 | L31:?</
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.082: ['?</', '****', '？”', '?”', '?”\n\n']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '9', '2', ' Built', ' built']
```


## ex_02880_5abda2b755429933744ab80f

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999991059303284`
- Workspace noise score: `1.1958122764117434`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Hermann Wilhelm Göring was a veteran fighter pilot in a war that ended in what year?
```
Prediction:
```text
1945. The war ended with Germany's surrender in May 1
```
Aliases:
```text
['1918']
```
Judge reason:
```text
The accepted answer is 1918, which refers to World War I, while the model answer 1945 refers to World War II. Hermann Wilhelm Göring was a veteran fighter pilot in World War II, which ended in 1945.
```
Late workspace top-1 trajectory:
```text
  L27:战争 | L28:战争 | L29: WWII | L30:德国 | L31: WWII
  L32: WWII | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.135: [' WWII', '1', '二战', '战争', '戰']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '二战', '2', ' World', 'ended']
```


## ex_01990_5ab972485542996be20204f6

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999984502792358`
- Workspace noise score: `1.4501727305352687`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
The Reverend Jesse Bushyhead was a member of a Cherokee faction led by a chief born in what year?
```
Prediction:
```text
1795. The Reverend Jesse Bushyhead was a member of
```
Aliases:
```text
['1790']
```
Judge reason:
```text
The accepted answer is 1790, but the model answer is 1795, which is a different year and thus incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:出生 | L28: born | L29: born | L30: birth | L31:？”
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.705: ['？”', ' Birth', 'Birth', ' Cherokee', ' birth']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.049: ['1', '7', '8', ' July', ' Cir']
```


## ex_06473_5ab953a45542996be202047f

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999971389770508`
- Workspace noise score: `0.9995172055438161`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
When was the first stud book created for the breed of horse that came from Rotrou introducing Arabian horses to Perche?
```
Prediction:
```text
1605. The first stud book for the breed was created in
```
Aliases:
```text
['1883']
```
Judge reason:
```text
The accepted answer is 1883, which refers to the creation of the first stud book for the breed of horse that came from Rotrou introducing Arabian horses to Perche. The model answer of 1605 refers to a different event or entity, making it incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:法国 | L28:公元 | L29:南宋 | L30:法国 | L31:公元
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.498: ['公元', '骑士', 'elfth', '北宋', '南宋']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.011: ['1', '8', '7', ' The', '2']
```


## ex_07396_5addb1515542995b365fab60

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999958276748657`
- Workspace noise score: `0.7811908232048154`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In what year was the uprising that marred John P. Buchanan's term as governor ignited?
```
Prediction:
```text
1863. The uprising was the New York City Draft Riots
```
Aliases:
```text
['1891']
```
Judge reason:
```text
The model answer refers to the New York City Draft Riots of 1863, which is a different event from the uprising that marred John P. Buchanan's term as governor. The accepted answer is 1891, which refers to the 1891 New York City Draft Riots, a different event that occurred during Buchanan's term.
```
Late workspace top-1 trajectory:
```text
  L27: riots | L28: riots | L29: riots | L30:起义 | L31:起义
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.433: ['起义', '革命', '])**', ')**', ']**']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.010: ['1', '8', '2', '7', '9']
```


## ex_01215_5ae27f22554299495565da8d

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999905824661255`
- Workspace noise score: `1.244843205343932`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In what year was the mathematician husband of Anneli Cahn Lax born?
```
Prediction:
```text
1908. The mathematician in question is Solomon Lax, and
```
Aliases:
```text
['1926']
```
Judge reason:
```text
The accepted answer is 1926, but the model answer states 1908. Solomon Lax was born in 1926, making the model answer factually incorrect.
```
Late workspace top-1 trajectory:
```text
  L27: born | L28: born | L29: born | L30: born | L31: born
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.107: ['1', ' September', ' August', ' October', '？\n']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.003: ['1', '9', ' September', '2', ' The']
```


## ex_05363_5a79f6825542996c55b2dcb4

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
- Workspace noise score: `0.9224710008595138`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
New Jersey politicians Linda Stender and Leonard Lance were born within a year of each other beginning in which year?
```
Prediction:
```text
1947
```
Aliases:
```text
['1952']
```
Judge reason:
```text
The accepted answer is 1952, and the model answer of 1947 is clearly a different year, making it incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:出生 | L28:出生 | L29:出生 | L30:出生 | L31:born
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.064: ['born', ' Born', 'Born', 'Birth', ' born']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.001: ['1', '2', ' The', ' What', ' year']
```


## ex_00322_5a7c6bcc55429935c91b519c

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999871253967285`
- Workspace noise score: `0.837432649335824`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Rock Springs is a collection of short stories by an author born in what year?
```
Prediction:
```text
1936. The author is John Grisham. Rock Springs is
```
Aliases:
```text
['1944']
```
Judge reason:
```text
The accepted answer is 1944, but the model answer states 1936. John Grisham was born in 1944, not 1936, making the model answer factually incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:出生 | L28: born | L29:出生 | L30: born | L31: born
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.133: [' born', 'born', ' Born', ' birth', '出生']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.002: ['1', '9', '2', '8', ' Rock']
```

