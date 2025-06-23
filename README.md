# Shop API Based On Django And DRF

This is RESTful API based on django REST framework, which allows users to browse and add the products to the shopping cart and order them they can also write reviews for products, and has a customized admin panel for managing products and users.

## 🛠️ Tech Stack
- **Backend:** Django (Python), Django REST framework
- **Database:** SQLite (default for development)


## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone (https://github.com/MohammadHossein007/Shop-API)
   cd Shop-API
   
2. **Create and activate virtual environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

5. **Apply migrations**
    ```bash
    python manage.py migrate

6. **Run the server**
   ```bash
   python manage.py runserver
