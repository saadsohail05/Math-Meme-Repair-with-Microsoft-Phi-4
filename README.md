# Math Meme Repair with Phi-4

This project uses Microsoft's Phi-4 model fine-tuned to repair incorrect mathematical statements commonly found in memes. The model is trained to identify mathematical errors and provide correct explanations.

## Features

- Fine-tuned Phi-4 model for mathematical correction
- FastAPI backend for model inference
- Jupyter notebooks for both training and inference
- Optimized with Unsloth for faster training and inference

## Project Structure

```
├── app_meme.py              # FastAPI application
├── inference_notebook_meme.ipynb    # Inference notebook
├── Phi_4_MathMemeRepair.ipynb      # Training notebook
├── requirements.txt         # Project dependencies
└── examples/               # Example memes and corrections
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the FastAPI server:
```bash
uvicorn app_meme:app --host 0.0.0.0 --port 7860
```

## Model Details

The model is fine-tuned on Phi-4 using LoRA (Low-Rank Adaptation) with the following configurations:
- Rank: 16
- Alpha: 16
- Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- Training with Unsloth optimizations for reduced VRAM usage

## Usage

You can use the model through:
1. The FastAPI endpoint
2. Running the inference notebook
3. Direct model usage from Hugging Face: `saadsohail/Phi_4-MathMemeRepair`

## License

This project uses the Phi-4 model which is subject to Microsoft's license terms.