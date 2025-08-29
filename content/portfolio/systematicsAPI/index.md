+++
authors = ["Josh Fairhead"]
title = "Resource Library"
description = "A library for storing general systematics or qualitive systems. These are structured ontologies useful for semantic search and compilation amongst other things. Work in progress or research in motion ;)"
date = 2024-01-01
[taxonomies]
tags = ["Design", "Systems", "Architecture", "AI"]
[extra]
featured = true
weight = 1
draft = false
+++

![Engineering](HeptadEngineeringTemplate.png#no-hover)

[Here is the v0.0.2 codebase](https://github.com/Joshfairhead/SystematicsAPI-v0.0.2)

#### Background
The systematics API started as a way to store, preserve, search and retrieve the work of Tony Hodgson and JG Bennett - as well as other traditions that make use of such semantic structures. In short these systems are ways of organising information into knowledge ecologies.

Its probably best to look at this initiative in horizons; so this basic funcitionality can be considered horizon one. The potential use cases of these structures in horizon two or three would seem to go much further than storage and preservation, but for now I'd like to keep things scoped to generic functionality rather than more visionay aspects of the work. 

#### Initial thinking and Learnings

In the process of creating this API I basically articulated the various systems and tried implementing them in various ways. The simplist was through the Rust type system; enumerating the various systems and their values and then bundling this all up in a hash table. I then added an interface, which created the issue of state management so I rebuilt the state model but not the interface. The issue with this implementation is that it's not very composable.

Indexs, coordinates, terms, were needed to create the graphs, which were then constructed with a builder pattern. Doing this in state the 'naieve way' meant that I needed to articulate every permutation of index, coord, term and all the combinations of combinations (for links) to get the composability I wanted. While possible, this was not extensible because adding another object would requrie updating the state machine with exponential permutations. 

This is basically where v0.0.2 lies; rigidly defined structures. I basically got it to a place where it worked and then decided to refactor. Following the white rabbit led me to category theory and some pretty advanced maths I'd never encountered.

The current v0.0.3 attempts implementation by articulating base 'elements' such as index, coord, term as entries and then use link moprhisms to compose the systems. This is in the right direction, but is still not producting the desired results. Basically we have different link types that are transitive and/or commute using the category theory criterea of Identity, Association and Composition. Connect an index, coordinate and/or term with an 'identity' link to create a higher order entity - this creates a groupoid through transitivy (meaning that if I connect index and coord, where term is connected to coord, then term and index automatically connect). Then connect any of these base elements in groupoid A, to another with an 'association' link in groupoid B and all the elements should link automaticall through asymetric transitivity - meaning that connecting index in groupoid A to any element in groupoid B such as a coordinate or term maps all index, coord, terms across groupoids A and B. 

This actually works as a proof of concept but it's a blunt approach that requires deeper research. Namely that there are higher order structures than just terms and connectives like designations and coherence attributes. As far as base connectivity goes this is fine within a system, but what about composing across systems such as dyads > triads? or comparing systems of the same type but with different semantics?

A field of action starts emerging here; objects and categories, morphisms and functors. However when it comes to code, it seems to imply that category theory needs to be implemented before I can construct systems correctly and even then things are quite messy. 

For instance; if we compare a triad by Bennet and a triad by Landry we are comparing isomoprhic structures, with isomorphic nodes (though nodes within the structures are probably internally polymorphic). Now, the question about this is if such a morphism is also a functor? From the perspective of triad to triad, the mapping is isomorphic because its within the category of 'triad'. However we are also mapping across the categorical instances of 'Bennett' and 'Landry', which would make it a functor. 

Not being a mathmatician or computer scientist I'm out of my depth to say how such people think about these problems, but it seems they have encountered a thing called 'Russels Paradox' which is a set of all sets issue. The uncertainty of which they seem to resolve by creating a hierarchy of universes. This set off a lightbulb because for some reason the Benned duodecad is presented as a hierarchy of 12 levels, so I gave that a go to little success. The issue here becomes both the rigid hierarchy and the infinite horizonal categories... the rock and the whirlpool. 

The rock represents the need for categorical hierarchy (the category of categories), yet the whirlpool resists because we have infinite possible horizontal categories where there is no hierarchy - such as index and coordinates (the categories of topolagy vs geometry). In computer science this dyad is stack and heap.

So the question is how the hell to do this on a computing infrastructure built on binary logic?? Well from an earlier (unmentioned) excrusion of equating mathmatical operations to systems I discovered operation types such as 'union', 'intersect', 'product', 'superset' and so fourth - which all have a qualitive flavour. Having tried and failed to implement these, while getting utterly lost in recursion, I discovered another term in category theory called DSU or "Disjoint Set, Union". Is this the monad of monads or even a nullad I wonder? Maybe. Then it dawns on me that Holochain as a distributed hash table with content addressable storage is essentially a DSU, which has generic types of 'entries' and 'links' as its fundemental dyad.

So I'm basically still in research mode, but assuming that I can use entries to represent types of objects and categroies and links to represent morphisms and functors (it actully looks like the system may be built on category theory), I still need to work out the relativity of the various 'elements'. In other words theres specific units needed in order to describe a system (index, coordinate, term = node) and there are critical functions that are not directly needed as part of the system, but give it critical funcitonality - such as the morphism or functor types. 

So, looking back to the heptad of engineering template, I wonder if this the research portion nearing completion? Is the next step imagination and/or prototype? How does this relate to the octad? Have I mapped out the units as systems? critical functions as objects, categories, morphisms and functiors? The platform as Holochain? And am now working on resources? It seems so though it was pretty unintentional - even resisted.

![Octad](8GenericOctad.png#no-hover)