# Testing code for graph.py
from graph import DSAGraph

def test_graph():
    # Create a graph
    graph = DSAGraph()

    # Add locations
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")

    # Add roads between locations
    graph.add_edge("A", "B", 20)
    graph.add_edge("B", "C", 50)

    # Display the graph
    graph.display_graph()

    print("\nCheck is_path")
    graph.is_path("A", "C") #true
    graph.is_path("A", "D") #false

    print("\nCheck is_path when src=dest")
    graph.is_path("A", "A") #should print source and dest is the same.

    print("\nCheck is_path when source or destination is not the same")
    graph.is_path("A", "F")
   



    print("\nNo Error? Okay still working :)")

if __name__ == "__main__":
    test_graph()
