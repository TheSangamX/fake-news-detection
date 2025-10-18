import sys
import importlib
import os
from pathlib import Path

class StreamlitErrorChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
    
    def check_dependencies(self):
        """Check if required packages are installed"""
        required_packages = [
            'streamlit', 'pandas', 'numpy', 'plotly'
        ]
        
        for package in required_packages:
            try:
                importlib.import_module(package)
                self.info.append(f"✅ {package} is installed")
            except ImportError:
                self.errors.append(f"❌ {package} is not installed")
    
    def check_file_structure(self):
        """Check if essential files exist"""
        essential_files = {
            'app.py': 'Main application file',
            'requirements.txt': 'Dependencies file'
        }
        
        for file, description in essential_files.items():
            if os.path.exists(file):
                self.info.append(f"✅ {file} exists ({description})")
            else:
                self.warnings.append(f"⚠️ {file} missing ({description})")
    
    def check_streamlit_config(self):
        """Check Streamlit configuration"""
        config_path = Path('.streamlit/config.toml')
        if config_path.exists():
            self.info.append("✅ Streamlit config found")
        else:
            self.warnings.append("⚠️ No Streamlit config found")
    
    def analyze_python_file(self, filepath):
        """Analyze Python file for common issues"""
        if not os.path.exists(filepath):
            self.errors.append(f"❌ File {filepath} not found")
            return
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for common issues
            if 'st.cache' in content and '@st.cache_data' not in content:
                self.warnings.append(f"⚠️ {filepath}: Using deprecated @st.cache")
            
            if 'st.beta_' in content:
                self.warnings.append(f"⚠️ {filepath}: Using deprecated st.beta_ functions")
            
            if 'st.experimental_' in content:
                self.warnings.append(f"⚠️ {filepath}: Using experimental functions")
            
            # Check for proper imports
            if 'import streamlit' not in content:
                self.warnings.append(f"⚠️ {filepath}: Streamlit not imported")
            
            self.info.append(f"✅ {filepath} analyzed successfully")
            
        except Exception as e:
            self.errors.append(f"❌ Error reading {filepath}: {str(e)}")
    
    def run_full_check(self):
        """Run all checks"""
        print("🔍 Running Streamlit Project Analysis...\n")
        
        self.check_dependencies()
        self.check_file_structure()
        self.check_streamlit_config()
        
        # Check main files
        python_files = ['app.py', 'main.py', 'streamlit_app.py']
        for file in python_files:
            if os.path.exists(file):
                self.analyze_python_file(file)
        
        self.print_results()
    
    def print_results(self):
        """Print analysis results"""
        print("=" * 50)
        print("📊 ANALYSIS RESULTS")
        print("=" * 50)
        
        if self.errors:
            print("\n🚨 ERRORS (Must Fix):")
            for error in self.errors:
                print(f"  {error}")
        
        if self.warnings:
            print("\n⚠️ WARNINGS (Should Fix):")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if self.info:
            print("\n✅ INFO (All Good):")
            for info in self.info:
                print(f"  {info}")
        
        print("\n" + "=" * 50)
        
        # Summary
        total_issues = len(self.errors) + len(self.warnings)
        if total_issues == 0:
            print("🎉 No issues found! Your project looks good.")
        else:
            print(f"📋 Found {len(self.errors)} errors and {len(self.warnings)} warnings")

if __name__ == "__main__":
    checker = StreamlitErrorChecker()
    checker.run_full_check()