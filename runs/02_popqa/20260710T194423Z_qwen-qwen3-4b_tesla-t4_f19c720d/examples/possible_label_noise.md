# Possible Label Noise

## ex_01824_2491290

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.4986723065376282`
- Workspace noise score: `2.5227885484695434`
- Quadrant: ``

Question:
```text
What genre is For Sale?
```
Prediction:
```text
1980s pop
```
Aliases:
```text
['pop music', 'pop', 'Pop']
```
Judge reason:
```text
The accepted answers are 'pop music', 'pop', and 'Pop', which are general categories. The model answer '1980s pop' specifies a time period, which may be relevant but is not explicitly covered by the accepted answers. Therefore, the answer is partially correct but not clearly equivalent.
```
Late workspace top-1 trajectory:
```text
  L27: music | L28: music | L29:摇滚 | L30: music | L31:摇滚
  L32: rock | L33: Hip | L34:2
```
Noisiest late layer top tokens:
```text
L32 entropy=3.310: [' rock', '摇滚', ' hip', ' music', ' Jazz']
```
Cleanest late layer top tokens:
```text
L27 entropy=1.576: [' music', '音乐', '摇滚', ' genre', ' musical']
```


## ex_00409_542248

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.6961039900779724`
- Workspace noise score: `1.0740604370832443`
- Quadrant: ``

Question:
```text
What is Tadhg Dall Ó hUiginn's occupation?
```
Prediction:
```text
19th-century Irish poet. Tadhg Dall
```
Aliases:
```text
['poet', 'poetess', 'bard']
```
Late workspace top-1 trajectory:
```text
  L27:书法家 | L28: Irish | L29: Irish | L30: Irish | L31: Irish
  L32: Irish | L33: Irish | L34: Irish
```
Noisiest late layer top tokens:
```text
L27 entropy=2.790: ['书法家', '画家', '英格兰', 'Composer', ' politician']
```
Cleanest late layer top tokens:
```text
L30 entropy=0.183: [' Irish', '爱尔兰', ' Dublin', ' Ireland', ' Gael']
```


## ex_01679_1750783

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.4659063220024109`
- Workspace noise score: `1.5543038487434386`
- Quadrant: ``

Question:
```text
What genre is John K. Samson?
```
Prediction:
```text
1990s alternative rock. John K. Sam
```
Aliases:
```text
['rock music', 'rock and roll', 'rock', 'Rock']
```
Late workspace top-1 trajectory:
```text
  L27:摇滚 | L28:音乐 | L29:摇滚 | L30: Canadian | L31: bands
  L32: folk | L33: Alternative | L34: Alternative
```
Noisiest late layer top tokens:
```text
L31 entropy=2.177: [' bands', '摇滚', ' band', ' Canadian', ' rock']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.370: ['摇滚', '音乐', '乐队', ' music', '吉他']
```


## ex_00520_3403435

- Correct primary: `True`
- Strict correct: `True`
- Expanded correct: `True`
- Label source: `strict_exact`
- Label quality: `high`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.6131290793418884`
- Workspace noise score: `1.1800569534301757`
- Quadrant: ``

Question:
```text
What is Bedřich Smetana's occupation?
```
Prediction:
```text
Composer
```
Aliases:
```text
['composer', 'pianist']
```
Late workspace top-1 trajectory:
```text
  L27:国籍 | L28:音乐 | L29: Czech | L30: Czech | L31: Czech
  L32: Czech | L33: Composer | L34: Composer
```
Noisiest late layer top tokens:
```text
L28 entropy=2.536: ['音乐', '艺术家', '钢琴', '画家', '国籍']
```
Cleanest late layer top tokens:
```text
L31 entropy=0.060: [' Czech', ' Composer', ' Slovak', ' composer', ' Hungarian']
```


## ex_03582_4497762

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `True`
- Judge verdict: `None` (None)
- First content token prob: `0.7042424082756042`
- Workspace noise score: `1.4700300216674804`
- Quadrant: ``

Question:
```text
In what country is Parks?
```
Prediction:
```text
1. United States
```
Aliases:
```text
['United States of America', 'the United States of America', 'America', 'U.S.A.', 'USA', 'U.S.', 'US', 'the US', 'the USA', 'US of A', 'the United States', 'U. S. A.', 'U. S.', 'the States', 'the U.S.', "'Merica", 'U.S', 'United States', "'Murica"]
```
Late workspace top-1 trajectory:
```text
  L27:Scotland | L28:Scotland | L29:Scotland | L30: Scotland | L31: Scotland
  L32: Scotland | L33: parks | L34:1
```
Noisiest late layer top tokens:
```text
L34 entropy=3.221: ['1', ' Scotland', 'Scotland', '2', ' parks']
```
Cleanest late layer top tokens:
```text
L33 entropy=0.588: [' parks', ' Parks', ' Scotland', 'Scotland', ' UK']
```


## ex_03811_5837309

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.8285616040229797`
- Workspace noise score: `0.014864110585767776`
- Quadrant: ``

Question:
```text
In what country is Storsteinnes Chapel?
```
Prediction:
```text
Norway.  The chapel is located in the municipality of S
```
Aliases:
```text
['Norway', 'Kingdom of Norway', 'Norge', 'Norvège\u200f', 'NO', 'NOR', 'no', 'Noreg', 'Norwegen\u200f', '🇳🇴']
```
Late workspace top-1 trajectory:
```text
  L27: Norway | L28: Norway | L29: Norway | L30: Norway | L31: Norway
  L32: Norway | L33: Norway | L34: Norway
