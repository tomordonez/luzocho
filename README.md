# Reading List with Google Books

A small CLI app that lets you query Google Books API.

* A query displays a list of 5 books (author, title, publishing company)
* You can select a book from the list to save to a "Reading List"
* You can view the "Reading List" with all books saved

# Install/Run

**From Terminal**

1. Git clone the repo.
2. Open repo directory `cd luzocho`
3. Install the conda env `conda env create --file=environment.yml`
4. Activate the env `conda activate luzocho`
5. From the terminal `python -m readinglist`

**From PyCharm**

1. Open cloned repo
2. Main menu/File/Open
3. Browse the directory that has the repo source file and the environment.yml
4. More details in PyCharm [here](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#conda-requirements)
5. Then run `__main__.py`.

# TDD

See `use_cases.md` for details.

Tested:

* User input when selecting an option from the menu
* Get a response from Google Books API using a mock

# How Google Books API search works

As seen in [Google Books API](https://developers.google.com/books/docs/v1/using), searching 
doesn't require authentication. You can get an url like this, and it returns 10 results:

    https://www.googleapis.com/books/v1/volumes?q=test+driven+development

Request the URL using the following syntax:

    url = urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=test+driven+development")

You can see the response status with:

    url.status

Then parse it with json:

    import json
    json_data = json.loads(data.decode('utf-8'))

The results are contained in `json_data['items']`. Then each book data is located in `[index]
['volumeInfo']`

# References

* Remove punctuation in a string [here](https://stackoverflow.com/a/266162)