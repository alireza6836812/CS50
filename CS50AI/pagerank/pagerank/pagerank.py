import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    mylinks = corpus[page]
    l = len(mylinks)
    output: ProbabilityMap = {}
    if l == 0:
        p = 1 / len(corpus)
        for i in corpus:
            output[i] = p
        return output
    p = (1 - damping_factor) / len(corpus)
    for i in corpus:
        output[i] = p
    p = damping_factor / l
    for i in mylinks:
        output[i] += p
    return output


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    value_of_visits: dict[str, int] = {}
    for possible_page in corpus:
        value_of_visits[possible_page] = 0
    p = random.choice(list(corpus.keys()))
    value_of_visits[p] += 1
    for i in range(n - 1):
        model = transition_model(corpus, p, damping_factor)
        p = random.choices(population=list(model.keys()), weights=list(model.values()), k=1)[0]
        value_of_visits[p] += 1
    ranks: PageRankMap = {}
    for i in corpus:
        ranks[i] = value_of_visits[i] / n
    print("iteration sample: ", sum(ranks.values()))
    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    count_of_pages = len(corpus)
    pages = corpus.keys()
    target: Corpus = {}
    ranks: PageRankMap = {}
    p1 = 1 / count_of_pages
    for i in corpus:
        ranks[i] = p1
        target[i] = set()
        l = len(corpus[i])
        if l == 0:
            corpus[i] = set(pages)
    for i in corpus:
        for j in corpus[i]:
            target[j].add(i)
    max = 0.001
    p2 = (1 - damping_factor) / count_of_pages
    while True:
        s = True
        for j in corpus:
            oldrank = ranks[j]
            newrank = 0
            sources = target[j]
            for k in sources:
                l = len(corpus[k])
                newrank += ranks[k] / l
            newrank *= damping_factor
            newrank += p2
            ranks[j] = newrank
            delta = abs(newrank - oldrank)
            s = s and delta < max
        if s:
            break
    return ranks


if __name__ == "__main__":
    main()
