 🐱 PurrScript

A programming language that speaks cat.

PurrScript is a transpiler that translates cat commands into Python. No more boring `print`, only `meow`. No more `True`, only `treat`.

---

## ⚙️ Installation

### Requirements
- Python 3.6+

### Quick Install

git clone https://github.com/FelineFantasy/PurrScript.git
cd PurrScript
python purrscript.py install

After installation, run `.purr` files from anywhere:

purr hello.purr

---

## 🧪 Example

Create a file `hello.purr`:

MR
treat
meow("Привет, я кот!")
PR

Run:

purr hello.purr

Output:

Привет, я кот!

---

## 📦 Commands

PurrScript        | Python
------------------|-----------------------
MR                | # program started
PR                | # program finished
treat             | treat = True
meow(...)         | print(...)
beg(...)          | input(...)
sniff             | if
peer              | elif
other_paw         | else
and_paw           | and
or_paw            | or
not_paw           | not
nap               | def
box               | class
bring             | return
hunt              | while
zoom              | for
hiss              | break
gimme             | import
out_of            | from
with_blanket      | with
as_paw            | as
yowl              | raise
purr(...)         | str(...)
bite(...)         | int(...)
lick(...)         | float(...)
mood(...)         | bool(...)
tail(...)         | list(...)
basket(...)       | tuple(...)
clowder(...)      | set(...)
scent(...)        | dict(...)
void_box          | None
claw(...)         | open(...)
scratch(...)      | write(...)
sniff_file(...)   | read(...)
close_door(...)   | close(...)
hiss_error        | try
catch_mouse       | except
finally_nap       | finally
YES               | True
NO                | False

---

## ⚠️ Errors

- EntryThresholdNotFound — missing MR at the beginning
- ExitDoorAjar — missing PR at the end
- NoSnacksError — missing treat

---

## 👤 Author

- FelineFantasy
- License: MIT
