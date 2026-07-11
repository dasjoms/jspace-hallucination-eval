# Possible Label Noise

## ex_00024_f646f3e064f06423fc25b98500796cf0

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.8541750907897949`
- Workspace noise score: `1.3225694119930267`
- Quadrant: ``

Question:
```text
What is someone who isn't clever, bright, or competent called?
```
Prediction:
```text
C) dull
```
Aliases:
```text
['stupid']
```
Judge reason:
```text
The model answer 'dull' is semantically equivalent to the accepted answer 'stupid' in the context of describing someone who is not clever, bright, or competent.
```
Late workspace top-1 trajectory:
```text
  L27:选项 | L28:选项 | L29:答案 | L30:选项 | L31:选项
  L32: Answer | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L31 entropy=2.606: ['选项', 'Choices', '？\n', '答案', ' Choices']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.438: [' C', '\tC', 'C', ' Answer', 'Answer']
```


## ex_00057_63cf1adb5fe302b9867ead8bc8103d0b

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.8561965227127075`
- Workspace noise score: `0.4350075341761112`
- Quadrant: ``

Question:
```text
Where would you go if you wanted to have fun with a few people?
```
Prediction:
```text
E) fairgrounds
```
Aliases:
```text
["friend's house"]
```
Judge reason:
```text
The accepted answer 'friend's house' is specific to a social setting with friends, while 'fairgrounds' is a more general and possibly time-sensitive location that may not always be the best answer for 'having fun with a few people.' The model answer is not semantically equivalent to the accepted answer, but it could be considered a valid context for fun, making the verdict ambiguous.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29::E | L30: E | L31: E
  L32: E | L33: E | L34: E
```
Noisiest late layer top tokens:
```text
L29 entropy=1.469: [':E', ' E', '>E', '\tE', ',E']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.021: [' E', 'E', '\tE', ':E', '_E']
```


## ex_00065_2d33cde5e3987adc8fa2bca0af4dd3dd

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.8993746638298035`
- Workspace noise score: `1.3819251835346222`
- Quadrant: ``

Question:
```text
Where is a human likely to go as a result of being hungry?
```
Prediction:
```text
C) have lunch
```
Aliases:
```text
['eat in restaurant']
```
Judge reason:
```text
The accepted answer 'eat in restaurant' is semantically related to the model answer 'have lunch', but 'have lunch' is a specific activity that may not cover all scenarios of being hungry. The answer is partially correct but not fully equivalent to the broader accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:选项 | L29:答案 | L30:选项 | L31:选项
  L32: Answer | L33: C | L34: C
```
Noisiest late layer top tokens:
```text
L31 entropy=2.868: ['选项', '答案', 'Answer', 'getOption', '**\n']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.199: [' C', 'C', '\tC', ' Answer', 'Answer']
```


## ex_00071_c1c7a9efa379b8a7024a71cf364a144c

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9230465888977051`
- Workspace noise score: `1.618696939945221`
- Quadrant: ``

Question:
```text
Sally used a clipboard to hold her papers while she read off names at the beginning of the day.  Where might she work?
```
Prediction:
```text
A) desk
```
Aliases:
```text
['school']
```
Judge reason:
```text
The accepted answer 'school' is a broad category, while 'desk' is a specific object. 'Desk' could be in a school, but it could also be in other places like an office or a home. The model answer is not semantically equivalent to the accepted answer, but it is not clearly incorrect either, making the verdict ambiguous.
```
Late workspace top-1 trajectory:
```text
  L27:场景 | L28:关键词 | L29:"E | L30:"E | L31::A
  L32: A | L33: E | L34: A
```
Noisiest late layer top tokens:
```text
L27 entropy=3.021: ['场景', '应用场景', '关键词', '目的', '需要用到']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.484: [' A', ' E', ' \\', ' The', ' Answer']
```


## ex_00112_80697d599280d994d8a584c95824ef1f

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9768417477607727`
- Workspace noise score: `1.4974250316619873`
- Quadrant: ``

Question:
```text
Where might an unused chess set be stored?
```
Prediction:
```text
D) attic
```
Aliases:
```text
['cupboard']
```
Judge reason:
```text
The accepted answer 'cupboard' is a common storage place for an unused chess set, but 'attic' is a possible alternative. However, 'attic' is not explicitly listed as an accepted alias, and the question does not specify a particular context that would make 'attic' the only valid answer. Therefore, the model answer is not clearly equivalent to the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27: Unused | L28: Unused | L29: Unused | L30: Unused | L31: unused
  L32: unused | L33: unused | L34:1
