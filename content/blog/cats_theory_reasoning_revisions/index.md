+++
date = 2025-01-19
authors = ["Josh Fairhead"]
title = "Cats Theory Primer: Reasoning and Revisions"
description = "Addressing critiques and diving deeper into the fundamentals of category theory through examples and definitions"
[taxonomies]
tags = ["Exposition", "Mathematics", "Category Theory"]
[extra]

+++

### Reflection on Feedback

Sharing my last post, the critique was blunt, "nothing here that you can't find in an introductory book on Category Theory" - which is probably true but having never read one, I couldn't tell you! 

Two books I've been recommended for beginners requiring almost no background:
1) Computational Category Theory 
2) Category Theory for Programmers

The constructive element of the critique asked some questions; namely whats and object and morphism? How are they defined? Provide an example of these. What is a category, provide an example, how do you split categories into different types? So here is an attempt at answering:

### What is an Object?

An object is a conceptual placeholder. You might consider it a point, which would indeed be an object but it's more general better thought of as an element in a space. In this example an element is an object in topological space.

### What is a Morphism?

A morphism is a conceptual mapping. You might consider it a line or arrow, which would indeed be a morphism again but it's probably better thought of as a mapping between objects. In this example a line would be a morphism in topological space.

### What is a Category?

A category is a conceptual space. At this point, we run into difficulty relying on the topology analogy. If we were to keep going with that general path of abstraction we would say its a plane because that's the next topological level, but I'm pretty sure the theorists would start shouting about that. 

Let's wrestle with this alligator. Based on the previous definition that a category requires identity, association and composition I'm going to go out on a limb and define it for now as a third order logic - I can hear the theorists shouting already! 

As far as I'm aware a category is a very abstract concept which means it generalises. A map is a generalisation of the territory. A menu is an abstraction of the meal. A category is an abstraction of a set of items with the named properties of identity, associativity and composition. It's not the set, its the tools that act as a visor. 

### A Topological Example

In the example of topology the object has the identity of being a point, if we multiply a point by itself we get itself, so we have identity. A line connecting between two points is associativity; a mapping from one to another, so we have association. If we add a third point and another connection we can follow the connectives from the first point to third point, via the second A > B > C - but we could just as easily map from A > C; this is composition. The lingo here is that its said to 'commute'. Hence in by the definitions I've provided, a simple polygon or plane is a category. 

This is probably not useful. Who cares if a plane is a category? I don't, but working through this example helps show that CT goes beyond true/false boolean logic and is more relational in its nature. So why is category theory important? Because it's a dynamic form of maths that makes it suitable for coming to understanding rather than just knowledge - at this point, according to Bennetts General Systematics, we can say that its a triadic symbolic language.

### Types of Categories

This point seems both a good point to stop, but also a point of transition to the remaining questions of "how do you split categories up? (for example free categories vs non-free categories)" which is where I'm shakey and don't actually know, I'll have to look up the definitions, make inferences, ask questions and express my best approximation...

A post for next time.