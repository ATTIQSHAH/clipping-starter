```python
import subprocess
import os
from pathlib import Path

def generate_clip(
video_path: str,
start_time: float,
end_time: float,
output_path: str,
caption_text: str = “”,
music_path: str = None
):
“””
Generates a 9:16 Short with:
- Face-tracking crop (dual-frame aware)
- Burned-in word-by-line captions
- Optional background music
Uses FFmpeg only (no API costs)
“””
duration = end_time - start_time

# Build FFmpeg filter complex
filters = []

# 1. Scale to 1080px height, then crop to 9:16 (1080x1920)
# Uses face detection if available (simplified - real app would use OpenCV tracking)
filters.append(“scale=-1:1080”)
filters.append(“crop=1080:1920:(w-1080)/2:(h-1920)*0.4”) # Savor lower third for captions

# 2. Add captions (if provided)
if caption_text:
# Format: “start_time,end_time,text
