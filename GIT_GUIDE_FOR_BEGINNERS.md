# Git & GitHub Guide for Your Thesis

## 🎯 What You Need to Know

Think of Git as a "save game" system for your code, and GitHub as the cloud backup.

---

## 📝 The Basic Workflow

### Every time you work, follow these steps:

### 1️⃣ **PULL** - Get latest changes from GitHub
```bash
git pull origin main
```
**What it does:** Downloads any changes from GitHub to your Mac  
**When to do it:** Start of every work session  
**Why:** Ensures you have the latest version

---

### 2️⃣ **WORK** - Make your changes
- Edit files in your project
- Add new notebooks
- Run experiments
- Update documentation

---

### 3️⃣ **STATUS** - Check what changed
```bash
git status
```
**What it does:** Shows which files you modified  
**Output colors:**
- 🔴 Red = Modified but not staged
- 🟢 Green = Staged (ready to commit)
- ⚪ White = Untracked (new files)

---

### 4️⃣ **ADD** - Stage your changes
```bash
# Add specific file
git add filename.py

# Add all changed files
git add .

# Add all Python files
git add *.py

# Add a folder
git add notebooks/
```
**What it does:** Marks files to be included in your next snapshot  
**Think of it as:** Selecting which changes to save

---

### 5️⃣ **COMMIT** - Save a snapshot
```bash
git commit -m "Your descriptive message here"
```
**What it does:** Creates a save point with your changes  
**Message tips:**
- Be descriptive: ✅ "Add data preprocessing notebook"
- Not vague: ❌ "Updated stuff"
- Use present tense: "Add" not "Added"

**Examples:**
```bash
git commit -m "Add initial data exploration notebook"
git commit -m "Implement RQ-VAE encoder architecture"
git commit -m "Fix bug in semantic ID generation"
git commit -m "Update README with project overview"
```

---

### 6️⃣ **PUSH** - Upload to GitHub
```bash
git push origin main
```
**What it does:** Uploads your commits to GitHub  
**When to do it:** After every commit or at end of work session  
**Why:** Backs up your work and makes it accessible from Colab

---

## 🚀 Complete Example Workflow

Let's say you just created your first notebook:

```bash
# 1. Start your work session
cd /Users/zoislanaras/Thesis
git pull origin main

# 2. Create a new notebook (or edit files)
# ... you create 01_data_exploration.ipynb ...

# 3. Check what changed
git status
# Output: "Untracked files: notebooks/01_data_exploration.ipynb"

# 4. Add the file
git add notebooks/01_data_exploration.ipynb

# 5. Commit with message
git commit -m "Add initial data exploration notebook for Amazon reviews"

# 6. Push to GitHub
git push origin main

# ✅ Done! Your work is now backed up on GitHub
```

---

## 🔄 Accessing Files in Google Colab

Since you'll work in Colab, here's how to sync:

### Method 1: Clone Repository in Colab
```python
# In a Colab cell:
!git clone https://github.com/zoislan/semantic-ids-large-scale-recommendations.git
%cd semantic-ids-large-scale-recommendations
```

### Method 2: Pull Latest Changes (if already cloned)
```python
# In a Colab cell:
%cd semantic-ids-large-scale-recommendations
!git pull origin main
```

### Method 3: Mount Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')

