In Group Nebula, we defined the 'data' to avoid encountering undefined variable errors as was indicated in the initial running of the script

Upon further debuggging we realized that there was an improper line indentation inside the analyze_list_elements function on line 24.

We further went on to remove the data.remove(element) line because we felt it was unnecessary

On line 41 we further changed the condition