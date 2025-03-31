# Spectral-Spatial-Sparse-Coding-Model-for-Hyperspectral-Image-Restoration

 Hyperspectral Image Restoration – Model Testing

## 📌 Project Overview
This project focuses on testing the model proposed in the paper: **"A Trainable Spectral-Spatial Sparse Coding Model for Hyperspectral Image Restoration"**. The goal is to evaluate the model's performance on various noise conditions and datasets, and to analyze its strengths and limitations.We also applied explainability methods to understand the factors driving the model's decision-making and gain deeper insights into its performance.

## 📖 Paper Reference
- **Title:** A Trainable Spectral-Spatial Sparse Coding Model for Hyperspectral Image Restoration  
- **Authors:** [Bodrito, Theo and Zouaoui, Alexandre and Chanussot, Jocelyn and Mairal, Julien]  
- **Link:** https://proceedings.neurips.cc/paper/2021/file/2b515e2bdd63b7f034269ad747c93a42-Paper.pdf  

## 📁 Repository Structure
📂 project-root │-- 📂 data/ # Datasets used for testing │-- 📂 models/ # Model weights and configurations │-- 📂 results/ # Output images, metrics, and plots │-- 📂 scripts/ # Python scripts for preprocessing, evaluation, and visualization │-- 📜 README.md # Project documentation (this file) │-- 📜 requirements.txt # Required dependencies │-- 📜 main.ipynb # Jupyter Notebook for running tests
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
bash
Copy
Edit

## 🚀 Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
2️⃣ Install Dependencies
It's recommended to use a virtual environment:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Download Datasets
Dataset Used: [ICVL / DC Mall / Other dataset names]

Provide instructions to download and place datasets in the /data directory.

🎯 Experiments & Results
✅ Model Training & Testing
Pretrained Model: [Link to pretrained weights if available]

Datasets: Mention dataset sizes, preprocessing steps

Noise Types Tested: [Gaussian, Poisson, Mixed, etc.]

Training Details: (if applicable) Number of epochs, learning rate, hardware used

📊 Key Observations
Performance on different noise levels

Limitations (e.g., oversmoothing, loss of high-frequency details)

Computational constraints (e.g., long training time)

📷 Visualization
Sample images before/after denoising

Heatmaps of residual noise

Spectral error plots

🛠️ Usage
Run Testing Script
bash
Copy
Edit
python scripts/test_model.py --data_path data/icvl --model_path models/pretrained.pth
Run Jupyter Notebook
bash
Copy
Edit
jupyter notebook main.ipynb
📝 Future Work
Exploring alternative denoising techniques

Fine-tuning the model on different datasets

Investigating explainability methods

👨‍💻 Contributors
Your Name (@your-github)

[Other contributors if applicable]

📜 License
[Specify the license, e.g., MIT License]

📬 Contact
For any questions, feel free to reach out via [your email] or open an issue.

nginx
Copy
Edit

Tout est bien en un seul bloc cette fois ! 🚀
