# Deployment Instructions for Tailwind CSS

You have recently switched from using a Tailwind CDN to a local Tailwind installation to fix loading issues (e.g., on BSNL networks).

## Option 1: The Easiest Way (No Node.js needed on server)

1.  **On your Local Machine (Windows):**
    *   Make sure you have built the CSS file (I already did this for you).
    *   Commit the compiled CSS file to your git repository:
        ```bash
        git add static/style/tailwind.css static/js/swiper-bundle.min.js static/style/swiper-bundle.min.css package.json tailwind.config.js templates/main/base.html
        git commit -m "Switch to local Tailwind CSS and Swiper"
        git push origin main
        ```

2.  **On your AWS Lightsail Server:**
    *   Navigate to your project folder.
    *   Pull the latest changes:
        ```bash
        git pull origin main
        ```
    *   Run collectstatic to move the new files to your public static folder:
        ```bash
        python3 manage.py collectstatic --noinput
        ```
    *   Restart your web server (Command depends on your setup, examples below):
        ```bash
        # If using Gunicorn/Nginx:
        sudo systemctl restart gunicorn
        sudo systemctl restart nginx
        
        # If using Apache:
        sudo systemctl restart apache2
        ```

## Option 2: Building on the Server (If you want to edit CSS on the server)

1.  **Install Node.js and npm on the Server:**
    ```bash
    # For Ubuntu/Debian:
    sudo apt update
    sudo apt install -y nodejs npm
    ```

2.  **Install Dependencies:**
    Navigate to your project directory on the server and run:
    ```bash
    npm install
    ```

3.  **Build the CSS:**
    ```bash
    npm run build:css
    ```

4.  **Collect Static Files:**
    ```bash
    python3 manage.py collectstatic --noinput
    ```
