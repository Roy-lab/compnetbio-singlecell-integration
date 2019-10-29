# Integrating single cell gene expression datasets
Slides, notebook, and datasets for integrating single cell gene expression datasets

#### Before class
- `git clone` this repository onto your home directory on the biostat server, or,
- Simply download the whole repository, `scp` the compressed file to your home directory on the biostat server, and unzip.

#### At the beginning of class
1. Login to the biostat server.
2. On the server, `cd` to the directory with the notebook and the dataset directories.
3. On the server, start up Jupyter notebook using the specific environment where all dependencies were pre-installed for you:
```
port=<your favorite 4 digit number>
<TBD directory>/jupyter notebook --no-browser --port=$port
```
4. BACK ON YOUR COMPUTER, open command line/terminal, and claim the port:
```
port=<the port tunneled in step 3>
ssh -N -f -L \
 localhost:${port}:localhost:${port} \
 <your biostat login>@<biostat server you created the port in>
```
5. On your computer, copy and paste in the localhost:port URL into a browser.


