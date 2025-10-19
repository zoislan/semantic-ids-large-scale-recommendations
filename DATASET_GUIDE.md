# Dataset Selection Guide for Semantic IDs Thesis

## 🎯 Which Dataset Should You Use?

### **My Recommendation: Use the SAME dataset as the paper!**

**Why?**
- ✅ Direct comparison with paper's results
- ✅ Validate their findings
- ✅ Easier to defend in thesis ("following the methodology of...")
- ✅ Your professor can better evaluate your work

---

## 📖 How to Find the Dataset from the Paper

### **Step 1: Read the Paper's Experiment Section**

Open your primary paper: **"Better Generalization with Semantic IDs"**

Look for these sections:
- **"Experiments"**
- **"Experimental Setup"**
- **"Datasets"**
- **"Data"**
- **"Evaluation"**

### **Step 2: What to Look For**

The paper will typically mention:
- Dataset name (e.g., "Amazon Reviews 2018")
- Category (e.g., "Books", "Electronics", "Sports")
- Statistics (e.g., "100k items", "500k interactions")
- Download link or citation

### **Example of What You Might Find:**

```
"We evaluate our method on the Amazon Reviews dataset [1], 
specifically the Books and Electronics categories. 
The dataset contains..."

[1] McAuley et al., Amazon Reviews 2018
```

---

## 📊 Common Amazon Datasets in Recommendation Research

### **Option 1: Amazon Reviews 2018 (Most Common)**

**Source:** Julian McAuley, UCSD

**Website:** https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/

**Categories Available:**
- Books
- Electronics
- Movies and TV
- CDs and Vinyl
- Clothing, Shoes and Jewelry
- Sports and Outdoors
- Cell Phones and Accessories
- Tools and Improvement
- Toys and Games
- ...and 20+ more

**What's Included:**
- ✅ Item metadata (title, description, category, price)
- ✅ User reviews (rating, text, timestamp)
- ✅ User-item interactions
- ✅ Rich text descriptions (NEEDED for Semantic IDs!)

**Size:**
- Small categories: ~50k-100k items
- Large categories: 500k-1M+ items

**Download Format:**
- JSON files
- Gzipped (compressed)

**Pros:**
- ✅ Most cited in research
- ✅ Rich item descriptions
- ✅ Multiple categories to choose from
- ✅ Clean and well-documented

**Cons:**
- ⚠️ Large files (GB-sized)
- ⚠️ May need preprocessing

---

### **Option 2: Amazon Reviews 2023 (Latest)**

**Source:** Updated version with more recent data

**Website:** Check McAuley's website for updates

**Pros:**
- ✅ More recent data
- ✅ Larger scale

**Cons:**
- ⚠️ Less established in research
- ⚠️ Harder to compare with existing papers

---

### **Option 3: Amazon Reviews 2014 (Older)**

**Source:** Earlier version

**Website:** https://jmcauley.ucsd.edu/data/amazon/

**Pros:**
- ✅ Smaller, easier to handle
- ✅ Good for prototyping

**Cons:**
- ⚠️ Outdated
- ⚠️ Smaller item descriptions

---

## 🎯 My Recommendation Strategy

### **Phase 1: Start with Paper's Dataset**

1. **Read your primary paper** carefully
2. **Identify the exact dataset** they used
3. **Download the same category** (e.g., if they used "Books", use Books)
4. **Replicate their preprocessing** steps

### **Phase 2: If Not Specified or Unavailable**

Use **Amazon Reviews 2018 - Books** or **Electronics** category

**Why Books or Electronics?**
- ✅ Rich descriptions (novels have summaries, electronics have specs)
- ✅ Reasonable size (~50k-200k items)
- ✅ Commonly used in papers
- ✅ Clear semantic structure

---

## 📥 How to Download Amazon Reviews 2018

### **Method 1: Direct Download (Recommended for Colab)**

```python
import urllib.request
import gzip
import json
import pandas as pd

# Example: Download Books category
CATEGORY = "Books"
BASE_URL = "https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/"

# Download metadata (item info)
metadata_url = f"{BASE_URL}metaFiles2/meta_{CATEGORY}.json.gz"
urllib.request.urlretrieve(metadata_url, "meta_Books.json.gz")

# Download reviews (interactions)
reviews_url = f"{BASE_URL}categoryFiles/{CATEGORY}.json.gz"
urllib.request.urlretrieve(reviews_url, "Books_reviews.json.gz")

print("✅ Download complete!")
```

### **Method 2: Using Command Line (in Colab)**

```bash
# Books category
!wget https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/metaFiles2/meta_Books.json.gz
!wget https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/Books.json.gz

# Electronics category
!wget https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/metaFiles2/meta_Electronics.json.gz
!wget https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/Electronics.json.gz
```

### **Method 3: Parse the Data**

