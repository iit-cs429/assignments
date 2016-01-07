## Assignment 1: Ranking (50 points)

In this assignment, you'll implement a search engine over Wikipedia documents. The file `documents.txt.gz` contains 5,435 snippets from the Wikipedia pages in the "Wiki Small" collection [here](http://www.search-engines-book.com/collections/). Each line is a separate snippet. Here is an example:
```
"Take My Breath Away" is the name of a love song from the film Top Gun, written by Giorgio Moroder and Tom Whitlock, performed by the band Berlin. It won the Academy Award for Best Original Song as well as the Golden Globe Award for Best Original Song in 1987.
```

1. Complete the methods in [searcher.py](searcher.py). You will:
  1. Create an index containing tf-idf values.
  2. Rank documents based on cosine similarity between query and document tf-idf vectors.
  3. Create a champion list, optionally searching that instead of the traditional index.

In addition to the doctests, the expected output of `python searcher.py` is in [Log.txt](Log.txt).

To view the web interface, you'll need to install
[Flask](http://flask.pocoo.org/) (`pip install Flask`). Then you can run
`python run.py` to launch the Flask server, which will respond to requests on
localhost (typically `http://127.0.0.1:5000/`).
