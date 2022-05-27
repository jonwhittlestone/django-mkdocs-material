# mkdocs-in-django3
Serve MkDocs from Django.

The docs are accessible as a valid Django user.

username: jon
password: asdfghj

## Usage

1. Install Python dependencies
    ```bash
    pip install -r requirements.txt
    ```

2. Compile markdown files to .html 
    ```bash
    mkdocs build
    ```

3. Run dev server
    ```bash
    python manage.py runserver
    ```

4. Try to view the docs as unauthenticated:
    http://127.0.0.1:8000/docs

5. Log in, and then revisit






With many thanks going to: 

https://www.hacksoft.io/blog/integrating-a-password-protected-mkdocs-in-django
