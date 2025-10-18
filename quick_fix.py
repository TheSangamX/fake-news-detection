import os
import subprocess
import sys

def create_missing_files():
    """Create missing essential files"""
    
    # Create requirements.txt if missing
    if not os.path.exists('requirements.txt'):
        with open('requirements.txt', 'w') as f:
            f.write("""streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
plotly>=5.15.0
""")
        print("✅ Created requirements.txt")
    
    # Create .streamlit directory and config
    os.makedirs('.streamlit', exist_ok=True)
    if not os.path.exists('.streamlit/config.toml'):
        with open('.streamlit/config.toml', 'w') as f:
            f.write("""[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[server]
runOnSave = true
""")
        print("✅ Created .streamlit/config.toml")

def install_dependencies():
    """Install missing dependencies"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")

def main():
    print("🔧 Running Quick Fix...")
    create_missing_files()
    
    if input("Install dependencies? (y/n): ").lower() == 'y':
        install_dependencies()
    
    print("🎉 Quick fix completed!")

if __name__ == "__main__":
    main()