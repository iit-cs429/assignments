## Assignment 2: Ranking II

In this assignment, you will implement three different ranking functions and four different evaluation functions.  

You will apply these to the [TIME dataset](http://ir.dcs.gla.ac.uk/resources/test_collections/time/). This contains binary relevance judgements for 83 queries on a collection of 423 documents.

1. Compare the following ranking functions:
  1. **Cosine similarity:** Convert each query and document to tf-idf and sort the documents according to the cosine similarity between query and document.
  2. **RSV:** See the definition on the last slide of [lecture 12](https://github.com/iit-cs429/main/tree/master/lectures/lec12).
  3. **BM25:** See the definition on the last slide of [lecture 12](https://github.com/iit-cs429/main/tree/master/lectures/lec12).
    1. Consider 2 values for k (1, 2) and 2 values for b (.5, 1) (so, 4 different settings in total).

2. For each system, compute the following evaluation metrics:
  - Precision
  - Recall
  - F1
  - Mean Average Precision (MAP)

There are many functions for you to complete across four different files. Each function has doctests that you should use to check your implementation (e.g., `python -m doctest index.py`):
  - **evaluate.py:** This contains the code to evaluate a ranked list using the relevance judgements. You'll implement Precision, Recall, F1, and MAP
  - **score.py:** This contains code to rank documents by relevance, using Cosine, BM25, and RSV.
  - **index.py:** This represents the term-document index. While much of this code is similar to the previous assignment, there are a few distinctions. Primarily, the postings list will consist of (document id, term frequency) tuples; in the previous assignment, these were (document id, tf-idf values). This change is to support the three different scoring functions.
  - **main.py:** You'll have to write code to parse the raw data, as well as some code to put all the pieces together.

Running `python main.py` should produce `Results.md` that matches the given values. `Log.txt` contains what should be written to STDOUT by `main.py`.

Other clarifications:

- Results.md reports the average evaluation measures over all queries.
- You should ignore query terms that do not appear in any document.
- Compute precision/recall/F1 using only the top 10 results
- When computing MAP, if a relevant document is not in the top 10, assume 0% precision for those relevant documents.
- Note that IDs are assigned to queries and documents according to their position in the file, starting at ID 1. Thus, in TIME.REL, the line "1 268" indicates that the first query in TIME.QUE is relevant to the 268th document in TIME.ALL.