# Then clone into Drive once:
# !git clone https://github.com/zoislan/semantic-ids-large-scale-recommendations.git /content/drive/MyDrive/Thesis
```

**Recommended:** Method 3 (Google Drive) - persistent across Colab sessions

---

## 📊 Working with Colab Notebooks

### Strategy 1: Store notebooks in GitHub
- Keep `.ipynb` files in your repo
- Commit and push after major changes
- Pull in Colab to get latest version

### Strategy 2: Save to Google Drive
- Work in Drive-mounted Colab
- Use Git for code files (`.py`, data processing scripts)
- Notebooks stay in Drive for quick iteration

**My recommendation:** Start with Strategy 1 (Git), switch to Strategy 2 if too slow

---

## ⚠️ Important Git Rules

### DO ✅
- Commit often (every meaningful change)
- Write clear commit messages
- Pull before you start working
- Push at end of each session
- Keep large data files OUT of Git (use `.gitignore`)

### DON'T ❌
- Don't commit large files (>100MB) - GitHub will reject them
- Don't commit data files - put them in `.gitignore`
- Don't commit `venv/` folder - already in `.gitignore`
- Don't commit API keys or passwords
- Don't use `git push --force` unless you know what you're doing

---

## 📁 What to Commit vs What to Ignore

### ✅ COMMIT (Track in Git):
- Python code (`.py` files)
- Jupyter notebooks (`.ipynb` files)
- Documentation (`.md` files)
- Configuration files (`requirements.txt`, `config.yaml`)
- Small test data files (<10MB)
- Analysis results (plots, tables)

### ❌ IGNORE (Don't track in Git):
- Large datasets (download separately)
- Trained models (save to Google Drive)
- Virtual environments (`venv/`, `.env/`)
- Cache files (`__pycache__/`, `.ipynb_checkpoints/`)
- Personal notes (use a `.gitignore`)
- API keys and secrets

---

## 🛠️ Useful Git Commands

### Check Repository Status
```bash
git status                 # What changed?
git log                    # Show commit history
git log --oneline          # Compact history
git diff                   # Show exact changes
```

### Undo Changes
```bash
# Undo changes to a file (not staged yet)
git checkout -- filename.py

# Unstage a file (undo git add)
git reset HEAD filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️ CAREFUL!
git reset --hard HEAD~1
```

### Branches (Advanced - optional for now)
```bash
git branch experiment      # Create new branch
git checkout experiment    # Switch to branch
git checkout main          # Back to main
git merge experiment       # Merge branch into main
```

---

## 🆘 Common Problems & Solutions

### Problem: "error: failed to push some refs"
**Cause:** Someone (maybe you from another computer) pushed changes  
**Solution:**
```bash
git pull origin main
git push origin main
```

### Problem: "merge conflict"
**Cause:** Same file edited in two places  
**Solution:**
```bash
# Open the conflicted file
# Look for <<<<<<< and >>>>>>>
# Edit to keep the version you want
git add filename.py
git commit -m "Resolve merge conflict"
git push origin main
```

### Problem: "fatal: not a git repository"
**Cause:** You're not in the right folder  
**Solution:**
```bash
cd /Users/zoislanaras/Thesis
```

### Problem: "large files detected"
**Cause:** Trying to commit files >100MB  
**Solution:**
```bash
# Remove the file from staging
git reset HEAD large_file.csv

# Add to .gitignore
echo "large_file.csv" >> .gitignore
git add .gitignore
git commit -m "Ignore large data files"
```

---

## 🎯 Your First Git Tasks

### Task 1: Update README
```bash
# Edit README.md in Cursor
# Then:
git add README.md
git commit -m "Update README with thesis description"
git push origin main
```

### Task 2: Create .gitignore
```bash
# Create the file (see next section)
git add .gitignore
git commit -m "Add gitignore for Python and data files"
git push origin main
```

### Task 3: Add your first notebook
```bash
# After creating a notebook:
git add notebooks/01_data_exploration.ipynb
git commit -m "Add data exploration notebook"
git push origin main
```

---

## 📚 Learning Resources

- **Git Basics:** https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
- **GitHub Guides:** https://guides.github.com/
- **Interactive Tutorial:** https://learngitbranching.js.org/
- **Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf

---

## 💡 Pro Tips

1. **Commit messages are for future you** - be descriptive!
2. **Commit atomically** - one logical change per commit
3. **Don't commit generated files** - models, datasets, cache
4. **Use GitHub Issues** - track TODOs and bugs
5. **README is your project homepage** - keep it updated

---

## When Working With Me (Cursor AI)

### What I'll tell you before Git operations:
- ✅ "I'll now add these files to Git"
- ✅ "This command will commit your changes"
- ✅ "Let me push this to GitHub"

### What I WON'T do without asking:
- ❌ Force pushes
- ❌ Deleting branches
- ❌ Committing without you knowing

### You're always in control!
- You can reject any command I propose
- You can modify commands before running them
- You can undo changes if needed

---

## 🎓 Remember

**Git is like a time machine for your code.**

Every commit is a save point you can return to. GitHub is your backup. Don't be afraid to experiment - you can always go back!

**Start simple:** Just master the pull → work → add → commit → push cycle. That's 90% of what you need!

