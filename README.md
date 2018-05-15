
# testDirectoryCreation

A simple utility for creating a temporary directory full of specific files

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