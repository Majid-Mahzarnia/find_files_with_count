# find files with count
Traverses the directory recursively &amp; Collects files by their modification date in a directory where the key is the date and the value is a list of files modified on that date <br />
- Finds the most recently modified file and its modification time <br />
- Finds all files with the same modification time as the last modified file <br />
- Writes the name and modification time of the last modified file <br />
- Writes the list of files that have the same modification time <br />
- Writes the latest modification date and lists all files modified on that date to result.log <br />
- The modification dates are sorted to determine the most recent date <br />
