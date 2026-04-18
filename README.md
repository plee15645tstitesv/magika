# Magika

> Fork of [google/magika](https://github.com/google/magika) — AI-powered file type detection.

Magika is a novel AI-powered file type detection tool that relies on the content of files (rather than metadata like file extensions) to accurately identify them.

## Features

- **AI-powered detection**: Uses a custom deep learning model to identify file types from content
- **Fast**: Optimized for speed with minimal overhead
- **Accurate**: Outperforms traditional tools like `file` on many content types
- **Multi-language**: Available as Python library, CLI tool, and Rust crate

## Installation

### Python

```bash
pip install magika
```

### From source

```bash
git clone https://github.com/your-org/magika.git
cd magika
pip install -e python/
```

## Usage

### CLI

```bash
# Detect file type
magika file.pdf

# Detect multiple files
magika *.txt

# Output as JSON
magika --json file.bin

# Recursive directory scan
magika -r ./directory
```

### Python API

```python
from magika import Magika

m = Magika()
result = m.identify_path("file.pdf")
print(result.output.ct_label)  # e.g. "pdf"
print(result.output.score)     # confidence score
```

### Batch processing

```python
from pathlib import Path
from magika import Magika

m = Magika()
paths = [Path("file1.txt"), Path("file2.bin")]
results = m.identify_paths(paths)
for path, result in zip(paths, results):
    print(f"{path}: {result.output.ct_label} ({result.output.score:.2f})")
```

## Supported Content Types

Magika supports detection of 100+ content types including:

- Documents: PDF, DOCX, XLSX, PPTX, ODT
- Code: Python, JavaScript, TypeScript, Rust, Go, Java, C/C++
- Archives: ZIP, TAR, GZ, 7Z, RAR
- Images: PNG, JPEG, GIF, WebP, BMP
- Media: MP3, MP4, WAV, AVI
- Data: JSON, XML, CSV, YAML, TOML
- And many more...

## Development

### Prerequisites

- Python 3.8+
- Rust (for the Rust crate)
- Docker (optional, for containerized builds)

### Setup

```bash
git clone https://github.com/your-org/magika.git
cd magika
python -m venv .venv
source .venv/bin/activate
pip install -e "python/[dev]"
```

### Running tests

```bash
cd python
pytest tests/
```

### Useful one-liners for quick local testing

```bash
# Check a bunch of mixed files at once and grep for low-confidence results
magika --json -r ./samples | python -c "import sys,json; [print(r) for r in json.load(sys.stdin) if r['result']['output']['score'] < 0.7]"

# List only the detected content-type labels, one per line (handy for piping into sort/uniq)
magika --json -r ./samples | python -c "import sys,json; [print(r['result']['output']['ct_label']) for r in json.load(sys.stdin)]"
```

## Contributing

Contributions are welcome! Please read our contributing guidelines and check existing issues before opening a new one.

When reporting a misdetection, please use the [misdetection issue template](.github/ISSUE_TEMPLATE/misdetection.md).

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.

This project is a fork of [google/magika](https://github.com/google/magika), which is also licensed under Apache 2.0.
