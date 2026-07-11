# Confident Wrong Clean Blindspots

## ex_02001_1830615

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9919995069503784`
- Workspace noise score: `1.4979499459266663`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is The Experts?
```
Prediction:
```text
1970s crime drama. The Experts is a
```
Aliases:
```text
['comedy film', 'comedy movie']
```
Judge reason:
```text
The model answer '1970s crime drama' is not semantically equivalent to the accepted answers 'comedy film' or 'comedy movie'. The correct genre for 'The Experts' is comedy, not crime drama.
```
Late workspace top-1 trajectory:
```text
  L27: comedy | L28: comedy | L29: comedy | L30: horror | L31: mystery
  L32: mystery | L33: Horror | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.502: [' Horror', ' Comedy', ' horror', '喜剧', ' comedy']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.715: ['1', ' Comedy', ' comedy', ' Mystery', ' mystery']
```


## ex_02607_5930018

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9898300766944885`
- Workspace noise score: `1.052446436882019`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is The Great Moment?
```
Prediction:
```text
1950s musical comedy. The Great Moment is
```
Aliases:
```text
['biographical film', 'biopic', 'biography film', 'biography movie', 'biographical movie', 'biographical picture']
```
Judge reason:
```text
The model answer refers to 'The Great Moment' as a '1950s musical comedy,' which is not semantically equivalent to any of the accepted answers (biographical film, biopic, etc.). The film 'The Great Moment' is actually a 1950s biographical film about the life of actor James Cagney, making the model answer factually incorrect.
```
Late workspace top-1 trajectory:
```text
  L27: comedy | L28: comedy | L29: comedy | L30: comedy | L31: comedy
  L32: comedy | L33: comedy | L34:1
```
Noisiest late layer top tokens:
```text
L29 entropy=1.961: [' comedy', ' film', '喜剧', '电影', ' cinema']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.213: ['1', '2', ' comedy', ' musical', ' Musical']
```


## ex_02340_3591887

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9863966107368469`
- Workspace noise score: `1.1313076972961427`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is Little Things?
```
Prediction:
```text
2013 film directed by Judd Apatow
```
Aliases:
```text
['traditional music', 'traditional folk music', 'popular melody', 'folk music', 'music traditions', 'musical folklore', 'pop music', 'pop', 'Pop']
```
Judge reason:
```text
The model answer refers to a 2013 film, which is unrelated to the genre of 'Little Things' (a song or musical piece). The accepted answers all pertain to music genres, while the model answer refers to a film director and movie, making it a different entity.
```
Late workspace top-1 trajectory:
```text
  L27:电影 | L28:电影 | L29:犯罪 | L30: crime | L31: mystery
  L32: crime | L33: crime | L34:2
```
Noisiest late layer top tokens:
```text
L28 entropy=2.478: ['电影', ' cinema', '犯罪', ' film', ' thriller']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.573: [' crime', ' mystery', '犯罪', ' thriller', ' Crime']
```


## ex_01548_5638006

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.985687792301178`
- Workspace noise score: `1.4663366436958314`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is Quake II?
```
Prediction:
```text
1997. What is the answer? 1
```
Aliases:
```text
['first-person shooter', 'fps', 'first person shooter video games', 'first-person shooter video game', 'FPS', 'FPS game', 'FPS video game', 'first-person shooter game']
```
Judge reason:
```text
The model answer '1997. What is the answer? 1' is clearly incorrect as it refers to a year and a number, not the genre of Quake II. The accepted answers all identify Quake II as a 'first-person shooter' genre, which is semantically distinct from the model's response.
```
Late workspace top-1 trajectory:
```text
  L27:游戏 | L28:游戏 | L29:游戏 | L30:射击 | L31:FPS
  L32:FPS | L33: first | L34:1
```
Noisiest late layer top tokens:
```text
L32 entropy=2.226: ['FPS', ' shooter', '动作', ' Shooter', '射击']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.448: ['游戏', ' gameplay', '的游戏', ' multiplayer', ' gaming']
```


## ex_03743_1891599

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9853581190109253`
- Workspace noise score: `0.878600561618805`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
In what country is Brazil at the 1968 Summer Olympics?
```
Prediction:
```text
1968 Summer Olympics were held in Mexico City
```
Aliases:
```text
['Brazil', 'Federative Republic of Brazil', 'BR', 'BRA', 'br', '🇧🇷']
```
Judge reason:
```text
The model answer states that the 1968 Summer Olympics were held in Mexico City, which is correct, but the question asks for the country where Brazil was represented. Brazil was a participating nation in the 1968 Olympics, not the host country. The accepted answers list Brazil and its aliases, not Mexico City.
```
Late workspace top-1 trajectory:
```text
  L27: Czech | L28: Czech | L29: Czech | L30: Mexico | L31: Mexico
  L32: Mexico | L33: Mexico | L34:1
```
Noisiest late layer top tokens:
```text
L27 entropy=2.724: [' Czech', ' Mexico', 'Mexico', 'Italy', ' Netherlands']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.642: [' Mexico', ' Czech', 'Mexico', ' México', ' Egypt']
```


