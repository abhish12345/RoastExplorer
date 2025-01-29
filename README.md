# Coffee Roast Selector

This is a Flask-based web application that helps users select different coffee roast types and provides details such as temperature, duration, flavor notes, and profile descriptions. The project is deployed on Vercel for easy access.

## Project Structure
```
CoffeeRoastProject/
│── coffee_roast_model.py  # Flask backend
│── coffee_roast_data.csv  # Coffee roast dataset
│── templates/
│   └── index.html         # Frontend UI
│── static/
│   └── images/
│       ├── light.jpg
│       ├── medium.jpg
│       ├── dark.jpg
│── vercel.json            # Vercel configuration file
│── runtime.txt            # Python runtime version
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## Features
✅ Select coffee roast types (Light, Medium, Dark)
✅ View details like roasting temperature, duration, and flavor notes
✅ Display roast images dynamically
✅ Hosted on Vercel for easy access

## Installation & Running Locally
### Prerequisites
- Python 3.x
- Flask
- Pandas
- Gunicorn

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/CoffeeRoastProject.git
   cd CoffeeRoastProject
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask application:**
   ```bash
   python coffee_roast_model.py
   ```
5. **Open in browser:**
   - Go to `http://127.0.0.1:5000/`

## Deploying on Vercel
### 1. Install Vercel CLI
```bash
npm install -g vercel
```
### 2. Login to Vercel
```bash
vercel login
```
### 3. Initialize Deployment
```bash
vercel init
```
### 4. Deploy the Application
```bash
vercel --prod
```

## Technologies Used
- **Flask** - Web framework
- **Pandas** - Data handling
- **Gunicorn** - Production WSGI server
- **Vercel** - Deployment platform

## Live Demo
🔗 [Your Vercel Deployed Link](https://roast-explorer.vercel.app/)

---
🚀 Happy Brewing! ☕

