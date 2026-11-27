# Bgremover (Background-Remover)

An automated background removal web tool built with Python and Flask that isolates subjects from images and outputs crisp, transparent PNGs. Designed for speed and simplicity, it lets users upload an image through a clean drag-and-drop interface and download the background-free result.

## Features

* **Automated Subject Isolation:** Uses `rembg` to detect foreground subjects with high edge accuracy.
* **In-Memory Image Processing:** Processes image data directly in RAM using `io.BytesIO` and Pillow (`PIL`) without cluttering the disk with temporary files.
* **Pure CSS Drag-and-Drop UI:** Lightweight HTML & CSS frontend with zero heavy JavaScript dependencies.
* **Multiple Format Support:** Accepts `JPG`, `PNG`, and `WEBP` uploads and exports transparent `PNG` files.

## Tech Stack

* **Backend:** Python, Flask
* **Image Processing:** `rembg`, Pillow (`PIL`)
* **Frontend:** HTML5, CSS3

## How It Works

1. **Upload:** The user selects or drags an image into the web form (`POST /upload`), which sends the file to the Flask backend.
2. **Binary Read & Removal:** The server reads the uploaded image as raw binary bytes and passes them to `rembg.remove()` to strip the background.
3. **In-Memory Conversion:**
   ```python
   out_img = Image.open(io.BytesIO(out_data))
   ```
   This converts the raw output bytes directly in memory into a usable Pillow (`PIL`) Image object without needing to save a temporary intermediate file to the hard drive.
4. **Output:** The processed transparent PNG is returned to the user.

## Getting Started

### Prerequisites
* Python 3.9 or higher
* `pip`

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Krish0579/Background-Remover.git
   cd Background-Remover
   ```

2. **Install dependencies**
   ```bash
   pip install flask rembg pillow
   ```

3. **Run the application**
   ```bash
   python3 app.py
   ```
   *(Note: On the very first run, `rembg` will automatically download the background-removal ONNX model.)*

4. **Open in browser**
   Visit `http://127.0.0.1:5000` in your browser.

## Future Improvements

* Add live before-and-after image preview on the result page
* Support custom background color replacement alongside transparent PNG export
* Add batch processing for multiple images at once
