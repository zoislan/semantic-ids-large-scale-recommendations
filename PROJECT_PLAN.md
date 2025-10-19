# Thesis Project Plan: Semantic IDs for Large-Scale Recommendations

## 🎯 Project Overview
**Title:** Leveraging Semantic IDs for Large-Scale Recommendations  
**Advisor Requirement:** Focus on "Better Generalization with Semantic IDs" paper  
**Computational Environment:** Google Colab (GPU-enabled)

---

## 📚 Phase 0: Understanding the Foundation (Week 1)

### Key Concepts to Master:
1. **Semantic IDs**: Structured codes that represent items meaningfully
2. **RQ-VAE (Residual Quantized Variational AutoEncoder)**: Method to create Semantic IDs
3. **Generative Recommendation**: Predicting item codes instead of item IDs
4. **Codebooks**: Lookup tables where each code represents a semantic concept

### Papers to Read:
- ✅ "Better Generalization with Semantic IDs" (PRIMARY - focus here!)
- ✅ "Generative Recommendation with Semantic IDs: Practitioner's Handbook"
- ✅ "Recommender Systems with Generative Retrieval"

---

## 🛠️ Phase 1: Data Acquisition & Preparation (Week 2-3)

### Step 1.1: Find Amazon Reviews Dataset
**Requirements:**
- Items with descriptions/text content
- User-item interactions (reviews/ratings)
- Sufficient scale (10k-100k items minimum)

**Recommended Datasets:**
1. **Amazon Reviews 2018** (Julian McAuley)
   - Categories: Books, Electronics, Movies, etc.
   - Includes: item metadata, descriptions, reviews
   - Link: https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/

2. **Amazon Product Data (2023)**
   - Updated version with more recent data

### Step 1.2: Data Preprocessing
**Colab Notebook 1: `01_data_preparation.ipynb`**
```
Tasks:
- Download dataset
- Extract item descriptions/titles
- Clean and filter data
- Create user-item interaction matrix
- Train/validation/test split (chronological)
```

**Expected Output:**
- `items.csv` (item_id, title, description, category, etc.)
- `interactions.csv` (user_id, item_id, rating, timestamp)
- `train.csv`, `val.csv`, `test.csv`

---

## 🧬 Phase 2: Building Semantic IDs (Week 4-6) ⭐ CORE TASK

### Step 2.1: Item Text Embeddings
**Colab Notebook 2: `02_item_embeddings.ipynb`**
```
Tasks:
- Use pre-trained language model (BERT, Sentence-BERT, etc.)
- Encode item descriptions into dense vectors
- Save embeddings for all items
```

**Expected Output:**
- `item_embeddings.npy` (shape: [num_items, embedding_dim])

### Step 2.2: Train RQ-VAE Model
**Colab Notebook 3: `03_semantic_id_generation.ipynb`**
```
Architecture:
- Encoder: item embedding → latent code
- Residual Quantization: multiple codebooks (e.g., 3-5 codebooks)
- Decoder: reconstruct item embedding from codes

Hyperparameters to explore:
- Number of codebooks: 3, 4, 5
- Codebook size: 256, 512, 1024
- Embedding dimension: 768 (from BERT)
```

**Expected Output:**
- `semantic_ids.csv` (item_id, code_1, code_2, code_3, ...)
- `codebooks.pkl` (trained codebook matrices)
- `rqvae_model.pt` (saved model)

### Step 2.3: Semantic ID Quality Analysis
**Colab Notebook 4: `04_semantic_id_analysis.ipynb`**
```
Analysis Tasks:
- Reconstruction quality (cosine similarity)
- Code distribution (are codes used uniformly?)
- Semantic coherence (do similar items get similar codes?)
- Visualization (t-SNE of codes vs embeddings)
```

---

## 🤖 Phase 3: Generative Recommendation Model (Week 7-9)

### Step 3.1: Prepare Sequential Data
**Colab Notebook 5: `05_sequence_preparation.ipynb`**
```
Tasks:
- Convert user interaction history to sequences
- Map item_ids to semantic_ids
- Create training sequences: [history] → [next_semantic_id]
```

### Step 3.2: Train Generative Model
**Colab Notebook 6: `06_generative_model.ipynb`**
```
Model Options:
1. Transformer-based (like Tiger paper)
2. GRU/LSTM baseline
3. BERT4Rec adapted for Semantic IDs

Training:
- Input: User history (sequence of semantic IDs)
- Output: Next semantic ID (multi-target prediction for each codebook)
```

