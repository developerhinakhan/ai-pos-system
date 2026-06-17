# 🤖 AI-Powered POS System

> A production-grade Point of Sale system built with FastAPI, PostgreSQL, Redis, and Groq AI — deployed on Railway with full Docker support and 28 automated tests.

**Live Demo:** [ai-pos-system-production.up.railway.app](https://ai-pos-system-production.up.railway.app/docs)  
**Portfolio:** [developerhinakhan.github.io](https://developerhinakhan.github.io)  
**GitHub:** [github.com/developerhinakhan/ai-pos-system](https://github.com/developerhinakhan/ai-pos-system)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Local Setup](#local-setup)
- [Docker Setup](#docker-setup)
- [Running Tests](#running-tests)
- [Deployment](#deployment)

---

## 🎯 Overview

An AI-powered Point of Sale (POS) system designed for small to medium businesses. Built with a layered architecture pattern following production-grade standards. The system includes intelligent inventory analysis, sales insights, and business recommendations powered by Groq AI (LLaMA 3.3 70B).

This project was built from scratch to demonstrate real-world backend development skills including:
- RESTful API design with FastAPI
- Relational database management with PostgreSQL
- Caching layer with Redis
- AI integration with Groq API
- Containerization with Docker
- Cloud deployment on Railway
- Test-driven development with pytest

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | FastAPI |
| **Language** | Python 3.11 |
| **Database** | PostgreSQL (Supabase) |
| **ORM** | SQLAlchemy |
| **Migrations** | Alembic |
| **Caching** | Redis (Upstash) |
| **AI** | Groq API (LLaMA 3.3 70B) |
| **Auth** | JWT + OAuth2 |
| **Testing** | pytest + httpx |
| **Container** | Docker + Docker Compose |
| **Deployment** | Railway |
| **Version Control** | Git + GitHub |

---

## ✨ Features

### Core Features
- **JWT Authentication** — Secure register/login with OAuth2PasswordRequestForm
- **Role-Based Access** — Admin and Cashier roles with protected routes
- **Products Management** — Full CRUD with SKU tracking and stock management
- **Categories Management** — Organize products with category system
- **Customers Management** — Customer profiles and purchase history
- **Sales Management** — Complete sales processing with automatic stock deduction
- **Redis Caching** — Cached responses for products and categories (300s TTL)

### AI Features (Powered by Groq LLaMA 3.3 70B)
- **Low Stock Analysis** — AI-powered inventory alerts and recommendations
- **Sales Insights** — Intelligent analysis of sales patterns and trends
- **Business Recommendations** — Strategic business advice based on data

### Technical Features
- Layered architecture (Router → Service → Repository → Database)
- Docker containerization with multi-service setup
- 28 automated pytest tests across all modules
- Alembic database migrations
- Professional Git branching workflow
- Environment-based configuration with Pydantic Settings

---

## 🏗️ Architecture

```
Client Request
      ↓
   Router (FastAPI endpoints)
      ↓
   Service (Business Logic)
      ↓
   Repository (Database Queries)
      ↓
   Database (PostgreSQL)
      ↓ (caching layer)
   Redis Cache
```

Each module follows this strict layered pattern:
- `router.py` — API endpoints and request/response handling
- `service.py` — Business logic and validation
- `repo.py` — Database queries and data access
- `model.py` — SQLAlchemy database models
- `schema.py` — Pydantic validation schemas

---

## 📁 Project Structure

```
ai-pos-system/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── cache.py          # Redis caching utilities
│   │   │   ├── config.py         # Pydantic settings
│   │   │   ├── dependencies.py   # Auth dependencies
│   │   │   └── security.py       # JWT + password hashing
│   │   ├── modules/
│   │   │   ├── ai/               # Groq AI endpoints
│   │   │   ├── auth/             # Authentication
│   │   │   ├── categories/       # Categories CRUD
│   │   │   ├── customers/        # Customers CRUD
│   │   │   ├── products/         # Products CRUD
│   │   │   ├── sales/            # Sales management
│   │   │   └── users/            # Users management
│   │   ├── database.py           # Database connection
│   │   └── main.py               # FastAPI application
│   ├── alembic/                  # Database migrations
│   ├── tests/                    # pytest test suite
│   │   ├── conftest.py           # Test configuration
│   │   ├── test_auth.py          # Auth tests (4 tests)
│   │   ├── test_products.py      # Products tests (6 tests)
│   │   ├── test_categories.py    # Categories tests (6 tests)
│   │   ├── test_customers.py     # Customers tests (6 tests)
│   │   └── test_sales.py         # Sales tests (6 tests)
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Register new user | ❌ |
| POST | `/auth/login` | Login and get JWT token | ❌ |

### Products
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/products/` | Get all products (cached) | ✅ |
| POST | `/products/` | Create product | ✅ |
| GET | `/products/{id}` | Get product by ID | ✅ |
| PUT | `/products/{id}` | Update product | ✅ |
| DELETE | `/products/{id}` | Delete product | ✅ |
| GET | `/products/low-stock` | Get low stock products | ✅ |

### Categories
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/categories/` | Get all categories (cached) | ✅ |
| POST | `/categories/` | Create category | ✅ |
| GET | `/categories/{id}` | Get category by ID | ✅ |
| PUT | `/categories/{id}` | Update category | ✅ |
| DELETE | `/categories/{id}` | Delete category | ✅ |

### Customers
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/customers/` | Get all customers | ✅ |
| POST | `/customers/` | Create customer | ✅ |
| GET | `/customers/{id}` | Get customer by ID | ✅ |
| PUT | `/customers/{id}` | Update customer | ✅ |
| DELETE | `/customers/{id}` | Delete customer | ✅ |

### Sales
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/sales/` | Get all sales | ✅ |
| POST | `/sales/` | Create sale (auto-deducts stock) | ✅ |
| GET | `/sales/{id}` | Get sale by ID | ✅ |
| DELETE | `/sales/{id}` | Delete sale | ✅ |

### AI Features
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/ai/low-stock` | AI low stock analysis | ✅ |
| GET | `/ai/sales-insights` | AI sales insights | ✅ |
| GET | `/ai/recommendations` | AI business recommendations | ✅ |

---

## ⚙️ Environment Variables

Create a `.env` file in the `backend/` folder:

```env
# App
APP_NAME=AI POS System
DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/pos_db

# Redis
REDIS_URL=redis://localhost:6379

# AI
GROQ_API_KEY=your-groq-api-key-here
```

---

## 💻 Local Setup

### Prerequisites
- Python 3.11+
- PostgreSQL
- Redis
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/developerhinakhan/ai-pos-system.git
cd ai-pos-system

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r backend/requirements.txt

# Set up environment variables
cp backend/.env.example backend/.env
# Edit .env with your values

# Run database migrations
cd backend
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

Visit: `http://localhost:8000/docs`

---

## 🐳 Docker Setup

### Prerequisites
- Docker Desktop

### Run with Docker Compose

```bash
# Clone the repository
git clone https://github.com/developerhinakhan/ai-pos-system.git
cd ai-pos-system

# Start all services (app + PostgreSQL + Redis)
docker-compose up --build

# Run migrations
docker exec -it ai_pos_app alembic upgrade head
```

Visit: `http://localhost:8000/docs`

### Services
| Service | Port | Description |
|---------|------|-------------|
| FastAPI App | 8000 | Main application |
| PostgreSQL | 5433 | Database |
| Redis | 6379 | Cache |

---

## 🧪 Running Tests

```bash
cd backend
pytest tests/ -v
```

### Test Results
```
tests/test_auth.py::test_register_success          PASSED ✅
tests/test_auth.py::test_register_duplicate_email  PASSED ✅
tests/test_auth.py::test_login_success             PASSED ✅
tests/test_auth.py::test_login_wrong_password      PASSED ✅
tests/test_categories.py::test_create_category     PASSED ✅
tests/test_categories.py::test_get_categories      PASSED ✅
tests/test_categories.py::test_get_single_category PASSED ✅
tests/test_categories.py::test_update_category     PASSED ✅
tests/test_categories.py::test_delete_category     PASSED ✅
tests/test_categories.py::test_create_without_token PASSED ✅
tests/test_customers.py (6 tests)                  PASSED ✅
tests/test_products.py (6 tests)                   PASSED ✅
tests/test_sales.py (6 tests)                      PASSED ✅

28 passed in ~11s 🏆
```

### Test Architecture
- **Test Database:** SQLite (isolated from production)
- **Test Client:** FastAPI TestClient
- **Fixtures:** Module-scoped database setup/teardown
- **Coverage:** Auth, Products, Categories, Customers, Sales

---

## 🚀 Deployment

This application is deployed on **Railway** with:
- **Database:** Supabase (PostgreSQL)
- **Cache:** Upstash (Redis)
- **App:** Railway (Docker)

**Live URL:** https://ai-pos-system-production.up.railway.app/docs

---

## 👩‍💻 Developer

**Hina Khan** — Python Backend Developer  
📍 Okara, Pakistan  
🌐 [Portfolio](https://developerhinakhan.github.io)  
💼 [GitHub](https://github.com/developerhinakhan)  

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).