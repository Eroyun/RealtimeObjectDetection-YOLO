# Real-time Object Detection YOLOv8

The aim of this project is to test YOLOv8 model that is trained to detect objects in realtime.

In this project YOLOv8m-oiv7 pretrained model is used. This pretrained model has been trained with Open Images dataset and in this project it has been trained using COCO dataset.

**1. Create a Virtual Environment:**

- **General Approach:**

  - Ensure you have Python 3 installed (version 3.9 or higher recommended).
  - Choose a suitable virtual environment tool (e.g., `venv`, `virtualenv`, `conda`).
  - Create the virtual environment in a convenient location.

- **Example with `venv`:**

  ```bash
  python3.9 -m venv my_env  # Replace "my_env" with your desired name
  ```

- **Activation:**
  - Activate the environment to isolate its dependencies. Refer to your chosen tool's documentation for specific activation commands (e.g., `source my_env/bin/activate` for `venv`).

**2. Install Dependencies:**

- **Method 1: Using a `requirements.txt` file:**
  - If you have a `requirements.txt` file listing all required packages, install them using:
  ```bash
  pip install -r requirements.txt
  ```
- **Method 2: Manual Installation:**
  - If you don't have a `requirements.txt`, install each dependency individually using `pip`:
  ```bash
  pip install numpy pandas matplotlib
  ```

**3. Updating Dependencies:**

- **Install New Dependencies:**
  - Use `pip` to add new packages:
  ```bash
  pip install <new-dependency>
  ```
- **Update `requirements.txt`:**
  - Keep your `requirements.txt` file in sync with installed packages:
  ```bash
  pip freeze > requirements.txt
  ```

Here's an improved version of the PyTorch installation instructions:

**4. Install PyTorch with CUDA:**

While CPU training is possible, it can be significantly slower (CPU training can take several days or even weeks, compared to hours with a GPU) than using a GPU with CUDA. For large datasets or complex models, using a GPU is highly recommended.

**Installation:**

1. Open a terminal or command prompt.
2. Run the following command:

   ```bash
   pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   ```

**Verification:**

```python
import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
```

**Additional Notes:**

- Replace `cu121` with the appropriate index URL for your CUDA version: [https://pytorch.org/get-started/previous-versions/](https://pytorch.org/get-started/previous-versions/)
- For detailed instructions and troubleshooting, visit: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
