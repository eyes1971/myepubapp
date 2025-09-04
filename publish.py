#!/usr/bin/env python3
"""
PyPI Publishing Script for MyEPUBApp
"""

import subprocess
import sys
import shutil
from pathlib import Path


def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run(command, check=True,
                                capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False


def clean_build_files():
    """Clean previous build files using Python modules"""
    print("\n🔧 Cleaning previous builds...")
    try:
        # Remove directories
        for dir_name in ["dist", "build"]:
            if Path(dir_name).exists():
                shutil.rmtree(dir_name)
                print(f"Removed directory: {dir_name}")

        # Remove egg-info files
        for egg_info in Path(".").glob("*.egg-info"):
            if egg_info.is_dir():
                shutil.rmtree(egg_info)
                print(f"Removed directory: {egg_info}")

        print("✅ Cleaning previous builds completed successfully")
        return True
    except Exception as e:
        print(f"❌ Cleaning previous builds failed: {e}")
        return False


def main():
    """Main publishing workflow"""
    print("🚀 MyEPUBApp PyPI Publishing Script")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Please run this script from the project root.")
        sys.exit(1)

    if not Path("src/myepubapp").exists():
        print("❌ Error: src/myepubapp directory not found.")
        sys.exit(1)

    # Step 1: Clean previous builds
    if not clean_build_files():
        sys.exit(1)

    # Step 2: Build the package
    if not run_command("python -m build", "Building package"):
        sys.exit(1)

    # Step 3: Check the built package
    if not run_command("twine check dist/*", "Checking built package"):
        sys.exit(1)

    # Step 4: Upload to Test PyPI first (optional)
    print("\n📦 Ready to publish!")
    print("\nChoose publishing option:")
    print("1. Upload to Test PyPI (recommended first)")
    print("2. Upload to Production PyPI")
    print("3. Cancel")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            print("\n🧪 Uploading to Test PyPI...")
            if not run_command("twine upload --repository testpypi dist/*", "Uploading to Test PyPI"):
                sys.exit(1)
            print("\n✅ Successfully uploaded to Test PyPI!")
            print("You can test the installation with:")
            print("pip install --index-url https://test.pypi.org/simple/ myepubapp")
            break

        elif choice == "2":
            print("\n⚠️  WARNING: You are about to upload to PRODUCTION PyPI!")
            confirm = input(
                "Are you sure? This cannot be undone easily. (yes/no): ").strip().lower()
            if confirm == "yes":
                if not run_command("twine upload dist/*", "Uploading to Production PyPI"):
                    sys.exit(1)
                print("\n🎉 Successfully uploaded to Production PyPI!")
                print("Users can now install with:")
                print("pip install myepubapp")
            else:
                print("Upload cancelled.")
            break

        elif choice == "3":
            print("Publishing cancelled.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n📚 Publishing complete!")
    print("\nNext steps:")
    print("1. Check your package on PyPI: https://pypi.org/project/myepubapp/")
    print("2. Test installation: pip install myepubapp")
    print("3. Test functionality: myepubapp --help")


if __name__ == "__main__":
    main()
