from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(num):
    """Checks if a number is prime using an optimized trial division."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    if n == 1:
        return 2
    count = 1
    num = 3
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 2  # Check only odd numbers after 2

@app.route('/api/prime/<int:n>', methods=['GET'])
def get_nth_prime(n):
    """API endpoint to get the nth prime number."""
    if n <= 0:
        return jsonify({'error': 'Please provide a positive integer for n.'}), 400

    # Add a reasonable limit to prevent server overload
    if n > 10000:
        return jsonify({'error': 'This calculator supports n up to 10,000 to ensure a quick response.'}), 400

    try:
        prime = find_nth_prime(n)
        return jsonify({'n': n, 'prime': prime})
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
