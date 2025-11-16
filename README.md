
# 💎 Django Jewelry Shop – E-commerce Web Application

A complete, production-ready jewelry e-commerce platform built with Django. This application supports user authentication, product browsing, cart and checkout functionality, and an administrative dashboard for product and order management.

---

## 🚀 Project Overview

This web application is being developed as part of a final year academic project. It showcases how to build a robust full-stack e-commerce system using Django, featuring a responsive UI for both desktop and mobile users.

> ⚠️ **Note**: The project is still under development. New features and improvements are being actively added.

---

## 🛠️ Tech Stack

| Layer         | Technology                   |
|---------------|------------------------------|
| Backend       | Python, Django               |
| Frontend      | HTML5, CSS3, Bootstrap       |
| Database      | SQLite (can switch to PostgreSQL/MySQL) |
| Authentication| Django's Built-in Auth System|
| Environment   | Virtualenv                   |

---

## ✨ Key Features

- ✅ User registration, login, and logout
- 🛍️ Product listing with categories
- 🔍 Product detail view with images & descriptions
- 🛒 Add to cart, update quantity, remove items
- 💳 Checkout and order confirmation
- 🧾 Admin dashboard for product, order, and user management
- 📱 Mobile responsive design
- 📧 Order confirmation via email

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vedantthate/Online_Shoping_Website.git
cd Online_Shoping_Website-main 
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open in browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Admin Access

- Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Use the superuser credentials created earlier.

---

## 📂 Project Structure

```
django-jewelry-shop/
├── jewelry/                  # Main Django app (models, views, urls)
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/                # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── product_list.html
│   ├── product_detail.html
│   ├── cart.html
│   └── checkout.html
│
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                    # Uploaded media (product images, etc.)
│
├── db.sqlite3                # SQLite database
├── manage.py
├── requirements.txt
└── venv/                     # Python virtual environment

```

---


## 📸 Screenshots

### 🏠 Homepage
![Homepage](screenshots/homepage.png)

### 📃 Product Listing
![Product Listing](screenshots/product-list.png)

### 📄 Product Detail
![Product Detail](screenshots/product-detail.png)

### 🛒 Cart Page
![Cart Page](screenshots/cart.png)

### 🔐 Admin Dashboard
![Admin Dashboard](screenshots/admin-dashboard.png)

---

## 📌 Future Enhancements

- 📝 Product reviews & ratings
- 🚚 Real-time order tracking
- 🔐 Social login (Google, Facebook)
- 💸 Refund & return system
---

## 📄 License

This project is developed for educational purposes only. Commercial use is not permitted without prior permission.

---

## 🙋‍♂️ Author & Contact

- **Name**: Damini Gudape  
---

## ✅ Academic Use Disclaimer

This project is created solely for academic and educational demonstration as part of a final year project submission.
