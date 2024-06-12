# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

I used the `bronte.txt` file at my data source to run the mapred stream improve script.

Works over text files with a Python3 installed and execute permissions.

To modify the maper/reducer python file, I needed to install vim on each nodes of the Hadoop cluster.
I create the following file and chmod to set the execute permissoin

# step 1
```bash
sgberhault@instance-20240607-040704:~$ cat install-vi.sh 
#sudo docker exec -it hadoop-sandbox-datanode-1 apt-get update
sudo docker exec -it hadoop-sandbox-datanode-1 apt-get -y install vim
#sudo docker exec -it hadoop-sandbox-namenode-1 apt-get update
sudo docker exec -it hadoop-sandbox-namenode-1 apt-get -y install vim
#sudo docker exec -it hadoop-sandbox-clientnode-1 apt-get update
sudo docker exec -it hadoop-sandbox-clientnode-1 apt-get -y install vim
#sudo docker exec -it hadoop-sandbox-nodemanager-1 apt-get update
sudo docker exec -it hadoop-sandbox-nodemanager-1 apt-get -y install vim
sgberhault@instance-20240607-040704:~$
```

# step 2
```bash
sandbox@clientnode:~/scripts$ chmod 777 *v2.py
sandbox@clientnode:~/scripts$ ls -lrt
total 16
-rwxrwxrwx 1 sandbox sandbox  189 Jun  7 04:29 mapper.py
-rwxrwxrwx 1 sandbox sandbox  606 Jun  7 04:29 reducer.py
-rwxrwxrwx 1 sandbox sandbox  856 Jun 12 17:27 mapper_v2.py
-rwxrwxrwx 1 sandbox sandbox 1054 Jun 12 17:33 reducer_v2.py
```

# step 3a
```bash
sandbox@clientnode:~/scripts$ hdfs dfs -rm -r /user/sandbox/words
Deleted /user/sandbox/words
```
# step 3b
```bash
sandbox@clientnode:~/scripts$ hdfs dfs -ls /user/sandbox/words
ls: `/user/sandbox/words': No such file or directory
```

# step 4
```bash
mapred streaming \
-input /user/sandbox/books \
-output /user/sandbox/words \
-mapper mapper_v2.py \
-reducer reducer_v2.py \
-file scripts/mapper_v2.py \
-file scripts/reducer_v2.py
```

# step 5
```bash
mapred streaming -input /user/sandbox/books/bronte.txt  -output /user/sandbox/words -mapper mapper_v2.py -reducer reducer_v2.py -file scripts/mapper_v2.py -file scripts/reducer_v2.py
2024-06-12 18:11:03,929 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [scripts/mapper_v2.py, scripts/reducer_v2.py] [/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar] /tmp/streamjob2697759388717242502.jar tmpDir=null
2024-06-12 18:11:05,778 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at resourcemanager/172.18.0.4:8032
2024-06-12 18:11:06,172 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at resourcemanager/172.18.0.4:8032
2024-06-12 18:11:06,587 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/sandbox/.staging/job_1718208270710_0002
2024-06-12 18:11:07,210 INFO mapred.FileInputFormat: Total input files to process : 1
2024-06-12 18:11:07,304 INFO mapreduce.JobSubmitter: number of splits:2
2024-06-12 18:11:08,090 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1718208270710_0002
2024-06-12 18:11:08,090 INFO mapreduce.JobSubmitter: Executing with tokens: []
2024-06-12 18:11:08,686 INFO conf.Configuration: resource-types.xml not found
2024-06-12 18:11:08,687 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2024-06-12 18:11:08,862 INFO impl.YarnClientImpl: Submitted application application_1718208270710_0002
2024-06-12 18:11:08,915 INFO mapreduce.Job: The url to track the job: http://resourcemanager:8088/proxy/application_1718208270710_0002/
2024-06-12 18:11:08,919 INFO mapreduce.Job: Running job: job_1718208270710_0002
2024-06-12 18:11:19,157 INFO mapreduce.Job: Job job_1718208270710_0002 running in uber mode : false
2024-06-12 18:11:19,159 INFO mapreduce.Job:  map 0% reduce 0%
2024-06-12 18:11:32,378 INFO mapreduce.Job:  map 50% reduce 0%
2024-06-12 18:11:33,387 INFO mapreduce.Job:  map 100% reduce 0%
2024-06-12 18:11:40,475 INFO mapreduce.Job:  map 100% reduce 100%
2024-06-12 18:11:41,494 INFO mapreduce.Job: Job job_1718208270710_0002 completed successfully
2024-06-12 18:11:41,626 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=1122341
                FILE: Number of bytes written=3182511
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=685451
                HDFS: Number of bytes written=112031
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters 
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=23384
                Total time spent by all reduces in occupied slots (ms)=11726
                Total time spent by all map tasks (ms)=23384
                Total time spent by all reduce tasks (ms)=5863
                Total vcore-milliseconds taken by all map tasks=23384
                Total vcore-milliseconds taken by all reduce tasks=5863
                Total megabyte-milliseconds taken by all map tasks=23945216
                Total megabyte-milliseconds taken by all reduce tasks=12007424
        Map-Reduce Framework
                Map input records=12726
                Map output records=122078
                Map output bytes=878179
                Map output materialized bytes=1122347
                Input split bytes=204
                Combine input records=0
                Combine output records=0
                Reduce input groups=10023
                Reduce shuffle bytes=1122347
                Reduce input records=122078
                Reduce output records=10023
                Spilled Records=244156
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=313
                CPU time spent (ms)=6390
                Physical memory (bytes) snapshot=727904256
                Virtual memory (bytes) snapshot=8625111040
                Total committed heap usage (bytes)=408944640
                Peak Map Physical memory (bytes)=255877120
                Peak Map Virtual memory (bytes)=2726035456
                Peak Reduce Physical memory (bytes)=217026560
                Peak Reduce Virtual memory (bytes)=3176886272
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=685247
        File Output Format Counters 
                Bytes Written=112031
