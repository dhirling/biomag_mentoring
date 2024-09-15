# Terminal commands 

## Useful commands on Linux

### less
Open text files in a scrollable way:
```
less test.txt
```
You can navigate the file using the arrow keys.\
Quit the file by hitting q.\
Note: less does not have to read the entire input file in one go, so it is very handy to open large files.

***

### man
Open system manual pager for installed programs
```
man less
```
Man is helpful to explore a CLI program's expected options, arguments and other capabilities.

***

### pwd
Print working directiory (same as the current directory)
```
pwd
```

#### Path basics
There are some special paths in linux:
* `.` relative path to the current directory
* `..` relative path to a directory a level above the current directory
* `/` absolute path to the root directory
* `~` (tilde) this is an absolute path to the logged in user's home directory, It is defined in the envoronmental variable `$HOME`

Examples for relative path: `./Document` or `../../dev/null` \
Examples for absloute paths: `/home/username/Document` or `~/Document`

***

### cd
Change the current directory to the path provided:
```
cd ~/Documents/
```
If a path is not provided cd takes you to your home directory (~):
```
cd
```
A dash as an argument will take you to the previous directory visited:
```
cd -
```
***



Run shell script
bash script.sh or 
```
./script.sh
```
### ls

ls lists the files at the provided paths:
```
ls
```

Use switches to  get more  details
"a" will add dates, "l"  will write the  permissions
```
ls -al
```



copy file
```
cp source/path/file1.txt target/path/file1.txt
```
move file

```
mv source/path/file1.txt target/path/file1.txt
```
Delete file
```
rm -rf file
```


chmod command can change permissions to file
For example this makes script.sh executable
```
chmod +x script.sh
```

Use ls command to check permissions 
ls -l
This will list the nvidia video cards, usage and status. 
Devices Ids underlined with red.
```
nvidia-smi  
```

<img src='images/nvidiasmi.png'><br>

To restrict videocard usage to  number you can specify it  your python code
or

run your script with "CUDA_VISIBLE_DEVICES=deviceid(s)"

This example will run the script on the  0 and 1 ID GPUs
```
CUDA_VISIBLE_DEVICES=0,1 python3 train_deep_learning_important_unique_word_champion_segmentation.py
```

This will list the CPU, RAM usage and processes  similar to task manager
```
htop
```

you can kill  processes using this command


kill <check_for  pid in htop example>
```
kill 30850
```

if you have a stuck  process  or  you would  like  to cancel it  use

CTRL +  C


## SSH 
connect to remote server on ssh:

ssh user@server
password

### ssh tunneling

Ssh tunnel allows to forward port from a remote machine securely.

ssh -f -n -L LOCALPORT:serveradress:PORT user@server

In this case remote host 8001 port will be forwared to local 8000 port


example run  on local pc:
-f and -N commands allow to run it in background
```
ssh -f -N -L 8000:localhost:8001 user@server

```

## Scp
Copy files to remote server:

```
scp file.txt ```username```@minerva://storage01/```username```/
```


##  BIOMAG GPU servers:

- minerva
- diana
- persephone



## Virtualenv

Virtualenv is a tool to create isolated Python environments. This will  help you to keep your projects organized.

### Create virtualenv 
virtualenv path/to/env 

select python  verison:
to select python verison add the path of installed python like

/bin/python


### Activate virtualenv

Linux 
```
source path/to/env/bin/activate
```
  
Windows 
Use windows Powershell  or gitbash
if not  enabled to run scripts  run in powershell
```
set-executionpolicy remotesigned
```

```
.\path\to\env\Scripts\activate
```

### python package manager PIP

Install python packages with PIP

```
pip install opencv-python
```

If you have multiple package collect them into a requirements.txt file  and  
```
pip install -r requirements.txt
```





## Tmux

Tmux is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.

start a new session
```
tmux
```
exit from that session
```
tmux detach
```
attach  the first session

```
tmux a -t0
```

Commands

vertical split<br>
ctrl b + %
horizonatal split  <br> 
ctrl b + "

switch between  panes

ctrl b + arrow <br> 


Link to more :

https://tmuxcheatsheet.com/


## Jupyter server
Login to the server using ssh<br>
Create a virtual  enviroment for you project

```
pip install jupyter-notebook
```

Run jupyter server with the following command, set the port with --port 
```
jupyter-notebook --no-browser --port=8001
```



On local pc, create ssh tunnel that allows port forwarding

ssh -f -N -L 8000:localhost:8001 user@server





## GIT

Install git, on Ubuntu it is install by default. On windows it is suggest to install git bash 

Download a repository
```
git clone repositry
```
This will list the changes that are not commited
```
git status
```

```
git add <file_that changed>
```
```
git commit -m " a commit message like i have added a new function or changed this function"
```
```
git push origin <branch>
```
```
git checkout <branch>
```

add ".gitignore" file list the files that should not be uploaded: for example images, buld files  or virtualenv.
This example will ignore build,  dist __pychache__ folders,  files with  png,  and  spec  extenstion, and will  allow png files from  images  folder

```
build
dist
__pycache__
*.png
!images/*.png
*.spec
```




 # Windows softwares
 <br>
git bash https://www.git-scm.com/downloads
VSCODE https://code.visualstudio.com/ <br>
Bitwise
https://www.bitvise.com/ssh-client-download <br>

# Homework


- Push your python code into a repository that uses GPU, generates output (for example images, tables, texts,...)
- Connect to a server remotely. 
- Download your code.
- Check for avaliable gpus
- Run you code on one free GPU
- Download your results or model from server
