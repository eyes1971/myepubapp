# PyPI Publishing Guide for MyEPUBApp

This guide will help you publish MyEPUBApp to PyPI so others can easily install and use it.

## Prerequisites

Before publishing, make sure you have:

1. **Python packages installed**:
   ```bash
   pip install build twine
   ```

2. **PyPI account**:
   - Create an account at https://pypi.org/
   - Create an account at https://test.pypi.org/ (for testing)

3. **API tokens** (recommended):
   - Go to https://pypi.org/manage/account/#api-tokens
   - Create a new API token
   - Store it securely (don't commit to git)

## Quick Publishing

### Option 1: Use the Automated Script (Recommended)

1. **Run the publishing script**:
   ```bash
   python publish.py
   ```

2. **Follow the prompts**:
   - Choose to upload to Test PyPI first (recommended)
   - Test your package
   - Then upload to production PyPI

### Option 2: Manual Publishing

1. **Build the package**:
   ```bash
   python -m build
   ```

2. **Check the build**:
   ```bash
   twine check dist/*
   ```

3. **Upload to Test PyPI**:
   ```bash
   twine upload --repository testpypi dist/*
   ```

4. **Test the installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ myepubapp
   ```

5. **Upload to Production PyPI**:
   ```bash
   twine upload dist/*
   ```

## Configuration

### API Token Setup

Create a `.pypirc` file in your home directory:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcC...

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBp...
```

Replace the password values with your actual API tokens.

## Testing Your Package

After uploading to Test PyPI, test it thoroughly:

```bash
# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ myepubapp

# Test basic functionality
myepubapp --help

# Test with sample data
echo "※ⅰ Chapter 1
This is a test chapter." > test.txt

myepubapp -i test.txt --output-epub test.epub
```

## Production Release

Once you're satisfied with testing:

1. **Update version** in `pyproject.toml` if needed
2. **Run the publishing script** and choose production upload
3. **Verify** the package appears on https://pypi.org/project/myepubapp/

## Troubleshooting

### Common Issues

1. **"Package name already exists"**:
   - Choose a different name in `pyproject.toml`
   - Check if the name is available on PyPI

2. **"Invalid authentication"**:
   - Check your `.pypirc` file
   - Verify your API token is correct

3. **"Build failed"**:
   - Ensure all dependencies are listed in `pyproject.toml`
   - Check for syntax errors in your code

### Getting Help

- PyPI documentation: https://packaging.python.org/
- Twine documentation: https://twine.readthedocs.io/
- Build documentation: https://build.pypa.io/

## Post-Publishing

After successful publishing:

1. **Update your GitHub repository** with release tags
2. **Announce** the release on relevant forums/communities
3. **Monitor** for issues and user feedback
4. **Plan** future updates and maintenance

## Version Management

When releasing new versions:

1. Update the version in `pyproject.toml`
2. Update the changelog
3. Create a git tag
4. Publish the new version

Remember: Once published to production PyPI, you cannot delete or modify the package, only upload new versions!
