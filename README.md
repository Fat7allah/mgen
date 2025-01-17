# MGEN - Modern Generic ERP System

MGEN is a modern, flexible, and user-friendly Enterprise Resource Planning system built on the Frappe Framework.

## Features

- Modern UI/UX
- Modular Architecture
- Extensible Design
- RESTful API Support
- Real-time Updates
- Multi-tenant Support

## Installation

1. Install Frappe Bench:
```bash
pip install frappe-bench
```

2. Initialize a new bench:
```bash
bench init frappe-bench
cd frappe-bench
```

3. Create a new site:
```bash
bench new-site mysite.local
```

4. Get MGEN app:
```bash
bench get-app mgen
```

5. Install app on your site:
```bash
bench --site mysite.local install-app mgen
```

## Development Setup

1. Clone this repository:
```bash
git clone https://github.com/your-username/mgen.git
cd mgen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## License

MIT License. See LICENSE file for more information.

## Support

For support and discussions, please raise an issue in the GitHub repository.
