# Data

In this directory you can store your data. These data can be in various
stages of analysis. There can be raw data from an instrument or data
from an external source, from which you derive intermediate data and
end results.

It is usually a good idea to separate the original data (raw or external)
from the processed data. You usually do not want to alter the raw or external
files in any way, so saving them in separate directories avoids accidentally
changing these files.

## Subdirectories

The data directory contains the following subdirectories:

- external: To store external data,
- raw: To store raw data from the instrument,
- intermediate: To store intermediate data products while processing,
- processed: To store the end results of the processing.

## Link to large file storage

If your datasets are large, it is best to store them on a disk with high
capacity. You can still include them in this directory structure by creating
a symbolic link. It is best to replace the current directory. For example,
the `external` directory needs to be removed before we can make a link to
an existing directory elsewhere. Be careful with the `rm` command!
```
# First check whether the external directory is empty:

user@linux:~/nwo-cookiecutter/data> ls external/

# If the directory does not contain anything that you want to keep, then remove it:

user@linux:~/nwo-cookiecutter/data> rm -rf external/
```

If we have the external data stored in `/path/to/storage/external`, then
we can create the new link with the command:
```
user@linux:~/nwo-cookiecutter/data> ln -s /path/to/storage/external external
```
The data will still be available at `data/external`, but the files will be
physically stored in `/path/to/storage/external`.


