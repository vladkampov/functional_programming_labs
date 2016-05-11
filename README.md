# Functional programming in NTUU "KPI"
*Few pshe-notation*
![Dancing cat](http://img.photobucket.com/albums/v105/lahgs/animations/Cat.gif)
## Dependencies
All you need is install CLISP by `sudo apt-get install clisp` in your UNIX system.

## Usage
### Labs 1-6
To run lab just start `clisp` in your terminal. 
After that load necessary lab into it by `(load "labX_X.lisp")`
Now you can use following function for current lab by `(function param '(list like param))`. For example:
```
[1]> (load "lab6_10.lisp")
;; Loading file lab6_10.lisp ...
;; Loaded file lab6_10.lisp
T
[2]> (allSubsets '(a b c)) ; Function that returned all subsets of current set.
(NIL (C) (B) (B C) (A) (A C) (A B) (A B C))
```
And for get out of this hellish environment use `(bye)`.

*And never forget about polish pshe-notation.* **NEVER!**
![POLSHA STRONG](http://all-reg.net/templates/exet/images/tegstrong.png)

### Labs 7-9
This labs are written in Python, so to run you need to go to lab work directory and:
```bash
virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install -r requirements.txt
python main.py
```
Enjoy! (*Now you can forget about polish notation*)