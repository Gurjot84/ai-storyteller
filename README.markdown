# AI Story Generator

## Overview
This is a Flask-based web application that generates creative short stories using the Gemini API. Users can input a story prompt, and the app produces a 200-300 word story with a clear beginning, middle, and end. The project is designed for educational purposes and to demonstrate integration of AI with web technologies.

## Features
- Input a custom story prompt via a simple web interface.
- Generate engaging, unique stories using the Gemini API.
- Display the generated story or any errors directly on the webpage.

## Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- Requests library (`pip install requests`)
- A valid Gemini API key (obtainable from Google Cloud)

## Project Structure
- `app.py`: The main Flask application file containing the backend logic.
  - Sets up the Flask app and defines the `/` route.
  - Handles POST requests with user prompts, calls the Gemini API, and renders the response.
- `templates/index.html`: The HTML template for the web interface.
  - Includes a form for prompt input and a section to display the generated story or errors.
- `service-account-key.json`: (Not included in repo) Contains API credentials. This file should be kept secure and loaded via environment variables.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/flask-story-generator.git
   cd flask-story-generator
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   (Note: Create a `requirements.txt` file with `Flask` and `requests` if not already present.)
4. Set up your Gemini API key:
   - Store the key in an environment variable named `API_KEY` (e.g., using a `.env` file with `python-dotenv`).
   - Example: `export API_KEY="your_api_key_here"`
5. Run the application:
   ```
   python app.py
   ```
   Access it at `http://127.0.0.1:5000/`.

## Usage
1. Open the app in your browser.
2. Enter a story prompt (e.g., "A time traveler visits ancient Egypt").
3. Click "Generate Story" to see the result.
4. The generated story or any errors will be displayed on the page.

## Configuration
- The `maxOutputTokens` is set to 500 for longer stories.
- The `temperature` (0.7), `topK` (50), and `topP` (0.9) parameters control the creativity and randomness of the output.
- Adjust these in `app.py` as needed.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Ensure to follow the project structure and update the README if adding new features.

## License
This project is open-source under the MIT License (see LICENSE file for details).

## Acknowledgments
- Built with Flask and the Gemini API by Google.
- Inspired by AI storytelling experiments.