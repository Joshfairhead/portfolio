+++
authors = ["Josh Fairhead"]
title = "Resource Library"
description = "A library for storing general systematics or qualitive systems. These are structured ontologies useful for semantic search and compilation. Work in progress or research in motion ;)"
date = 2024-01-01
[taxonomies]
tags = ["Design", "Systems", "Architecture", "AI"]
[extra]
featured = true
weight = 1
draft = false
+++

## General Systematics Resource Library

The systematics API started as a way to preserve the work of Tony Hodgson and JG Bennett. Probably best to look at this one in horizons, so horizon one is about archival, preservation and storage. In essence I was building the systematic structures for storage and retrieval of graphs with semantic structure. 

The first move was to create a basic library of the canonical references based on the terminology provided by Tony Hodgeson and JG Bennett as sources. Each system might be considered an autonomous unit. Ideally I would have liked the implementation of these systems to be correct by construction, using category theory and homotopic type theory - as this would make them much more useful on the Post Web / Dweb - however after creating v0.0.2 I tried just this and found it much harder than anticipated so have decided to scope things back. 

For Horizon 1, retrieval of canonical systems and retrieval of custom instances are probably the only critical functions needed. Thats what the API currently enables. Humble beginnings.

Here is the code:
https://github.com/Joshfairhead/SystematicsAPI-v0.0.2

#### Learnings

In the process of creating this API I basically articulated the various systems and tried implementing them in various ways. The simplist was throught the type system; enumerating the various systems and their values and then bundling this all up in a hash table. I then added an interface, which created the issue of state management so I rebuilt. The issue was this wasn't very composable.

Indexs, coordinates, terms, were needed to be wrapped up with a builder pattern. Doing this in state the 'naieve way' meant that I needed to articulate every permutation of index, coord, term and all the combinations of combinations (for links) to get the composability I wanted. This however was not extensible because adding another object would requrie updating the state machine with exponential permutations. 

This is basically where v0.0.2 lies; rigidly defined structures. I basically got it to a place where it worked and then decided to refactor. Following the white rabbit led me to category theory and some pretty advanced maths I'd never encountered.

The current v0.0.3 attempts implementation by articulating base 'elements' such as index, coord, term as entries and then use link moprhisms to compose the systems. This is in the right direction, but is still not producting the right results. Basically we have different link types that are transitive and/or commute using the category theory criterea of Identity, Association and Composition. Connect an index, coordinate and/or term with an 'identity' link to create a higher entity - this creates a groupoid through transitivy (if I connect index and coord where term is connected to coord, then term and index automatically connect). Then connect any of these elements to another element with an 'association' link and the groupoids are asymetrically transitive, meaning that connecting coord in groupoid A to any type in groupoid B connects to index, coord, terms across groupoids A and B. 

This actually works as a proof of concept but it's a blunt approach that requires more research. Namely that there are higher order structures than just terms and connectives that I want to figure out. As far as base connectivity goes this is fine within a system, but what about composing across systems such as dyads > triads? or comparing systems of the same type but with different semantics?

A field of action is emerging here; objects and categories, morphisms and functors. But yeah this needs to be implemented as code before it can be applied to the systems. In other words we need a generic 'isomorphism' for comparing systems to systems or nodes within a given system with their counterparts. Or we need generic functor operations for translating between categories both at the implementation level with base catefories (index > coordinate) and at the level of transformations (system to system).

How I represent this in state is currently an exploration. I believe frameworks like Holochain probably lay the foundations for this as the hashtable is essentially a DSU (Disjoint set / union), and frameworks like AD4M are equivelent to very abstract intersections, but I may be wrong about this. As such I'm sticking to my own little playground to figure out the implementation details for now. 

#### Orientation
![Engineering](content/portfolio/systematicsAPI/HeptadEngineeringSketch.png)






