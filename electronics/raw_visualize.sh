#!/bin/bash

neato -Tpng circuit_graph.dot -o circuit_graph_spread.png

xdg-open circuit_graph_spread.png
