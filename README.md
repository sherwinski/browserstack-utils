# browserstack-utils

A CLI tool for quickly and easily managing your Browserstack jobs. You will need a [BrowserStack](https://www.browserstack.com/) account, which will provide a `USERNAME` and `ACCESS_KEY`. These will be required to interact with BrowserStack's API.

## Basic setup

Install the requirements:
```
$ pip install -r requirements.txt
```

Save your BrowserStack account credentials into `utils/auth.py`:
```
USERNAME = "USERNAME"
ACCESS_KEY = "ACCESS_KEY"
```

Run the application:
```
$ python -m browserstack_utils --help
```

## Usage:

Fetch all workers that are currently running:
```
$ python browserstack-utils.py fetch

[ 
    ...
]

Stored in new file workers1576455085.806158.json
```

Terminate all workers by passing the name of the file as an argument:
```
$ python browserstack-utils.py delete workers1576455085.806158.json
```

Optionally, cleanup all worker files once done:
```
$ python browserstack-utils.py clean

Deleting file:  workers1576455085.806158.json
```

To run the tests:
```
$ pytest
```
