This is an unofficial manual for the [`couchdb`](https://pythonhosted.org/CouchDB/) Python module I wish I had had.

## Installation

```nohighlight
pip install couchdb
```

## Importing the module

```python
import couchdb
```

## Connection

If you only need read access, use an anonymous connection:

```python
couchserver = couchdb.Server("http://couchdb:5984/")
```

To write to the database, create an authenticated connection:

```python
user = "admin"
password = "my secret password"
couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))
```

## Listing databases

Simply iterate over the server object like this:

```python
for dbname in couchserver:
    print(dbname)
```

## Selecting/creating a database to work with

```python
dbname = "mydb"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)
```

## Deleting a database

```python
del couchserver[dbname]
```

## Writing a document to a database

Storing a document with an auto-generated ID:

```python
doc_id, doc_rev = db.save({'key': 'value'})
```

`doc_id` is the generated document ID, `doc_rev` is the revision identifier.

Setting a specific ID:

```python
db["my_document_id"] = {'key': 'value'}
```

Writing multiple documents in one call is done via the `update()` method of the database object. This can either create new documents (when no `_id` field is present per document) or update existing ones.

```python
docs = [{'key': 'value1'}, {'key': 'value2'}]
for (success, doc_id, revision_or_exception) in db.update(docs):
    print(success, docid, revision_or_exception)
```

## Retrieving documents by ID

```python
doc_id = "my_document_id"
doc = db[doc_id]  # or db.get(doc_id)
```

## Querying documents from views

If your database has a design document and view under the path `/db_name/_design/design_doc/_view/view_name`, you can iterate this view using this syntax:

```python
for item in db.view('design_doc/view_name'):
    print(item.key, item.id, item.value)
```

Limiting the output to a certain number of items:

```python
for item in db.view('design_doc/view_name', limit=100):
    print(item.key, item.id, item.value)
```

Skipping the first n items:

```python
for item in db.view('design_doc/view_name', skip=100):
    print(item.key, item.id, item.value)
```

Reverse sorting:

```python
for item in db.view('design_doc/view_name', descending=True):
    print(item.key, item.id, item.value)
```

Including source documents in result entries:

```python
for item in db.view('design_doc/view_name', include_docs=True):
    print(item.key, item.id, item.value)
```

Allow outdated data to be returned, prevent updating the view before returning results:

```python
for item in db.view('design_doc/view_name', stale="ok"):
    print(item.key, item.id, item.value)
```

Update the view after returning the results:

```python
for item in db.view('design_doc/view_name', stale="update_after"):
    print(item.key, item.id, item.value)
```

### Grouping results

Grouping the results by key, using the Reduce function, must be activated explicitly:

```python
for item in db.view('design_doc/view_name', group=True):
    print(item.key, item.value)
```

If the Map function emits a structured key (an array with multiple elements), the grouping level can be determined:

```python
for item in db.view('design_doc/view_name', group=True, group_level=1):
    print(item.key, item.value)
```

### Filtering

Return only entries from the view matching a certain key:

```python
for item in db.view('design_doc/view_name', key="my_key"):
    print(item.key, item.id, item.value)
```

Return entries with keys in a certain range:

```python
for item in db.view('design_doc/view_name', startkey="startkey", endkey="endkey"):
    print(item.key, item.id, item.value)
```

The `key`, `startkey` and `endkey` parameters also accept arrays, e. g.

```python
for item in db.view('design_doc/view_name', startkey=["foo", "a"], endkey=["foo", "z"]):
    print(item.key, item.id, item.value)
```
