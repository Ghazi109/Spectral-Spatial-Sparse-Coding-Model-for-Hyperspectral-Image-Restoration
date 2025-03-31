# Spectral-Spatial-Sparse-Coding-Model-for-Hyperspectral-Image-Restoration

 Hyperspectral Image Restoration – Model Testing

## 📌 Project Overview
This project focuses on testing the model proposed in the paper: **"A Trainable Spectral-Spatial Sparse Coding Model for Hyperspectral Image Restoration"**. The goal is to evaluate the model's performance on various noise conditions and datasets, and to analyze its strengths and limitations.We also applied explainability methods to understand the factors driving the model's decision-making and gain deeper insights into its performance.

## 📖 Paper Reference
- **Title:** A Trainable Spectral-Spatial Sparse Coding Model for Hyperspectral Image Restoration  
- **Authors:** [Bodrito, Theo and Zouaoui, Alexandre and Chanussot, Jocelyn and Mairal, Julien]  
- **Link:** https://proceedings.neurips.cc/paper/2021/file/2b515e2bdd63b7f034269ad747c93a42-Paper.pdf  

## 📁 Repository Structure
📂 project-root/
│
├── 📂 pretrained_models/          # Your fine-tuned models
│   ├── 📄 epoch11.ckpt           # Trained for dcmall data 11 epochs (11,057 KB)
│   ├── 📄 icvl_constant_5.ckpt    # Constant noise σ=5 (9,781 KB)
│   └── 📄 icvl_uniform_95.ckpt   # Uniform noise σ=95 (10,686 KB)
│
├── 📂 results/                    # Your experimental outputs
│   ├── 📂 2025-03-23_15-41-05/   # Tests on constant σ=5
│   └── 📂 2025-03-30_22-52-17/   # Tests on stripes σ=25
│
├── 📂 t3sc/                       # Original TS3C repo 
│   ├── 📂 data/                   # Original datasets
│   ├── 📂 models/                 # Baseline architectures
│   └── 📜 LICENSE                 # Original license
│
├── 📜 .gitignore                  # Custom excludes (e.g., .ckpt)
├── 📜 README.md                   
└── 📜 requirements.txt            # updated requirements

## 🛠️ Code Modifications
1) **Less Requirements**  
   The versions of some dependencies are no longer specified in the `requirements.txt` file, as these versions are incompatible with Python 3.12. This update ensures that the code remains compatible with the latest Python releases without version restrictions on dependencies.

2) **Changes in `train.py`**  
   In the `train.py` script, lines 60 and 61 were commented out to ensure compatibility with recent versions of PyTorch. These lines previously instantiated the trainer with the following code:
```python
   # Instantiate trainer
   trainer = pl.Trainer(
       callbacks=callbacks,
       logger=tb_logger,
       #progress_bar_refresh_rate=0,
       #**cfg.trainer.params,
   )
```

Since the progress_bar_refresh_rate argument and other configurations are no longer supported in the recent versions of PyTorch Lightning, these lines were disabled to avoid errors.

3) **Changes in data/factories/icvl**
The download function in the data/factories/icvl directory has been modified due to the old URL being no longer valid. Additionally, the download mechanism was updated to use the requests library instead of subprocess. This change was made to avoid errors caused by the previous method, ensuring a more reliable and efficient downloading process for datasets.

4) **Changes in in t3sc/models/multilayer.py**
In the t3sc/models/multilayer.py file, the following line was modified:

```python

d = torch.load(to_absolute_path(self.ckpt), weights_only=False)
```
The weights_only=False argument was explicitly added to prevent errors during model loading.



## 🔬 Experimental Setup & Results

We conducted several experiments to evaluate the model's performance under different noise conditions, datasets, and explainability analyses. These experiments provide insights into the model's robustness, generalization, and interpretability. The results of these experiments can be found in the provided Jupyter Notebook.

### 📌 Inference & Model Evaluation  
We tested the pretrained model under different noise conditions to assess its denoising capabilities:  
- **Evaluate Model Performance on Noise with Constant Sigma = 5, Trained on Constant Sigma = 5 Noise**  
- **Evaluate Model Performance on Noise with Stripes (Sigma = 25), Trained on Constant Sigma = 5**  
- **Comparing the Performance of a Model Trained on Uniform Noise with Striped Noise**  

These experiments help determine how well the model generalizes to different noise distributions.

### 📌 Training on the DCMall Dataset  
To further test the model's adaptability, we trained and evaluated it on the DCMall dataset with various noise conditions:  
- **Training and Testing with DCMall**  
- **Training on the DCMall Dataset with Uniform Gaussian Noise (Variance = 55)**  

These tests assess the model's ability to handle real-world hyperspectral imaging data with varying noise levels.

### 📌 Explainability & Analysis  
We also applied explainability methods to better understand how the model makes decisions and what factors influence its performance:  
- **Residuals Heatmap**  
- **How Does the Denoising Error Vary Across Spectral Bands?**  
- **Dictionary Composition for Sparse Coding in Hyperspectral Imaging**  

These analyses provide insights into the effectiveness of sparse coding and highlight which spectral bands contribute most to the denoising process.

All results and visualizations are available in the Jupyter Notebook.

