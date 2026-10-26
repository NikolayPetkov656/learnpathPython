# LearnPath

LearnPath is a Django web application for organizing certain learning goals from users into roadmaps, managing learning steps, and collecting reusable educational resources.

The application is a shared workspace without any way of registration, login, or user-specific data. All visitors work with the same roadmaps, steps, and resources.

## Features

### Roadmaps

- Create, view, edit, and delete learning roadmaps.
- Assign beginner, intermediate, or advanced difficulties.
- Search roadmaps by titles and descriptions.
- Filter roadmaps via a filter.
- Sort roadmaps by title, newest first, or oldest first.
- View completion progress calculated from added learning steps.

### Learning steps

- Create steps belonging to a roadmap.
- Set the position of each step.
- View and edit learning instructions.
- Mark steps as completed or incomplete.
- Attach multiple learning resources.
- View a step's linked resources.
- Delete steps through a confirmation page.

### Resource library

- Create, view, edit, and delete learning resources.
- Store a title, URL, resource type, and optional description.
- View the steps associated with a resource.
- Open learning links in a separate browser tab.

### Dashboard and interface

- View roadmap, resource, completed-step, and remaining-step counts.
- View overall completion progress.
- Access recently created roadmaps and pending steps.
- Navigate through a shared header and footer.
- Access a page-not-found preview through the footer.
- Use responsive Bootstrap styling.

## Technologies

- Python 3.14
- Django 6.1.2
- SQLite
- Django Template Language
- Bootstrap 5.3.3
- Git and GitHub

The exact Python package versions are listed in `requirements.txt`.

## Project structure

```text
learnpathPython/
├── config/                  # Project settings and root URL configuration
├── roadmaps/                # Roadmap model, forms, views, and dashboard
│   ├── migrations/
│   └── templatetags/        # Custom completion-label filter
├── steps/                   # Learning-step model, form, and views
│   └── migrations/
├── resources/               # Resource model, form, and views
│   └── migrations/
├── templates/
│   ├── partials/            # Shared navigation, footer, and form rendering
│   ├── roadmaps/
│   ├── steps/
│   ├── resources/
│   ├── base.html
│   ├── dashboard.html
│   └── 404.html
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Database design

### Roadmap

Stores a learning path with:

- Title
- Description
- Difficulty
- Creation timestamp

Completion counts and progress are calculated in % from the roadmap's steps rather than stored separately.

### Step

Stores a learning activity with:

- Parent roadmap
- Title
- Description
- Position
- Completion status
- Linked resources
- Creation timestamp

### Resource

Stores learning material with:

- Title
- Website address
- Resource type
- Optional description
- Creation timestamp

### Relationships

- Roadmap to Step: one-to-many. Each step belongs to one roadmap, and a roadmap can contain multiple steps.
- Step to Resource: many-to-many. A step can use multiple resources, and a resource can support multiple steps.

### Deletion behavior

- Deleting a roadmap also deletes its steps.
- Deleting a step does not delete its roadmap or resource records.
- Deleting a resource removes its associations with steps without deleting those steps.
- Delete operations require confirmation through a POST form.

## Installation and startup

No environment variables, credentials, API keys, or database passwords are required for local use.

```powershell
git clone [https://github.com/NikolayPetkov656/learnpathPython.git](https://github.com/NikolayPetkov656/learnpathPython.git)
cd learnpathPython
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Open loopback, `http://127.0.0.1:8000/` in a browser.

## Configuration

- Database: SQLite, stored locally as `db.sqlite3`.
- Environment variables: none are required..
- Credentials: none are required.
- External API keys: none are required.
- Authentication: no registration, login, or logout functionality is implemented.
- Admin access: not required for creating or managing application objects.

Django's built-in authentication-related components remain in the generated project configuration, but the application's workflow does not use user accounts.

### Styling dependency

Bootstrap CSS is loaded from a public CDN. Internet access is needed to load that stylesheet.

The application does not require an external API or hosted database. Its pages and forms remain functional without the Bootstrap stylesheet, but the intended styling will not be available.

### Development security

The committed settings use `DEBUG=True` and a development-only secret key to support local execution without configuration changes.

This configuration is not suitable for public deployment. Before deployment, use a new private secret key, disable debugging, configure allowed hosts, and review Django's deployment checklist.

Do not use the committed development key to protect a production application.

## Starting with an empty database

The application does not require preloaded records.

Use the navigation links to create data:

1. Open Roadmaps and select Create roadmap.
2. Enter a title, description, and difficulty.
3. Open Resource library and select Add resource.
4. Enter a title, valid HTTP/HTTPS address, and resource type.
5. Return to the roadmap and open its details.
6. Select Add step.
7. Enter a title, description, and position.
8. Optionally select resources and save.
9. Open the step and select Edit step.
10. Mark it completed and save.
11. Return to the roadmap or dashboard to view updated progress.

Resources are optional when creating a step. They can be added later by editing the step.

If the resource list is empty, create resources through the Resource library first.

## Validation

Examples of implemented validation include:

- Roadmap and step titles must contain at least 3 characters.
- Resource titles must contain at least 3 characters.
- Roadmap and step descriptions must contain at least 10 characters.
- Step positions must be whole numbers starting from 1.
- Resource addresses must be valid HTTP or HTTPS URLs.
- Difficulty and resource type must use the available choices.
- Required fields cannot be omitted.
- A saved step's parent roadmap cannot be changed through its edit form.

Forms display customized labels, help text, placeholders, and validation messages.

Creation timestamps are not exposed as editable fields.

## Templates

The project uses:

- A shared base template.
- Template inheritance.
- Reusable navigation, footer, and form partials.
- Built-in template filters, including `date`, `truncatewords`, and `linebreaks`.
- A custom `completion_label` filter for readable completion status.

Main page templates:

1. Dashboard
2. Roadmap list
3. Roadmap details
4. Roadmap creation
5. Roadmap editing
6. Roadmap deletion confirmation
7. Step details
8. Step creation
9. Step editing
10. Step deletion confirmation
11. Resource list
12. Resource details
13. Resource creation
14. Resource editing
15. Resource deletion confirmation

(The custom 404 template is additional to these pages. The base template and partials are not included in this count.)

## Custom 404 page

Use the Page-not-found preview link in the footer to view the styled error page during local development.

The preview intentionally returns HTTP status 404, as required.

With `DEBUG=True`, an actual unknown URL normally displays Django's technical 404 page. With debugging disabled and suitable allowed hosts configured, Django uses the custom `404.html` template.

The preview allows the design to be inspected without changing the default local configuration.

## Code organization

- Models define stored data, relationships, and model-level validation.
- Forms define editable fields, presentation, and input validation.
- Views handle requests, object retrieval, and redirects.
- Templates display content.
- Each Django app owns a distinct part of the learning workflow.

Django's class-based views are reused for standard CRUD behavior rather than duplicating request-handling code.

## Scope

LearnPath is a shared local learning workspace, not a multi-user learning platform.

It does not include:

- User accounts or personal progress.
- Login, logout, or registration.
- Certificates.
- Automatic resource scraping.
- Prepopulated learning content.