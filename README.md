# Zoneage

As a part of my job I have to spend a lot of time diagramming things in Visio.

This is not fun.

However, I don't my coding, so I figured why not turn one of my pain points (network zoning models) in to  project.

The plan is to have a tool that can generate the required diagrams from supplied data. If given enough detail it may even be possible to generate other things off the output, such as firewall rules, automated risk assessments and so on.

## Concept

The zone model is simply an overlay of various "nodes" (servers, apps, logical abstractions of things) on to network "zones". 

Essentially it becomes some sort of node graph overlaid over some sort of topology. I've probably worded that very, very badly, but that's how it is.

Anyway, it boils down to four core entities:

* The Node: The actual physical or logical elements of an application, server, service, or superset thereof.
* The Flow: The connections between nodes, such as HTTP, file transfers, something even more abstracted...
* The Zone: A local trust zone. Things inside zones can generally talk to each other, communications between zones normally require some extra security.
* The Zone Flow: You got it, what zones are allowed to talk to other zones.

There's also some other elements that can be thrown in to the mix:

* Environments: Simple. Test, Dev and Prod. Test and Dev might be OK to talk to each other, but neither should talk to prod (except maybe for CICD tooling).
* Location: I couldn't think of a better term for this. Generally blindly applying a zone model to a whole organisation, it's subsidiaries and the cloud can lead to *bad things*. The idea here is that a Presentation Tier in one location (ie the cloud) probably shouldn't talk to an application tier inside the network, at least not without some thinking.

This is all a really casual write-up. There's 50 page beheamoths that fail to describe what I've just failed to describe... so... enjoy.

