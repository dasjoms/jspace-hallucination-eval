# Confident Wrong Noisy

## ex_00305_91629c6f9e4af3e6acf385eb23fd8068

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.99312424659729`
- Workspace noise score: `2.1909655809402464`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What do you write letter in in America?
```
Prediction:
```text
C) envelope
```
Aliases:
```text
['english alphabet']
```
Judge reason:
```text
The model answer 'envelope' refers to the object used to hold letters, while the accepted answer 'english alphabet' refers to the set of letters used in the English language. The two are not semantically equivalent.
```
Late workspace top-1 trajectory:
```text
  L27:写 | L28:写 | L29:地址 | L30: letter | L31:地址
  L32: address | L33: address | L34: letter
```
Noisiest late layer top tokens:
```text
L28 entropy=3.227: ['写', '填写', '书写', '邮寄', '地址']
```
Cleanest late layer top tokens:
```text
L31 entropy=1.553: ['地址', ' address', '写', 'address', ' Address']
```


## ex_00905_2f1680da0d388a8453150ff3637e4689

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9712845683097839`
- Workspace noise score: `2.13637957572937`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Where would you be concerned about finding a cavity?
```
Prediction:
```text
D) unbrush
```
Aliases:
```text
['teeth']
```
Judge reason:
```text
The model answer 'unbrush' is not semantically equivalent to 'teeth' and does not address the question of where one would be concerned about finding a cavity. 'Unbrush' refers to a state or action, not a location or body part where cavities are found.
```
Late workspace top-1 trajectory:
```text
  L27:风险 | L28:你会 | L29:你 | L30: Areas | L31:你会
  L32:你会 | L33: D | L34: D
```
Noisiest late layer top tokens:
```text
L32 entropy=3.066: ['你会', 'You', '…\n', ' You', 'you']
```
Cleanest late layer top tokens:
```text
L34 entropy=1.052: [' D', ' You', ' \\', ' Answer', ' you']
```


## ex_00448_e98031901c815e55040d9fe28c4d9387

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9711681604385376`
- Workspace noise score: `1.6877570867538452`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Where would a cat snuggle up with their human?
```
Prediction:
```text
C
```
Aliases:
```text
['comfortable chair']
```
Judge reason:
```text
The model answer 'C' is not semantically equivalent to the accepted answer 'comfortable chair' and does not provide a meaningful answer to the question.
```
Late workspace top-1 trajectory:
```text
  L27:常见 | L28:通常 | L29:通常 | L30:人们 | L31:通常
  L32: Cats | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L32 entropy=2.808: [' Cats', ' cats', ' Usually', 'Most', ' Typically']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.725: [' C', ' \\', '通常', '选项', ' cats']
```


## ex_00941_c61790eb63ff6652b878ca051493c07d

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `low`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (low)
- First content token prob: `0.9420775771141052`
- Workspace noise score: `1.9539812564849854`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Where do you keep a pail in your house?
```
Prediction:
```text
A
```
Aliases:
```text
['utility room']
```
Judge reason:
```text
{"verdict":"incorrect","confidence":"high","reason":"The model answer 'A' is not semantically equivalent to the accepted answer 'utility room' and does not provide a valid answer to the question 'Where do you keep a pail in your house?'"}
}
```
Late workspace top-1 trajectory:
```text
  L27:常见 | L28:常见 | L29:常见 | L30:Probably | L31:Probably
  L32: A | L33: A | L34: A
```
Noisiest late layer top tokens:
```text
L31 entropy=3.226: ['Probably', '\tA', ' A', '“A', '一般']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.410: [' A', ' C', ' \\', ' The', ' Answer']
```


## ex_00915_3c6e2d95a63316b31986e8c7979582c9

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9166463017463684`
- Workspace noise score: `2.268186926841736`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What will happen to animals after eating food?
```
Prediction:
```text
B) digestion
```
Aliases:
```text
['feel pleasure']
```
Judge reason:
```text
The model answer 'digestion' refers to a process that occurs after eating, but it is not semantically equivalent to 'feel pleasure,' which is the accepted answer. The accepted answer describes a subjective experience, while the model answer describes a physiological process.
```
Late workspace top-1 trajectory:
```text
  L27:之后 | L28:食物 | L29:过程 | L30:过程 | L31:消化
  L32: After | L33:消化 | L34: B
