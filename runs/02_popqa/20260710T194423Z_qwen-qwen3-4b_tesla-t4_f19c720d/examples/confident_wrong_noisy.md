# Confident Wrong Noisy

## ex_01924_2342917

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9970899820327759`
- Workspace noise score: `1.6297951936721802`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What genre is BOND?
```
Prediction:
```text
007.00000000
```
Aliases:
```text
['synth-pop', 'synthesizer pop', 'techno-pop', 'synthpop']
```
Judge reason:
```text
The model answer '007.00000000' is not semantically equivalent to any of the accepted answers. '007' refers to the James Bond secret agent code, not a music genre. The accepted answers are all music genres, and the model answer does not match any of them.
```
Late workspace top-1 trajectory:
```text
  L27:电影 | L28:电影 | L29:电影 | L30: films | L31: thriller
  L32: spy | L33: spy | L34:0
```
Noisiest late layer top tokens:
```text
L30 entropy=2.283: [' films', '谍', 'films', '电影', ' film']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.695: ['0', '1', '2', ' Bond', ' spy']
```


## ex_01582_3682187

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9945386052131653`
- Workspace noise score: `1.654141940921545`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What genre is Chariot Race?
```
Prediction:
```text
1970s action film
```
Aliases:
```text
['racing video game', 'racing game', 'racing video games', 'racer']
```
Judge reason:
```text
The model answer '1970s action film' is not semantically equivalent to the accepted answers, which are all related to video games. The question asks for the genre of 'Chariot Race,' which is a video game, not a film.
```
Late workspace top-1 trajectory:
```text
  L27: cinema | L28:电影 | L29:电影 | L30: films | L31: cinema
  L32:1 | L33:1 | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.484: ['1', '赛车', ' racing', ' horror', ' martial']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.034: ['1', '2', ' racing', '赛车', '3']
```


## ex_10838_4442437

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.994041919708252`
- Workspace noise score: `2.0972330808639525`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Who is the author of Free to Choose?
```
Prediction:
```text
1980. The author of "Free to Choose
```
Aliases:
```text
['Milton Friedman', 'Milton Fridman']
```
Judge reason:
```text
The model answer '1980. The author of "Free to Choose"' is clearly incorrect as it refers to the year the book was published, not the author. The accepted answers are 'Milton Friedman' and 'Milton Fridman', which are the correct authors.
```
Late workspace top-1 trajectory:
```text
  L27:经济学家 | L28:经济学家 | L29:经济学家 | L30:经济学家 | L31:经济学家
  L32: Friedrich | L33: Friedrich | L34: Friedrich
```
Noisiest late layer top tokens:
```text
L33 entropy=2.832: [' Friedrich', '经济学家', ' Milton', '米尔', ' economist']
```
Cleanest late layer top tokens:
```text
L28 entropy=0.447: ['经济学家', '经济学', ' Economist', ' economist', ' economists']
```


## ex_10244_2938273

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9914933443069458`
- Workspace noise score: `1.614118804037571`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What sport does 2013 Torneo di Viareggio play?
```
Prediction:
```text
2013 Torneo di Viareggio plays
```
Aliases:
```text
['association football', 'football', 'soccer']
```
Judge reason:
```text
The model answer is incomplete and does not specify the sport. The accepted answers clearly state that the sport is association football, football, or soccer. The model answer only states that the event 'plays' without identifying the sport, making it incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:足球 | L28:足球 | L29:足球 | L30: soccer | L31: volleyball
  L32: football | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L32 entropy=2.735: [' football', ' basketball', ' tennis', ' Football', ' volleyball']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.119: ['2', ' football', '1', '7', '3']
```


## ex_06566_85486

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9847182035446167`
- Workspace noise score: `2.0593833804130552`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Who was the director of Fear Strikes Out?
```
Prediction:
```text
1958. The film "Fear Strikes Out
```
Aliases:
```text
['Robert Mulligan', 'Robert Patrick Mulligan']
```
Judge reason:
```text
The model answer provides a year and a film title, which are not semantically equivalent to the accepted answer (director's name). The answer does not identify the director, making it incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:导演 | L28:导演 | L29:导演 | L30:导演 | L31:导演
  L32: George | L33: George | L34: George
```
Noisiest late layer top tokens:
```text
L34 entropy=3.364: [' George', ' Richard', '1', ' Tony', ' Gordon']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.397: ['导演', '执导', '编剧', ' filmmakers', '电影']
```


