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

You can also use the `*` and `?` wildcards in paths (there are other globbing patterns too):
* `?` represent one joker character
* `*` represents any number of characters

**Examples:**\
Let we have a directory with the following files in it:
```
asd.txt    asd.csv    brekeke.txt
```
* `./asd.*` will match `asd.txt` and `asd.csv`
* `./asd.?` won't match anything
* `./asd.???` will match `asd.txt` and `asd.csv`
* `*.txt` will match `asd.txt` and `brekeke.txt`

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

### ls

ls lists the files at the provided paths:
```
ls ./Documents
```

Most handy switches to use with ls:
* `-a`  lists all files (even hidden files which name starts with a dot)
* `-l` uses long format with the following fields
```
-rwxrw-r--    10    root   root 2048    Jan 13 07:11 afile.exe
?UUUGGGOOOS   00  UUUUUU GGGGGG ####    MON DD XX:XX FILENAME
^ ^  ^  ^ ^    ^      ^      ^    ^      ^            ^- Filename.
| |  |  | |    |      |      |    |      \-------------- Time of last modification.
| |  |  | |    |      |      |    \--------------------- File Size OR for directory size of the metadata.
| |  |  | |    |      |      \-------------------------- Group Name (for example, Users, Administrators, etc)
| |  |  | |    |      \--------------------------------- Owner Account
| |  |  | |    \---------------------------------------- Link count (what constitutes a "link" here varies)
| |  |  | \--------------------------------------------- Alternative Access (blank means none defined, anything else varies)
| \--\--\----------------------------------------------- Read, Write and Special access modes for [U]ser, [G]roup, and [O]thers (everyone else)
\------------------------------------------------------- File type flag
```
* `-h` makes the sizes human readable: eg. instead of `2888249` in bytes it is printed as `2.8M`
Example for using switches:
```
ls -lah
```
***

### grep
Using grep we are able to search for files containing an expression or find section of files containing an expression.
grep uses regular expressions. Regex is an incredibly usefull tool, however it is not in the scope for this document. You can learn more about regex here: https://www.rexegg.com/regex-quickstart.php \
Eg. this will list all the lines which contain the string `"export"` :
```
grep "export" ~/.bashrc
```
Most useful switches:
* `-c` instead of returning the lines themselves, this will return the count of occurences of the expression
* `-l` instead of returning the lines themselves, this will return the files with matches to the expression
* `-i` ignore case
* `-n` returns the line number alongside with the line matched

For other oprions checkout the manual: `man grep`

### cp, mv, ln, rm

#### cp
Copy files to a specified destination:
```
cp source/path/file1.txt target/path/file1.txt
```
Use `-r` `--recursive` switch for multiple files and directories:
```
cp -r source/path/* target/path/
```

#### mv
Moves a file or directory to the target path:
```
mv source/path/file1.txt target/path/file1.txt
```
#### ln
Create a hard link to a file:
```
ln source/path/file1.txt target/path/file1.txt
```
A hard link can only be created on the same filesystem. If the original file is moved, the hard link will be still valid. \
Create symbolic(soft) link to a file:
```
ln -s source/path/file1.txt target/path/file1.txt
```
Soft links can span between filesystems. however they will break if the original file is renamed, moved or deleted. \
Links are very useful for example to make "shortcuts" for binaries or scripts to a folder which are in the `$PATH` environmental variable. That way the will be callable from anywhere. Don't overdo it.
#### rm
Remove a file or files form the filesystem:
```
rm file
```
You can remove empty directories with `rmdir`:
```
rm directory
```
Handy switches:
* `-r` removes files and directories recursively. You can remove non empty folders with this command
* `-f` force remove: won't prompt for warning (Only use this if you must)
* `-d` remove **empty** directories
Example:
```
rm -r ./nonempty-dir
```

***

### Running scripts

