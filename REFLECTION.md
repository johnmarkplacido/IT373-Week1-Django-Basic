

Setting up the Django environment was both exciting and challenging. At first, I encountered difficulties with installing the correct Python version because my system had multiple versions already installed. To solve this, I used `py -m venv venv` to create a dedicated virtual environment, which ensured that the project dependencies did not conflict with my global installation. Another challenge was installing Django itself. I initially forgot to activate my virtual environment before running `pip install django`, which caused the package to install globally. After realizing the mistake, I reinstalled it inside the virtual environment.

Running the Django development server for the first time also presented issues. I faced migration errors because I hadn’t applied the initial database migrations. Running `python manage.py migrate` solved this and allowed the server to start successfully. Finally, setting up Git and connecting it to a remote repository took some trial and error, particularly with SSH keys. Once I configured GitHub correctly, I was able to commit my files and push them to the repo.

Overall, these challenges helped me better understand environment management, the importance of virtual environments, and proper Git workflow. The process gave me confidence to troubleshoot issues and strengthened my foundational skills in web development.
