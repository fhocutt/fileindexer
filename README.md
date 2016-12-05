##File Indexer
This project is written as a step towards implementing an indexer/term
frequency counter that finds the top ten words for a given collection of texts.
In its current development state, it contains the logic for word splitting
(note: while this implementation will process texts containing Unicode code
points, the results may be poor) and term frequency counting, yielding the top
ten most common words and the number of times they occur in the text.

###Installation
It is suggested that you install this module into a virtual environment to make
per-project dependency management easier. Resources on creating virtual
environments: [`virtualenv` docs](https://virtualenv.pypa.io/en/stable/),
[a useful guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once your virtual environment is installed and activated, run:
```
> git clone https://github.com/fhocutt/fileindexer
> pip install fileindexer
```

You should then be able to run `import fileindexer.counter` with no errors.

###Tests
Unit tests, along with an example text, are located in the `tests/` folder.
To run the unit tests:
```
> cd /path/to/fileindexer/tests/
> pytest
```

You also may run the `counter.py` script from the top `fileindexer` folder
and print the top ten words of _Anne of Green Gables_ with the following
commands:
```
> cd /path/to/fileindexer/
> python3 fileindexer/counter.py
```

### Next steps
* Write a command-line application to take multiple texts as input and return
  the top ten words from all of them combined.
* Extend to execute concurrently.
* Extend to be distributed.

This project is coded as an exercise for Rackspace Managed Security.
