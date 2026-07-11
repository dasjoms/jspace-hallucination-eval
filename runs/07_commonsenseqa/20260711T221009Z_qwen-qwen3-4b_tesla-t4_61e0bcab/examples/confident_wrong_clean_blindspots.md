# Confident Wrong Clean Blindspots

## ex_00450_2ac72eaf30a633c410b1bd658bbef0ba

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9856018424034119`
- Workspace noise score: `1.1400508910417557`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Where do cars usually travel at very high speeds?
```
Prediction:
```text
A
```
Aliases:
```text
['race track']
```
Judge reason:
```text
The model answer 'A' is not semantically equivalent to the accepted answer 'race track' and does not provide a valid answer to the question about where cars usually travel at very high speeds.
```
Late workspace top-1 trajectory:
```text
  L27:Option | L28:选项 | L29:选项 | L30:选项 | L31:	A
  L32: A | L33: A | L34: A
```
Noisiest late layer top tokens:
```text
L30 entropy=2.382: ['选项', 'Option', '\tA', 'Choices', ' OPTION']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.091: [' A', ' C', ' \\', ' The', '选项']
```


## ex_00197_b63e5cd88bfe75d29ff9fdc6dd97fed6

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.984957218170166`
- Workspace noise score: `0.9521945379674435`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What do airplanes do as they are arriving at the gate?
```
Prediction:
```text
D) land
```
Aliases:
```text
['slow down']
```
Judge reason:
```text
The accepted answer is 'slow down', which refers to the action of reducing speed as an airplane approaches the gate. 'Land' refers to the action of touching down on the runway, which is a different stage in the process. Therefore, the model answer is not semantically equivalent to the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29::E | L30::E | L31: D
  L32: Answer | L33: D | L34: D
```
Noisiest late layer top tokens:
```text
L28 entropy=3.063: ['答案', 'Answer', '\tD', '选项', '\tDD']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.036: [' D', '\tD', ' Answer', 'D', ' E']
```


## ex_01016_7ae17f5aecacf18c94a47cc48deb6c36

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.983234703540802`
- Workspace noise score: `1.438040305674076`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
If you were looking for a blowfish, you wouldn't look on dry land, you'd look in a what?
```
Prediction:
```text
C
```
Aliases:
```text
['body of water']
```
Judge reason:
```text
The model answer 'C' is not semantically equivalent to the accepted answer 'body of water' and does not provide a valid answer to the question. The correct answer is a specific type of body of water, not the letter 'C'.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29:答案 | L30:getOption | L31:WHERE
  L32: C | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L31 entropy=3.392: ['WHERE', '\tC', '\tD', 'Where', '\tCHECK']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.034: [' C', 'C', ' \\', ' A', ' The']
```


## ex_00323_b5baf77d3855935c87f01f5fb2216667

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9822266101837158`
- Workspace noise score: `1.1989694654941558`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
If a person were going to bed, what would be their goal?
```
Prediction:
```text
C
```
Aliases:
```text
['falling asleep']
```
Judge reason:
```text
The model answer 'C' is not semantically equivalent to the accepted answer 'falling asleep' and does not provide a meaningful answer to the question about the goal of going to bed.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:选项 | L29:答案 | L30:选项 | L31:选项
  L32: C | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L30 entropy=2.639: ['选项', 'Ｃ', ':E', '选', '\tC']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.055: [' C', '\tC', 'C', '-C', ' D']
```


## ex_00520_18eb6a3b54ccf4989e268cfb9ea90f9c

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9771900177001953`
- Workspace noise score: `1.1231658667325974`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What would friends do if they need each others' help?
```
Prediction:
```text
A
```
Aliases:
```text
['group together']
```
Judge reason:
```text
The model answer 'A' is not semantically equivalent to the accepted answer 'group together' and does not provide a meaningful response to the question.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29:答案 | L30:答案 | L31:	A
  L32: A | L33: A | L34: A
```
Noisiest late layer top tokens:
```text
L31 entropy=2.733: ['\tA', ':A', ' A', '(A', '答案']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.171: [' A', ' According', ' \\', ' The', ' When']
```


