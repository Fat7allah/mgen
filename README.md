# MGEN

Modern Generic Enterprise Resource Planning System

## Installation

1. [Install bench](https://github.com/frappe/bench).

2. Create a new bench:
```sh
bench init frappe-bench
cd frappe-bench
```

3. Add the app:
```sh
bench get-app mgen
```

4. Create a new site:
```sh
bench new-site mysite.local
```

5. Install the app on the site:
```sh
bench --site mysite.local install-app mgen
```

6. Start the development server:
```sh
bench start
```

## License

MIT
