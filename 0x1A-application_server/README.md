![](./c7d1ed0a2e10d1b4e9b3.jpg)


# Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

# Resources
## Read or watch:

- Application server vs web server(https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw)
- How to Serve a Flask Application with Gunicorn and Nginx
on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using
virtualenv, just install everything globally)(https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA)
- Running Gunicorn (https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
- Be careful with the way Flask manages slash in route - strict_slashes(https://intranet.alxswe.com/rltoken/lEg0zpkkDcLtdl3VD4ACRQ)
- Upstart documentation(https://intranet.alxswe.com/rltoken/cldrneY3Qr7LlDysygzRHw)
# Requirements
## General
A README.md file, at the root of the folder of the project, is mandatory
Everything Python-related must be done using python3
All config files must have comments
## Bash Scripts
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
