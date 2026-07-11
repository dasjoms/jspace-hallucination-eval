# Confident Correct Clean

## ex_03993_qw-6834

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `1.0`
- Workspace noise score: `1.3374296228233107`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
The capital of Brazil was moved from Rio de Janeiro to the purpose-built capital city of Brasilia in what year?
```
Prediction:
```text
1960. The capital of Brazil was moved from Rio de Janeiro to
```
Aliases:
```text
['1960', 'one thousand, nine hundred and sixty', '1960', '1960', 'one thousand nine hundred and sixty', '', '']
```
Late workspace top-1 trajectory:
```text
  L27:巴西 | L28:巴西 | L29:巴西 | L30:巴西 | L31:巴西
  L32:巴西 | L33: Braz | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.910: [' Braz', ' Bras', '***\n', '巴西', 'bras']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '9', ' Wikimedia', '１', ' Braz']
```


## ex_00828_qb-1379

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999998807907104`
- Workspace noise score: `1.0631009972872563`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
The Euro is divided into how many cents?
```
Prediction:
```text
100. The Euro is divided into 100 cents. Wait
```
Aliases:
```text
['100', '100', 'one hundred', 'one hundred', '100', '', '']
```
Judge reason:
```text
The model answer '100. The Euro is divided into 100 cents. Wait' is semantically equivalent to the accepted answers, providing the correct numerical value and additional context.
```
Late workspace top-1 trajectory:
```text
  L27:欧元 | L28:欧元 | L29:欧元 | L30:欧元 | L31: cents
  L32: hundred | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=1.837: [' cents', '欧元', '**\n', 'EUR', '**']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' cents', ' Hund', ' hundred', ' cent']
```


## ex_05280_sfq-1864

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999997615814209`
- Workspace noise score: `1.1502916812896729`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Which year saw the assassination of US President James Garfield?
```
Prediction:
```text
1881. The assassination of U.S. President James Garfield occurred
```
Aliases:
```text
['1881', 'one thousand, eight hundred and eighty-one', '1881', 'one thousand eight hundred and eighty one', '1881', '', '']
```
Late workspace top-1 trajectory:
```text
  L27: assassination | L28: assassination | L29: assassination | L30: assassination | L31: assassination
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=1.764: ['1', ' assassination', ']**', '身亡', '?\n']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.071: [' assassination', ' assass', '杀害', '杀了', ' Assass']
```


## ex_06172_sfq-12016

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999995231628418`
- Workspace noise score: `0.6118495058268308`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In what decade was Darwin's 'On the Origin of Species' first published?
```
Prediction:
```text
1850s. The answer is the 1850s
```
Aliases:
```text
['1850s', '1850s', '1850–1859', "1850's", '1850-1859', 'Eighteen-fifties', 'eighteen fifties', '1850 s', '1850s', '1850–1859', '1850 1859', '', '']
```
Late workspace top-1 trajectory:
```text
  L27: Darwin | L28: Darwin | L29: Darwin | L30: nineteenth | L31: nineteenth
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L27 entropy=2.355: [' Darwin', '出版', ' Victorian', '近代', '这本书']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.028: ['1', '8', '2', '9', '3']
```


## ex_08543_odql-11994

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999993443489075`
- Workspace noise score: `0.5157903982297057`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In which year in the 1930's were Bonnie and Clyde killed?
```
Prediction:
```text
1934. The answer is 1934. Bonnie and
```
Aliases:
```text
['1934', 'one thousand, nine hundred and thirty-four', '1934', '1934', 'one thousand nine hundred and thirty four', '', '']
```
Late workspace top-1 trajectory:
```text
  L27:杀害 | L28:Year | L29:民国 | L30:民国 | L31:1
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L29 entropy=3.175: ['民国', '__;', '____', '****', 'Year']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', ' Answer', ' The', ' They']
```


## ex_00919_qb-2498

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999992847442627`
- Workspace noise score: `1.5084715105593205`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many square stickers are on each face of a classic Rubik’s Cube?
```
Prediction:
```text
9. The classic Rubik’s Cube has 9 stickers per face. Each
```
Aliases:
```text
['Nine', '9', 'nine', 'Nine', 'nine', '9', '', '']
```
Judge reason:
```text
The model answer '9. The classic Rubik’s Cube has 9 stickers per face. Each' is semantically equivalent to the accepted answers and provides the correct information about the number of square stickers on each face of a classic Rubik’s Cube.
```
Late workspace top-1 trajectory:
```text
  L27: squares | L28: squares | L29: stickers | L30: squares | L31: stickers
  L32:？
 | L33:九 | L34:9
