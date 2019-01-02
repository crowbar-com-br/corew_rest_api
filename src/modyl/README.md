# Modyl
Library to import and use modules on HUG REST API

## Implementation

### Usage
The structure of the module, is the same of a package, so, you got:
* A ```___init__.py``` file to import the file with the code, and say that the folder is a package
* A file with your code and a ```start(api: 'HUG API object')``` method, this file need to have the same name as the package
* A ```info.json``` file to describe the module

How to create a module:

1. Make a folder with the module name:
```
$ mkdir test && cd test
```
2. Transform this folder into a package, by:
```
$ nano __init__.py
```
3. In nano, write this, and then save and close it(by pressing ctrl+o and then ctrl+x):
```
from  . import test
```
4. Now let's create a file for our code:
```
$ nano test.py
```
5. In nano, write this, and then save and close it(by pressing ctrl+o and then ctrl+x):
```
import hug

def start(api):

  def tested():
    return "Yeahhhh!!!!"

  hug.get('/work', api=api)(tested)
```
6. Create the info for the module:
```
$ nano info.json
```
7. In nano, write this, and then save and close it(by pressing ctrl+o and then ctrl+x):
```
{
  "name": "test",
  "description": "Just a test module",
  "file": "test",
  "version": "1",
  "author": "Gruber"
}
```
8. Now, zip this files and the module is done!
9. And, let's test it:
```
$ curl -v -H "filename: test.zip" -H "Content-Type: applications/octet-stream" --data-binary @test.zip -X POST http://localhost:8000/uploadModule
```
