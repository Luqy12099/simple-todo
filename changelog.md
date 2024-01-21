### Changelog `Todolist`
<b>Full Changelog</b>

---
#### v 0.0.4 -- 2024/01/21
###### New:
* API (views)
    * todolist_app/item_create
    * todolist_app/item_update

* urls
    * item/create
    * item/update

###### Change:
* Templates 
    * todolist_app/todolist_edit.html
        * Add 2 column in class="container-fluid" (for add item and read item)
        * Add script to handle async checkbox for "completed" item

---
#### v 0.0.3 -- 2024/01/20
###### New:
* Make django app (todolist_app)
* Add Db (models) todolist_app (ToDoList and item) (done makemigrations and migrate)
* Add todolist\todolist_app\form.py class "form_create"

* API (views)
    * todolist_app/todolist_create
    * todolist_app/todolist_read
    * todolist_app/todolist_delete
    * todolist_app/todolist_update

* urls
    * todolist/create
    * todolist/
    * todolist/delete/<int:todo_id>/

* Templates 
    * todolist_app/todolist_create
    * todolist_app/todolist_read
    * todolist_app/todolist_edit.html


###### Change:
* API (views)
    * register/register
        * Change HttpResponseRedirect('/login')
    
* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['todolist_app.apps.TodolistAppConfig', ]
    * first_django\urls.py
        * Add path('todolist/', include("todolist_app.urls")),
    * register\base.html
        * Add lokasi sidebar ToDo

---
#### v 0.0.2 -- 2024/01/20
###### New:
* Make django app (register)
* Add pip install crispy-bootstrap4
* Add todolist\register\form.py

* API (views)
    * register/base
    * register/register
    * register/logout_view

* Templates ()
    * register/base
    * register/register
    * registration/login
    * register/base_wo_sidebar

* urls
    * /
    * register/register
    * register/logout_view
    

###### Change:
* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['register.apps.RegisterConfig', "crispy_forms", "crispy_bootstrap4",]
        * Add CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
        * Add CRISPY_TEMPLATE_PACK = "bootstrap4"
        * Add LOGIN_REDIRECT_URL = '/'
        * Add LOGIN_URL = '/login/'
        * Add LOGOUT_REDIRECT_URL = '/login/'
    * first_django\urls.py
        * Add path('', include('django.contrib.auth.urls')),
        * Add path('', include("register.urls")),

---

#### v 0.0.1 -- 2024/01/19
###### New:
* Make initial file {changelog, pip_req}
* Make django project

###### Change:
* -

---
