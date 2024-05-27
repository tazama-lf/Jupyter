<!-- SPDX-License-Identifier: Apache-2.0 -->

<div align="center">
    <h1>Jupyter Notebook</h1>
    <img alt="GitHub" src="https://img.shields.io/github/license/frmscoe/Jupyter">
</div>

This repository contains a jupyter notebook with a **Python** runtime environment. The notebook leverages tools like `matplotlib` and `pandas` to create visualisations of a set of transactions


<h3 align="center">Environment</h3>

|     VARIABLE             |Description                                          |
|--------------------------|-----------------------------------------------------|
|`ARANGO_HOST`	           |Where your database is hosted                        |
|`ARANGO_DATABASE`         |The name of the database where the collection resides|
|`ARANGO_USER`             |Database auth `user`                                 |
|`ARANGO_PASSWORD`         |Password for the `ARANGO_USER` variable              |
|`PREVIOUS_BEST_COUNT`	   |Count of previous best transactions to compare with  |
|`SQL_HOST`                |SQL host endpoint                                    |
|`SQL_DB`                  |Name of SQL database                                 |
|`SQL_USER`                |SQL auth user                                        |
|`SQL_PASS`                |Password for `SQL_USER`                              |
|`SQL_DRIVER`              |Name of the SQL driver currently in use              |

> [!IMPORTANT] 
> You may need to update the notebook to be compatible with your SQL driver. The notebook is using [`pyodbc`](https://github.com/mkleehammer/pyodbc)

A [`Dockerfile`](Dockerfile) has been provided that spins up a minimal Jupyter stack:

```sh
docker build .
```
