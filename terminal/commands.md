# Terminal commands 

## Useful commands on Linux
Change directory with
cd absolute or relative path 
```
cd /absolutepath/documents/
```

Run shell script
bash script.sh or 
```
./script.sh
```
list files
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
This will list the nvidia video cards, usage and status
```
nvidia-smi  
```
This will list the CPU, RAM usage and processes  similar to task manager

htop

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

create ssh tunnel  for  monitoring

ssh -f -n -L LOCALPORT:serveradress:PORT user@server

this will forward remote host 8001 port to local 8000 port


example run  on local pc:
```
ssh -f -n -L 8000:localhost:8001
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



Copy files to remote server:

```
scp file.txt ```username```@minerva://storage01/```username```/
```


 Windows software

VSCODE https://code.visualstudio.com/ <br>
Bitwise
https://www.bitvise.com/ssh-client-download <br>

# Homework


- Push your python code into a repository
- Connect to server  remotely. 
- Download your code.
- Check for avaliable gpus
- Run you code on one free GPU
- Download your  result or modell from server
