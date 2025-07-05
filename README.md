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
- `templates/index.html`: The HTML template for the web interface.
- `service-account-key.json`: (Not included in repo) Contains API credentials. This file should be kept secure and loaded via environment variables.

## Installation
1. Clone the repository:
