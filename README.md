# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

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
hdfs dfs -rm -r /user/sandbox/words
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
mapred streaming -input /user/sandbox/books -output /user/sandbox/words -mapper mapper_v2.py -reducer reducer_v2.py -file scripts/mapper_v2.py -file scripts/reducer_v2.py
2024-06-12 17:55:34,054 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [scripts/mapper_v2.py, scripts/reducer_v2.py] [/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar] /tmp/streamjob10762390395523043863.jar tmpDir=null
2024-06-12 17:55:35,887 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at resourcemanager/172.18.0.4:8032
2024-06-12 17:55:36,165 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at resourcemanager/172.18.0.4:8032
2024-06-12 17:55:37,068 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/sandbox/.staging/job_1718208270710_0001
2024-06-12 17:55:38,365 INFO mapred.FileInputFormat: Total input files to process : 3
2024-06-12 17:55:38,477 INFO mapreduce.JobSubmitter: number of splits:3
2024-06-12 17:55:39,162 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1718208270710_0001
2024-06-12 17:55:39,162 INFO mapreduce.JobSubmitter: Executing with tokens: []
2024-06-12 17:55:39,571 INFO conf.Configuration: resource-types.xml not found
2024-06-12 17:55:39,572 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2024-06-12 17:55:40,414 INFO impl.YarnClientImpl: Submitted application application_1718208270710_0001
2024-06-12 17:55:40,499 INFO mapreduce.Job: The url to track the job: http://resourcemanager:8088/proxy/application_1718208270710_0001/
2024-06-12 17:55:40,505 INFO mapreduce.Job: Running job: job_1718208270710_0001
2024-06-12 17:55:55,018 INFO mapreduce.Job: Job job_1718208270710_0001 running in uber mode : false
2024-06-12 17:55:55,020 INFO mapreduce.Job:  map 0% reduce 0%
2024-06-12 17:56:14,357 INFO mapreduce.Job:  map 33% reduce 0%
2024-06-12 17:56:15,365 INFO mapreduce.Job:  map 100% reduce 0%
2024-06-12 17:56:24,480 INFO mapreduce.Job:  map 100% reduce 100%
2024-06-12 17:56:25,511 INFO mapreduce.Job: Job job_1718208270710_0001 completed successfully
2024-06-12 17:56:25,733 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=3107906
                FILE: Number of bytes written=7466233
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1880162
                HDFS: Number of bytes written=167484
                HDFS: Number of read operations=14
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters 
                Killed map tasks=1
                Launched map tasks=3
                Launched reduce tasks=1
                Data-local map tasks=3
                Total time spent by all maps in occupied slots (ms)=54048
                Total time spent by all reduces in occupied slots (ms)=16010
                Total time spent by all map tasks (ms)=54048
                Total time spent by all reduce tasks (ms)=8005
                Total vcore-milliseconds taken by all map tasks=54048
                Total vcore-milliseconds taken by all reduce tasks=8005
                Total megabyte-milliseconds taken by all map tasks=55345152
                Total megabyte-milliseconds taken by all reduce tasks=16394240
        Map-Reduce Framework
                Map input records=35379
                Map output records=332971
                Map output bytes=2441958
                Map output materialized bytes=3107918
                Input split bytes=307
                Combine input records=0
                Combine output records=0
                Reduce input groups=14400
                Reduce shuffle bytes=3107918
                Reduce input records=332971
                Reduce output records=14400
                Spilled Records=665942
                Shuffled Maps =3
                Failed Shuffles=0
                Merged Map outputs=3
                GC time elapsed (ms)=496
                CPU time spent (ms)=10950
                Physical memory (bytes) snapshot=1045041152
                Virtual memory (bytes) snapshot=11356282880
                Total committed heap usage (bytes)=720371712
                Peak Map Physical memory (bytes)=295383040
                Peak Map Virtual memory (bytes)=2729447424
                Peak Reduce Physical memory (bytes)=218783744
                Peak Reduce Virtual memory (bytes)=3174785024
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=1879855
        File Output Format Counters 
                Bytes Written=167484
2024-06-12 17:56:25,735 INFO streaming.StreamJob: Output directory: /user/sandbox/words
```
