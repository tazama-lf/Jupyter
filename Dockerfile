# SPDX-License-Identifier: Apache-2.0

FROM jupyter/minimal-notebook

ARG ODBC_VER=18

USER root

RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
RUN curl https://packages.microsoft.com/config/debian/11/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql${ODBC_VER}
RUN apt-get install -y unixodbc-dev

USER ${NB_UID}

RUN pip install python-arango pandas numpy matplotlib pyodbc

COPY ./analytics.ipynb ./analytics.ipynb

ENV SQL_HOST=
ENV SQL_DB=
ENV SQL_USER=
ENV SQL_PASS=
ENV SQL_DRIVER=
ENV ARANGO_HOST=
ENV ARANGO_DATABASE=
ENV ARANGO_USER=
ENV ARANGO_PASSWORD=
ENV PREVIOUS_BEST_COUNT=
