# Minimal test app for Alpine + HTMX error

To reproduce error, do the following

1. Run the app:

    ```sh
    FLASK_APP="min_test_alpine_htmx.app:app" FLASK_ENV="development" flask run
    ```

2. Navigate to the URL on the command line (defaults to `http://127.0.0.1:5000`)

3. Open your browser's console

4. Click through to page 3 (url should be `<base>/page3`)

5. Press the browser's back button

6. Observe the console warnings + errors in your browser's console