## ex_11321_1200458

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9797654747962952`
- Workspace noise score: `2.433528423309326`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Who is the author of Saturday?
```
Prediction:
```text
1962. The author of Saturday is the author
```
Aliases:
```text
['Ian McEwan', 'Ian Russell McEwan']
```
Judge reason:
```text
The model answer provides a year (1962) and a redundant statement, which is semantically unrelated to the actual author of 'Saturday,' which is Ian McEwan. The answer does not identify the author and is factually incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:作家 | L28:作家 | L29:小说 | L30:作家 | L31:作家
  L32:George | L33: Douglas | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=3.483: [' Douglas', 'Philip', ' Kurt', ' Cyril', ' George']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.092: ['作家', '写作', ' novelist', '小说', '作者']
```


## ex_06484_3039072

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9770660400390625`
- Workspace noise score: `1.8925568044185639`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Who was the director of The Sugarland Express?
```
Prediction:
```text
1974. The director of The Sugarland Express
```
Aliases:
```text
['Steven Spielberg', 'Steven Allan Spielberg', 'Spielberg']
```
Judge reason:
```text
The model answer provides the year 1974 and the phrase 'The director of The Sugarland Express,' which is not semantically equivalent to the accepted answers. The accepted answers identify the director as Steven Spielberg, while the model answer does not name the director and instead provides a year and a phrase that does not answer the question directly.
```
Late workspace top-1 trajectory:
```text
  L27:导演 | L28:导演 | L29:导演 | L30:导演 | L31:导演
  L32: Steven | L33: Alan | L34:1
```
Noisiest late layer top tokens:
```text
L34 entropy=3.183: ['1', ' Richard', '执导', ' Robert', 'George']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.109: ['导演', '执导', ' director', '电影', '影片']
```


## ex_01323_1643922

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9693533778190613`
- Workspace noise score: `1.806520688533783`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
What genre is Branded?
```
Prediction:
```text
1950s Western
```
Aliases:
```text
['science fiction film', 'sci-fi film', 'science fiction movie', 'sci-fi movie', 'scifi film', 'scifi movie', 'sci fi film', 'sci fi movie', 'scifi-film', 'scifi']
```
Judge reason:
```text
The model answer '1950s Western' is not semantically equivalent to any of the accepted answers, which are all related to 'science fiction film' or 'sci-fi film'. The model answer refers to a different genre and time period, making it clearly incorrect.
```
Late workspace top-1 trajectory:
```text
  L27:电影 | L28:电影 | L29:电影 | L30: cowboy | L31: thriller
  L32: crime | L33: crime | L34: Western
```
Noisiest late layer top tokens:
```text
L33 entropy=3.040: [' crime', ' Western', '动作', '1', ' adventure']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.887: [' crime', ' drama', '犯罪', ' thriller', ' mystery']
```


## ex_03138_6311127

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9680622816085815`
- Workspace noise score: `2.0621281385421755`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Who is the father of Meinhardt Schomberg, 3rd Duke of Schomberg?
```
Prediction:
```text
2nd Duke of Schomberg
```
Aliases:
```text
['Frederick Schomberg, 1st Duke of Schomberg']
```
Judge reason:
```text
The model answer refers to the 2nd Duke of Schomberg, but the accepted answer identifies the father as Frederick Schomberg, 1st Duke of Schomberg. The model answer is clearly a different entity and not semantically equivalent to the accepted answer.
```
Late workspace top-1 trajectory:
```text
  L27:Charles | L28:Charles | L29:Charles | L30: Charles | L31: Charles
  L32: William | L33:2 | L34:2
```
Noisiest late layer top tokens:
```text
L27 entropy=3.169: ['Charles', '父亲', 'Father', '祖父', 'Edward']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.430: ['2', '1', ' William', ' Richard', ' John']
```


## ex_10942_2308114

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9642374515533447`
- Workspace noise score: `1.9106218338012695`
- Quadrant: `high_confidence__noisy_workspace`

Question:
```text
Who is the author of Magic?
```
Prediction:
```text
1984. The author of "Magic" is
```
Aliases:
```text
['Isaac Asimov', 'Isaak Osimov', 'Paul French', 'Asimov', 'Isaak Ozimov']
```
Judge reason:
```text
The model answer '1984. The author of "Magic" is' is clearly incorrect as it refers to the year 1984, which is not the author of the book "Magic". The accepted answers list authors, not years, and the model answer does not provide any valid author name from the accepted list.
```
Late workspace top-1 trajectory:
```text
  L27:作家 | L28:小说 | L29:作家 | L30:作者 | L31:作者
  L32: Robert | L33: Douglas | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=3.059: [' Robert', ' Douglas', ' Richard', ' Michael', ' George']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.732: ['作家', '作者', '小说', '创作', '编剧']
```

