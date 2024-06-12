# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

To modify the maper/reducer python file, I needed to install vim on each nodes of the Hadoop cluster.
I create the following file and chmod to set the execute permissoin

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
