# Competitive Programming

My competitive programming solutions, work in progress, and practice templates in Python and C++.

| Folder | Contents |
| --- | --- |
| `codeforces/cpp/` | Codeforces C++ solutions and drafts |
| `codeforces/python/` | Codeforces Python solutions |
| `cses/` | CSES Problem Set practice |
| `usaco/` | USACO practice, including the `speeding/` sample files |
| `leetcode/` | LeetCode solutions and generated problem stubs |
| `atcoder/` | AtCoder practice |
| `practice/` | General exercises and experiments |
| `practice/drafts/` | Older, distinct drafts retained alongside newer versions |
| `practice/starters/io/` | Input/output templates and sample inputs; see its README |
| `practice/starters/usaco-simulation/` | USACO simulation scaffolds |

Some files are unfinished drafts or empty problem stubs. Their presence does not indicate an accepted solution.

## Running locally

Python example:

```sh
python3 cses/WeirdAlgorithm.py < input.txt
```

C++ example (using GCC with C++20 support):

```sh
g++ -std=c++20 -O2 codeforces/cpp/A_Watermelon.cpp -o /tmp/watermelon
/tmp/watermelon < input.txt
```

For programs using named input/output files, run from the folder containing the expected `.in` file. LeetCode snippets use the judge's provided types and harness.

Compiled binaries, Python caches, and local editor/test-runner state are ignored by Git.
