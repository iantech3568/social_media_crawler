# Social Media Crawler

This is a simple Django-based web application for crawling social media posts.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/social_media_crawler.git
    cd social_media_crawler
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- The homepage will display the crawled social media posts.

## Crawling Script

The crawling script is located in `crawler/crawl.py`. Modify the `crawl_social_media` function to customize the crawling logic.

## License

This project is licensed under the MIT License.
