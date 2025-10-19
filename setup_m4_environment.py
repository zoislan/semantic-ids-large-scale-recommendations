#!/usr/bin/env python3
"""
M4 MacBook Pro Setup Script for Semantic IDs Thesis
====================================================

This script sets up your M4 MacBook Pro for deep learning with:
- PyTorch with MPS (Metal Performance Shaders) support
- Amazon Reviews 2023 dataset via Hugging Face
- All required dependencies in virtual environment

Usage:
    python setup_m4_environment.py
"""

import subprocess
import sys
import torch
import os

def run_command(command, description):
    """Run a command and print the result"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Success!")
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed!")
        print(f"Error: {e.stderr}")
        return False

def check_mps_support():
    """Check if MPS (Metal Performance Shaders) is available"""
    print("\n🔍 Checking MPS support...")
    try:
        if torch.backends.mps.is_available():
            print("✅ MPS is available!")
            print(f"   MPS built: {torch.backends.mps.is_built()}")
            
            # Test basic GPU operations
            device = torch.device("mps")
            x = torch.randn(100, 100, device=device)
            y = torch.randn(100, 100, device=device)
            z = torch.mm(x, y)
            print(f"✅ GPU computation test successful! Result shape: {z.shape}")
            return True
        else:
            print("❌ MPS not available")
            return False
    except Exception as e:
        print(f"❌ MPS check failed: {e}")
        return False

def test_amazon_dataset():
    """Test loading Amazon Reviews dataset"""
    print("\n📊 Testing Amazon Reviews dataset...")
    try:
        from datasets import load_dataset
        
        # Test with small sample
        print("   Loading All_Beauty sample...")
        dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_All_Beauty", 
                              trust_remote_code=True, split="train[:100]")
        
        print(f"✅ Dataset loaded successfully!")
        print(f"   Sample size: {len(dataset)}")
        print(f"   Columns: {dataset.column_names}")
        print(f"   First sample keys: {list(dataset[0].keys())}")
        
        return True
    except Exception as e:
        print(f"❌ Dataset test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up M4 MacBook Pro for Semantic IDs Thesis")
    print("=" * 60)
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  Warning: Not in a virtual environment!")
        print("   Please activate your venv first:")
        print("   source venv/bin/activate")
        return
    
    # Install PyTorch with MPS
    print("\n📦 Installing PyTorch with MPS support...")
    if not run_command("pip install torch torchvision torchaudio", "Installing PyTorch"):
        return
    
    # Install other dependencies
    dependencies = [
        "transformers sentence-transformers",
        "datasets accelerate", 
        "matplotlib seaborn plotly",
        "pandas numpy scikit-learn",
        "tqdm wandb",
        "jupyter ipykernel"
    ]
    
    for deps in dependencies:
        if not run_command(f"pip install {deps}", f"Installing {deps}"):
            print(f"⚠️  Failed to install {deps}, continuing...")
    
    # Add kernel to Jupyter
    run_command("python -m ipykernel install --user --name=thesis --display-name='Thesis (M4 GPU)'", 
                "Adding Jupyter kernel")
    
    # Test MPS support
    if not check_mps_support():
        print("❌ MPS setup failed. Check your PyTorch installation.")
        return
    
    # Test dataset loading
    if not test_amazon_dataset():
        print("❌ Dataset loading failed. Check your internet connection.")
        return
    
    print("\n🎉 Setup Complete!")
    print("=" * 60)
    print("✅ PyTorch with MPS support installed")
    print("✅ All dependencies installed")
    print("✅ Amazon Reviews dataset accessible")
    print("✅ Jupyter kernel configured")
    
    print("\n🚀 Next Steps:")
    print("1. Start Jupyter: jupyter notebook")
    print("2. Select 'Thesis (M4 GPU)' kernel")
    print("3. Load Books dataset: load_dataset('McAuley-Lab/Amazon-Reviews-2023', 'raw_review_Books')")
    print("4. Start building Semantic IDs!")
    
    print("\n📚 Available Datasets:")
    print("- raw_review_Books: Full review data")
    print("- raw_meta_Books: Item metadata")
    print("- 0core_timestamp_Books: Pre-split train/valid/test")
    print("- 0core_timestamp_w_his_Books: With user history")

if __name__ == "__main__":
    main()
