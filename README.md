pydap.handlers.csv
==================

This handler allows Pydap to serve data from a file with comma separated
values. Here's a simple example:

```bash
$ cat simple.csv
"index","temperature","site"
10,15.2,"Diamond_St"
11,13.1,"Blacktail_Loop"
12,13.3,"Platinum_St"
13,12.1,"Kodiak_Trail"
```

Note that strings must be explicitely quoted. Additional metadata may be added
by creating a JSON file with the same name (`simple.csv.json` in this case):

```json
{
    "sequence": {
        "temperature": {
            "units": "degC"
        }
    }
}
```
