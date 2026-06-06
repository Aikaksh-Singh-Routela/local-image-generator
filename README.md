## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Model** | Stable Diffusion 1.5 |
| **Framework** | Diffusers, PyTorch |
| **Backend** | Flask |
| **Frontend** | HTML/CSS/JS |
| **Optimization** | FP16, Attention slicing, CPU offload |

## 🔗 Links

- **GitHub**: [local-image-generator](https://github.com/Aikaksh-Singh-Routela/local-image-generator)

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Aikaksh-Singh-Routela/local-image-generator.git
cd local-image-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# First run will download the model (~2GB)
python generate.py
🔧 Usage
Run the Backend
bash
python generate.py
Open the Frontend
Open frontend/index.html in your browser.

API Example
bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "cute golden retriever puppy"}'
📊 Sample Images
Prompt	Time	Result
"cute golden retriever puppy"	25s	✅ Generated
"beautiful sunset over mountains"	28s	✅ Generated
"futuristic cyberpunk city"	30s	✅ Generated
🔧 Optimization Notes
This project includes specific optimizations for 6GB GPUs:

FP16 (half precision) - Reduces memory usage by 50%

Attention slicing - Further memory reduction

CPU offload - Moves unused models to RAM

🚀 Performance
Hardware	Resolution	Time
GTX 1660 6GB	512x512	20-30 seconds
GTX 1660 6GB	768x768	40-60 seconds
📁 Project Structure
text
local-image-generator/
├── generate.py          # Flask backend + model
├── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html       # Web interface
└── README.md            # Documentation


📄 License
MIT License

Built with 🖼️, 🐍, and ⚡ by Aikaksh Singh Routela
