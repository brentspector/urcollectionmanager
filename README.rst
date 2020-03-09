Urban Rivals Collection Management API (urcollectionmanager)
============================================================

Something something

How To Use Tools:
    Poetry_
        - To run the project (preferably configure venv first)

        >>> poetry install

        - To configure your venv

        >>> python -m venv /path/to/new/virtual/environment
        >>> poetry env info

            - If `env info` does not match your path, try manually running \
              `Scripts/activate` inside that environment

        - To add a dependency (add a -D if it's only for development)

        >>> poetry add <dependency>

    Commitizen_
        >>> git add
        >>> cz c

    - More options can be found under options under Commitizen_
    - See if structure is good.

    PreCommit_
        Update .pre-commit-config.yaml, then run

    >>> pre-commit install
    >>> pre-commit run --all-files

    - More hook plugins can be found at PreCommitHooks_

TODO:

- Screenscraper UR for player data (need to test)
- Use UR-API_ to collect player data. UR-API-Example_
- Default to file output (excel or some form of that)
- Enable link to database
- Testing (pytest, Coverage-py_)
- Documentation (Sphinx_)

Not Required at this Time:

- Black_
- iSort_

.. _UR-API: https://www.urban-rivals.com/api/developer/
.. _UR-API-Example: https://github.com/Buscatrufas/UrbanRivals/blob/master/index.php
.. _Coverage-py: https://coverage.readthedocs.io/en/latest/config.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _AutoPEP8: https://github.com/hhatto/autopep8#usage
.. _Black: https://github.com/psf/black#version-control-integration
.. _iSort: https://github.com/pre-commit/mirrors-isort
.. _Commitizen: https://woile.github.io/commitizen/
.. _PreCommit: https://pre-commit.com/
.. _PreCommitHooks: https://pre-commit.com/hooks.html
.. _Poetry: https://python-poetry.org/docs/cli/
.. _PypiToken: https://pypi.org/help/#apitoken