# FAQ Management System with Multilingual Support

## Overview
This project is a Django-based FAQ management system with multilingual support. The system allows users to store Frequently Asked Questions (FAQs) along with their answers, which can be dynamically translated into multiple languages. The answers are formatted using a WYSIWYG editor (powered by Django CKEditor). The system supports multilingual content, a REST API for CRUD operations, caching for translation storage, and automated translations via Google Translate API.

---

## Features

- **Multilingual FAQ Storage:** FAQs can be stored with multiple translations for different languages.
- **WYSIWYG Editor:** Rich text answers can be added using Django CKEditor, enabling formatted content.
- **Caching with Redis:** FAQs and their translations are cached for improved performance.
- **REST API:** A RESTful API for managing FAQs, supporting dynamic language selection via query parameters.
- **Google Translate Integration:** Automatic translation of FAQ content in different languages.
- **Django Admin Panel:** Manage FAQs easily through a user-friendly admin interface.

---

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **Django Rest Framework**: To build the API for managing FAQs.
- **Django CKEditor**: For WYSIWYG editor support for answers.
- **Redis**: Used for caching translations for better performance.
- **Google Translate API**: For automatic translations.
- **Docker**: Containerization of the application.
- **PostgreSQL**: The database used for storing FAQs.

---

## Installation

Follow the steps below to set up the project locally:

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose (optional for containerization)
- Redis (for caching translations)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ARTHON9611/faq_project.git
   cd faq_project
   ```

2. **Create a Python virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add your Google Translate API key:

   ```bash
   GOOGLE_TRANSLATE_API_KEY=<your-google-translate-api-key>
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### 1. **Fetch FAQs**

- **GET** `/api/faqs/`
- Fetch a list of FAQs in English (default language).

#### Example Request:

```bash
curl http://localhost:8000/api/faqs/
```

### 2. **Fetch FAQs with Language Selection**

- **GET** `/api/faqs/?lang=<language_code>`
- Fetch FAQs in a specified language.

#### Example Request:

```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

Where `lang` can be any of the supported languages like `hi` (Hindi), `bn` (Bengali), etc.

---

## Models

The FAQ model consists of the following fields:

- **question**: The question in English (TextField).
- **answer**: The answer text, supported by CKEditor (RichTextField).
- **question_<lang_code>**: Translations for the question, e.g., `question_hi` for Hindi.
- **answer_<lang_code>**: Translations for the answer, e.g., `answer_hi` for Hindi.

### Model Method

A model method is implemented to retrieve translated text dynamically based on the selected language.

---

## WYSIWYG Editor

We use **django-ckeditor** to enable users to format the answers with rich text. This allows users to add styled text, images, and other content directly through the admin panel.

---

## Caching with Redis

Redis is used for caching translations of FAQs. This improves performance by reducing the need to repeatedly translate the same content.

- **Caching Translations**: Translations are stored in Redis for quick access.
- **Fallback**: If a translation is not available, the application defaults to English.

---

## Unit Tests

Unit tests are written to ensure the correctness of the FAQ models and API endpoints. To run the tests, execute:

```bash
python manage.py test
```

---

## Docker Support

This project includes **Docker** and **Docker Compose** support for containerization.

1. **Build and run the containers**:

   ```bash
   docker-compose up --build
   ```

2. **Run migrations inside the Docker container**:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

---

## Deployment

This project can be deployed on platforms like **Heroku** or **AWS**. Docker support is provided for easy deployment and scaling.

---

## Git Commit Messages

Ensure that your commit messages follow the **conventional commit** format:

- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API examples`

---

## Contribution

Feel free to fork the repository, make changes, and create a pull request. Please follow the contribution guidelines and ensure that your code adheres to the project's coding standards.

### Steps to contribute:

1. Fork the repository.
2. Clone your fork and create a new branch.
3. Implement your changes and test them.
4. Commit your changes with clear messages.
5. Push the changes and create a pull request.

---

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django CKEditor](https://django-ckeditor.readthedocs.io/en/latest/)
- [Google Translate API](https://cloud.google.com/translate)
- [Redis](https://redis.io/)

### Instructions for Customizing

- Replace `<your-google-translate-api-key>` with your actual Google Translate API key.
- You can customize the `API Endpoints` section as per your specific setup.
- Add any other tools or libraries you used that are relevant to the project.
