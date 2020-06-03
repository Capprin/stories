# Stories

This project generates well-defined stories from a collection of vignettes. The generated stories are not text, but instead collections of _actions_ performed on story actors. The purpose of this project is to improve procedural generation in vidogames, which to date produces shallow experiences despite promising expansive worlds.

## Overview

This program heavily depends on the idea of a _vignette_: a quantized element of a story. This approach assembles a set of vignettes into a story. Because the vignettes are (in theory) robust pieces of story on their own, the resultant assembly should be satisfactory.

### Vignettes

Vignettes describe the progression of the story. Each vignette takes a set of input _actors_: think of characters, items, or settings in the story. The vignette also defines a set of actions to perform on these actors to progress the story.

Vignettes are defined with `yaml` files. Each vignette has three properties: `title`, `inputs`, and `actions`.
- `title` generally describes the vignette (to developers)
- `inputs` contains a list of [Cypher](https://neo4j.com/developer/cypher-query-language/) queries, pulling requesite actors from the story graph.
  - Inputs are run to determine whether a vignette can be used in the current story.
  - Inputs also pull requesite actors from the graph when `actions` are applied.
  - Because inputs should not modify graph state, the keywords `CREATE`, `DELETE`, `SET`, and `REMOVE` are not permitted.
- `actions` also contains a list of Cypher queries, responsible for modifying the graph.
  - Actions are only run as the story is created, updating the actor graph with story state.
  - Actions are permitted to run any Cypher queries.

### Story

The "story" object, as the name implies, stores the story. It's responsible for updating a graph of actors and their relationships, storing the "state" of the story. As the story is built, vignettes are assessed for whether they can be applied to the story; only "fitting" vignettes can be pushed.

### Author

The "author" object compiles vignettes into the story. It is responsible for further constraining vignettes to make the story sensible.

## Dependencies
- [Neo4j](http://www.neo4j.com)
