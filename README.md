# ToDo API ![alt text](https://images.pexels.com/photos/4065894/pexels-photo-4065894.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940)

### How to use API?

https://todolist-service-api.herokuapp.com/

#### Tasks

All tasks: \
GET `https://todolist-service-api.herokuapp.com/api/v1/tasks/`

Create new task: \
POST `https://todolist-service-api.herokuapp.com/api/v1/tasks/`

Mark task as completed: \
POST `https://todolist-service-api.herokuapp.com/api/v1/tasks/<id_of_task>/done/`

Mark task as priority: \
POST `https://todolist-service-api.herokuapp.com/api/v1/tasks/<id_of_task>/priority/`

Delete a task: \
DELETE `https://todolist-service-api.herokuapp.com/api/v1/tasks/<id_of_task>/`

Update a task: \
PUT `https://todolist-service-api.herokuapp.com/api/v1/tasks/<id_of_task>/`

#### Users

Create new user: \
POST `https://todolist-service-api.herokuapp.com/auth/users/`

Create access and refresh tokens: \
POST `https://todolist-service-api.herokuapp.com/auth/jwt/create/`

Get a new access and refresh tokens: \
POST `https://todolist-service-api.herokuapp.com/auth/jwt/refresh/`

Info about user: \
POST `https://todolist-service-api.herokuapp.com/auth/users/me/`