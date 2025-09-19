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

Sharing my last post the critique was blunt: "nothing here that you can't find in an introductory book on Category Theory". True - and you would find a whole lot more! 

The purpose was and is:
1) learn in public
2) share where I'm at
3) test my understanding

Two books were recommended requiring almost no background:
1) [Computational Category Theory](https://www.cs.man.ac.uk/~david/categories/book/book.pdf)
2) [Category Theory for Programmers](https://unglueit-files.s3.amazonaws.com/ebf/e90890f0a6ea420c9825657d6f3a851d.pdf)

The constructive elements of the critique asked some questions; namely whats and object and morphism? How are they defined? Provide an example of these. What is a category, provide an example, how do you split categories into different types? So here is an attempt at answering:

### What is an Object?

An object is a conceptual placeholder. You might consider it a point, which would indeed be an object but it's more general than that so better thought of as a conceptual element within a space. In this example the point in topological space is an object.

### What is a Morphism?

A morphism is a conceptual mapping. You might consider it a line or arrow, which would indeed be a morphism but technically they are more general than that, so probably better defined as a mapping between objects. In this example a line in topological space is a morphism.

### What is a Category?

A category is a conceptual space. At this point, we run into difficulty relying on the topology analogy. If we were to keep going with that general path of abstraction we would say its a plane because that's the next topological level, but I'm pretty sure the theorists would start shouting!

Let's wrestle with this alligator:

Based on the previous definition that a category requires identity, association and composition I'm going to go out on a limb and describe a category as form of relational or third order logic. 

A category is an abstract conceptual space with concrete instantiations; a map is an abstraction of the territory, A menu is an abstraction of the meal. A category is an abstraction of any structured grouping of objects and morphisms provided there is identity, associativity and composition. 

### A Topological Example

In the example of topology the object has the identity of being a point, if we multiply a point by itself we get itself, so we have identity. A line connecting between two points is associativity; a mapping from one to another, so we have association. If we add a third point and another connection we can follow the connectives from the first point to third point, via the second A > B > C - but we could just as easily map from A > C; this is composition. The lingo here is that its said to 'commute'. Hence in by the definitions I've provided, a simple polygon or plane is a category. 

This is probably not useful. Who cares if a plane is a category or not? I don't, but working through this example helps show that CT goes beyond true/false boolean logic and is probably more relational in its nature. 

So why is category theory important? Because it's a dynamic form of maths that makes it suitable for coming to understandings rather than just knowledge - at this point, according to Bennetts General Systematics, we can say that its a triadic symbolic language.

### Types of Categories

This point seems both a good point to stop, but also a point of transition to the remaining questions of "how do you split categories up? (for example free categories vs non-free categories)" which is where I'm shakey and don't actually know, I'll have to look up the definitions, make inferences, ask questions and express my best approximation...

A post for next time.