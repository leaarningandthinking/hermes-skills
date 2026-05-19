---
name: chinese-path-encoding
category: devops
description: Handling file paths with Chinese characters on macOS/Linux systems using byte strings and proper UTF-8 encoding
---

# Chinese Path Encoding on macOS/Linux

When working with file paths containing Chinese characters in Python scripts, use byte strings to avoid encoding issues.

## Problem

Python's string handling can cause `FileNotFoundError` when paths contain Chinese characters, especially when:
- Using subprocess calls
- Passing paths through shell commands
- Working with nested directories

## Solution: Byte Strings

Use byte strings with explicit UTF-8 encoding:

```python
import os, json

# Correct way for Chinese paths
parent = b"/path/to/parent"
folder = b"\xe4\xb8\xad\xe6\x96\x87\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9"  # 中文文件夹
full_path = os.path.join(parent, folder)

# Read file
with open(os.path.join(full_path, b"data.json"), 'r', encoding='utf-8') as f:
    data = json.load(f)
```

## Common Patterns

### 1. Directory Listing
```python
contents = os.listdir(full_path)
for item in contents:
    if isinstance(item, bytes):
        print(item.decode('utf-8'))
```

### 2. Subprocess Calls
```python
import subprocess

result = subprocess.run(
    ["/usr/bin/python3", script_path, data_path, output_path],
    capture_output=True,
    text=True
)
```

### 3. File Path Construction
```python
# Hardcode UTF-8 bytes for known paths
# Replace the byte sequence with your own folder/file names
script_path = b'/path/to/parent/\xe4\xb8\xad\xe6\x96\x87\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9/your_script.py'
data_path   = b'/path/to/parent/\xe4\xb8\xad\xe6\x96\x87\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9/data.json'
```

## Discovering the Correct Byte Sequence

If you don't know the exact byte representation of your Chinese folder name, encode it:

```python
folder_name = "中文文件夹"
print(folder_name.encode("utf-8"))
# b'\xe4\xb8\xad\xe6\x96\x87\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9'
```

Or list the parent directory in bytes mode to copy the exact byte string:

```python
import os
for item in os.listdir(b"/path/to/parent"):
    print(item)  # bytes objects you can copy verbatim
```

## Finding Files by Pattern

```python
import subprocess

# Use find command (works regardless of encoding)
result = subprocess.run(
    ["find", "/path/to/parent", "-name", "*关键词*", "-type", "f"],
    capture_output=True,
    text=True
)
print(result.stdout)
```

## Python Version Considerations

- Python 3.9+ on macOS: May need `--break-system-packages` for pip
- System Python: `/usr/bin/python3`
- Homebrew Python: `/opt/homebrew/bin/python3`

## Testing Path Existence

```python
print(f"Path: {full_path}")
print(f"Exists: {os.path.exists(full_path)}")
print(f"Contents: {os.listdir(full_path)}")
```

## macOS-Specific Considerations

On macOS, Python subprocess calls are especially sensitive to Chinese paths.

### Complete macOS Workflow

```python
import os, subprocess

# Step 1: Discover exact byte representation of your Chinese folder
parent = b"/path/to/parent"
target_keyword = b"\xe4\xb8\xad\xe6\x96\x87"  # part of "中文" — adjust to your folder
for item in os.listdir(parent):
    if isinstance(item, bytes) and target_keyword in item:
        print(f"Found: {item}")

# Step 2: Construct full byte paths
folder_bytes = b'\xe4\xb8\xad\xe6\x96\x87\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9'  # 中文文件夹
script_path = os.path.join(parent, folder_bytes, b'your_script.py')
data_path   = os.path.join(parent, folder_bytes, b'input.json')
output_path = os.path.join(parent, folder_bytes, b'output.json')

# Step 3: Execute with system Python
result = subprocess.run(
    ["/usr/bin/python3", script_path, data_path, output_path],
    capture_output=True, text=True
)
```

### Alternative: Copy to ASCII Path

If byte paths are too complex, copy files to a temporary ASCII-only path (e.g. `/tmp/work/`), run the script, then copy results back.

## Common Pitfalls

1. **Double escaping**: Don't use `\\xe6` in byte strings, use actual bytes `\xe6`
2. **String vs bytes**: Ensure consistency — don't mix `str` and `bytes` in `os.path.join`
3. **Shell commands**: Use `shlex.quote()` for shell arguments with special characters
4. **Encoding**: Always specify `encoding='utf-8'` when reading/writing files
5. **macOS subprocess**: Always use byte paths (`b"..."`) for paths with non-ASCII characters in subprocess calls
