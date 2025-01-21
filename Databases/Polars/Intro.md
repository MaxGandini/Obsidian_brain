Philosophy

The goal of Polars is to provide a lightning fast DataFrame library that:

- Utilizes all available cores on your machine.
- Optimizes queries to reduce unneeded work/memory allocations.
- Handles datasets much larger than your available RAM.
- A consistent and predictable API.
- Adheres to a strict schema (data-types should be known before running the query).

Polars is written in Rust which gives it C/C++ performance and allows it to fully control performance-critical parts in a query engine.

personal Note:

The query structure is key for understanding polars's advantage over pandas. It allows for integration with [[SQL]] like commands and optimizes, the memory usage. 