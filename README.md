---
license: cc-by-nc-4.0
language:
- si
pipeline_tag: feature-extraction
library_name: fasttext
tags:
- sinhala
- embeddings
- fasttext
- low-resource-languages
- word-vector
- remeinium
- nlp
---
# UgannA Siyabasa — FastText Sinhala Embedding Model 🇱🇰

**UgannA Siyabasa** (උගන්නැ සියබස) is the first public FastText embedding model released by **Remeinium Corp**.
The name comes from Kumaratunga Munidasa’s timeless quote:

> “උගන්නැ සියබස – මත් වන්නැ එහි රසයෙන්”  
> *Learn Sinhala – be intoxicated with its beauty.*

Just as Munidasa envisioned nurturing the Sinhala language, this model represents teaching it to machines.

---

## 📌 Key Features

* **Type:** FastText (official library)
* **Vector size:** 100 dimensions
* **File size:** ~1.56GB
* **Training data:** 6.2GB processed Sinhala text
* **Performance:**
  * Similar-word retrieval accuracy: **0.90+** (tested)
  * Outperforms `cc.si.300.bin` baseline (~0.76)

---

## 🔧 Usage

### Hugging Face Model
You can directly load the model from Hugging Face:  
👉 [Hugging Face Model Page](https://huggingface.co/Remeinium/UgannA_Siyabasa)

```python
import fasttext

# Load the model from Hugging Face (after downloading)
model = fasttext.load_model("UgannA_Siyabasa.bin")

# Get vector for a word
vector = model.get_word_vector("අම්මා")

# Get nearest neighbors
neighbors = model.get_nearest_neighbors("අම්මා", k=10)
print(neighbors)
```

### GitHub Repository
We also provide code samples and utilities on GitHub:  
👉 [Remeinium GitHub](https://github.com/Remeinium/UgannA_Siyabasa)

---

## 📂 Training Data

* **Processed and cleaned training corpus:** ~6.2GB
* Preprocessing: tokenization, normalization, deduplication

---

## 🗜️ License

This model is released under **CC BY-NC 4.0** (non-commercial use).  
🔗 For commercial usage, please contact: **[support@remeinium.com](mailto:support@remeinium.com)**

---

## ⚠️ Limitations

* Vocabulary coverage limited to training dataset.
* May reflect cultural/linguistic biases from sources.
* Optimized for Sinhala; not multilingual (future versions will expand).

---

## 🤝 Collaboration

You are welcome to:

* Use this model for **research & personal projects**
* Share improvements, benchmarks, or downstream applications

📧 Contact us: [support@remeinium.com](mailto:support@remeinium.com)
