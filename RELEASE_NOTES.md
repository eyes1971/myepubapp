# Release Notes - MyEPUBApp v1.0.2

## 📅 Release Date
2025-09-05

## 🔧 Changes

### 🐛 Bug Fixes
- **Critical TOC Generation Fix**: Fixed a critical bug in the table of contents generation that was causing missing chapters in EPUB files
- **TOC Chapter Skipping**: Resolved issue where TOC only showed first few chapters, skipping subsequent ones in multi-chapter documents
- **Recursive Index Management**: Fixed index management in `build_toc_level()` function to prevent chapter skipping during TOC generation

### ✅ Improvements
- **Multi-Group Chapter Support**: TOC now correctly handles any number of chapter groups (tested with 2, 3, 4+ groups)
- **Hierarchy Level Support**: Enhanced support for all chapter hierarchy combinations (h1+h2, h1+h3, h2+h3, etc.)
- **Robust Testing**: Added comprehensive testing for various chapter structures and hierarchies

## 🐛 Technical Details

### Root Cause
The bug was in the `TOCGenerator.build_toc_level()` function's recursive logic. When processing chapters with child elements, the function was incorrectly managing the index after returning from recursion, causing subsequent chapters at the same level to be skipped.

### Fix Implementation
```python
# Before (buggy)
i = build_toc_level(chapter_list, i + 1, actual_next_level)

# After (fixed)
end_i = build_toc_level(chapter_list, i + 1, actual_next_level)
i = end_i - 1  # Correctly handle recursion end position
```

### Impact
- ✅ All existing EPUB files with multiple chapters now generate correct TOC
- ✅ New EPUB files with any number of chapters work properly
- ✅ All chapter hierarchy combinations (h1, h2, h3) are supported
- ✅ Backward compatibility maintained

## 🧪 Testing

### Test Cases Verified
- ✅ 2 groups of chapters (h1 h2 h2)
- ✅ 3 groups of chapters (h1 h2 h2 h1 h2 h2)
- ✅ 4+ groups of chapters (multiple Vol + chapters)
- ✅ Different hierarchy levels (h1+h3, h2+h3)
- ✅ Mixed chapter structures

### Example Test Case
```
Input: 4 Volumes with 2 chapters each
Output: TOC correctly shows all 4 volumes with their respective chapters
```

## 📦 Files Changed
- `src/myepubapp/generators/toc.py` - Fixed TOC generation logic
- `pyproject.toml` - Version bump to 1.0.2
- `README.md` - Updated changelog and version info
- `dist/myepubapp-1.0.2.tar.gz` - Source distribution
- `dist/myepubapp-1.0.2-py3-none-any.whl` - Wheel distribution

## 🔄 Migration
No migration required. This is a bug fix that maintains full backward compatibility.

## 🙏 Acknowledgments
Thanks to users who reported the TOC generation issues, enabling us to identify and fix this critical bug.

---

**Installation**: `pip install myepubapp==1.0.2`
**Repository**: https://github.com/eyes1971/myepubapp
**Documentation**: See README.md for usage instructions
