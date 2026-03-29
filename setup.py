#!/usr/bin/env python3
"""
Smart Campus Security System - Project Setup Script
Initializes all directories and checks dependencies
"""

import os
import sys
from pathlib import Path
import subprocess

def create_directories():
    """Create project directory structure"""
    print("=" * 70)
    print("CREATING PROJECT STRUCTURE")
    print("=" * 70)
    
    directories = [
        'enrolled_faces',
        'scenario_images',
        'test_images',
        'outputs',
        'outputs/visualizations',
        'outputs/results'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {directory}/")
    
    print(f"\n✓ Project structure created successfully!\n")

def check_python_version():
    """Check Python version"""
    print("=" * 70)
    print("CHECKING PYTHON VERSION")
    print("=" * 70)
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version OK (3.8+)\n")
        return True
    else:
        print("✗ Python 3.8+ required\n")
        return False

def check_pip():
    """Check if pip is available"""
    print("=" * 70)
    print("CHECKING PIP")
    print("=" * 70)
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ pip available: {result.stdout.strip()}\n")
            return True
    except Exception as e:
        print(f"✗ Error checking pip: {e}\n")
    return False

def install_dependencies():
    """Install required packages"""
    print("=" * 70)
    print("INSTALLING DEPENDENCIES")
    print("=" * 70)
    
    packages = [
        'jupyter',
        'matplotlib',
        'pandas',
        'numpy',
        'opencv-python',
        'scikit-learn',
        'scipy',
        'Pillow',
        'torch',
        'torchvision',
        'transformers',
        'insightface'
    ]
    
    print(f"Installing {len(packages)} packages...")
    print("This may take several minutes...\n")
    
    for i, package in enumerate(packages, 1):
        print(f"[{i}/{len(packages)}] Installing {package}...", end=' ', flush=True)
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', package],
                         check=True, timeout=300)
            print("✓")
        except subprocess.TimeoutExpired:
            print("✗ (Timeout - package may be large)")
        except subprocess.CalledProcessError as e:
            print(f"✗ (Error: {e})")
        except Exception as e:
            print(f"✗ (Error: {e})")
    
    print("\n")

def verify_installations():
    """Verify key packages are installed"""
    print("=" * 70)
    print("VERIFYING INSTALLATIONS")
    print("=" * 70)
    
    packages_to_check = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'cv2': 'OpenCV',
        'PIL': 'Pillow',
        'torch': 'PyTorch',
        'transformers': 'Transformers',
    }
    
    all_ok = True
    for module, name in packages_to_check.items():
        try:
            __import__(module)
            print(f"✓ {name:20} installed")
        except ImportError:
            print(f"✗ {name:20} NOT found")
            all_ok = False
    
    # Check GPU availability
    print("\n" + "=" * 70)
    print("GPU CHECK")
    print("=" * 70)
    try:
        import torch
        if torch.cuda.is_available():
            print(f"✓ GPU available: {torch.cuda.get_device_name(0)}")
            print(f"  CUDA version: {torch.version.cuda}")
        else:
            print("⚠ GPU not available (will use CPU - slower)")
    except Exception as e:
        print(f"⚠ Could not check GPU: {e}")
    
    print()
    return all_ok

def create_sample_data_guide():
    """Create a sample data guide"""
    print("=" * 70)
    print("SETUP COMPLETE!")
    print("=" * 70)
    
    guide = """
NEXT STEPS:

1. COLLECT YOUR DATA
   ├── Enroll 5+ people: Place photos in enrolled_faces/
   ├── Capture 10+ scenarios: Place photos in scenario_images/
   └── Collect 10+ test images: Place photos in test_images/
   
   See DATA_COLLECTION_GUIDE.md for detailed instructions

2. RUN THE NOTEBOOK
   ├── Start Jupyter: jupyter notebook
   ├── Open SCS_main.ipynb
   ├── Fill in team info at the top
   └── Execute: Kernel → Restart & Run All

3. REVIEW RESULTS
   ├── Check console output for processing logs
   ├── View visualizations: outputs/visualizations/
   ├── Check results table: outputs/results/security_results.csv
   └── Read report: outputs/results/system_report.txt

4. IMPROVE & ITERATE
   ├── Analyze failure cases
   ├── Refine activity labels if needed
   ├── Re-run pipeline with adjustments
   └── Add bonus extensions (optional)

PROJECT STRUCTURE:
"""
    
    print(guide)
    
    # Show directory structure
    print("Current project directories:")
    for directory in Path('.').glob('*'):
        if directory.is_dir():
            count = len(list(directory.glob('*')))
            print(f"  {directory.name:25} ({count} items)")
        elif directory.is_file() and directory.name.endswith(('.ipynb', '.md', '.py')):
            size = directory.stat().st_size / 1024  # KB
            print(f"  {directory.name:25} ({size:.1f} KB)")

def main():
    """Main setup function"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "SMART CAMPUS SECURITY SYSTEM" + " " * 24 + "║")
    print("║" + " " * 20 + "PROJECT SETUP SCRIPT" + " " * 29 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    # Check Python
    if not check_python_version():
        print("✗ Setup failed: Python 3.8+ required")
        return False
    
    # Check pip
    if not check_pip():
        print("✗ Setup failed: pip not available")
        return False
    
    # Create directories
    create_directories()
    
    # Ask about installing packages
    response = input("Do you want to install Python dependencies? (y/n): ").strip().lower()
    if response == 'y':
        install_dependencies()
        verify_installations()
    else:
        print("⚠ Skipping dependency installation")
        print("Note: You'll need to install packages manually to run the notebook\n")
    
    # Show what's next
    create_sample_data_guide()
    
    print("\n" + "=" * 70)
    print("✓ PROJECT SETUP COMPLETE!")
    print("=" * 70)
    print("\nFor detailed instructions, read:")
    print("  • README.md - Project overview and quick start")
    print("  • DATA_COLLECTION_GUIDE.md - How to collect images")
    print()
    return True

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n✗ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Setup failed with error: {e}")
        sys.exit(1)