## ex_01775_2299289

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9850368499755859`
- Workspace noise score: `1.1053960263729095`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is Alone in the Dark?
```
Prediction:
```text
1998 action-adventure horror video game
```
Aliases:
```text
['horror film', 'horror movie', 'slasher film', 'slasher movie', 'slasher']
```
Judge reason:
```text
The model answer refers to 'Alone in the Dark' as a 1998 action-adventure horror video game, which is a specific media type and release, while the accepted answers focus on the genre (horror film/movie/slasher film/movie/slasher). The model answer does not align with the genre classification provided in the accepted answers.
```
Late workspace top-1 trajectory:
```text
  L27: horror | L28: Horror | L29: horror | L30: horror | L31: horror
  L32: horror | L33: Survival | L34: horror
```
Noisiest late layer top tokens:
```text
L27 entropy=1.977: [' horror', '游戏', ' Horror', ' thriller', ' gameplay']
```
Cleanest late layer top tokens:
```text
L30 entropy=0.469: [' horror', ' Horror', '恐怖', '鬼', '恐惧']
```


## ex_01747_4081582

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9838493466377258`
- Workspace noise score: `0.9689416408538818`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is The Gamble?
```
Prediction:
```text
1970s crime drama. The Gamble is
```
Aliases:
```text
['comedy film', 'comedy movie']
```
Judge reason:
```text
The model answer '1970s crime drama' is not semantically equivalent to the accepted answers 'comedy film' or 'comedy movie'. The correct genre for 'The Gamble' is comedy, not crime drama.
```
Late workspace top-1 trajectory:
```text
  L27: comedy | L28: comedy | L29: comedy | L30: comedy | L31: comedy
  L32: crime | L33: comedy | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=1.862: [' comedy', ' Comedy', ' crime', '喜剧', ' Crime']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.393: [' comedy', '喜剧', ' crime', ' Comedy', ' drama']
```


## ex_03115_2256210

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.977531909942627`
- Workspace noise score: `0.8572461009025574`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
Who is the father of Estrid Svendsdatter?
```
Prediction:
```text
Svend Sorensen
```
Aliases:
```text
['Sweyn I of Denmark', 'Sweyn Forkbeard', 'Sweyn, King of Denmark']
```
Judge reason:
```text
Svend Sorensen is not the father of Estrid Svendsdatter. The accepted answers identify Sweyn I of Denmark, Sweyn Forkbeard, or Sweyn, King of Denmark as her father, all of whom are historically recognized as the father of Estrid Svendsdatter.
```
Late workspace top-1 trajectory:
```text
  L27:答案 | L28:答案 | L29:答案 | L30: Stephen | L31:丹麦
  L32: Sv | L33: Sv | L34: Sv
```
Noisiest late layer top tokens:
```text
L30 entropy=2.766: [' Stephen', ' Viking', '丹麦', 'Stephen', 'Edward']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.009: [' Sv', ' sv', '_sv', '(sv', 'sv']
```


## ex_10488_1070535

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9660313129425049`
- Workspace noise score: `0.6689777642488479`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What sport does 1995 Cook Islands Round Cup play?
```
Prediction:
```text
1995 Cook Islands Round Cup played rugby league
```
Aliases:
```text
['association football', 'football', 'soccer']
```
Judge reason:
```text
The model answer states that the 1995 Cook Islands Round Cup played rugby league, which is not semantically equivalent to the accepted answers of association football, football, or soccer. The event is clearly associated with football/soccer, not rugby league.
```
Late workspace top-1 trajectory:
```text
  L27: rugby | L28: rugby | L29: rugby | L30: rugby | L31: rugby
  L32: rugby | L33: Rugby | L34: rugby
```
Noisiest late layer top tokens:
```text
L34 entropy=1.276: [' rugby', ' Rugby', '1', ' football', '2']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.107: [' rugby', ' Rugby', '足球', ' football', ' Football']
```


## ex_01894_5348157

- Correct primary: `False`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_incorrect`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `incorrect` (high)
- First content token prob: `0.9646967053413391`
- Workspace noise score: `1.413031816482544`
- Quadrant: `high_confidence__clean_workspace`

Question:
```text
What genre is Ordeal in Space?
```
Prediction:
```text
1980s action-adventure. Ordeal in
```
Aliases:
```text
['short story', 'tale', 'pripovijetka']
```
Judge reason:
```text
The model answer '1980s action-adventure. Ordeal in' is clearly a different entity/fact. 'Ordeal in Space' is a short story, not an action-adventure genre. The accepted answers are 'short story', 'tale', and 'pripovijetka', which are all synonyms for a short story, not a genre.
```
Late workspace top-1 trajectory:
```text
  L27:游戏 | L28:游戏 | L29:游戏 | L30:游戏 | L31: arcade
  L32: arcade | L33: arcade | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.254: [' arcade', ' Simulation', ' Survival', '动作', ' puzzle']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.160: ['游戏', ' gameplay', '的游戏', ' gaming', ' Gameplay']
```