```
./script.sh
# or
./script.py
```
These will only work if the interpreter is specified with a shebang (#!) in the beginning of the source file.\
E.g:
```
#!/usr/bin/bash

# or

#!/usr/bin/python
```
To find out where your interpretter lives, you can use the `which` command eg.: `which python` or `which bash` 

If it is not specified in the script, the user should call the interpretter explicitly:
```
bash ./script.sh

# or

python ./script.py
```

***

### chmod
By default linux don't give execute permission for new files.
```
touch script.sh
./script.sh

# OUTPUT:
bash: permission denied: ./script.sh
```

chmod command can change permissions to file. \
For example this makes script.sh executable:
```
chmod +x script.sh
```

Permissions is an important subject. However, it is not in the scope of this document. To learn more about the basics of unix/linux permissions, you can visit: \
https://www.redhat.com/sysadmin/linux-file-permissions-explained

Remember, use `ls -l` command to check permissions 


## SSH 
Connect to remote server on ssh:
```
ssh <user>@<server>
# ssh will prompt you for your password
```

### ssh tunneling

ssh tunnel allows to forward port from a remote machine securely.

ssh -fNL <LOCALPORT>:<serveradress>:<PORT> <user>@<server>
* `-f` allows to run it in the background
* `-N` tells not to try reading a command from standard input
* `-L` opens a local port

In this case remote host `8001` port will be forwared to local `8000` port


example run  on local pc:

```
ssh -fNL 8000:localhost:8001 <username>@minerva
```

### scp
Copy files to/from remote server:
you can use `-r` here as well as with `cp`
```
scp file.txt <username>@minerva://storage01/<username>/
```


###  BIOMAG GPU servers:

- minerva
- diana
- persephone

***

## nvidia-smi

On the server this will list the nvidia video cards. It will also display their status and usage. \
You can only use this locally if you have nvidia video card with proprietary drivers installed.

```
nvidia-smi  
```
Device IDs are underlined with red: \
<img src='images/nvidiasmi.png'><br>

You can have a simplified list of the devices via `nvidia-smi -L`, This will list the device ids, device names, along with their UUID.

To restrict videocard usage you can specify the device IDs in your python script or set the CUDA_VISIBLE_DEVICES environmental variable:
* If you want to select the devices only for one run
execute your script with `CUDA_VISIBLE_DEVICES=deviceid(s)` as a script parameter.
* If you are going to use the same device throughout your session, you can just export it as:
`export CUDA_VISIBLE_DEVICES=deviceid(s)`

This example will run the script on the  0 and 1 ID GPUs
```
CUDA_VISIBLE_DEVICES=0,1 python3 train_deep_learning_important_unique_word_champion_segmentation.py
```
This will do the same for multiple training:
```
export CUDA_VISIBLE_DEVICES=0,1
python3 train_deep_learning_important_unique_word_champion_segmentation.py
python3 train_deep_learning_important_something_else.py
```

## Redirection and Pipeing

In linux we can manipulate how a program uses is's STDIN (input), STDOUT (output), and STDERR (error output) streams.

### Redirection

You can redirect a programs output from STDOUT to a file with the `>` operator.
eg:
```
ls -lah > directory_contents.txt
```
You will see that the terminal won't display the results this time since it was redirected to `directory_contents.txt`. Open the new file and check out it's content.
If we try it again we would overwrite the file we just created. we can append to existing files with the `>>` operator:
```
ls -lah >> directory_contents.txt
```
We can also redirect the STDERR stream. This is very useful for logging purposes. To do this you can use the `2>` operator:
```
not_existing_app 2> errors.txt
```
You will see that the error message is written into `bash: not_existing_app: command not found...` is logged into the file. To append errors we can use `2>>`. Main difference is if we use simple `>` redirect the error wouldn't be logged in the file, it would be printed to the console. \
Redirecting errors also very useful if we are not interested in the errors at all. Eg. We can run any program in the background with `&` like this: `firefox &`. \
Most of the time we are not really insterested in the warnings/errors out browser throws at us on STDERR. In these cases we can redirect the STDERR to `/dev/null`. Anything that goes to `/dev/null` is discarded:
```
firefox 2> /dev/null &

# or we can discard both STDIN and STDERR:

firefox > /dev/null 2>&1 &
```

### Piping

Piping is a very powerfull Unix concept. With the pipe operator we are able to send data between multiple processes on the fly without writing it on disk.
Eg.:
```
ls -lah | grep "^d" | wc -l
```
This will give you how many directory tou have in the current dir `ls -lah` lists every file/directory in current dir. It's output is piped into `grep "^d"`'s input. `grep "^d"` filters for every line which starts with a `"d"` and pipe it's output to `wc -l`'s input. `wc -l` counts how many lines there are in `grep "^d"`'s outut. You can also redirect the result ot a file as we did it before:
```
ls -lah | grep "^d" | wc -l > num_dirs.txt
```
You can do more with pipes and redirects. To learn more visit:
https://ryanstutorials.net/linuxtutorial/piping.php


## Process handling basics

### ps
Lists all proccesses running in the current shell:
```
ps
```
This will most likely only list the current shell interpreter and ps. Let's add a new process to the current shell in the background:
```
sleep 100000 &
ps
```

### kill
To kill sleep we need to check it's process ID in ps:
```
ps

# MY OUTPUT:
#    PID TTY          TIME CMD
#   3727 pts/0    00:00:01 zsh
# 172339 pts/0    00:00:00 sleep     <--- This is what we want to terminate
# 172361 pts/0    00:00:00 ps

kill 172339
```
If a foreground process get stuck or you would  like to cancel it use `CTRL +  C`

### htop
htop is an interactive process viewer. It will list the CPU, RAM usage and processes similar to task manager. You can also send signals to processes. (such as SIGTERM to kill a process)

htop is not always installed to linux distros by default. You can install it with your package manager:
Debian/Ubuntu based distros:
```
sudo apt install htop
```
Fedora and other distros which use dnf:
```
sudo dnf install htop
```
Arch based distros:
```
sudo pacman -S htop
```
Usage:
```
htop
```
You can monitor all running proceses in this program, order your programs on CPU/mem usage, search in the list, you can even trminate them from here.


## Virtualenv

Virtualenv is a tool to create isolated Python environments. This will  help you to keep your projects organized.

From python 3.3+ venv module is part of python and can be used as:
```
python -m venv envname
# OR
python3 -m venv envname
# this depends on the linux distribution
```
For older python versions you need to install virtualenv.
To install virtualenv:
Ubuntu:
```
sudo apt install python3-venv
```
Fedora:
```
sudo dnf install python3-virtualenv
```
Arch:
```
sudo pacman -S python-virtualenv
```

### Create virtualenv 
```
virtualenv path/to/env 
```

select python  verison:
to select python verison add the path of installed python like `/bin/python`


### Activate virtualenv

#### Linux 
```
source path/to/env/bin/activate
```
  
#### Windows
Use Powershell or gitbash
if you are not enabled to run scripts, then run in powershell
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

Start a new session
```
tmux
```
Exit from that session
```
tmux detach
```
Attach  the first session

```
tmux a -t0
```

#### Commands

vertical split - `ctrl b + %`

horizontal split - `ctrl b + "`

Switch between  panes - `ctrl b + arrow`

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

ssh -fNL 8000:localhost:8001 user@server


## GIT

Install git, on Ubuntu it is install by default. On windows it is suggest to install git bash 

Download a repository
```
git clone <url-to-repositry>
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

add files/folders/globs to the `.gitignore` file. These files won't be tracked by git and won't be uploaded to the remot repository either. Add for example images, build files or the venv.

This example will ignore build, dist __pychache__ folders, files with png and spec extenstion. Also it will track png files from images folder.

```
build
dist
__pycache__
*.png
!images/*.png
*.spec
```

# Windows softwares

git bash https://www.git-scm.com/downloads \
VSCODE https://code.visualstudio.com/ \
Bitwise https://www.bitvise.com/ssh-client-download

# Homework

- Push your python code into a repository that uses GPU, generates output (for example images, tables, texts,...)
- Connect to a server remotely. 
- Download your code.
- Check for avaliable gpus
- Run you code on one free GPU
- Download your results or model from server
