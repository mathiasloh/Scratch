# Scratch Website 
## Getting started 
### Version Control
We will use [Git/Github](https://desktop.github.com/) for version controls. This will enable us to work simultaneously on the same project. 
(It works similar like google docs). For more information, please visit the [documentation for Git](https://git-scm.com/).
### Software versions
  1. Python3.4 and above.  [Link to download](https://www.python.org/downloads/).
  2. Pip3. Automatically installed for Python3.4+
  3. Django 1.9.1 and other plugins. Using Command Prompt (Windows) or Terminal (Mac), run the following commands  
    ```
    pip3 install django  
    ```  
    ```
    pip3 install django-registration-redux  
    ```  
    ``` 
    pip3 install django-crispy-forms  
    ```  
    **! Attention !** If you are running on a mac, you might need a ```sudo``` behind each command  

## How to use these files?
All modern websites these days are seperated into 2 repositories, **dynamic** (things that changes: urls) and **static** 
(things that does not change: images, styles, javascript). Django is useful because it helps to separate these two. We will only deal
with **django_files** folder. However, please download both files in this case.

In **django_files** folder, it contains all our files that generates webpages, admin sites, etc. This is in _development mode_, meaning
only you will be able to view the server yourself. At the end of the project, we will need to find a **web hosting services that includes Python** to set up our 
server on _production mode_. 

### How to run the server  
Again, using either command prompt [(tutorial)](http://cli.learncodethehardway.org/book/) or terminal [(tutorial)](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)
``` sh
cd \<downloaded folder>\django_files\ (Windows)  
cd /<downloaded folder>/django_files/ (Mac)
```  
After which, run the following commands
``` sh
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
- The first statement is used whenever we included new static files to our ```\django_files\static\our_static``` folder. This will
automatically add files into our ```/static_in_env/``` folder. 
- The second statement is used to make migrations the databases whenever we add entries / make new tables (base de donnees)  
- The third statement is used to migrate the databases
- **The last statement is used to run our server**

To view the server is _development mode_, point your browser to ```http://127.0.0.1:8000```

## Current features implemented
1. **Admin page**. Go to ```http://127.0.0.1:8000/admin``` to access the admin page. _user=admin_, _password=admin_  
  We will be able to do a lot of things there. **! Attention !** Still a work in progress!
2. **Webpage generator**. We are now equipped to create new webpages with minimal effort. 

## Future features (To-do)
1. Registration pages
2. List of all uploaded Scratch projects (?)
3. Development blog
4. Design cleanups / formatting
5. Proper name for our website
  
