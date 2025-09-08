# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2025-09-08

### Changed
- Replaced Chinese comments with English comments in source code for better internationalization
- Cleaned up project directory by removing unused temporary files and test artifacts

### Removed
- Removed temporary directories: `temp_epub/`, `temp_final/`, `temp_original/`
- Removed test files: `test_append.txt`, `test_debug.epub`, `test_debug2.epub`, `test_merge.py`, `test_merged.epub`, `test_output.epub`, `test.txt`, `append_content.txt`, `initial_content.txt`

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
