# *The Game Boy Archive* Core

The code that powers [*The Game Boy Archive*](https://github.com/gb-archive) project. Periodically mirrors Game Boy related software, hardware and literature. Keeps those forks synced to upstream and provides access to everything archived.

## Backend

- **fork.py**. Forks everything linked in the awesome-gbdev repository which is a GitHub repository.
- **sync.py**. Checks every fork in gb-archive. If has a parent, it syncs the repo to upstream with the last commits.

## Frontend

TODO

### Resources and documentation

- [GitHub REST API v3](https://developer.github.com/v3/)
- [Requests](https://media.readthedocs.org/pdf/requests/latest/requests.pdf)
- [Syncing a fork via API](https://stackoverflow.com/questions/26846667/how-to-update-a-fork-from-its-original-via-the-github-api)
