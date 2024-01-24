# event-generator

Generates Events with formatted fake data for streams. The intention is for development and testing purposes without relying on real data.

Refer [faker-events](https://github.com/johnbrandborg/faker-events) page for detailed info.

## run locally

Script will produce infinite event stream with 1 EPS rate 
```
faker-events -n 5 -s src/generator.py
```