```
Noisiest late layer top tokens:
```text
L32 entropy=2.340: ['？\n', 'nine', '中心', '-center', '？\n\n']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.013: ['9', '？\n', '1', '4', '3']
```


## ex_06041_sfq-10454

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999992847442627`
- Workspace noise score: `0.9334251020365627`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
When was the first stamp, the Penny Black, issued in Britain?
```
Prediction:
```text
1840. The Penny Black was issued on May 1
```
Aliases:
```text
['1840', '1840', 'one thousand, eight hundred and forty', 'one thousand eight hundred and forty', '1840', '', '']
```
Late workspace top-1 trajectory:
```text
  L27:英镑 | L28:英镑 | L29:英镑 | L30:英镑 | L31: January
  L32:1 | L33: January | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=1.665: [' January', '1', '邮', 'January', '邮政']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', ' January', '¹', '2', ' February']
```


## ex_06883_sfq-20357

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999990463256836`
- Workspace noise score: `1.113423702272121`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In what year did the five founding members of OPEC hold their first meeting?
```
Prediction:
```text
1960. The five founding members of OPEC were Iran, Iraq
```
Aliases:
```text
['1960', 'one thousand, nine hundred and sixty', '1960', '1960', 'one thousand nine hundred and sixty', '', '']
```
Late workspace top-1 trajectory:
```text
  L27:石油 | L28:石油 | L29:石油 | L30:石油 | L31: petroleum
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=2.564: [' petroleum', '石油', 'pet', ' Petroleum', '*</']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '9', ' September', ' petroleum', '?\n']
```


## ex_09715_qg-1986

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.9999990463256836`
- Workspace noise score: `1.4184428551845485`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Name the year: The Macintosh is introduced, Louisiana hosted the last World’s Fair to be held in the US, Vanessa Williams resigns her Miss America crown, Band Aid records the song “Do They Know It’s Christmas” for famine relief, Union Carbide wipes out a good chunk of Bhopal, India
```
Prediction:
```text
1988. The Macintosh was introduced in 1984
```
Aliases:
```text
['1984', '1984', 'one thousand, nine hundred and eighty-four', '1984', 'one thousand nine hundred and eighty four', '', '']
```
Late workspace top-1 trajectory:
```text
  L27:改革开放 | L28:改革开放 | L29:改革开放 | L30:)(( | L31:?;

  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L31 entropy=3.534: ['?;\n', ':YES', '改革开放', '?</', '上世纪']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['1', '2', '�', ' Answer', ' What']
```


## ex_07787_odql-2653

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_correct`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `correct` (high)
- First content token prob: `0.9999988079071045`
- Workspace noise score: `1.054125265032053`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
How many books are there in the New Testament of the Bible?
```
Prediction:
```text
27. The New Testament contains 27 books. The answer is
```
Aliases:
```text
['27', '27', 'twenty-seven', '27', 'twenty seven', '', '']
```
Judge reason:
```text
The model answer '27. The New Testament contains 27 books.' is semantically equivalent to the accepted answers and provides a clear, correct response to the question.
```
Late workspace top-1 trajectory:
```text
  L27:圣经 | L28:圣经 | L29: books | L30: books | L31: books
  L32: books | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L29 entropy=2.053: [' books', '圣经', 'Books', '书籍', '_books']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.000: ['2', '1', '4', '3', ' books']
```

