# mySQLace

Python interface for MySQL connections.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Python

The latest versions of Mac OS, CentOS, Fedora, Redhat Enterprise (RHEL) and Ubuntu come with Python 2.7 out of the box.

    $ command -v python

If Python is not installed you can [follow the next instructions](https://wiki.python.org/moin/BeginnersGuide/Download).

#### Setuptools & Pip
The two most crucial third-party Python packages are setuptools and pip.

Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default.

To see if pip is installed, open a command prompt and run

    $ command -v pip

To install pip, follow the [official pip installation guide](https://pip.pypa.io/en/latest/installing/) (this will automatically install the latest version of setuptools).

### Installing

Just use ´pip´ to install

    pip install mySQLace

Or to upgrade

    pip install --upgrade mySQLace

## Deployment

If your server allows it you can install `mySQLace` the same way it was explained above.

If not you can just download this project into your server alongside your project and import the package like

    from mySQLace import mySQLace

Running a simple file just containing the import statement must output no errors.

## Built With

* [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) - Backend connector for MySQL calls.
* [Pandoc](http://pandoc.org/) - To get your nicely formatted README on the module's PyPi page.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jordanncg/mySQLace/tags).

## Authors

* **Jordan Cortes** - *Initial work* - [jordanncg](https://github.com/jordanncg)

See also the list of [contributors](AUTHORS.txt) who participated in this project.

## License

Third-party software components have their own licenses inside each pacakge.

Except where otherwise noted, this project is licensed under the GPL License - see the [LICENSE](https://github.com/jordanncg/mySQLace/LICENSE.txt) file for details.