2024-06-12 18:11:41,659 INFO streaming.StreamJob: Output directory: /user/sandbox/words
```

# step 6
```bash
sandbox@clientnode:~$ !101
hdfs dfs -ls /user/sandbox/words
Found 2 items
-rw-r--r--   1 sandbox sandbox          0 2024-06-12 18:11 /user/sandbox/words/_SUCCESS
-rw-r--r--   1 sandbox sandbox     112031 2024-06-12 18:11 /user/sandbox/words/part-00000
sandbox@clientnode:~$ !102
hdfs dfs -head /user/sandbox/words/part-00000
A 61
ACTUAL 1
AGREE 2
AGREEMENT 1
AND 1
ANY 3
ANYTHING 1
AS 1
ASCII 2
About 9
Above 1
Abstract 1
Accursed 1
Additional 1
Afraid 1
After 16
Afterwards 3
Ah 21
Aha 2
Alas 2
All 11
Always 1
Am 2
America 1
American 1
Among 1
An 12
And 259
Annie 1
Another 2
Answer 2
Any 3
Anybody 1
Apparently 1
April 2
Arabian 1
Archer 1
Archive 13
Are 30
Art 1
As 39
Ask 1
At 38
Atlantic 1
Attentive 1
August 2
Aunt 4
Author 1
Aw 2
Away 2
Ay 3
B 3
BE 1
BEFORE 1
BREACH 2
BUT 1
Bad 2
Badly 1
Bang 1
Banish 1
Baptists 1
Be 13
Because 7
Before 8
Begone 5
Being 3
Besides 9
Between 1
Beware 1
Bible 7
Bibles 1
Black 3
Blackhorse 1
Bonny 1
Book 1
Both 5
Branderham 6
Brethren 1
Bring 1
Brooad 1
Bud 3
But 159
By 17
C 5
CHAPTER 34
CONSEQUENTIAL 1
CONTRACT 1
Call 1
Can 7
Cannot 4
Careful 1
Catherine 379
Catherines 1
Cathy 124
Cave 2
Certainly 2
Chapel 2
Charlie 3
Chase 1
Cheer 1
Chevy 1
China 1
Christendom 1
Christian 5
Christmas 5
Churstmassandbox@clientnode:~$
```
# step 7
```bash
mkdir words2
hdfs dfs -copyToLocal /user/sandbox/words .
sandbox@clientnode:~/words2/words$ ls
_SUCCESS  part-00000
```
# step 8
```bash
sandbox@clientnode:~/words2/words$ awk '{printf("%s" , $1 ? "\033[34m" : "\033[0m")} {printf("%s\033[0m] : %s\n", $1, $2)}' part-00000 | sort -nrk 2 part-00000 > result_sort.txt
```
# step 9
```bash
cat result_sort.txt
sandbox@clientnode:~/words2/words$ more result_sort.txt 
and 4554
the 4479
I 4103
to 3585
of 2330
a 2325
he 1709
you 1690
her 1507
in 1495
his 1379
that 1195
it 1194
she 1135
was 1119
me 1060
my 1031
not 936
him 917
as 907
for 846
s 839
with 832
on 797
at 760
be 730
had 681
is 627
t 618
have 618
but 531
from 495
Heathcliff 475
by 463
would 440
He 413
Linton 404
your 390
if 382
Catherine 379
or 378
said 375
ll 368
so 348
were 345
an 314
out 313
Mr 312
no 303
this 294
up 291
all 290
are 286
when 282
could 276
The 276
we 273
into 273
one 271
```


