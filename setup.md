# Setup & Orientation

Complete these steps **before the lab starts** if possible. If not, work through them at the beginning of the session.

## 1. Clone the Repository

```bash
git clone https://github.com/rs-kellogg/krs-summer-2026-lab.git
cd krs-summer-2026-lab
```

## 2. Verify Python

You need Python 3.9+ and `pandas`. On the Kellogg Linux Cluster:

```bash
module load python/3.11   # or your preferred version
pip install --user pandas pytest
```

Confirm it works:

```bash
python starter-code/firm_analysis.py
# Expected: "done" printed, and starter-code/output/summary.csv created
```

## 3. Verify R

You need R 4.x with `tidyverse` and `testthat`. On the Kellogg cluster:

```bash
module load R/4.3
```

In an R session:

```r
install.packages(c("tidyverse", "testthat", "optparse"))
```

## 4. Verify Your AI Tool

::::{tab-set}

:::{tab-item} GitHub Copilot CLI
```bash
gh copilot --version
# Should print something like: 1.x.x
```

If not installed, see the [Copilot CLI install instructions (macOS & Linux)](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli#installing-with-the-install-script-macos-and-linux) or run:

```bash
curl -fsSL https://gh.io/copilot-install | bash
```
:::

:::{tab-item} Claude Code CLI
```bash
claude --version
# Should print something like: claude 1.x.x
```

If not installed, see the [Claude Code install instructions (macOS & Linux)](https://code.claude.com/docs/en/setup#install-claude-code) or run:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```
:::

::::

## 5. Initialize Version Control

Even though you cloned a git repo, let's start fresh to practice the full workflow:

```bash
# (If you cloned the lab repo, skip this — you already have git history)
# If working in a fresh directory:
git init
git add .
git commit -m "initial commit: starter code and data"
```

:::{important}
Before moving on, confirm you have:

- [ ] `starter-code/output/summary.csv` was created when you ran `firm_analysis.py`
- [ ] `gh copilot --version` or `claude --version` returns a version number
- [ ] `git log --oneline` shows at least one commit
:::

---

**Next: [Part 1 · Introduction](part1-intro.md) →**
