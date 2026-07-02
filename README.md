# 🐱 PurrScript

**A programming language that speaks cat.**

PurrScript is a transpiler that translates cat commands into Python. No more boring `print()`, only `meow()`. No more `True`, only `treat`.

---

## ⚙️ Installation

### Requirements
* Python 3.6+

### Quick Install

```bash
git clone https://github.com/FelineFantasy/PurrScript.git
cd PurrScript
python purrscript.py install
```

After installation, run `.purr` files from anywhere:

```bash
purr hello.purr
```

---

## 🧪 Example

1. Create a file named `hello.purr`:
    ```purrscript
    MR
    treat
    meow("Привет, я кот!")
    PR
    ```

2. Run the script:
    ```bash
    purr hello.purr
    ```

3. Expected output:
    ```text
    Привет, я кот!
    ```

---

## 📦 Commands Reference

| PurrScript | Python | Description |
| :--- | :--- | :--- |
| **`MR`** | `# program started` | Entry point |
| **`PR`** | `# program finished` | Exit point |
| **`treat`** | `treat = True` | Default variable |
| **`meow(...)`** | `print(...)` | Output |
| **`beg(...)`** | `input(...)` | Input |
| **`sniff`** | `if` | Conditional |
| **`peer`** | `elif` | Conditional |
| **`other_paw`** | `else` | Conditional |
| **`and_paw`** | `and` | Logical AND |
| **`or_paw`** | `or` | Logical OR |
| **`not_paw`** | `not` | Logical NOT |
| **`nap`** | `def` | Function definition |
| **`box`** | `class` | Class definition |
| **`bring`** | `return` | Return statement |
| **`hunt`** | `while` | Loop |
| **`zoom`** | `for` | Loop |
| **`hiss`** | `break` | Break loop |
| **`gimme`** | `import` | Import module |
| **`out_of`** | `from` | Import from |
| **`with_blanket`**| `with` | Context manager |
| **`as_paw`** | `as` | Alias |
| **`yowl`** | `raise` | Raise exception |
| **`purr(...)`** | `str(...)` | String cast |
| **`bite(...)`** | `int(...)` | Integer cast |
| **`lick(...)`** | `float(...)` | Float cast |
| **`mood(...)`** | `bool(...)` | Boolean cast |
| **`tail(...)`** | `list(...)` | List creation |
| **`basket(...)`** | `tuple(...)` | Tuple creation |
| **`clowder(...)`**| `set(...)` | Set creation |
| **`scent(...)`** | `dict(...)` | Dictionary creation |
| **`void_box`** | `None` | None type |
| **`claw(...)`** | `open(...)` | Open file |
| **`scratch(...)`**| `write(...)` | Write to file |
| **`sniff_file(...)`**| `read(...)` | Read file |
| **`close_door(...)`**| `close(...)` | Close file |
| **`hiss_error`** | `try` | Try block |
| **`catch_mouse`** | `except` | Except block |
| **`finally_nap`** | `finally` | Finally block |
| **`YES`** | `True` | Boolean True |
| **`NO`** | `False` | Boolean False |

---

## ⚠️ Custom Errors

* 🚨 **`EntryThresholdNotFound`** — missing `MR` at the beginning of the file.
* 🚨 **`ExitDoorAjar`** — missing `PR` at the end of the file.
* 🚨 **`NoSnacksError`** — missing required `treat` declaration.

---

## 👤 Author

- **FelineFantasy**
- **License**: MIT
