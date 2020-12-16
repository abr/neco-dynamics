# Installation Notes

Running these demo notebooks requires that you have installed the `ssp` package included
in this repository. Please follow the instructions included
in the subfolder for that package, and then do the following in same the Python
environment from this subdirectory:

```
pip install -e .
``` 

Notebooks require imagemagick to display animations of MSP dynamics. 
On Ubuntu, you may have this installed already, but if not, do the following:

```
sudo apt install imagemagick
```

On Mac, you can install with homebrew:

```
brew install imagemagick
```
