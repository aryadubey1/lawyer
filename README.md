# Subhash Mishra & Associates — Premium Law Firm Website (Django)

A high-end, classical-editorial full-stack law firm web application crafted with **Django 6.0.3**, **Django REST Framework 3.16.1**, **PostgreSQL**, **Cloudinary Media Storage**, **Tailwind CSS**, **Alpine.js**, and **Django Q2** for asynchronous Telegram notifications.

Every single piece of content (practice areas, blog insights, team members, photo gallery, client logos, about-page profile, and firm contact information) is 100% manageable through the Django Admin Panel (`/admin/`).

---

## 🏛️ Key Features

- **Design System**: Dark Charcoal (`#1A1714`) + Gold Accent (`#B08D57`) + Warm Off-White (`#F7F5F2`) aesthetic with Playfair Display editorial typography and subtle grain texture.
- **Admin-First Architecture**: Designed for non-technical law firm partners with rich text editing via CKEditor, drag-order slides/cards, and inline management.
- **Asynchronous Telegram Bot Alerts**: Instant alerts sent to the managing partner's Telegram chat via `django-q2` background tasks upon contact form submission (never blocking the user).
- **Public REST API**: Read-only public DRF endpoints (`/api/v1/`) with `django-filter` support and a public write endpoint for contact submissions.
- **Dynamic Interactivity (Alpine.js)**: Hero carousel with fade transitions and pause-on-hover, category-filtered photo gallery with click-to-lightbox, sticky navbar with dynamic dropdowns, mobile menu, and scroll-to-top.
- **SEO & Compliance Ready**: Automatic `sitemap.xml`, `robots.txt`, per-page meta title and description tags, Bar Council of India disclaimer flatpage, and privacy policy.

---

## ⚙️ Requirements & Tech Stack

- **Python**: 3.12+
- **Django**: 6.0.3
- **Database**: PostgreSQL (or local fallback via `dj-database-url`)
- **Media**: Cloudinary (with local filesystem fallback for development)
- **Async Queue**: `django-q2` (ORM-based cluster)
- **CSS**: Tailwind CSS via `django-tailwind`
- **Node.js**: v18+ (for compiling Tailwind source)

---

## 🚀 Quickstart & Setup Guide

### 1. Clone & Setup Virtual Environment

```bash
cd lex-chambers
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration (`.env`)

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```ini
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_SETTINGS_MODULE=config.settings.development
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL Connection String
DATABASE_URL=postgres://postgres:postgres@localhost:5432/lex_chambers

# Cloudinary Media Storage (Free tier: https://cloudinary.com/)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Telegram Bot (Optional in dev, required for instant message alerts)
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

> **Note**: If `CLOUDINARY_CLOUD_NAME` is left empty, media uploads will gracefully fall back to the local `media/` directory.

---

### 4. Database Migrations & Initial Seed Data

Run migrations and seed the database with realistic law firm dummy content (12 practice areas, 6 team members, 6 blog posts, 10 gallery photos, 5 clients, and about profile):

```bash
python manage.py migrate
python manage.py seed_db
```

This creates a default administrator:
- **Admin URL**: `http://127.0.0.1:8000/admin/`
- **Username**: `admin`
- **Password**: `adminpassword123`

---

### 5. Running the Application

In your first terminal, start the Django development server:

```bash
python manage.py runserver
```

In a second terminal, start the **Django Q Cluster** (to process asynchronous Telegram contact form notifications):

```bash
python manage.py qcluster
```

In a third terminal (if developing Tailwind CSS):

```bash
python manage.py tailwind start
```

---

## 📱 Telegram Notifications Setup

1. Open Telegram and search for `@BotFather`.
2. Send `/newbot` and follow the prompts to create your bot. Copy the **HTTP API Token**.
3. Send a message to your new bot.
4. Visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` in your browser to get your `chat_id`.
5. Enter these credentials directly in the Django Admin under **Site Configuration** (`/admin/core/siteconfig/1/change/`) or in `.env`.
6. Whenever a visitor submits the contact form, an instant formatted Telegram alert with client contact details will be dispatched via `qcluster`.

---

## 🌐 Public REST API Endpoints

All endpoints are available under `/api/v1/`:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/v1/practice-areas/` | List all active practice areas |
| `GET` | `/api/v1/practice-areas/{slug}/` | Practice area details |
| `GET` | `/api/v1/team/` | List all advocates and counsel |
| `GET` | `/api/v1/blog/posts/` | List published blog posts (supports `?category__slug=`) |
| `GET` | `/api/v1/blog/categories/` | List blog categories |
| `GET` | `/api/v1/gallery/` | List photo gallery (supports `?category=`) |
| `GET` | `/api/v1/clients/` | List client logos |
| `POST`| `/api/v1/contact/` | Public contact submission endpoint |

---

## 📁 Directory Structure

```
lex-chambers/
├── config/                          # Django settings package
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── components/              # Modular settings (apps, db, q_cluster, etc.)
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── core/                        # SiteConfig singleton, Homepage, Seed command
│   ├── practice_areas/              # Practice areas list & detail + DRF
│   ├── team/                        # Team members & Founder spotlight + DRF
│   ├── blog/                        # Blog posts, categories, CKEditor + DRF
│   ├── gallery/                     # Photo gallery with Alpine tabs + DRF
│   ├── clients/                     # Client logos strip + DRF
│   ├── about/                       # AboutPage singleton + Stats
│   └── contact/                     # Contact form, Telegram service & Q2 task
├── api/                             # DRF v1 aggregate router
├── templates/                       # Jinja/Django templates with components & partials
├── theme/                           # Django-tailwind app
├── static/                          # Static assets (Alpine.js, styles.css, JS)
├── fixtures/                        # 7 JSON seed fixtures
└── scripts/                         # Standalone utility scripts
```

---

## 🛡️ License

Confidential and proprietary to Subhash Mishra & Associates. All rights reserved.
