# Reading List with Google Books

A small CLI app that lets you query Google Books API.

* A query displays a list of 5 books (author, title, publishing company)
* You can select a book from the list to save to a "Reading List"
* You can view the "Reading List" with all books saved

# Run the program

From the terminal using `python -m readinglist` or from an IDE, run `__main__.py`.

# TDD

See `use_cases.md` for details.

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