```
Noisiest late layer top tokens:
```text
L27 entropy=0.838: [' Norway', ' Sweden', '丹麦', '挪威', ' Finland']
```
Cleanest late layer top tokens:
```text
L32 entropy=0.000: [' Norway', '挪威', ' Sweden', ' Denmark', ' Finland']
```


## ex_12509_1446356

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.7222476601600647`
- Workspace noise score: `0.5575090885162354`
- Quadrant: ``

Question:
```text
What is the capital of Empire of Japan?
```
Prediction:
```text
东京 (Tokyo) is the capital of the Empire of
```
Aliases:
```text
['Tokyo', 'Tōkyō', 'Tôkyô', 'Tokyo-to', 'Tokyo Metropolitan prefecture', 'Tōkyō-to', 'Tôkyô-to', 'Tokyo Metropolis', 'Tokio', 'Tokyo Prefecture']
```
Late workspace top-1 trajectory:
```text
  L27:东京 | L28:东京 | L29: Tokyo | L30: Tokyo | L31: Tokyo
  L32: Tokyo | L33:东京 | L34:东京
```
Noisiest late layer top tokens:
```text
L33 entropy=0.786: ['东京', ' Tokyo', ' Kyoto', '京都', 'Tok']
```
Cleanest late layer top tokens:
```text
L34 entropy=0.347: ['东京', ' Tokyo', '京都', 'Tok', ' Kyoto']
```


## ex_01584_6440806

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.4362862706184387`
- Workspace noise score: `0.6267780005931854`
- Quadrant: ``

Question:
```text
What genre is Pearl Jam?
```
Prediction:
```text
Alternative rock.  Pearl Jam is an American rock band formed
```
Aliases:
```text
['alternative rock', 'alternative music', 'alt-rock', 'alternative', 'alt rock', 'pop/rock', 'Alternative Rock']
```
Late workspace top-1 trajectory:
```text
  L27:摇滚 | L28:摇滚 | L29:摇滚 | L30:摇滚 | L31: rock
  L32: rock | L33: rock | L34: Alternative
```
Noisiest late layer top tokens:
```text
L34 entropy=1.363: [' Alternative', ' alternative', ' rock', 'alternative', 'Alternative']
```
Cleanest late layer top tokens:
```text
L29 entropy=0.019: ['摇滚', ' rock', '乐队', ' guitar', '-rock']
```


## ex_02045_5810347

- Correct primary: `None`
- Strict correct: `False`
- Expanded correct: `False`
- Label source: `llm_judge_ambiguous_excluded`
- Label quality: `ambiguous`
- Temporal unstable: `False`
- Exclusion reason: `llm_judge_ambiguous`
- Fuzzy suggested: `False`
- Judge verdict: `ambiguous` (medium)
- First content token prob: `0.9917780756950378`
- Workspace noise score: `1.8121743083000184`
- Quadrant: ``

Question:
```text
What genre is Jan Miense Molenaer?
```
Prediction:
```text
17th-century Dutch Golden Age painting. The answer is
```
Aliases:
```text
['genre painting', 'petit genre']
```
Judge reason:
```text
The model answer refers to '17th-century Dutch Golden Age painting' which is a historical period and style, while the accepted answers 'genre painting' and 'petit genre' are more specific art categories. The model answer is partially correct but not semantically equivalent to the accepted answers, and the term 'Dutch Golden Age' may be considered stale or time-sensitive in the context of art genre classification.
```
Late workspace top-1 trajectory:
```text
  L27:画家 | L28:画家 | L29:荷兰 | L30: Dutch | L31:荷兰
  L32: Bar | L33: Bar | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.575: [' Bar', ' Genre', 'genre', 'Genre', ' Flem']
```
Cleanest late layer top tokens:
```text
L27 entropy=0.666: ['画家', '艺术家', '油画', ' painter', '绘画']
```


## ex_01291_1664587

- Correct primary: `True`
- Strict correct: `False`
- Expanded correct: `True`
- Label source: `safe_contains`
- Label quality: `medium`
- Temporal unstable: `False`
- Exclusion reason: `None`
- Fuzzy suggested: `False`
- Judge verdict: `None` (None)
- First content token prob: `0.998867392539978`
- Workspace noise score: `1.1243807777762413`
- Quadrant: ``

Question:
```text
What genre is The Thing?
```
Prediction:
```text
1982 sci-fi horror film. The Thing is
```
Aliases:
```text
['horror film', 'horror movie', 'science fiction film', 'sci-fi film', 'science fiction movie', 'sci-fi movie', 'scifi film', 'scifi movie', 'sci fi film', 'sci fi movie', 'scifi-film', 'scifi']
```
Late workspace top-1 trajectory:
```text
  L27:科幻 | L28:科幻 | L29:科幻 | L30: horror | L31: horror
  L32: horror | L33: Sci | L34:1
```
Noisiest late layer top tokens:
```text
L33 entropy=2.256: [' Sci', ' sci', ' Horror', ' horror', '科幻']
```
Cleanest late layer top tokens:
```text
L30 entropy=0.096: [' horror', ' Horror', '科幻', '恐怖', '恐惧']
```

