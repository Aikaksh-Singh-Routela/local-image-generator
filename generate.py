# generate.py - Local Stable Diffusion Image Generator
# Runs on your PC with GTX 1660 6GB

from diffusers import StableDiffusionPipeline
import torch
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
import time
import os

app = Flask(__name__)
CORS(app)

# Model will be downloaded once (first run takes longer)
MODEL_ID = "runwayml/stable-diffusion-v1-5"

print("🚀 Loading Stable Diffusion...")
print("⏳ First run will download the model (~2GB)")

# Load with optimizations for 6GB GPU
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,  # Half precision saves memory
    safety_checker=None  # Disable for speed
)

# Memory optimizations
pipe.enable_attention_slicing()
pipe.enable_model_cpu_offload()

if torch.cuda.is_available():
    pipe = pipe.to("cuda")
    print("✅ GPU mode with optimizations")
else:
    print("⚠️ CPU mode (slower)")

print("✅ Model ready!\n")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'gpu': torch.cuda.is_available(),
        'model': MODEL_ID
    })

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    steps = data.get('steps', 20)  # 20 steps is good balance
    
    if not prompt:
        return jsonify({'error': 'No prompt'}), 400
    
    print(f"\n🎨 Generating: {prompt}")
    print(f"⚙️ Steps: {steps}")
    
    start = time.time()
    
    try:
        image = pipe(prompt, num_inference_steps=steps).images[0]
        
        # Convert to base64 for frontend
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        
        elapsed = time.time() - start
        print(f"✅ Generated in {elapsed:.1f} seconds")
        
        return jsonify({
            'success': True,
            'image': img_base64,
            'prompt': prompt,
            'time': round(elapsed, 1),
            'steps': steps
        })
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'ok', 'gpu_available': torch.cuda.is_available()})

if __name__ == '__main__':
    print("=" * 50)
    print("🖼️ LOCAL IMAGE GENERATOR")
    print("=" * 50)
    print(f"📍 Health: http://localhost:5000/health")
    print(f"🎨 Generate: POST http://localhost:5000/generate")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=False)