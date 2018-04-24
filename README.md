Parameter + Configurator = Paramerator
====


Paramerator is a library that aims to make managing config and parameter files easy for Python and especially for Data Scientists using Jupyter Notebooks.

- Format parameter/value pairs into human readable txt files
- Load from those files with type aware variable assignment
- Loaded files appear as attributes when loaded and assigned
- Create DEFAULT parameter files using a dictionary
- Allow for user input on attributes marked required
- Allow users to fill in their own sensitive information when sharing repos
	- I don't want to push my "mongo.cfg" or "api.keys" files to my repo, but when a module is called in my library that uses it, if the file is missing, it will generate a default and prompt for required fields.

#### Example:
```
mongo = param.loader('dat/mongo.cfg')
mongo
YEILDS
server.ip(str('123.45.67.890'))
server.host(int(123456))
server.db(str('my_database'))
server.coll((str('collection'))
```
So you can now pass mongo.server like so:
```
pymongo.connect(mongo.server.ip, mongo.server.host, mongo.server.db, mongo.server.coll)
```
If you make changes to "mongo.cfg" you can them as a new file or overwrite using param.writer('dat/mongo.cfg', mongo)

#### Results in files.
```
dat/mongo.cfg
##Server
ip				 = 123.45.67.890
host 			 = 123456
db   			 = my_database
coll 			 = collection
```


To do:
- Make this readme better
- Add encrpytion using named tuples

MORE SOON...
