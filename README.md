# NASA Astronomy Picture of the Day Viewer

This project displays the NASA Astronomy Picture of the Day (APOD) on a simple web page.

## Description

This application fetches the latest Astronomy Picture of the Day from the NASA API, downloads the image, and displays it on a web page using Streamlit. It also shows the explanation provided by NASA for the image.

## Features

-   Fetches the image and data from the NASA APOD API.
-   Downloads the image of the day.
-   Displays the image and its explanation on a user-friendly web interface.

## Requirements

The following Python libraries are required to run this application:

-   `streamlit`
-   `python-dotenv`
-   `requests`

You can install them using the `requirements.txt` file.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd WebPageWithAnImage
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add your NASA API key and the path to the image:
    ```
    NASA_API=your_nasa_api_key
    IMAGE_PATH=path_to_your_image/yyyy-mm-dd.jpg
    ```
    You can get a free API key from the [NASA API website](https://api.nasa.gov/).

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run main.py
```

This will open a new tab in your browser with the application running.
