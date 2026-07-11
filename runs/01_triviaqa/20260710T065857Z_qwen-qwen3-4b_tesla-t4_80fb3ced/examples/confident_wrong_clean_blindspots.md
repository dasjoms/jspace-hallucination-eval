# Confident Wrong Clean Blindspots

## ex_01133_qb-4673

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
- Workspace noise score: `0.8590346276832861`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In the Bible, how many psalms make up the Book of Psalms?
```
Prediction:
```text
150. The Book of Psalms in the Bible contains 1
```
Aliases:
```text
['150', '150', 'one hundred and fifty', '150', 'one hundred and fifty', '', '']
```
Judge reason:
```text
The model answer is incomplete and incorrect. The accepted answers clearly state that the Book of Psalms contains 150 psalms. The model answer provides '150. The Book of Psalms in the Bible contains 1' which is semantically incorrect and incomplete.
```
Late workspace top-1 trajectory:
```text
  L27: Psalm | L28: Psalm | L29: Psalm | L30: Psalm | L31: Psalm
  L32:一百 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=1.769: ['一百', '咏', '合唱', '一百多', ' songs']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '朗诵', '\n', ' ESV', ' $$']
```


## ex_04119_qw-8436

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
- Workspace noise score: `1.428848421573639`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In which year was the first robbery for which it is known that Jesse James was responsible, of the Davies's County Savings Association in Gallatin, Missouri, during which Jesse shot and killed the cashier, Captain John Sheets?
```
Prediction:
```text
1873
```
Aliases:
```text
['1869', '1869', 'one thousand, eight hundred and sixty-nine', '1869', 'one thousand eight hundred and sixty nine', '', '']
```
Judge reason:
```text
The model answer '1873' is clearly different from the accepted answers '1869', which is the correct year for the robbery described in the question.
```
Late workspace top-1 trajectory:
```text
  L27: Kansas | L28: Kansas | L29: Kansas | L30: Kansas | L31:]**
  L32:1 | L33:8 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.536: [']**', '**\n', '民国', ' Civil', '捻']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.147: ['1', '8', ' August', '\ufeff\n', ' ```\n']
```


## ex_04232_qw-10046

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999990463256836`
- Workspace noise score: `1.2441314019146374`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many decades are there in a millennium?
```
Prediction:
```text
10
```
Aliases:
```text
['100', '100', 'one hundred', 'one hundred', '100', '', '']
```
Judge reason:
```text
The model answer '10' is incorrect. A millennium consists of 1000 years, and since a decade is 10 years, there are 100 decades in a millennium. The accepted answers consistently state '100', making the model answer clearly incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:十年 | L28:十个 | L29:十个 | L30:十个 | L31:十个
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.517: ['十个', '十年', '三十年', '()</', '二十年']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', ' The', ' Ten', '5']
```


## ex_07228_sfq-24119

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999980330467224`
- Workspace noise score: `1.522302354904241`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
On what day of the month did the Roman ‘Ides’ of March fall?
```
Prediction:
```text
13. The Roman 'Ides' of March fell on the 1
```
Aliases:
```text
['15th', 'fifteen', '15', '15th', 'fifteen', '15th', '15', '', '']
```
Judge reason:
```text
The model answer '13' is incorrect. The Roman 'Ides of March' fell on the 15th day of March, which is clearly stated in the accepted answers as '15th', '15', 'fifteen', etc. The model answer is factually wrong.
```
Late workspace top-1 trajectory:
```text
  L27:日期 | L28:罗马 | L29:中间 | L30:Wednesday | L31:十三
  L32:第十 | L33:第十 | L34:1
```
Noisiest late layer top tokens:
```text
L30 entropy=2.666: ['Wednesday', '第十', '介', '预测', ' Wednesday']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' $$', '$id', 'iddle', '9']
```


## ex_03891_qw-5401

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999978542327881`
- Workspace noise score: `1.3739729904245905`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
111,111,111 squared gives what result?
```
Prediction:
```text
1234567898765432
```
Aliases:
```text
['12,345,678,987,654,321', '12345678987654321', 'twelve quadrillion, three hundred and forty-five trillion, six hundred and seventy-eight billion, nine hundred and eighty-seven million, six hundred and fifty-four thousand, three hundred and twenty-one', '12,345,678,987,654,321', 'twelve quadrillion three hundred and forty five trillion six hundred and seventy eight billion nine hundred and eighty seven million six hundred and fifty four thousand three hundred and twenty one', '12 345 678 987 654 321', '12345678987654321', '', '']
```
Judge reason:
```text
The model answer is missing the last digit '1' compared to the accepted answers, which correctly state the result as 12345678987654321. The model answer is clearly incorrect as it does not match the accepted result.
```
Late workspace top-1 trajectory:
```text
  L27:万亿 | L28:[( | L29:万亿 | L30:万亿 | L31:**,
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.541: ['**,', '\\\n', '\xa0', '**\r\n', '**\n\n']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' ', '2', '¹', '�']
```


## ex_08807_odql-14853

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999967813491821`
- Workspace noise score: `0.45471509417220657`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In which year did Brookside first appear on Channel 4?
```
Prediction:
```text
1992. The show first aired in 1992
```
Aliases:
```text
['1982', 'one thousand, nine hundred and eighty-two', '1982', 'one thousand nine hundred and eighty two', '1982', '', '']
```
Judge reason:
```text
The model answer states 1992, which is incorrect as the accepted answers clearly indicate 1982 as the correct year when Brookside first appeared on Channel 4.
```
Late workspace top-1 trajectory:
```text
  L27:BBC | L28:BBC | L29:BBC | L30:BBC | L31:1
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=1.315: ['1', 'BBC', ')((', '电视', ' BBC']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' The', '2', ' What', '9']
```


## ex_05574_sfq-5321

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999966621398926`
- Workspace noise score: `1.2004972329130397`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Which Olympic games saw the introduction of the Fosbury Flop?
```
Prediction:
```text
1956 Summer Olympics. The Fosbury Flop was introduced at
```
Aliases:
```text
['MEXICO 1968', 'MEXICO 1968', 'mexico 1968', '', '']
```
Judge reason:
```text
The model answer incorrectly states that the Fosbury Flop was introduced at the 1956 Summer Olympics, whereas the accepted answer indicates it was introduced at the 1968 Mexico Olympics.
```
Late workspace top-1 trajectory:
```text
  L27:运动员 | L28:运动员 | L29: Olympic | L30:东京 | L31:第五届
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.166: ['第五届', '1', '东京', ' nineteen', '十九届']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '�', ' nineteen', ' Championships', ' championships']
```


## ex_08821_odql-15006

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999963045120239`
- Workspace noise score: `1.5626275956630706`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In music how many quavers make a minim?
```
Prediction:
```text
2
```
Aliases:
```text
['Four (4)', 'Four (4)', 'four 4', '', '']
```
Judge reason:
```text
The model answer '2' is incorrect. In music, a minim is equivalent to two quavers, not four. The accepted answers clearly state 'Four (4)', which is the correct answer.
```
Late workspace top-1 trajectory:
```text
  L27:节奏 | L28:节奏 | L29:两个 | L30:Two | L31:Two
  L32:Two | L33: two | L34:2
```
Noisiest late layer top tokens:
```text
L32 entropy=1.991: ['Two', ' two', '____', ' Two', 'two']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.367: ['2', ' Two', 'Two', ' two', '两']
```


## ex_04655_qw-16494

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999955892562866`
- Workspace noise score: `1.1237194105308845`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Which was the first year in which the football World Cup final was broadcast on television in colour?
```
Prediction:
```text
1966. The 1966 World Cup final, held
```
Aliases:
```text
['1970', 'one thousand, nine hundred and seventy', '1970', '1970', 'one thousand nine hundred and seventy', '', '']
```
Judge reason:
```text
The model answer of 1966 is incorrect. The first year in which the football World Cup final was broadcast on television in colour was 1970, as stated in the accepted answers.
```
Late workspace top-1 trajectory:
```text
  L27:世界杯 | L28:电视 | L29: FIFA | L30:广播 | L31:广播
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L30 entropy=2.159: ['广播', ' broadcast', ' broadcasts', '直播', '播']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' broadcast', '₁', ' The', '１']
```


## ex_07611_odql-594

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9999949336051941`
- Workspace noise score: `1.062648696686665`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Name the year: American gangster AI Capone dies, Princess Elizabeth marries and India gains its independence?
```
Prediction:
```text
1929
```
Aliases:
```text
['1947', 'one thousand, nine hundred and forty-seven', '1947', '1947', 'one thousand nine hundred and forty seven', '', '']
```
Judge reason:
```text
The model answer '1929' is not semantically equivalent to the accepted answers, which all point to 1947. The events mentioned in the question—American gangster Al Capone's death, Princess Elizabeth's marriage, and India's independence—are all associated with 1947, not 1929.
```
Late workspace top-1 trajectory:
```text
  L27:英镑 | L28:英镑 | L29:伦敦 | L30:伦敦 | L31:抗战
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L28 entropy=2.827: ['英镑', ' WWII', '英国', 'year', 'Year']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '9', '2', ' The', '0']
```

