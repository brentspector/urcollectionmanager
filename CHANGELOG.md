## 'v1.1.3 (2020-07-19')

### Fix

- **find-missions-function**: allow missions to be created when given a list of only 1 element

## 'v1.1.2 (2020-07-19')

### Refactor

- **pull-master**: update local branch

### Fix

- **mission-category**: add black market category to list of supported categories

## 'v1.1.1 (2020-06-13')

### Fix

- **mission**: fix the issue where a completed mission caused tuple unpacking to fail

## 'v1.1.0 (2020-06-07')

### Feat

- **tests**: add unit tests for missions module
- **missions**: add support for mission management

### Fix

- **lint**: fix flake8 lint failure

## 'v1.0.1 (2020-03-18')

### Fix

- **purchase**: fix purchase date incompatibility bug

## 'v1.0 (2020-03-16')

### Refactor

- **pr**: remove test databases

### Feat

- **db**: add support for reading and writing purchase history with sqlite databases
- **api**: allow screenscraping with authenticated session

### Fix

- **db**: add support for databases, particularly sqlite