```
Noisiest late layer top tokens:
```text
L32 entropy=3.290: [' After', '消化', '**', ' B', '食物']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.497: ['过程', '消化', 'Process', '过程中', 'process']
```


## ex_00862_6f48ee564a48293eb501cc0d8197bdd9

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9093080759048462`
- Workspace noise score: `1.8944323897361754`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Where would you display a picture on a horizontal surface?
```
Prediction:
```text
E
```
Aliases:
```text
['shelf']
```
Judge reason:
```text
The model answer 'E' is not semantically equivalent to the accepted answer 'shelf' and does not represent a valid answer to the question 'Where would you display a picture on a horizontal surface?'. 'E' is not a recognized alias or equivalent term for a shelf in this context.
```
Late workspace top-1 trajectory:
```text
  L27:墙上 | L28:墙上 | L29:墙上 | L30:墙面 | L31:墙面
  L32:墙面 | L33: display | L34: E
```
Noisiest late layer top tokens:
```text
L33 entropy=2.605: [' display', ' Display', '墙面', '传统', ' displaying']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.168: ['墙上', '墙面', '墙', '挂在', '悬挂']
```


## ex_01032_35ad89c198d5d6311a71c993bb7b6cba

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9071621894836426`
- Workspace noise score: `1.6478752613067627`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Spraining an ankle while playing baseball will cause what?
```
Prediction:
```text
C
```
Aliases:
```text
['pain']
```
Judge reason:
```text
The model answer 'C' is not semantically equivalent to the accepted answer 'pain' and does not provide a valid answer to the question about the effect of spraining an ankle while playing baseball.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29:答案 | L30::E | L31::E
  L32: E | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L31 entropy=2.549: [':E', '\tC', ',E', '\tE', "'E"]
```
Cleanest late layer top tokens:
```text
L34 entropy=0.478: [' C', ' E', ' \\', ' Correct', ' Answer']
```


## ex_00087_0f4159e80f8dbf682819215bbf0f5b5a-1

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9043005108833313`
- Workspace noise score: `1.7128486633300781`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
If you're remembering something, it's because of your what of it to begin with?
```
Prediction:
```text
A
```
Aliases:
```text
['knowing']
```
Judge reason:
```text
The model answer 'A' is not semantically equivalent to the accepted answer 'knowing' and does not provide a meaningful or correct answer to the question.
```
Late workspace top-1 trajectory:
```text
  L27:记忆 | L28:记忆 | L29: ability | L30: Ability | L31: ability
  L32: Ability | L33: Ability | L34: A
```
Noisiest late layer top tokens:
```text
L33 entropy=2.504: [' Ability', 'Ability', ' ability', '记忆', '能力']
```
Cleanest late layer top tokens:
```text
L32 entropy=1.288: [' Ability', ' ability', 'Ability', '能力', ' Remember']
```


## ex_00800_cc8324b73ed9625e723ef041dfc77a37

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `low`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (low)
- First content token prob: `0.9032039642333984`
- Workspace noise score: `2.280828261375427`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What might happen if someone is not losing weight?
```
Prediction:
```text
A
```
Aliases:
```text
['death']
```
Judge reason:
```text
{"verdict":"incorrect","confidence":"high","reason":"The model answer 'A' is not semantically equivalent to the accepted answer 'death' and does not provide a meaningful or related response to the question.'}
```
Late workspace top-1 trajectory:
```text
  L27:肥胖 | L28:肥胖 | L29:肥胖 | L30:肥胖 | L31: obesity
  L32: gain | L33: obesity | L34: A
```
Noisiest late layer top tokens:
```text
L34 entropy=3.140: [' A', ' If', '2', '1', ' \\']
```
Cleanest late layer top tokens:
```text
L28 entropy=0.525: ['肥胖', '体重', ' obesity', ' Obesity', ' overweight']
```


## ex_00312_793672da43fbc609e8c5760630c7e239

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9019970297813416`
- Workspace noise score: `1.725459384918213`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What is the habitat of the fox?
```
Prediction:
```text
B
```
Aliases:
```text
['mountains']
```
Judge reason:
```text
The model answer 'B' is not semantically equivalent to the accepted answer 'mountains' and does not provide any meaningful information about the habitat of the fox.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:选项 | L29:选项 | L30:选项 | L31:	B
  L32: B | L33: B | L34: B
```
Noisiest late layer top tokens:
```text
L31 entropy=2.740: ['\tB', ' B', '根据', '选项', ':B']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.654: [' B', ' Answer', ' E', ' According', '\tB']
```