---

## 📊 Phase 4: Evaluation & Analysis (Week 10-11)

### Step 4.1: Recommendation Quality
**Colab Notebook 7: `07_evaluation.ipynb`**
```
Metrics:
- Hit Rate @ 10, 20
- NDCG @ 10, 20
- MRR (Mean Reciprocal Rank)
- Coverage (what % of items get recommended?)
```

### Step 4.2: Comparative Analysis
```
Compare:
1. Semantic IDs vs Random Item IDs
2. Different codebook configurations
3. Ablation study: effect of number of codebooks
```

### Step 4.3: Qualitative Analysis
```
Case Studies:
- Show example recommendations
- Analyze failure cases
- Interpret semantic meanings of codebooks
```

---

## 📝 Phase 5: Thesis Writing (Week 12-14)

### Thesis Structure:
1. **Introduction**
   - Problem statement
   - Why Semantic IDs matter for large-scale recommendations

2. **Related Work**
   - Generative retrieval
   - Semantic IDs literature
   - Recommendation systems

3. **Methodology**
   - RQ-VAE for Semantic ID generation
   - Generative recommendation model
   - Experimental setup

4. **Experiments**
   - Dataset description
   - Semantic ID quality analysis
   - Recommendation performance
   - Ablation studies

5. **Results & Discussion**
   - Main findings
   - Insights about Semantic IDs
   - Limitations

6. **Conclusion & Future Work**

---

## 🔧 Technical Setup for Colab

### Required Libraries:
```python
# Data processing
pandas, numpy, scipy

# Deep Learning
torch, transformers, pytorch-lightning

# Visualization
matplotlib, seaborn, plotly

# Recommendation
scikit-learn, sentence-transformers

# Utilities
tqdm, wandb (for experiment tracking)
```

### Colab GPU Tips:
- Use Colab Pro if training is slow
- Save checkpoints frequently to Google Drive
- Use mixed precision training (fp16)
- Batch processing for large datasets

---

## 📊 Success Criteria

### Minimum Viable Thesis:
✅ Successfully build Semantic IDs for Amazon dataset  
✅ Train generative recommendation model  
✅ Show that Semantic IDs improve over baselines  
✅ Provide analysis of what the model learned  

### Stretch Goals:
🌟 Test on multiple dataset categories  
🌟 Deploy demo recommendation system  
🌟 Novel contribution (e.g., improved RQ-VAE architecture)  
🌟 Publish findings at workshop/conference  

---

## 📅 Timeline Summary

| Phase | Duration | Deliverable |
|-------|----------|------------|
| Phase 0: Understanding | Week 1 | Paper notes, concepts clarified |
| Phase 1: Data | Week 2-3 | Clean dataset ready |
| Phase 2: Semantic IDs | Week 4-6 | Working RQ-VAE model + IDs |
| Phase 3: Recommendation | Week 7-9 | Trained generative model |
| Phase 4: Evaluation | Week 10-11 | Complete experiments + results |
| Phase 5: Writing | Week 12-14 | Thesis draft |

**Total:** ~14 weeks (3.5 months)

---

## 🎓 Key Questions for Your Advisor

Before you start coding, consider asking:
1. What scale of dataset is expected? (10k, 100k, 1M items?)
2. Should you implement from scratch or use existing code?
3. Are there specific baselines to compare against?
4. What's the expected length/depth of thesis?
5. Any specific analysis required beyond standard metrics?

---

## 📚 Useful Resources

### Codebases:
- Tiger paper implementation: Search GitHub for "TIGER recommendation"
- RQ-VAE implementations: "residual quantization VAE"

### Datasets:
- Amazon Reviews: https://cseweb.ucsd.edu/~jmcauley/datasets.html
- RecSys datasets: https://www.kaggle.com/datasets?search=recommendation

### Tutorials:
- Transformers for RecSys
- Vector Quantization in PyTorch
- Colab best practices for ML

---

## 🚀 Next Steps (Start Here!)

1. ✅ **Read the primary paper thoroughly** (Better Generalization with Semantic IDs)
2. ✅ **Download Amazon Reviews dataset** (choose a category)
3. ✅ **Set up first Colab notebook** for data exploration
4. ✅ **Validate dataset has descriptions** (required for Semantic IDs)

---

**Remember:** This is an iterative process. Start simple, get something working end-to-end, then improve!

