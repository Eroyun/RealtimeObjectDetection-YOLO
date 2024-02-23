1. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

   If you have multiple Python versions, specify Python 3.9 explicitly:

   ```bash
   py -3.9 -m venv .venv
   ```

2. **Activate the virtual environment:**

   ```bash
   source .venv/Scripts/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### **Updating Dependencies:**

1. **Install any new dependencies:**

```bash
pip install <new-dependency>
```

2. **Update the requirements file:**

   ```bash
   pip freeze > requirements.txt
   ```

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
