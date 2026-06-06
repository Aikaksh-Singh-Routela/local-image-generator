markdown

\# 🖼️ Local Stable Diffusion Image Generator



\[!\[Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

\[!\[PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)

\[!\[Stable Diffusion](https://img.shields.io/badge/Stable-Diffusion-orange.svg)](https://huggingface.co/runwayml/stable-diffusion-v1-5)

\[!\[GPU](https://img.shields.io/badge/GPU-GTX%201660-green.svg)]()



\## 📋 Overview



A \*\*fully local AI image generator\*\* that runs on consumer-grade hardware (GTX 1660 6GB). No API keys, no cloud costs, no rate limits - generate unlimited images on your own computer.



\### Key Features



| Feature | Description |

|---------|-------------|

| \*\*🏠 Fully Local\*\* | Runs entirely on your GPU - no internet required |

| \*\*🎨 Unlimited Generations\*\* | No API costs or rate limits |

| \*\*⚡ Optimized for 6GB VRAM\*\* | Memory optimizations for consumer GPUs |

| \*\*🚀 Fast Generation\*\* | 20-40 seconds per image |

| \*\*📡 REST API\*\* | Easy integration with any application |

| \*\*💻 Web Interface\*\* | Simple UI for quick testing |



\## 🏗️ Architecture

User Prompt

↓

Flask Backend

↓

Stable Diffusion Pipeline

↓

GPU (GTX 1660)

↓

Generated Image (PNG)

↓

Base64 Response → Frontend Display



text



\## 🛠️ Tech Stack



| Component | Technology |

|-----------|------------|

| \*\*Model\*\* | Stable Diffusion 1.5 |

| \*\*Framework\*\* | Diffusers, PyTorch |

| \*\*Backend\*\* | Flask |

| \*\*Frontend\*\* | HTML/CSS/JS |

| \*\*Optimization\*\* | Attention slicing, CPU offload |



\## 📦 Installation



```bash

\# Clone repository

git clone https://github.com/Aikaksh-Singh-Routela/local-image-generator.git

cd local-image-generator



\# Create virtual environment

python -m venv venv

source venv/bin/activate  # Linux/Mac

\# or

.\\venv\\Scripts\\activate  # Windows



\# Install dependencies

pip install -r requirements.txt



\# First run will download the model (\~2GB)

python generate.py

🔧 Usage

Run the Backend

bash

python generate.py

Open the Frontend

Open frontend/index.html in your browser.



API Example

bash

curl -X POST http://localhost:5000/generate \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{"prompt": "cute golden retriever puppy"}'

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

🔗 Links

GitHub: local-image-generator



📄 License

MIT License



Built with 🖼️, 🐍, and ⚡ by Aikaksh Singh Routela

