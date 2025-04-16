# Billboard Flask Application

This project is a Flask application that retrieves the top songs from various Billboard charts. It provides an API endpoint to access the data.

## Project Structure

```
Billboard
├── api
│   └── app.py          # Contains the Flask application and API endpoint
├── requirements.txt     # Lists the required Python dependencies
├── vercel.json          # Configuration for deploying to Vercel
└── README.md            # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Billboard
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application locally, use the following command:
```
python api/app.py
```

The application will be available at `http://127.0.0.1:5000/top-songs`.

## API Endpoint

- **GET /top-songs**
  - Query Parameters:
    - `chart`: The name of the Billboard chart (default is `hot-100`).
    - `limit`: The number of top songs to retrieve (default is `10`).
  - Response: A JSON array of the top songs with their rank, title, and artist.

## Deployment

To deploy the application to Vercel, ensure you have the `vercel.json` file configured correctly. Then, run the following command:
```
vercel
```

Follow the prompts to complete the deployment process.