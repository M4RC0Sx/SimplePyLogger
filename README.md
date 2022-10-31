# SimplePyLogger

![Sonarqube Workflow](https://github.com/M4RC0Sx/SimplePyLogger/actions/workflows/sonarqube.yml/badge.svg)
![Release Workflow](https://github.com/M4RC0Sx/SimplePyLogger/actions/workflows/release.yml/badge.svg)

[![Quality Gate Status](https://sonarqube.fronteraware.com/api/project_badges/measure?project=simplepylogger&metric=alert_status&token=36002ab2fbeb64200ad17e2e68388cc15d5679da)](https://sonarqube.fronteraware.com/dashboard?id=simplepylogger)
[![Reliability Rating](https://sonarqube.fronteraware.com/api/project_badges/measure?project=simplepylogger&metric=reliability_rating&token=36002ab2fbeb64200ad17e2e68388cc15d5679da)](https://sonarqube.fronteraware.com/dashboard?id=simplepylogger)
[![Security Rating](https://sonarqube.fronteraware.com/api/project_badges/measure?project=simplepylogger&metric=security_rating&token=36002ab2fbeb64200ad17e2e68388cc15d5679da)](https://sonarqube.fronteraware.com/dashboard?id=simplepylogger)
[![Bugs](https://sonarqube.fronteraware.com/api/project_badges/measure?project=simplepylogger&metric=bugs&token=36002ab2fbeb64200ad17e2e68388cc15d5679da)](https://sonarqube.fronteraware.com/dashboard?id=simplepylogger)
[![Vulnerabilities](https://sonarqube.fronteraware.com/api/project_badges/measure?project=simplepylogger&metric=vulnerabilities&token=36002ab2fbeb64200ad17e2e68388cc15d5679da)](https://sonarqube.fronteraware.com/dashboard?id=simplepylogger)

Simple Python Logger package to easily manage custom loggers in Python projects.

## Installation

Because the package is hosted on PyPi, the installation process is quite simple:

_Notice that the package name has a 3 in place of an E, this is due to the availability of names in PyPi._

```bash
pip install simplepylogg3r
```

## Upgrade to latest version

```bash
pip install simplepylogg3r -U
```

## Usage

Currently, the package supports 3 different loggers:

- Console Logger
- File Logger

**IMPORTANT NOTE:** Every logger must be configured before using it, this is done by calling the `configure` method of the logger. Once you have configured a logger, the configuration gets saved and everytime you use the logger again, it uses this initial configuration.

All logger configuration methods are static, so you can call them directly from the class. They also have all necessary parameters with default values, allowing you to use them without any configuration or customizing whatever you want.

### Console Logger

```python
from splogger.loggers import ConsoleLogger

ConsoleLogger.configure('logger_name')  # Logger configuration

ConsoleLogger.debug('Debug Message')
ConsoleLogger.info('Info Message')
ConsoleLogger.warning('Warning Message')
ConsoleLogger.error('Error Message')
ConsoleLogger.critical('Critical Message')
```

### File Logger

```python
from splogger.loggers import FileLogger

FileLogger.configure('logger_name', filename='example.log')  # Logger configuration

FileLogger.debug('Debug Message')
FileLogger.info('Info Message')
FileLogger.warning('Warning Message')
FileLogger.error('Error Message')
FileLogger.critical('Critical Message')
```

## To-Do List

- [x] Add README docs.
- [ ] Generate wiki docs.
- [x] Add Rotating File Logger (time).
- [ ] Add Rotating File Logger (size).
- [ ] Implement unit tests.
- [ ] Run unit tests on CI.

## License

Apache License 2.0
