# Six Python Competitive Programming I/O Starters

These templates intentionally contain **NO solution algorithms**. Your only job is to replace `raise NotImplementedError(...)` inside each `solve()` function with your own algorithm, and `return` the answer. The rest handles judge input/output.

## Files, judge rules, and required return values

| Python file | Original problem | Judge I/O | `solve()` must return |
|---|---|---|---|
| `blocked_billboard.py` | [USACO 2017 Dec Bronze — Blocked Billboard](https://usaco.org/index.php?page=viewproblem2&cpid=759) | `billboard.in` → `billboard.out` | integer visible area |
| `fence_painting.py` | [USACO 2015 Dec Bronze — Fence Painting](https://usaco.org/index.php?page=viewproblem2&cpid=567) | `paint.in` → `paint.out` | integer painted length |
| `white_sheet.py` | [Codeforces 1216C — White Sheet](https://codeforces.com/problemset/problem/1216/C) | standard input → standard output | `True` if visible, otherwise `False` |
| `square_pasture.py` | [USACO 2016 Dec Bronze — Square Pasture](https://usaco.org/index.php?page=viewproblem2&cpid=663) | `square.in` → `square.out` | integer minimum area |
| `do_you_know_your_abcs.py` | [USACO 2020 Dec Bronze — Do You Know Your ABCs?](https://usaco.org/index.php?page=viewproblem2&cpid=1059) | standard input → standard output | three numbers `(a, b, c)` |
| `two_tables.py` | [Codeforces 1555B — Two Tables](https://codeforces.com/problemset/problem/1555/B) | standard input → standard output | minimum distance, or `-1` |

**Why some USACO files differ:** Problems *before* December 2020 use the exact named input/output files in their statements. From December 2020 onwards, USACO uses standard input/output instead. Codeforces uses standard input/output.

## How to work on a problem

1. Open its `.py` file.
2. Locate `def solve(...):`.
3. Delete the `raise NotImplementedError(...)` line.
4. Put **your algorithm** where the `# TODO` comment is. Return the specified result. Do not print from inside `solve()`.
5. Do not change `main()` unless you deliberately want to alter the provided judge I/O.
6. Submit **only the `.py` file** to the judge (not sample input files or the entire zip).

## Local testing

Run these commands **from the unzipped folder**.

### File-based USACO (sample `.in` files are already included)

```bash
python blocked_billboard.py  # reads billboard.in; creates billboard.out
python fence_painting.py     # reads paint.in; creates paint.out
python square_pasture.py     # reads square.in; creates square.out
```

After finishing the algorithms, open the resulting `.out` files to see your answers. To test custom cases, edit the corresponding `.in` files.

### Standard input/output problems

**macOS / Linux / Windows PowerShell (with normal input redirection support):**

```bash
python white_sheet.py < samples/white_sheet_input.txt
python do_you_know_your_abcs.py < samples/abcs_input.txt
python two_tables.py < samples/two_tables_input.txt
```

PowerShell may not support `<` input redirection in some versions. In that case, use `Get-Content samples/abcs_input.txt | python do_you_know_your_abcs.py`, replacing the filename and script as needed.

Expected answers are in `samples/expected_outputs.txt`.

**Note:** The starter files will intentionally stop with `NotImplementedError` until you write your solutions. That is by design, so you cannot accidentally submit a placeholder answer.

## Special reminders

- `blocked_billboard.py` is the **2017 original**, involving **two billboards and one truck**, not *Blocked Billboard II*.
- `do_you_know_your_abcs.py` reads exactly **seven numbers**, with **no leading N**.
- `two_tables.py` handles **T test cases** for you and outputs a number for each; floating-point answers are printed to 9 decimal places.
- `white_sheet.py` converts the Boolean you return into exactly `YES` or `NO`.
- For the old USACO problems, your current working directory must be where the `.in` files are located when testing locally.