```
Noisiest late layer top tokens:
```text
L34 entropy=2.704: ['1', '2', '4', '6', '7']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.774: [' unused', ' Unused', 'unused', 'Unused', ' UNUSED']
```


## ex_00117_9dffd2021771e0ecddb19031acf3701b

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9307718276977539`
- Workspace noise score: `1.1204572558403014`
- Quadrant: ``

Question:
```text
Where could a person avoid the rain?
```
Prediction:
```text
B) tunnel
```
Aliases:
```text
['synagogue']
```
Judge reason:
```text
The accepted answer 'synagogue' is not semantically equivalent to 'tunnel' and does not logically represent a place where one could avoid the rain. However, the question is vague and does not specify the context or constraints, leading to potential ambiguity in the model's answer.
```
Late workspace top-1 trajectory:
```text
  L27:选项 | L28:选项 | L29:选项 | L30:选项 | L31:	B
  L32: B | L33: B | L34: B
```
Noisiest late layer top tokens:
```text
L29 entropy=2.601: ['选项', ':E', '\tE', ' OPTION', '\tB']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.322: [' B', '\tB', ' E', '\tE', 'B']
```


## ex_00132_b1f36d1c8ab7e5a28783cb38e8709c27

- Correct primary: `None`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `temporal_unstable_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `True`
- Exclusion reason: `temporal_unstable`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9860072731971741`
- Workspace noise score: `1.517156183719635`
- Quadrant: ``

Question:
```text
The victim was to take stand today, they were going to do what?
```
Prediction:
```text
A) testify
```
Aliases:
```text
['testify']
```
Late workspace top-1 trajectory:
```text
  L27:词 | L28:词 | L29:词 | L30:词 | L31:词
  L32: legal | L33: take | L34: The
```
Noisiest late layer top tokens:
```text
L34 entropy=2.748: [' The', ' legal', ' A', ' "', ' Answer']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.427: [' take', ' Take', 'take', ' Taking', 'Take']
```


## ex_00140_30e66db11e0257a14a17108b90cd69fb

- Correct primary: `None`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `temporal_unstable_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `True`
- Exclusion reason: `temporal_unstable`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.967264711856842`
- Workspace noise score: `1.3869943797588349`
- Quadrant: ``

Question:
```text
Jan tested the current, and noticed that it was high.  He thought that the wires might have too much what?
```
Prediction:
```text
D) resistance
```
Aliases:
```text
['resistance']
```
Late workspace top-1 trajectory:
```text
  L27:电压 | L28:电压 | L29:电压 | L30: high | L31: high
  L32:电流 | L33: High | L34: high
```
Noisiest late layer top tokens:
```text
L29 entropy=2.400: ['电压', '较高', 'higher', ' higher', '太高']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.298: [' high', '高', 'high', '-high', 'High']
```


## ex_00177_fa1f17ca535c7e875f4f58510dc2f430

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9190946817398071`
- Workspace noise score: `1.6221817135810852`
- Quadrant: ``

Question:
```text
What is a person called who doesn't have immortality?
```
Prediction:
```text
A) mortal
```
Aliases:
```text
['mortal']
```
Judge reason:
```text
The model answer 'A) mortal' is semantically equivalent to the accepted answer 'mortal' and is a valid shorter form of the compound answer.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:选项 | L29::E | L30:	E | L31:	A
  L32: Answer | L33: E | L34: A
```
Noisiest late layer top tokens:
```text
L31 entropy=2.978: ['\tA', '-A', ' A', '-E', '\tE']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.485: [' E', ' A', 'E', '\tE', ' Answer']
```


## ex_00182_2c845646032bbf27fb3904330d59d324

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9627992510795593`
- Workspace noise score: `1.3327294796705247`
- Quadrant: ``

Question:
```text
Where can children play with animals?
```
Prediction:
```text
D) zoos
```
Aliases:
```text
['fairgrounds']
```
Judge reason:
```text
While zoos are places where children can play with animals, the accepted answer 'fairgrounds' is more specific to events where animals are often present for entertainment. The model answer 'zoos' is partially correct but not fully equivalent to the accepted answer, leading to ambiguity.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28: OPTION | L29::E | L30::E | L31: D
  L32: D | L33: D | L34: D
```
Noisiest late layer top tokens:
```text
L31 entropy=2.602: [' D', '\tD', ':E', '(E', '>E']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.138: [' D', ' E', '\tD', 'D', '_D']
```

