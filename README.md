# Discount Coupon API

This project provides a simple REST API for generating and validating discount coupons for a given product and user. The API is built using **Flask** and stores data in a local JSON file (`db.json`). The API allows users to generate unique, time-bound coupons and validate them for specific products and users.

## Features

- **Generate Coupon**: Create a unique coupon for a product with a validity of 1 hour.
- **Validate Coupon**: Check if a coupon is valid for a product, user, and whether it is expired.
- **Mock Database**: A JSON file (`db.json`) to log and manage coupon data.

## Requirements

- **Python 3.x** or higher
- **Flask**: A lightweight web framework for Python
- **python-dotenv**: For managing environment variables
- **uuid**: For generating unique coupon codes

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Thenx0009/Discount-coupon-api.git
   cd discount-coupon-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory of the project (if not already created):
   ```bash
   echo "FLASK_ENV=development" > .env
   ```

## Project Structure

```
discount-coupon-api/
│
├── flaskr/                # Flask application folder
│   ├── __init__.py        # Initialize the Flask app and routes
│   ├── models.py          # Coupon generation and validation logic
│   ├── routes.py          # Routes for generating and validating coupons
│   └── db.json            # Mock database (stores coupon data)
│
├── .env                   # Environment variables
├── requirements.txt       # List of dependencies
├── run.py                 # Script to run the Flask app
└── README.md              # Project documentation
```

## Configuration

The project uses environment variables to configure the Flask environment. The `.env` file contains the following:

```
FLASK_ENV=development
```

You can customize this to fit your needs.

## API Endpoints

### **1. Generate Coupon**

- **Endpoint**: `/api/generate-coupon`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "product_id": 123,
    "user_id": 1
  }
  ```
- **Response**:
  ```json
  {
    "message": "Coupon generated successfully.",
    "coupon_code": "ABC12345",
    "expiry_date": "2024-12-26T15:00:00"
  }
  ```
- **Description**: This endpoint generates a unique coupon code for a specified product ID and user ID. The coupon will be valid for 1 hour.

### **2. Validate Coupon**

- **Endpoint**: `/api/validate-coupon`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "coupon_code": "ABC12345",
    "product_id": 123,
    "user_id": 1
  }
  ```
- **Response**:
  ```json
  {
    "message": "Coupon is valid."
  }
  ```
  - Or, in case the coupon is invalid:
  ```json
  {
    "error": "Coupon has expired."
  }
  ```
- **Description**: This endpoint validates a coupon code for a specified product ID and user ID. It checks whether the coupon is valid and has not expired.

## Running the Application

1. To start the Flask development server, run the following command:

   ```bash
   python run.py
   ```

2. The application will be available at `http://127.0.0.1:5000`.

3. Use **Postman** or **cURL** to interact with the API endpoints.

## Example Requests

### **Generate Coupon Request**
```bash
curl -X POST http://127.0.0.1:5000/api/generate-coupon -H "Content-Type: application/json" -d '{"product_id": 123, "user_id": 1}'
```

### **Validate Coupon Request**
```bash
curl -X POST http://127.0.0.1:5000/api/validate-coupon -H "Content-Type: application/json" -d '{"coupon_code": "ABC12345", "product_id": 123, "user_id": 1}'
```

## License

This project is open-source and available under the [MIT License](LICENSE).

