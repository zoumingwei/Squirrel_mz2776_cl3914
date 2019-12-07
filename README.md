# Squirrel Tracker

Squirrel Tracker is a Django based project that helps you keep track of all the known squirrels.

Import, export, add, or update squirrel records as you see them!

## Main features

**Management Commands**

* Import the data from the 2018 census file (in CSV format)

```bash
$ python manage.py import_squirrel_data /path/to/file.csv
```

* Export the data from the 2018 census file (in CSV format)

```bash
$ python manage.py export_squirrel_data /path/to/file.csv
```
**Views**

* Plot squirrel sightings
* List all squirrel sightings with links to edit and add sightings, located at `/sightings`
    * Update a particular sighting, located at  `/sightings/<unique-squirrel-id>`
    * Create a new sighting, located at `/sightings/add`
    * Provide general stats about sightings, located at `/sightings/stats`


## Usage

[Squirrel Tracker Map](https://tools-mz2776.appspot.com/map)
[Squirrel Tracker Sightings](https://tools-mz2776.appspot.com/sightings)
[Squirrel Tracker Sightings stats](https://tools-mz2776.appspot.com/sightings/stats)

## Contributing
Our group name: **Project Group 19**

Section: **SEC1**

UNIs: [cl3914, mz2776]
