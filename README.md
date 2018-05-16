
# testDirectoryCreation

The main benefit of this tool is being able to generate a directory tree from a blob of JSON. 

The use case is a developer trying to create a tool to validate a batch of files she will receive in the future and wants to generate a bunch of test files to test her code against.

This is a tool to make it very easy for a developer to write up a structured document describing a directory tree and very quickly see that directory tree materialize on a file system.

## Quick start

```bash
>>> git clone https://github.com/verbalhanglider/making_directory_tree
>>> cd making_directory_tree
>>> python3 -m venv venv 
>>> source venv/bin/activate
>>> python bin/test.py data/good_tree_contract
>>> find root
root/
root/mvol
root/mvol/0009
root/mvol/0009/0010
root/mvol/0009/0010/0011
root/mvol/0009/0010/0011/ALTO
root/mvol/0009/0010/0011/ALTO/mvol-0009-0010-011_0001.xml
root/mvol/0009/0010/0011/ALTO/mvol-0009-0010-011_0002.xml
root/mvol/0009/0010/0011/JPEG
root/mvol/0009/0010/0011/JPEG/mvol-0009-0010-011_0001.jpeg
root/mvol/0009/0010/0011/JPEG/mvol-0009-0010-011_0002.jpeg
root/mvol/0009/0010/0011/mvol-0009-0010-0011.dc.xml
root/mvol/0009/0010/0011/mvol-0009-0010-0011.mets.xml
root/mvol/0009/0010/0011/mvol-0009-0010-0011.struct.txt
root/mvol/0009/0010/0011/mvol-0009-0010-0011.txt
root/mvol/0009/0010/0011/TIFF
root/mvol/0009/0010/0011/TIFF/mvol-0009-0010-011_0001.tiff
root/mvol/0009/0010/0011/TIFF/mvol-0009-0010-011_0002.tiff
```

## Writing a Contract

The JSON contract describing a particular directory or set of files to be created is the heart and soul of this utility. Here are a couple examples!

```json
[{
  "type": "directory",
  "name": "test",
  "contents": [
   {
    "type": "file",
    "name": "test.jpeg",
    "mimetype": "image/jpeg"
   }
  ]
}]
```

```json
[{
  "type": "file",
  "name": "test.xml",
  "mimetype": "application/xml"
}]
```

Some rules to remember when you make your own contracts, however.

1. The document starts as a list of JSON records.
1. Each record has to have the following properties
    - type which can have a value of file or directory
    - name which is the full name of the item including path starting with root record and if it is a file the file extension
1. Any record with type file must have the property mime type with a value conforming to [Media Type Specifications and Registration Procedures](https://tools.ietf.org/html/rfc6838)
1. Any record with type directory must have a property contents that has a value that is a list of records
1. The only valid types are directory or file

## Author

- verbalhanglider (tyler@danstrom.com)