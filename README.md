# <p align=center> PacLean <sup><sub><sup>*made with [Textual](https://textual.textualize.io/)*</sup></sub></sup> </p>
#### <p align=center> PacLean is an interactive way to clean up explicitly installed packages on Arch Linux </p>

<sub>*recorded with [asciinema](https://asciinema.org/)*</sub>
![Demo](demo.gif)

---

### <ins> Prerequisites </ins>

This requires a few packages for full functionality (all of which can be found in the `extra` repository):

- [*uv*](https://github.com/astral-sh/uv) - Python package manager
- *expac* - used to get the size of packages
- \**pacman-contrib* - used to clear the pacman cache

<sub> \* *optional* </sub>

---

### <ins> Usage </ins>

For now, until I package this, you'll want to do the following:

1. Clone the repo:
   
   ```
   git clone https://github.com/eleinah/paclean.git
   ```

2. Enter the `paclean` directory and run:

   ```
   uv run main.py
   ```
   > This should automatically create a virtual environment and install the necessary packages.

3. Use the arrow keys to move around, `Tab` to switch focus between panes, and `Space`/`Enter` to make a selection

`Ctrl+Q` can be used to quit.

---

### <ins> Issues </ins>

If you experience any issues, feel free to open an issue here on GitHub. **Please let it be known that this may not run as smooth on older/weaker hardware** - this is something on my TODO I need to get around to.

---

<sub> *I will be evolving this project by rewriting it in Go and giving it a different name - stay tuned! More functionality and speed!* </sub>
