#!/bin/bash
# Launch Fresh, open the left tree panel, split the workspace vertically for btm,
# then split that right pane horizontally to run tig underneath it.
fresh . --cmd="split-vertical" --cmd="run btm" --cmd="split-horizontal" --cmd="run tig"
