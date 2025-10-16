# Nth Prime Number Calculator

## Summary

This is a minimal, full-stack web application that finds the nth prime number. The user can enter a positive integer 'n' into a web interface, and the application will calculate and display the corresponding prime number.

The application consists of a simple frontend built with HTML and vanilla JavaScript, and a backend API built with Python and the Flask framework.

## Setup

Follow these steps to get the application running on your local machine.

### Prerequisites

- Python 3.6+
- `pip` (Python package installer)
- A modern web browser

### Installation & Configuration

1.  **Create Project Files:**
    Create a new directory for the project and place the `main.py` and `index.html` files inside it.

2.  **Set up a Python Virtual Environment (Recommended):**
    Open your terminal or command prompt in the project directory and run:
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    With your virtual environment activated, install the required Python packages:
    ```bash
    pip install Flask Flask-CORS
    ```

## Usage

1.  **Start the Backend Server:**
    Run the Flask application from your terminal:
    ```bash
    python main.py
    ```
    The server will start and listen for requests, typically on `http://127.0.0.1:5000`.

2.  **Open the Frontend:**
    Open the `index.html` file directly in your web browser (e.g., by double-clicking it).

3.  **Find a Prime Number:**
    - Enter a positive integer into the input field (e.g., 10).
    - Click the "Find Prime" button.
    - The result will be displayed below the button.

## Code Explanation

### `main.py` (Backend)

-   **Framework:** Uses **Flask**, a lightweight Python web framework, to create the API.
-   **CORS:** `Flask-CORS` is used to allow the frontend (running on a `file://` protocol) to make requests to the backend server.
-   **API Endpoint:** Defines a single GET endpoint `/api/prime/<int:n>`.
    -   It accepts an integer `n` as part of the URL.
    -   It includes basic validation to ensure `n` is a positive integer and is not excessively large (to prevent server overload).
-   **Prime Calculation:**
    -   `find_nth_prime(n)`: The core logic function that iterates through numbers to find the nth prime.
    -   `is_prime(num)`: A helper function that uses an optimized trial division algorithm to efficiently check if a number is prime.
-   **Response:** The endpoint returns a JSON object with the result (e.g., `{"n": 10, "prime": 29}`) or an error message.

### `index.html` (Frontend)

-   **Structure:** A simple HTML5 page containing a title, a form with a number input and a submit button, and a `div` to display the results.
-   **Styling:** Inline CSS is used for a clean, modern, and user-friendly interface. The layout is centered and responsive.
-   **JavaScript:**
    -   An event listener is attached to the form's `submit` event.
    -   `event.preventDefault()` is used to stop the default page reload on submission.
    -   The `fetch()` API makes an asynchronous GET request to the backend's `/api/prime/` endpoint.
    -   It handles both successful responses and potential errors (e.g., network issues, server errors), displaying appropriate messages to the user.
    -   A helper function `ordinalSuffix()` is included to format the output nicely (e.g., "1st", "2nd", "10th").

## License

This project is licensed under the MIT License.
