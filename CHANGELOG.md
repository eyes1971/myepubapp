# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2025-09-08

### Added
- ✨ **Smart Volume Detection**: Automatic hierarchical TOC generation based on chapter level combinations
  - Detects h1+h2 pattern and makes h1 chapters into volumes
  - Detects h2+h3 pattern and makes h2 chapters into volumes
  - Detects h1+h3 pattern and makes h1 chapters into volumes
- 🎯 **Intelligent TOC Structure**: Creates nested table of contents for multi-volume books
- 📖 **Enhanced Chapter Processing**: Improved chapter ordering and Introduction page positioning

### Fixed
- 🐛 **Critical EPUB Generation Errors**: Resolved multiple epubcheck validation failures
  - Fixed duplicate cover image entries in manifest
  - Fixed undefined cover property errors
  - Fixed duplicate "cover" IDs causing OPF validation errors
- 🔧 **TOC Reading Order Issues**: Fixed NAV-011 warnings about TOC link order mismatch
  - TOC links now match spine reading order
  - Proper EPUB 3.0 compliance for navigation structure
- 📋 **Cover Image Handling**: Resolved cover image declaration and property issues
  - Fixed RSC-008 error: Referenced resource not declared in OPF manifest
  - Fixed OPF-027 error: Undefined property "cover"
  - Fixed RSC-005 error: Duplicate entries in ZIP file
- 📖 **Introduction Page Ordering**: Fixed Introduction page appearing at the end instead of beginning
  - Proper spine ordering: nav → intro → chapters
  - Correct TOC positioning for introduction content

### Changed
- 🔄 **TOC Generation Logic**: Completely refactored table of contents generation
  - Added automatic volume detection based on chapter level patterns
  - Improved hierarchical structure creation for complex documents
  - Enhanced EPUB 3.0 compliance with proper nav element usage
- 🏗️ **Cover Image Processing**: Simplified and optimized cover image handling
  - Uses ebooklib's built-in cover management
  - Eliminates duplicate manifest entries
  - Ensures proper OPF metadata generation
- 📑 **Chapter Ordering**: Improved chapter and spine ordering logic
  - Introduction pages now correctly positioned at the beginning
  - Proper reading order maintained throughout EPUB structure

### Technical Improvements
- ✅ **EPUB 3.0 Compliance**: All generated EPUB files now pass epubcheck validation
- 🧪 **Comprehensive Testing**: Added test cases for all volume detection scenarios
- 🧹 **Code Cleanup**: Removed unused imports and optimized code structure
- 📝 **Documentation Updates**: Updated CLI help text with new volume marker information

## [1.0.3] - 2025-09-08

### Changed
- This update primarily focuses on optimizing the core `src/myepubapp/core/book.py` module:
- Updated function documentation: `_extract_chapters_from_epub()` and `merge_existing_epub_with_new_chapters()`
- Updated log outputs: EPUB merge success and error messages
- Maintained functionality integrity: All changes are non-breaking, preserving all functional logic

## [1.0.2] - 2025-09-01

### Added
- Initial release of MyEPUBApp
- Text-to-EPUB conversion functionality
- Support for chapter markers (※ⅰ, ※ⅱ, ※ⅲ)
- Tag conversion feature (<書名> → 《書名》)
- EPUB validation capabilities
- Command-line interface with multiple modes (init, append, validate)

### Features
- Convert plain text files to EPUB format
- Append new chapters to existing EPUB files
- Automatic table of contents generation
- Support for introduction pages
- Custom metadata support
- Debug logging capabilities

### Technical Details
- Python 3.8+ compatibility
- Dependencies: ebooklib, beautifulsoup4
- Cross-platform support (Linux, macOS, Windows)
