REFEREE succ. 13, packet P-N5-STAU audit question (1). Own tools, no lane code.
- closure2.py: `git show ca0a4e97:docs/RESULTS.md > /tmp/R.md; python3 -I closure2.py /tmp/R.md R48 R50 > closure_R48_R50.txt`
  (prints the closure, the edges, and every excluded match: REFEREE-2 doc names, L-RED item numbers, labels; range starts like "R19-R22"
  are shown as excluded but are real citations whose members are all in the closure).
- fl.txt: the packet's 66 files (docs/ paths). hits_mine.txt (108) / hits_extended.txt (172): grep hits over those files at ca0a4e97
  (file names were written as <dir>__<name>.md copies; read them with `git show ca0a4e97:docs/<dir>/<name>.md`).
