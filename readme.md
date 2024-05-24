# Color Extraction Flask App

This is a Python Flask application that allows users to upload an image through a web browser. The app processes the image to extract the top ten dominant colors and returns these colors back to the browser using the Cologram library.

## Features

- Upload an image from your browser.
- Extract the top ten dominant colors from the image.
- Display the extracted colors back in the browser.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

## Usage

1. **Run the Flask app:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

3. **Upload an image:**
   - Click on the upload button and select an image from your device.
   - The app will process the image and display the top ten dominant colors.

## Project Structure

```
.
├── app.py
├── imagel.py
├── templates
│   └── index.html
├── static
│   └── css
│       └── style.css
├── requirements.txt
└── README.md
```

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML file for the web interface.
- `static/css/style.css`: The CSS file for styling the web interface.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Dependencies

- Flask
- cologram

Make sure to install the dependencies using the provided `requirements.txt` file.


## Contact

If you have any questions, feel free to reach out at [akingbadeboluwatife030@gmail.com](mailto:akingbadeboluwatife030@gmail.com).
