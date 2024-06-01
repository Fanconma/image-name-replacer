# image-name-replacer
A tool to replace filenames of images from A to B

# Usage
You should change the **Example usage** in the python file.
- *directory* : The directory of images you want to be changed
- *a_json_path* : The original filenames of those images
- *b_json_path* : The filenames that you want these images to be changed to
  
# Note
- The files `a.json` and `b.json` must follow the **JSON syntax**
- You must make sure that the a.json and b.json files **correspond to each other**, that is, the number of lines in the two files should be equal, and each line of `a.json` corresponds to each line of `b.json` in turn.
