# AUTONOMOUS-VEHICLE-MANAGEMENT-SYSTEM
The program will efficiently allow the user to add locations and destinations and create roads between them. Also, handles other operations like pathfinding between locations, and sorting vehicles based on distance to destination or battery level.

Autonomous Vehicle Fleet Management System

Project Overview

This project implements a data structure-driven vehicle management system for an autonomous vehicle fleet. The system allows users to manage locations, roads, vehicles, routes, and vehicle prioritisation using custom-built data structures and algorithms in Python.

The program was designed without relying on Python’s built-in list or dictionary functions, requiring the implementation of custom linked lists, hash tables, graph structures, and sorting algorithms.

System Features

The vehicle management system allows users to:

* Add locations to a road network
* Create roads between locations
* Check whether a path exists between two locations
* Add vehicles with unique vehicle IDs
* Search for vehicles by ID
* Delete vehicles from the system
* Display stored vehicle information
* Sort vehicles by distance to destination
* Sort vehicles by battery level

Data Structures Implemented

Graph

A custom graph structure was used to represent locations and roads. Each location is stored as a node, while roads between locations are represented as edges.

Graph functionality includes:

* Adding locations
* Adding roads between locations
* Displaying connected locations
* Finding neighbouring nodes
* Checking route availability using Depth First Search

Hash Table

A custom hash table was implemented to store and manage vehicle information. Each bucket uses a custom linked list to handle collisions through separate chaining.

Hash table functionality includes:

* Vehicle insertion
* Vehicle search
* Vehicle deletion
* Vehicle display
* Load factor monitoring
* Dynamic resizing using prime-number table sizes

Linked List

Custom linked lists were used across the program to support hash table buckets and graph adjacency lists. This allowed the system to manage dynamic data without using Python’s built-in list functions.

Sorting Algorithms

Two sorting algorithms were implemented directly on linked list data:

* Heapsort for sorting vehicles by distance to destination
* Quicksort for sorting vehicles by battery level

Helper methods were created to retrieve nodes by index and swap node data, as linked lists do not support direct random access.

Main Classes

DSAGraph

Manages the road network by storing locations as graph nodes and roads as weighted edges. It supports adding nodes, adding edges, displaying the graph, retrieving neighbours, and checking whether a path exists between two locations.

VehicleHashTable

Stores vehicle records using a custom hash table with linked list chaining. It supports inserting, searching, deleting, displaying, and resizing vehicle records.

Vehicle

Represents an individual autonomous vehicle. Each vehicle stores information such as:

* Vehicle ID
* Current location
* Destination
* Distance to destination
* Battery level

Sorting

Contains custom sorting logic for organising vehicles based on operational priority, such as shortest distance to destination or highest battery level.

Testing

The project includes separate test files for core components:

* Graph testing
* Vehicle hash table testing
* Vehicle object testing
* Sorting algorithm testing

Test cases were used to confirm that locations, roads, vehicles, pathfinding, insertion, deletion, searching, and sorting functions operated correctly.

Efficiency Analysis

Graph Operations

Depth First Search pathfinding has a time complexity of:

O(V + E)

where V is the number of vertices and E is the number of edges.

Hash Table Operations

Average-case time complexity for insertion, search, and deletion is:

O(1)

Worst-case complexity may degrade to:

O(n)

when many collisions occur.

Sorting Algorithms

Heapsort time complexity:

O(n log n)

Quicksort average-case time complexity:

O(n log n)

Quicksort worst-case time complexity:

O(n²)

Technologies Used

* Python
* Object-Oriented Programming
* Custom Linked Lists
* Custom Hash Tables
* Graph Algorithms
* Depth First Search
* Heapsort
* Quicksort

Skills Demonstrated

* Data Structures and Algorithms
* Object-Oriented Programming
* Graph Traversal
* Hash Table Design
* Linked List Implementation
* Algorithm Efficiency Analysis
* Sorting Algorithm Implementation
* Collision Handling
* Pathfinding Logic
* Modular Program Design
* Testing and Debugging
* Technical Documentation

Project Outcome

This project demonstrates the implementation of core data structures and algorithms in a practical fleet management context. By building custom linked lists, hash tables, graphs, and sorting methods, the system shows how autonomous vehicle data can be stored, searched, sorted, and connected through route-based logic.

The project also highlights the ability to design efficient program structures, analyse algorithm performance, and solve implementation challenges without relying on Python’s built-in data structures.

Future Improvements

Future improvements could include a graphical user interface, more advanced pathfinding algorithms such as Dijkstra’s algorithm, improved collision resolution strategies, larger-scale testing with simulated fleet data, and enhanced visualisation of vehicle routes and road networks.
