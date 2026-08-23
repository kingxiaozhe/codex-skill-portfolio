# Deploy the site to your own domain server

`site/` is a dependency-free static website. Upload the **contents** of this directory, including `assets/`, to the document root for the domain.

For example, if the site's document root is `/var/www/skills.example.com`, the final layout should be:

```text
/var/www/skills.example.com/
  index.html
  en/
    index.html
  styles.css
  assets/
```

For an Nginx virtual host, use this minimal configuration and replace `skills.example.com` with your domain:

```nginx
server {
    listen 80;
    server_name skills.example.com;

    root /var/www/skills.example.com;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~* \.(?:css|png)$ {
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

Enable HTTPS with the certificate workflow you already use for the server. The website contains no API, database, form, cookie, tracking code, or environment variable.

After the domain is live, replace the relative `og:image` value in both `index.html` and `en/index.html` with its final absolute URL, for example `https://skills.example.com/assets/hero-workflow-desk.png`. This enables reliable social sharing previews.

Before upload, run the repository checks from the project root:

```bash
python3 scripts/validate_inventory.py
python3 scripts/validate_site.py
```