## ex_00034_4acd496cc78d96c2431279a5fd87de7c

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9550168514251709`
- Workspace noise score: `0.2950864002108574`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
She was always helping at the senior center, it brought her what?
```
Prediction:
```text
A
```
Aliases:
```text
['happiness']
```
Judge reason:
```text
The model answer 'A' is not semantically equivalent to the accepted answer 'happiness' and does not provide a meaningful or valid response to the question.
```
Late workspace top-1 trajectory:
```text
  L27:情感 | L28: volunteering | L29: volunteering | L30: volunteering | L31: volunteering
  L32: volunteering | L33: volunteering | L34: A
```
Noisiest late layer top tokens:
```text
L27 entropy=2.176: ['情感', ' altru', '满足', '行为', '社会责任']
```
Cleanest late layer top tokens:
```text
L30 entropy=0.086: [' volunteering', ' altru', '志愿服务', ' donating', ' volunteer']
```


## ex_00095_5169f7ae0781b15161551de3a189ebef

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9501069188117981`
- Workspace noise score: `1.041959422826767`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What do you want someone to do when you illustrate point?
```
Prediction:
```text
C
```
Aliases:
```text
['understanding']
```
Judge reason:
```text
The model answer 'C' is not semantically equivalent to the accepted answer 'understanding' and does not represent a valid shorter form of a compound or list answer. 'C' is not a recognized alias or equivalent term for 'understanding' in this context.
```
Late workspace top-1 trajectory:
```text
  L27:目的 | L28:目的 | L29:目的 | L30:目的 | L31:目的
  L32: Purpose | L33: Illustr | L34: C
```
Noisiest late layer top tokens:
```text
L32 entropy=1.910: [' Purpose', '目的', 'Purpose', 'purpose', ' purpose']
```
Cleanest late layer top tokens:
```text
L28 entropy=0.246: ['目的', '目的是', ' Purpose', '意图', 'Purpose']
```


## ex_00990_159d50e325b59c6d29ec371500e173b4

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9486647248268127`
- Workspace noise score: `1.3087996959686279`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What is a form of anaerobic exercising?
```
Prediction:
```text
B
```
Aliases:
```text
['run']
```
Judge reason:
```text
The model answer 'B' is not semantically equivalent to the accepted answer 'run' and does not represent a form of anaerobic exercising. 'Run' is a form of aerobic exercise, not anaerobic.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:选项 | L29:选项 | L30:选项 | L31:	B
  L32: Answer | L33: Answer | L34: B
```
Noisiest late layer top tokens:
```text
L31 entropy=2.098: ['\tB', ':B', ' B', '选项', '.getB']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.657: [' Answer', 'Answer', ' B', '答案', '\tB']
```


## ex_00216_0f2377604e628c55ba588366139396b9

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9454497694969177`
- Workspace noise score: `0.8950977057218552`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What animal has quills all over it?
```
Prediction:
```text
D
```
Aliases:
```text
['hedgehog']
```
Judge reason:
```text
The model answer 'D' is not semantically equivalent to the accepted answer 'hedgehog' and does not refer to any known animal with quills all over it.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29:答案 | L30:答案 | L31:	D
  L32: D | L33: D | L34: D
```
Noisiest late layer top tokens:
```text
L30 entropy=2.405: ['答案', ':E', 'Both', ' BOTH', ' Both']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.090: [' D', '\tD', 'D', '_D', ',D']
```


## ex_01009_3ed6391c539e6daa5b5fdb1b6d5d8ace

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `low`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (low)
- First content token prob: `0.9385757446289062`
- Workspace noise score: `1.2602957982569933`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What does every person want?
```
Prediction:
```text
C
```
Aliases:
```text
['life partner']
```
Judge reason:
```text
{"verdict":"incorrect","confidence":"high","reason":"The model answer 'C' is not semantically equivalent to the accepted answer 'life partner' and does not provide a meaningful answer to the question 'What does every person want?'"}
}
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29:答案 | L30: C | L31: C
  L32: C | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L31 entropy=3.041: [' C', '\tC', ' QUESTION', 'QUESTION', '选项']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.026: [' C', 'C', '\tC', '_C', '*C']
```

