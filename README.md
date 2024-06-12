# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

```bash
hdfs dfs -rm -r /user/sandbox/words
mapred streaming \
-input /user/sandbox/books \
-output /user/sandbox/words \
-mapper mapper_v2.py \
-reducer reducer_v2.py \
-file scripts/mapper_v2.py \
-file scripts/reducer_v2.py
```
