# Google Colab Workflow Guide

## 🔄 Do I Need to Do This Every Time?

### **Short Answer:**
- **Mount Drive:** YES (every new session)
- **Clone Repo:** NO (only first time)
- **Pull Changes:** YES (to get updates)

---

## 📋 Complete Workflow

### **🆕 FIRST TIME ONLY (Initial Setup):**

```python
# Cell 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
# ⚠️ You'll need to click the link and authorize Google Drive access

# Cell 2: Clone your repository into Drive
!git clone https://github.com/zoislan/semantic-ids-large-scale-recommendations.git /content/drive/MyDrive/Thesis

# Cell 3: Navigate to project
%cd /content/drive/MyDrive/Thesis

# Cell 4: List files to confirm
!ls -la
```

**After this, your files live permanently in Google Drive!**

---

### **🔁 EVERY NEW SESSION (Regular Workflow):**

**Every time you open a new Colab notebook, run these:**

```python
# Cell 1: Mount Drive (required every time - Colab forgets after closing)
from google.colab import drive
drive.mount('/content/drive')

# Cell 2: Navigate to your project
%cd /content/drive/MyDrive/Thesis

# Cell 3: Pull latest changes from GitHub
!git pull origin main

# Cell 4: Check GPU
import torch
print(f"GPU Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")

# ✅ Now you're ready to work!
```

---

## 🎯 Why This Workflow?

### **Why Mount Drive Every Time?**
- Colab notebooks are temporary VMs (virtual machines)
- When you close the tab, the VM is destroyed
- Google Drive persists your files permanently
- Mounting connects the new VM to your Drive

### **Why Pull from GitHub?**
- If you made changes on your Mac (with Cursor) and pushed to GitHub
- Pull downloads those changes to Colab
- Keeps everything in sync

---

## 📂 Directory Structure in Colab

After setup, your structure looks like:

```
/content/drive/MyDrive/Thesis/
├── notebooks/              ← Your Jupyter notebooks
├── data/
│   ├── raw/               ← Original datasets
│   ├── processed/         ← Cleaned data
│   └── embeddings/        ← Item embeddings
├── models/                ← Saved model checkpoints
├── results/               ← Experiment results
├── papers/                ← Research papers
└── src/                   ← Python code modules
```

---

## 🔄 Full Development Cycle

### **Scenario 1: Working in Colab Only**

1. Open Colab notebook
2. Mount Drive + navigate to project
3. Pull latest changes
4. Do your work (train models, analyze data)
5. Files auto-save to Drive (notebooks, models, results)
6. Close Colab when done

**Next session:** Repeat steps 1-3

---

### **Scenario 2: Working with Cursor + Colab**

#### **On Mac (with Cursor):**
```bash
# Make changes to code
# Edit files, add new functions, etc.

# Commit changes
git add .
git commit -m "Add new preprocessing function"
git push origin main
```

#### **In Colab:**
```python
# Mount and navigate (every session)
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/Thesis

# Get the changes from Mac
!git pull origin main

# ✅ Now you have the latest code from Cursor!
```

---

## 💾 Saving Your Work

### **What Saves Automatically:**
- ✅ Colab notebooks (auto-save to Drive)
- ✅ Any files you create in `/content/drive/MyDrive/Thesis/`

### **What You Need to Save Manually:**
- ⚠️ Model checkpoints (use `torch.save()`)
- ⚠️ Processed data (use `pd.to_csv()` or `np.save()`)
- ⚠️ Results and plots (use `plt.savefig()`)

### **Example: Saving Model Checkpoint**
```python
# Save model
torch.save(model.state_dict(), '/content/drive/MyDrive/Thesis/models/rqvae_epoch10.pt')

# Load model later
model.load_state_dict(torch.load('/content/drive/MyDrive/Thesis/models/rqvae_epoch10.pt'))
```

---

## ⚠️ Important Colab Tips

### **1. Runtime Disconnects**
- Colab disconnects after ~90 minutes of inactivity
- Colab Pro: ~24 hours max runtime
- **Solution:** Save checkpoints frequently!

```python
# Save checkpoint every N epochs
if epoch % 5 == 0:
    torch.save(model.state_dict(), f'models/checkpoint_epoch{epoch}.pt')
```

### **2. GPU Limitations**
- Free Colab: Limited GPU hours per day
- If you run out: wait 12-24 hours or upgrade to Colab Pro
- **Check usage:** Settings > Resource usage

### **3. Large Files**
- Don't store huge datasets in GitHub
- Store in Drive: `/content/drive/MyDrive/Thesis/data/`
- Download datasets directly in Colab

### **4. Package Installation**
- Packages reset every session
- Install at the start of each notebook:
```python
!pip install sentence-transformers datasets wandb
```

---

## 🚀 Quick Start Template

**Copy this into every new Colab notebook:**

```python
# ========================================
# COLAB SETUP - RUN FIRST!
# ========================================

# 1. Mount Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Navigate to project
%cd /content/drive/MyDrive/Thesis

# 3. Pull latest changes
!git pull origin main

# 4. Install packages
!pip install -q sentence-transformers datasets

# 5. Import libraries
import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm

# 6. Check GPU
print(f"✅ GPU Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"   GPU: {torch.cuda.get_device_name(0)}")

# 7. Set random seeds
torch.manual_seed(42)
np.random.seed(42)

print("\\n✅ Setup complete! Ready to work.")
```

---

## 🆘 Troubleshooting

### Problem: "No such file or directory"
**Solution:** You're not in the right folder
```python
%cd /content/drive/MyDrive/Thesis
!pwd  # Verify current directory
```

### Problem: "Drive not mounted"
**Solution:** Mount Drive first
```python
from google.colab import drive
drive.mount('/content/drive')
```

### Problem: "Already up to date" but code looks old
**Solution:** Force pull
```python
!git fetch origin
!git reset --hard origin/main
```

### Problem: "Runtime disconnected"
**Solution:** Reconnect and remount Drive
- Click "Reconnect" button
- Re-run mount and navigation cells

---

## 📚 Summary

| Action | Frequency | Command |
|--------|-----------|---------|
| Mount Drive | Every session | `drive.mount('/content/drive')` |
| Clone repo | Once (first time) | `!git clone <url> <path>` |
| Navigate to project | Every session | `%cd /content/drive/MyDrive/Thesis` |
| Pull updates | Every session | `!git pull origin main` |
| Install packages | Every session | `!pip install <package>` |
| Save checkpoints | During training | `torch.save(...)` |

---

## 🎓 Pro Tip

**Create a "setup.ipynb" notebook:**
1. Put all setup code in one notebook
2. Save to Drive
3. Every new session: just run this notebook first
4. Then start your actual work notebook

This way you don't repeat the same setup code everywhere!

