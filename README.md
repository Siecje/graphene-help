## Traceback
```
Traceback (most recent call last):
  File "/home/cody/Desktop/cookbook/venv/lib/python3.7/site-packages/promise/promise.py", line 487, in _resolve_from_executor
    executor(resolve, reject)
  File "/home/cody/Desktop/cookbook/venv/lib/python3.7/site-packages/promise/promise.py", line 754, in executor
    return resolve(f(*args, **kwargs))
  File "/home/cody/Desktop/cookbook/venv/lib/python3.7/site-packages/graphql/execution/middleware.py", line 75, in make_it_promise
    return next(*args, **kwargs)
  File "/home/cody/Desktop/cookbook/cookbook/schema.py", line 20, in mutate
    return super().mutate(info, **args)
graphql.error.located_error.GraphQLLocatedError: 'super' object has no attribute 'mutate'
```

## Steps

```shell
python -m venv venv
venv/bin/python -m pip install pip setuptools wheel --upgrade
venv/bin/python -m pip install -r requirements.txt
venv/bin/python manage.py migrate
venv/bin/python manage.py runserver
```

Then go to http://127.0.0.1:8000/graphql

```
                    mutation createProject($name: String!) {
                        createProject(name: $name) {
                            id
                        }
                    }
```

QUERY VARIABLES
```
{"name": "foo"}
```
