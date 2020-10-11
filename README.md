# step 1
MySQL installed
execute sql statement to create database tables

# step 2
Anaconda installed
create a virtual environment for this project  
    ```  
      conda create --name weather python=3.6  
    ```
then activate it  
    ```
      conda activate weather  
    ```
install requirements  
    ```
      pip install requirements.txt
    ```
# step 3 
run this project  
First, get the data  
```
  python main.py  
```
After the first step is over, run web_api to generate API  
```
  python web_api.py  
```
