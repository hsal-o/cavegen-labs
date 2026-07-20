# CaveGenLabs (CGL)

> A Python-based testbed for experimenting with procedural cave generation algorithms.

CaveGenLabs (CGL) is a Python framework for procedural 2D cave generation. Its goal is to provide a consistent environment for implementing, visualizing, comparing, and exploring cave generation algorithms without the overhead of building a separate application for each algorithm. 

## Algorithms

CGL currently includes the following procedural cave generation algorithms:

| Algorithm | Description |
|-----------|-------------|
| Random Walk | Carves paths through a solid grid using one or more randomly moving walkers.
| Midpoint Displacement | Generates cave passages using recursive subdivision.
| Cellular Automata | Generate organic cave layouts by repeatdely updating cells based on their neighbors.
| Perlin Worms | Generates cave systems using Perlin noise.
| Binary Space Partitioning | Generates cave rooms by recursively dividing the given area into sections.
| Metaballs | Carves organic, blobby caves by summing the influence of randomly placed metaballs.
| Diffusion Limited Aggregation | Creates branching caves by simulating randomly moving particles that attach to a structure.

Additional algorithms will continue to be added as the project evolves. Contributions and suggestions are always welcome :)

## Getting Started

Follow the steps below to get CGL running locally.

### Prerequisites

- Python 3.14+
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/hsal-o/cavegen-labs.git
cd cavegen-labs
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run the application:

```bash
python -m cavegenlabs
```

## Roadmap

- [x] Establish a modular architecture for implementing cave generation algorithms
- [x] Create a common configuration and parameter system
- [x] Implement visualization for generated caves
- [x] Implement multiple procedural cave generation algorithms
- [ ] Automatically discover and register new algorithm definitions in AlgorithmRegistry
- [ ] Implement a menu bar and application shortcuts
- [ ] Add screenshot export functionality
- [ ] Support saving and loading generated caves
- [ ] Support algorithm parameter presets
- [ ] Implement step-by-stp algorithm iteration (Ex. Cellular Automata iteration Button)
- [ ] Add cave grading and evaluation metrics
- [ ] Provide tools for comparing algorithm output

### Future
- [ ] Continue expanding cave generation algorithms
- [ ] Improve documentation and examples
- [ ] Expand visualization and experimentation featues
- [ ] Add unit tests for core domain and application behavior

## Contributing

Contributions, ideas, and new procedural generation techniques are always welcome.

If you'd like to add a new algorithm, improve the architecture, or suggest features, feel free to open an issue or submit a pull request.