```python
import gzip
import json
import pandas as pd

def parse_json_gz(file_path):
    """Parse gzipped JSON file"""
    data = []
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# Load metadata
metadata = parse_json_gz('meta_Books.json.gz')
metadata_df = pd.DataFrame(metadata)

# Load reviews
reviews = parse_json_gz('Books.json.gz')
reviews_df = pd.DataFrame(reviews)

print(f"Items: {len(metadata_df)}")
print(f"Reviews: {len(reviews_df)}")
print(f"\\nMetadata columns: {metadata_df.columns.tolist()}")
print(f"Reviews columns: {reviews_df.columns.tolist()}")
```

---

## 📋 Dataset Requirements for Your Thesis

### **What You NEED:**

1. **Item Descriptions** ✅ CRITICAL
   - Text content to generate Semantic IDs
   - Amazon metadata has: title, description, category, features

2. **User-Item Interactions** ✅ CRITICAL
   - For training recommendation model
   - Amazon reviews has: user_id, item_id, rating, timestamp

3. **Sufficient Scale**
   - Minimum: ~10,000 items
   - Recommended: 50,000-200,000 items
   - More items = better but slower

4. **Temporal Information**
   - Timestamps for train/test split
   - Amazon reviews include timestamps

---

## 📊 Expected Dataset Structure

### **Metadata File (Items):**
```json
{
  "asin": "B001234567",          # Item ID
  "title": "The Great Book",     # Item title
  "description": "A wonderful story...",  # Description (KEY!)
  "category": ["Books", "Fiction"],
  "price": 12.99,
  "brand": "Publisher Name",
  "feature": ["Hardcover", "256 pages"]  # Additional features
}
```

### **Reviews File (Interactions):**
```json
{
  "reviewerID": "A2SUAM1J3GNN3B",  # User ID
  "asin": "B001234567",             # Item ID
  "overall": 5.0,                   # Rating
  "reviewText": "Great book!",      # Review text
  "unixReviewTime": 1362096000      # Timestamp
}
```

---

## 🎓 Action Plan for You

### **Step 1: Read the Paper (Today)**

- [ ] Open "Better Generalization with Semantic IDs" PDF
- [ ] Find "Experiments" or "Datasets" section
- [ ] Note the exact dataset name and category
- [ ] Check if download link is provided

### **Step 2: Initial Dataset Exploration (This Week)**

If paper specifies dataset:
- [ ] Download that exact dataset

If paper doesn't specify or is unclear:
- [ ] Start with Amazon Reviews 2018 - Books category
- [ ] Download metadata + reviews files

### **Step 3: Quick Analysis (This Week)**

Create a Colab notebook called `01_dataset_exploration.ipynb`:

```python
# Load and explore
metadata_df = pd.read_json('meta_Books.json.gz', lines=True)
reviews_df = pd.read_json('Books.json.gz', lines=True)

# Basic statistics
print(f"Number of items: {len(metadata_df)}")
print(f"Number of reviews: {len(reviews_df)}")
print(f"Number of users: {reviews_df['reviewerID'].nunique()}")

# Check descriptions
print(f"\\nItems with descriptions: {metadata_df['description'].notna().sum()}")
print(f"Average description length: {metadata_df['description'].str.len().mean():.0f} chars")

# Show example
print(f"\\nExample item:")
print(metadata_df.iloc[0][['title', 'description', 'category']])
```

### **Step 4: Report Back**

After you explore the paper and dataset:
- Tell me which dataset the paper uses
- Share basic statistics
- I'll help you with preprocessing!

---

## 💡 Quick Decision Tree

```
START HERE
    ↓
Does paper specify dataset?
    ↓
YES → Use that exact dataset
    ↓
NO → Use Amazon Reviews 2018
    ↓
Which category?
    ↓
Paper mentions category? → Use that
    ↓
NO → Use Books (rich descriptions, manageable size)
    ↓
Download and explore!
```

---

## 🚀 Next Steps

1. **Read your paper** - Find dataset info (spend 30-60 min)
2. **Let me know** what dataset they use
3. **I'll help you** write the download and exploration code
4. **Create first notebook** for data analysis

---

## 📚 Useful Resources

### **Amazon Reviews Datasets:**
- Main page: https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/
- Paper: "Justifying Recommendations using Distantly-Labeled Reviews and Fine-Grained Aspects" (McAuley et al., 2019)

### **Alternative Datasets (if Amazon doesn't work):**
- **MovieLens**: Movie recommendations (smaller, easier)
- **Goodreads**: Book recommendations
- **Steam**: Game recommendations
- **Yelp**: Business recommendations

### **Dataset Papers to Cite:**
```bibtex
@inproceedings{mcauley2019amazon,
  title={Justifying recommendations using distantly-labeled reviews and fine-grained aspects},
  author={Ni, Jianmo and Li, Jiacheng and McAuley, Julian},
  booktitle={EMNLP},
  year={2019}
}
```

---

## ✅ Summary

**My Strong Recommendation:**

1. **Read your paper TODAY** - find their dataset
2. **Use the same dataset** they used
3. **If unclear:** Use Amazon Reviews 2018 - Books category
4. **Let me know** what you find, and I'll help with the code!

This approach will make your thesis:
- ✅ More credible (following established work)
- ✅ Easier to compare results
- ✅ Easier to defend

**Don't overthink it - just start with what the paper uses!** 🚀

